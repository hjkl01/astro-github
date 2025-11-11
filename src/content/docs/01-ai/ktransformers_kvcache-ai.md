---
title: ktransformers
---

# ktransformers

## 功能介绍

KTransformers 是一个灵活的框架，用于体验前沿的LLM推理优化。它旨在通过高级内核优化和放置/并行策略增强您的🤗 Transformers体验。

KTransformers 是一个以Python为中心的设计灵活的框架，其核心是可扩展性。通过一行代码实现和注入优化模块，用户可以获得与Transformers兼容的接口、符合OpenAI和Ollama的RESTful API，甚至是一个简化的类似ChatGPT的Web UI。

KTransformers 的愿景是作为一个灵活的平台，用于实验创新的LLM推理优化。

## 主要特性

- 支持多种模型：DeepSeek-V3、R1、Qwen3、Kimi-K2 等
- 高级内核优化：支持Marlin、Llamafile、FP8 等
- 异构计算：GPU/CPU 卸载量化模型
- 多GPU支持
- 长上下文支持
- 与LLaMA-Factory集成进行微调
- 支持多种硬件：Intel、AMD、Ascend NPU 等

## 用法

### 安装

参考官方[安装指南](https://kvcache-ai.github.io/ktransformers/en/install.html)。

### 基本使用

1. 创建YAML注入模板
2. 使用 `optimize_and_load_gguf` 函数加载和优化模型
3. 使用标准的Transformers接口或提供的 `prefill_and_generate` 方法

示例代码：

```python
from transformers import AutoModelForCausalLM
import torch

with torch.device("meta"):
    model = AutoModelForCausalLM.from_config(config, trust_remote_code=True)
optimize_and_load_gguf(model, optimize_config_path, gguf_path, config)
# 使用模型进行推理
```

### 自定义模型

通过YAML规则文件匹配和替换模块，实现自定义优化。

详细教程见[注入教程](https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/injection_tutorial.md)。

## 引用

如果您在研究中使用KTransformers，请引用我们的论文：

```
@inproceedings{10.1145/3731569.3764843,
title = {KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models},
author = {Chen, Hongtao and Xie, Weiyu and Zhang, Boxin and Tang, Jingqi and Wang, Jiahao and Dong, Jianwei and Chen, Shaoyuan and Yuan, Ziwei and Lin, Chen and Qiu, Chengyu and Zhu, Yuening and Ou, Qingliang and Liao, Jiaqi and Chen, Xianglin and Ai, Zhiyuan and Wu, Yongwei and Zhang, Mingxing},
booktitle = {Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles},
year = {2025}
}
```
