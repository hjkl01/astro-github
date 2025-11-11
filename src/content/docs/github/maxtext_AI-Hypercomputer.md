---
title: MaxText
---

## 功能介绍

MaxText 是一个高性能、高可扩展的开源大语言模型 (LLM) 库和参考实现，使用纯 Python/JAX 编写，针对 Google Cloud TPUs 和 GPUs 进行训练。它提供了高性能模型库，包括 Gemma、Llama、DeepSeek、Qwen 和 Mistral 等模型。对于每个模型，MaxText 支持预训练（可扩展到数万个芯片）和可扩展的后训练，包括监督微调 (SFT) 和组相对策略优化 (GRPO，一种强化学习)。

MaxText 通过 JAX 和 XLA 编译器的强大功能，在保持简单和“优化免费”的同时，实现高模型 FLOPs 利用率 (MFU) 和每秒令牌数，从单主机到大型集群。

MaxText 是研究和生产中雄心勃勃的 LLM 项目的起点。我们鼓励您从开箱即用的 MaxText 开始实验，然后分叉并修改以满足您的需求。

## 用法

### 安装

通过 pip 安装 MaxText：

```bash
pip install maxtext
```

详细安装指南请参考 [官方文档](https://maxtext.readthedocs.io/en/latest/guides/install_maxtext.html)。

### 快速开始

访问 [Read The Docs 站点](https://maxtext.readthedocs.io/en/latest/) 或直接 [开始您的第一次运行](https://maxtext.readthedocs.io/en/latest/tutorials/first_run.html)。

### 支持的模型

- **Google**: Gemma 3 (4B, 12B, 27B), Gemma 2 (2B, 9B, 27B), Gemma 1 (2B, 7B)
- **Alibaba**: Qwen 3 MoE 2507 (235B, 480B), Qwen 3 MoE (30B, 235B), Qwen 3 Dense (0.6B, 1.7B, 4B, 8B, 14B, 32B)
- **DeepSeek**: DeepSeek-V3 0324 (671B) & DeepSeek-R1 0528 (671B), DeepSeek-V2 (16B, 236B)
- **Meta**: Llama 4 Scout (109B) & Maverick (400B), Llama 3.3 70B, 3.1 (8B, 70B, 405B), 3.0 (8B, 70B, 405B), Llama 2 (7B, 13B, 70B)
- **OpenAI**: GPT-OSS (20B, 120B), GPT3 (52K, 6B, 22B, 175B)
- **Mistral**: Mixtral (8x7B, 8x22B), Mistral (7B)

### 预训练

MaxText 可作为从头构建模型的参考实现，支持从小模型如 Llama 8B 到大 MoE 如 DeepSeek-V3 的训练。提供分片、量化、检查点等方面的优化实现。

### 后训练

使用 Tunix 进行可扩展的后训练框架，支持 SFT 和 GRPO 等技术。

示例脚本：

- [SFT](https://github.com/AI-Hypercomputer/maxtext/blob/main/end_to_end/tpu/llama3.1/8b/run_sft.sh)
- [GRPO](https://maxtext.readthedocs.io/en/latest/tutorials/grpo.html)

### 多模态支持

支持 Gemma 3 和 Llama 4 VLM 的多模态训练。

## 参与贡献

加入 [Discord 频道](https://discord.com/invite/2H9PhvTcDU)，或在 [GitHub Issues](https://github.com/AI-Hypercomputer/maxtext/issues/new/choose) 提交反馈。

许可证：Apache-2.0
