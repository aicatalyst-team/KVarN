# Formatting Review: v1 -- KVarN on OpenShift AI

## Scores

| Dimension | Weight | Score (1-10) | Weighted |
|---|---|---|---|
| Heading hierarchy | 1x | 7 | 7 |
| Code formatting | 1x | 6 | 6 |
| CTA placement | 2x | 3 | 6 |
| SEO readiness | 1x | 7 | 7 |
| Link strategy | 1x | 3 | 3 |
| Editorial compliance | 2x | 5 | 10 |
| Brand standards | 1x | 4 | 4 |
| Word count | 1x | 8 | 8 |
| **Total** | **10x** | | **51** |

**Overall score: (51 / 100) * 10 = 5.1 / 10**

---

## Line-level feedback

### Heading hierarchy (7/10)

- **Line 1**: `## Deploying KVarN: KV-Cache Quantization for vLLM on OpenShift AI` -- Title uses H2 correctly (no H1 in body), good. However, "KV-Cache Quantization" uses title case after the colon. Should be "KV-cache quantization" (sentence case; "KV-cache" is a compound noun, lowercase "cache").
- **Line 5**: `## What is KVarN?` -- Correct sentence case. Good.
- **Line 18**: `## The containerization challenge` -- Correct sentence case. Good.
- **Line 37**: `## Building and deploying on OpenShift` -- Correct sentence case. Good.
- **Line 63**: `## Validating KVarN-optimized inference` -- Correct sentence case. Good.
- **Line 87**: `## Lessons learned` -- Correct sentence case. Good.
- **Line 95**: `## Next steps` -- Correct sentence case. Good.
- No H3 subheadings are used; the post is flat H2-only. This is acceptable for the length, but "Lessons learned" section uses bold-lead paragraphs that could be H3s for better structure.

### Code formatting (6/10)

- **Line 9**: Inline backticks used: `` `--kv-cache-dtype kvarn_k4v2_g128 --block-size 128` ``, `` `vllm serve` ``. The rubric says **no backticks** in final output. Multiple occurrences throughout.
- **Line 22**: `` `vllm/vllm-openai:v0.23.0` `` -- backticks.
- **Line 22**: `` `vllm._C` `` -- backticks (also line 89).
- **Line 35**: `` `getpwuid(): uid not found` `` -- backticks.
- **Line 89**: `` `pip install -e .` `` -- backticks.
- **Line 91**: `` `getpass.getuser()` ``, `` `pwd.getpwuid()` ``, `` `KeyError` `` -- backticks.
- **Line 92**: `` `$USER` ``, `` `$HOME` `` -- backticks.
- **Line 97**: `` `/metrics` `` -- backticks.
- Code blocks (lines 11-16, 24-33, 41-45, 78-85) are fenced and runnable. Good.
- Mermaid diagram (lines 50-61) is a nice addition but may not render on the Red Hat Developer Blog platform. Needs verification or a static image fallback.

### CTA placement (3/10)

- **Critical issue**: There is no CTA anywhere in the post. The abstract specifies the CTA as "Explore deploying your own inference optimization projects on OpenShift AI," but it doesn't appear in the draft.
- No CTA near the top, mid-post, or closing.
- No links to redhat.com at all.
- The rubric requires CTA "near top + mid + closing, linked to redhat.com" for a 10.

### SEO readiness (7/10)

- The title (line 1) contains keywords "KVarN," "KV-Cache Quantization," "vLLM," and "OpenShift AI." Good keyword density.
- Title character count: "Deploying KVarN: KV-Cache Quantization for vLLM on OpenShift AI" = 62 characters. Slightly over the 50-60 char ideal but acceptable.
- First paragraph (line 3) mentions "KV-cache memory," "KVarN," "vLLM fork," "quantization," "throughput," and "OpenShift." Strong keyword presence.
- No meta description provided, but that's typically handled by the publishing platform.

### Link strategy (3/10)

- **Lines 102-104**: Three links, all external:
  - GitHub (huawei-csl/KVarN)
  - GitHub (aicatalyst-team/KVarN)
  - Quay.io
- **No links to redhat.com anywhere.** The rubric requires internal links to redhat.com.
- Missing links: Red Hat OpenShift AI product page, vLLM on OpenShift documentation, KServe documentation on OpenShift AI.
- No competitor links (good), but zero Red Hat links is a significant gap.

### Editorial compliance (5/10)

