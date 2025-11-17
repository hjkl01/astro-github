---
title: RLinf
---

# RLinf: 强化学习基础设施，用于代理AI

RLinf 是一个灵活且可扩展的开源基础设施，专为通过强化学习后训练基础模型（LLMs、VLMs、VLAs）而设计。'inf' 在 RLinf 中代表 `Infrastructure`，强调其作为下一代训练的强大骨干的作用。它也代表 `Infinite`，象征着系统对开放式学习、持续泛化和智能发展无限可能性的支持。

## 主要功能

### 具身智能

RLinf 支持主流 VLA 模型、主流基于 CPU 和 GPU 的模拟器，并通过标准化的 Worker 接口实现对 π₀ 和 π₀.₅ 模型系列的首次 RL 微调。

支持的模拟器包括：

- ManiSkill
- LIBERO
- BEHAVIOR
- MetaWorld
- 更多...

支持的模型包括：

- π₀ 和 π₀.₅
- OpenVLA
- OpenVLA-OFT
- GR00T
- Qwen2.5-VL

支持的 RL 算法包括：

- GRPO
- PPO
- DAPO
- Reinforce++
- SAC

### 代理 RL

RLinf 支持代理 RL，包括改善 LLM 推理能力的 RL 训练，如数学推理，以及代理的 RL 训练，如编码代理的 RL 训练。

### 高灵活性、效率和可扩展性

RLinf 具有高灵活性，支持多样化的 RL 训练工作流，同时隐藏分布式编程的复杂性。用户可以轻松将 RL 训练扩展到大量 GPU 节点，而无需修改代码。

支持多种后端集成：

- FSDP + HuggingFace/SGLang/vLLM：快速适应新模型和算法，适合初学者和快速原型。
- Megatron + SGLang/vLLM：针对大规模训练优化，为专家用户提供最大效率。

## 用法

### 安装

用户可以参考我们的[安装指南](https://rlinf.readthedocs.io/en/latest/rst_source/start/installation.html)来安装 RLinf。我们推荐使用提供的 Docker 镜像（即[安装方法 1](https://rlinf.readthedocs.io/en/latest/rst_source/start/installation.html#installation-method-1-docker-image)），因为具身 RL 的环境和依赖关系复杂。

### 快速开始

设置环境后，用户可以运行一个简单的具身 RL 示例，使用 ManiSkill3 模拟器，按照[此文档](https://rlinf.readthedocs.io/en/latest/rst_source/start/vla.html)操作。

更多 RLinf 教程和应用示例，请查看我们的[文档](https://rlinf.readthedocs.io/en/latest/index.html)和[示例库](https://rlinf.readthedocs.io/en/latest/rst_source/examples/index.html)。

## 主要结果

RLinf 在具身智能和数学推理任务上取得了最先进的性能。例如，在 ManiSkill 和 LIBERO 基准上，使用 PPO 和 GRPO 算法训练 Vision-Language-Action 模型，取得了显著改进。

在数学推理方面，RLinf 在 AIME 和 GPQA-diamond 等基准上超越了现有模型。

## 路线图

- 支持异构 GPU
- 支持异步管道执行
- 支持专家混合 (MoE)
- 支持更多模拟器和模型
- 支持真实世界 RL 具身智能

## 贡献

我们欢迎对 RLinf 的贡献。请阅读[贡献指南](https://github.com/RLinf/RLinf?tab=contributing-ov-file#contributing-to-rlinf)。

## 引用

如果您发现 RLinf 有帮助，请引用论文：

```
@misc{yu2025rlinfflexibleefficientlargescale,
  title={RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation},
  author={Chao Yu and Yuanqing Wang and Zhen Guo and Hao Lin and Si Xu and Hongzhi Zang and Quanlu Zhang and Yongji Wu and Chunyang Zhu and Junhao Hu and Zixiao Huang and Mingjie Wei and Yuqing Xie and Ke Yang and Bo Dai and Zhexuan Xu and Xiangyuan Wang and Xu Fu and Zhihao Liu and Kang Chen and Weilin Liu and Gang Liu and Boxun Li and Jianlei Yang and Zhi Yang and Guohao Dai and Yu Wang},
  year={2025},
  eprint={2509.15965},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2509.15965},
}
```
