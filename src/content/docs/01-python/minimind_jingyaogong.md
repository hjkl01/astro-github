---
title: minimind
---

## 项目简介

minimind 是一个开源项目，旨在完全从零开始训练一个小型语言模型 MiniMind。该项目使用 PyTorch 原生实现，不依赖第三方库的抽象接口。MiniMind 系列模型参数量极小，最小版本仅为 25.8M（约 0.02B），力求做到普通个人 GPU 也可快速训练。项目涵盖了大模型的全阶段开源代码，包括预训练 (Pretrain)、监督微调 (SFT)、LoRA 微调、直接偏好优化 (DPO)、强化学习训练 (RLAIF: PPO/GRPO/SPO) 以及模型蒸馏等。

## 主要功能

- **轻量级模型**：最小模型仅 26M 参数，支持单卡训练，训练成本低至 3 元人民币。
- **完整训练流程**：从数据预处理到模型训练，支持多种训练策略。
- **多模态扩展**：支持视觉多模态 VLM 扩展 (MiniMind-V)。
- **第三方生态兼容**：兼容 llama.cpp、vllm、ollama 等推理引擎，以及 Llama-Factory 训练框架。
- **推理模型支持**：复现 DeepSeek-R1 的推理模型，数据和模型全部开源。

## 使用方法

### 环境准备

1. 克隆仓库：

   ```
   git clone https://github.com/jingyaogong/minimind.git
   cd minimind
   ```

2. 安装依赖：

   ```
   pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
   ```

3. 测试 PyTorch CUDA 可用性：
   ```
   import torch
   print(torch.cuda.is_available())
   ```

### 数据下载

从 ModelScope 或 HuggingFace 下载数据集，放置到 `./dataset/` 目录下。推荐下载 `pretrain_hq.jsonl` 和 `sft_mini_512.jsonl` 用于快速复现。

### 训练步骤

进入 `trainer` 目录：

1. **预训练**：

   ```
   python train_pretrain.py
   ```

2. **监督微调**：
   ```
   python train_full_sft.py
   ```

其他训练如 LoRA、DPO、PPO 等可参考项目文档。

### 模型推理

下载预训练模型后，使用以下命令测试：

```
python eval_llm.py --load_from ./MiniMind2
```

### 第三方推理

- **ollama**：

  ```
  ollama run jingyaogong/minimind2
  ```

- **vllm**：
  ```
  vllm serve ./MiniMind2/ --served-model-name "minimind"
  ```

## 注意事项

- 训练时间：单卡 3090 下，预训练 + SFT 约 2 小时，成本约 3 元。
- 支持多卡训练：使用 `torchrun --nproc_per_node N train_xxx.py`。
- 模型权重：训练后权重保存为 `./out/*.pth`，可转换为 Transformers 格式使用。
