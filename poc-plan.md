# PoC Plan: KVarN

## Project Classification
- **Type:** model-serving
- **Key Technologies:** vLLM, PyTorch, CUDA, Triton, KV-cache quantization
- **ODH Relevance:** KVarN directly enriches the Model Inference strategy area by demonstrating advanced KV-cache quantization on OpenShift AI. It validates that the Red Hat AI Inference Server can support next-generation optimization techniques that deliver 3-5x more KV-cache capacity with FP16-level accuracy.

## PoC Objectives
1. Deploy KVarN (vLLM fork with KV-cache quantization) as an OpenAI-compatible inference server on OpenShift with GPU
2. Validate that the KVarN quantization flag (`--kv-cache-dtype kvarn_k4v2_g128`) activates correctly and serves accurate responses
3. Demonstrate the OpenAI-compatible REST API works for chat completions
4. Verify the Prometheus metrics endpoint exposes KV-cache utilization data

## Infrastructure Requirements
- **Resource Profile:** gpu
- **GPU Required:** Yes (NVIDIA, compute capability 7.5+, minimum 16GB VRAM)
- **Persistent Storage:** 20Gi PVC for HuggingFace model cache
- **Sidecar Containers:** None
- **Deployment Model:** deployment (long-running inference server)
- **Port:** 8000 (OpenAI-compatible API)

## Test Scenarios

### Scenario 1: Health Check
- **Description:** Verify the vLLM server is running and responding to health requests
- **Type:** http
- **Endpoint:** /health
- **Expected:** Returns 200 OK
- **Timeout:** 300 seconds (model loading may take time)

### Scenario 2: Model Listing
- **Description:** Verify the loaded model appears in the models endpoint
- **Type:** http
- **Endpoint:** /v1/models
- **Expected:** Returns JSON with at least one model entry
- **Timeout:** 30 seconds

### Scenario 3: Chat Completion
- **Description:** Send a chat completion request and verify response
- **Type:** http
- **Endpoint:** /v1/chat/completions
- **Input:** {"model": "Qwen/Qwen2.5-1.5B", "messages": [{"role": "user", "content": "What is KV-cache quantization in one sentence?"}], "max_tokens": 64}
- **Expected:** Returns a valid chat completion response with generated text
- **Timeout:** 60 seconds

### Scenario 4: Metrics Endpoint
- **Description:** Verify Prometheus metrics are exposed
- **Type:** http
- **Endpoint:** /metrics
- **Expected:** Returns Prometheus-format metrics including vllm_* prefixed metrics
- **Timeout:** 30 seconds

## Dockerfile Considerations
- Use the existing `docker/Dockerfile` with `--target vllm-openai-nonroot` build target
- The nonroot target already supports OpenShift's arbitrary UID assignment (UID 2000, GID 0)
- Base image: `nvidia/cuda:13.0.2-devel-ubuntu22.04` (build) / `nvidia/cuda:13.0.2-base-ubuntu22.04` (runtime)
- UBI conversion is not feasible due to CUDA toolkit + JIT compilation requirements
- Use a small model (Qwen/Qwen2.5-1.5B) to fit within available GPU memory

## Deployment Considerations
- **Deployment model:** Deployment with Service (long-running server on port 8000)
- **GPU resource:** Request 1 nvidia.com/gpu
- **Model caching:** Mount a PVC at /home/vllm/.cache/huggingface to cache downloaded models
- **Environment variables:** Set HF_HOME=/home/vllm/.cache/huggingface
- **Startup time:** First launch downloads model; readiness probe should have a long initial delay (300s)
- **Test strategy:** HTTP - all tests hit the OpenAI-compatible REST API
