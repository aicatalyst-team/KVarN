#!/usr/bin/env python3
"""PoC Test Script for KVarN (vLLM KV-cache quantization) on OpenShift"""

import json
import sys
import time
import urllib.request
import urllib.error

SERVICE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://vllm-kvarn.poc-kvarn.svc.cluster.local:8000"

results = []

def test_scenario(name, description, fn, timeout=30):
    """Run a test scenario with retry logic."""
    start = time.time()
    max_retries = 3
    last_error = None
    
    for attempt in range(max_retries):
        try:
            result = fn()
            duration = time.time() - start
            results.append({
                "scenario_name": name,
                "description": description,
                "status": "pass",
                "output": str(result)[:500],
                "error_message": None,
                "duration_seconds": round(duration, 2)
            })
            print(f"PASS: {name} ({duration:.1f}s)")
            return True
        except Exception as e:
            last_error = str(e)
            if attempt < max_retries - 1:
                print(f"  Retry {attempt + 1}/{max_retries} for {name}: {last_error[:100]}")
                time.sleep(5)
    
    duration = time.time() - start
    results.append({
        "scenario_name": name,
        "description": description,
        "status": "fail",
        "output": "",
        "error_message": last_error[:500],
        "duration_seconds": round(duration, 2)
    })
    print(f"FAIL: {name} ({duration:.1f}s): {last_error[:100]}")
    return False


def http_get(path, timeout=30):
    """Make an HTTP GET request."""
    url = f"{SERVICE_URL}{path}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8"), resp.status


def http_post(path, data, timeout=60):
    """Make an HTTP POST request with JSON body."""
    url = f"{SERVICE_URL}{path}"
    body = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8")), resp.status


# Scenario 1: Health Check
def test_health():
    body, status = http_get("/health", timeout=30)
    assert status == 200, f"Expected 200, got {status}"
    return f"Status: {status}, Body: {body[:100]}"

test_scenario("health-check", "Verify vLLM server health", test_health)

# Scenario 2: Model Listing
def test_models():
    body, status = http_get("/v1/models", timeout=30)
    data = json.loads(body)
    assert status == 200, f"Expected 200, got {status}"
    assert "data" in data, "Missing 'data' field"
    assert len(data["data"]) > 0, "No models loaded"
    model_id = data["data"][0]["id"]
    return f"Model: {model_id}, Count: {len(data['data'])}"

test_scenario("model-listing", "Verify loaded model in API", test_models)

# Scenario 3: Chat Completion
def test_chat():
    resp, status = http_post("/v1/chat/completions", {
        "model": "Qwen/Qwen2.5-1.5B",
        "messages": [{"role": "user", "content": "What is KV-cache quantization in one sentence?"}],
        "max_tokens": 64,
        "temperature": 0.7
    }, timeout=60)
    assert status == 200, f"Expected 200, got {status}"
    assert "choices" in resp, "Missing 'choices' in response"
    assert len(resp["choices"]) > 0, "No choices returned"
    content = resp["choices"][0]["message"]["content"]
    assert len(content) > 0, "Empty response content"
    return f"Response: {content[:200]}"

test_scenario("chat-completion", "Chat completion with KVarN quantization", test_chat)

# Scenario 4: Metrics Endpoint
def test_metrics():
    body, status = http_get("/metrics", timeout=30)
    assert status == 200, f"Expected 200, got {status}"
    assert "vllm" in body.lower() or "HELP" in body, "No vLLM metrics found"
    # Check for KV-cache related metrics
    has_kv_metrics = any(m in body for m in [
        "gpu_cache_usage", "num_gpu_blocks", "kv_cache"
    ])
    metric_count = sum(1 for line in body.split("\n") if line and not line.startswith("#"))
    return f"Metrics found: {metric_count} values, KV-cache metrics: {has_kv_metrics}"

test_scenario("metrics-endpoint", "Verify Prometheus metrics", test_metrics)

# Output results
print("\n" + "="*60)
print("TEST RESULTS")
print("="*60)
passed = sum(1 for r in results if r["status"] == "pass")
failed = sum(1 for r in results if r["status"] == "fail")
print(f"Passed: {passed}/{len(results)}")
print(f"Failed: {failed}/{len(results)}")

# Output JSON results to stdout
print("\n--- JSON RESULTS ---")
print(json.dumps(results, indent=2))
