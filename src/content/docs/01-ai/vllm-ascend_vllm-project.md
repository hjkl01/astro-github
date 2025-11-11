---
title: vllm-ascend
---

# vllm-ascend_vllm-project

## 功能

vLLM Ascend (`vllm-ascend`) 是社区维护的硬件插件，用于在Ascend NPU上无缝运行vLLM。它遵循硬件可插拔接口的原则，支持Transformer-like、Mixture-of-Expert、Embedding、Multi-modal LLMs等流行开源模型。

## 用法

### 前提条件

- 硬件：Atlas 800I A2 Inference series, Atlas A2 Training series, Atlas 800I A3 Inference series, Atlas A3 Training series, Atlas 300I Duo (Experimental)
- OS: Linux
- 软件：Python >= 3.9, < 3.12; CANN >= 8.3.rc1; PyTorch == 2.7.1, torch-npu == 2.7.1; vLLM (与vllm-ascend相同版本)

### 快速开始

推荐使用以下版本：

- v0.11.0rc0 (最新发布候选)：参考 [QuickStart](https://vllm-ascend.readthedocs.io/en/latest/quick_start.html) 和 [Installation](https://vllm-ascend.readthedocs.io/en/latest/installation.html)
- v0.9.1 (最新稳定版本)：参考 [QuickStart](https://vllm-ascend.readthedocs.io/en/v0.9.1-dev/quick_start.html) 和 [Installation](https://vllm-ascend.readthedocs.io/en/v0.9.1-dev/installation.html)

更多详情请参考官方文档：[https://vllm-ascend.readthedocs.io/](https://vllm-ascend.readthedocs.io/)
