---
title: ktransformers
---

# ktransformers

## 项目简介

ktransformers 是一个灵活的框架，用于体验前沿的大语言模型（LLM）推理和微调优化。该项目专注于通过 CPU-GPU 异构计算实现高效的推理和微调。

## 主要功能

- **高效推理**：支持多种量化技术（如 INT4/INT8），优化 CPU-GPU 混合推理。
- **微调支持**：集成 LLaMA-Factory，支持 LoRA 微调大型 MoE 模型。
- **多模型兼容**：支持 DeepSeek-R1、V3、Qwen3、Kimi-K2 等模型。
- **异构计算**：利用 CPU 和 GPU 的优势，实现资源高效利用。
- **扩展性**：模块化设计，便于集成到其他框架如 SGLang。

## 用法

### 安装

克隆仓库并安装依赖：

```bash
git clone https://github.com/kvcache-ai/ktransformers.git
cd ktransformers
pip install -r requirements.txt
```

### 推理使用

对于 kt-kernel 模块：

```bash
cd kt-kernel
pip install .
```

然后使用 Python API 进行推理。

### 微调使用

对于 kt-sft 模块：

```bash
cd kt-sft
# 按照 README.md 安装环境
USE_KT=1 llamafactory-cli train examples/train_lora/deepseek3_lora_sft_kt.yaml
```

更多详细教程请参考项目文档。