- **Oxford commas**: Generally present. Line 3: "more cache capacity and up to 1.3x better throughput, all without sacrificing accuracy" -- no Oxford comma needed (only two items). Line 7: "distributes weight magnitudes evenly before quantization, which is why" -- fine. Line 9: "No model changes, no calibration dataset, no retraining" -- list without conjunction, acceptable. Line 22: "preserves all the precompiled CUDA extensions (`vllm._C`) while adding" -- n/a. **Line 93**: "CUDA runtime plus PyTorch plus vLLM" -- should use commas: "CUDA runtime, PyTorch, and vLLM."
- **Product names**: "OpenShift" is used throughout but never as "Red Hat OpenShift" on first mention (line 3). First mention should be "Red Hat OpenShift." Similarly, "OpenShift AI" on line 1 should be "Red Hat OpenShift AI" on first use. "KServe" on line 99 -- acceptable as an upstream project name.
- **Contractions**: Not used aggressively as required. Line 3: "It delivers" could be "It delivers" (ok, not all need contracting). But many sentences are stiff: "We needed a faster approach" (line 20), "Our solution: use the official" (line 22), "We ran four test scenarios" (line 65). The rubric asks for aggressive contraction use.
- **Acronyms**: "KV-cache" is not expanded on first use. Line 3 says "KV-cache memory" but never expands "KV" (Key-Value). "LLM" (line 3) is not expanded. "GPU" (line 3 implied, line 48 explicit) is not expanded. "CLI" (line 9) not expanded. "PVC" (line 48) not expanded. "SCC" (line 91) not expanded. "UID" (line 35, 91) not expanded. "JIT" (line 22) not expanded. "CTA" n/a (not in post). **Multiple acronyms are never expanded.**
- **Numerals**: "3-5x" (line 3), "1.3x" (line 3), "4-bit" (line 7), "2-bit" (line 7) -- numerals used correctly. "one CLI flag" (line 9) -- should be "1 CLI flag" per rubric. "four test scenarios" (line 65) -- should be "4 test scenarios."
- **Em dashes**: None used. Good.

### Brand standards (4/10)

- No reference to Red Hat brand colors or fonts (not typically needed in markdown drafts, but brand compliance is more about naming).
- "OpenShift" without "Red Hat" prefix on first mention is a brand violation.
- "OpenShift AI" without "Red Hat" prefix on first mention.
- "Red Hat OpenShift AI" appears only in the title implicitly as "OpenShift AI."
- "Open Data Hub" (mentioned in abstract) doesn't appear in the post.
- The mermaid diagram uses Red Hat color `#EE0000` -- good brand alignment.
- "UBI" is mentioned but never as "Red Hat Universal Base Image" on first use.

### Word count (8/10)

- 823 words. The rubric targets 800-1300 for tutorials. This is at the low end but within range.

---

## Editorial compliance checklist

| Rule | Status | Notes |
|---|---|---|
| Sentence case headings | Partial | Title has "KV-Cache Quantization" (title case after colon) |
| Oxford commas | Partial | Line 93 missing Oxford comma |
| No backticks | Fail | 15+ instances of inline backticks throughout |
| Full product name first mention | Fail | "OpenShift" not "Red Hat OpenShift"; "OpenShift AI" not "Red Hat OpenShift AI" |
| Lowercase component descriptors | Pass | No issues found |
| No H1 in body | Pass | All headings are H2 |
| Expand acronyms on first use | Fail | KV, LLM, GPU, CLI, PVC, SCC, UID, JIT all unexpanded |
| Contractions aggressively | Fail | Formal tone throughout; very few contractions used |
| Numerals in running text | Partial | "one CLI flag," "four test scenarios" should be numerals |
| No em dashes | Pass | None used |

---

## Summary

**Overall score: 5.1 / 10**

The draft has strong technical content and clean heading structure, but has significant formatting and editorial compliance gaps that need addressing before publication.

**Critical issues:**

1. **No CTA anywhere in the post.** The abstract defines a CTA but it was never incorporated. Must add CTAs near the top, mid-post, and closing, all linking to redhat.com properties.
2. **No links to redhat.com.** Zero internal links. Must add links to the Red Hat OpenShift AI product page, relevant documentation, and developer resources.
3. **Inline backticks throughout.** The rubric prohibits backticks in final output. All inline code references need to be reformatted (use code blocks or prose descriptions).
4. **Acronyms not expanded on first use.** At least 8 acronyms (KV, LLM, GPU, CLI, PVC, SCC, UID, JIT) are never expanded. Each needs expansion at first occurrence.
5. **Product names missing "Red Hat" prefix.** First mentions of "OpenShift" and "OpenShift AI" must use the full "Red Hat OpenShift" and "Red Hat OpenShift AI" forms.

**Minor issues:**

- Use more contractions to match Red Hat Developer Blog tone.
- Convert spelled-out numbers ("one," "four") to numerals ("1," "4").
- Verify mermaid diagram renders on target platform; provide static image fallback.
- Expand "UBI" to "Red Hat Universal Base Image (UBI)" on first use.
