---
title: mlx-lm
---


# mlx-lm

**项目地址**：<https://github.com/ml-explore/mlx-lm>

## 概述
mlx‑lm 是一个基于 Apple MLX 的轻量级语言模型框架，旨在提供高效、低延迟的推理体验。它支持多种现代大语言模型，并可在 CPU、GPU 和 TPU 上运行。

## 主要特性
- **零拷贝推理**：直接使用 MLX 的张量操作，避免不必要的数据拷贝。  
- **跨平台**：兼容 macOS、Linux、Windows（CPU），以及苹果 Silicon、NVIDIA GPU、Google TPU。  
- **可扩展模型**：内置对 LLaMA、Phi‑2、GPT‑NeoX 等模型的支持，可通过 `mlx_lm.load()` 轻松加载。  
- **流式推理**：支持逐步输出 token，适合聊天或实时预测。  
- **简洁 API**：仅需数行代码即可完成模型加载、生成、推理。  

## 功能概览
| 功能 | 说明 |
|------|------|
| **模型加载** | `model, tokenizer = mlx_lm.load("model_name")` |
| **文本生成** | `output = model.generate(input_tokens, max_tokens=128)` |
| **流式输出** | `for token in model.generate_stream(input_tokens): print(token)` |
| **自定义推理配置** | `model.generate(..., temperature=0.7, top_k=40)` |
| **多设备支持** | `model.to("cuda")` / `model.to("mps")` / `model.to("tpu")` |

## 用法示例

```python
import mlx_lm

# 1. 加载模型与分词器
model, tokenizer = mlx_lm.load("phi-2", device="mps")  # 或 "cpu", "cuda", "tpu"

# 2. 编码输入
prompt = "请简述机器学习的基本流程："
input_tokens = tokenizer.encode(prompt)

# 3. 生成文本（一次性）
output_tokens = model.generate(input_tokens, max_tokens=200)
print(tokenizer.decode(output_tokens))

# 4. 流式生成
for token in model.generate_stream(input_tokens, max_tokens=200):
    print(tokenizer.decode([token]), end="", flush=True)
print()
```

> **提示**  
> - 通过 `model.generate(..., temperature=0.8, top_k=50)` 控制随机性与多样性。  
> - 若想在 GPU 上加速，确保已安装 MLX 的 GPU 版本并将 `device="cuda"`。  
> - 在 macOS 上使用 Apple Silicon 时，将 `device="mps"` 可获得最佳性能。

## 结语
mlx‑lm 为需要高效推理的 Python 开发者提供了一个简洁、跨平台且易于扩展的框架。无论是在本地实验还是在云端部署，均可通过最小的代码实现强大的语言模型功能。