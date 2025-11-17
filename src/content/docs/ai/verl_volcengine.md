---
title: verl
---

# verl: Volcano Engine Reinforcement Learning for LLMs

verl 是一个灵活、高效且生产就绪的强化学习（RL）训练库，专为大型语言模型（LLMs）设计。它是 HybridFlow 框架的开源版本，由 ByteDance Seed 团队发起，并由 verl 社区维护。

## 功能特性

verl 提供了以下核心功能：

### 易于扩展的 RL 算法

- 支持多种 RL 算法，如 PPO、GRPO、GSPO、ReMax、REINFORCE++、RLOO、PRIME、DAPO、DrGRPO 等。
- 混合控制器编程模型允许灵活表示和高效执行复杂的后训练数据流。
- 几行代码即可构建 RL 数据流。

### 无缝集成现有 LLM 基础设施

- 与 FSDP、FSDP2 和 Megatron-LM 集成用于训练。
- 与 vLLM、SGLang 和 HF Transformers 集成用于生成 rollout。
- 支持 HuggingFace Transformers 和 Modelscope Hub 兼容模型，如 Qwen-3、Qwen-2.5、Llama3.1、Gemma2、DeepSeek-LLM 等。

### 灵活的设备映射

- 支持将模型放置在不同 GPU 集上，以实现高效资源利用和跨不同集群大小的可扩展性。

### 高性能和效率

- 状态-of-the-art 的 LLM 训练和推理引擎集成，提供 SOTA RL 吞吐量。
- 3D-HybridEngine 实现高效的 actor 模型重分片，消除内存冗余并显著减少训练和生成阶段之间的通信开销。

### 其他特性

- 支持监督微调（SFT）。
- 支持基于模型的奖励和基于函数的可验证奖励，用于数学、编码等任务。
- 支持视觉-语言模型（VLMs）和多模态 RL，如 Qwen2.5-vl、Kimi-VL。
- 支持多轮对话和工具调用。
- 支持 LoRA、序列打包、序列并行等。
- 可扩展到 671B 模型和数百个 GPU，使用专家并行。
- 支持多 GPU LoRA RL 以节省内存。
- 实验跟踪支持 wandb、swanlab、mlflow 和 tensorboard。

## 用法

### 安装

请参考官方文档：[安装指南](https://verl.readthedocs.io/en/latest/start/install.html)

### 快速开始

1. 准备数据：为后训练准备数据，包括实现奖励函数。
2. 配置训练：使用提供的配置模板设置 PPO、GRPO 等算法。
3. 运行训练：使用命令行脚本启动训练过程。

### 示例用法

- **PPO 示例**：运行 PPO 训练器以优化 LLM 策略。
- **GRPO 示例**：使用 GRPO 算法进行 RL 训练，支持数学和编码任务。
- **多模态 RL**：训练视觉-语言模型进行多模态任务。

### 编程指南

verl 使用混合流编程模型，允许用户轻松定义和执行复杂的 RL 数据流。详细的编程指南请参考：[编程指南](https://verl.readthedocs.io/en/latest/hybrid_flow.html)

### 性能调优

verl 提供了详细的性能调优指南，帮助优化训练吞吐量和内存使用：[性能调优指南](https://verl.readthedocs.io/en/latest/perf/perf_tuning.html)

## 贡献

verl 欢迎社区贡献。请参考：[贡献指南](https://github.com/volcengine/verl/blob/main/CONTRIBUTING.md)

## 许可证

Apache-2.0 License
