---
title: sglang
---

# SGLang

## 项目简介

SGLang 是一个高性能的服务框架，专为大型语言模型（LLM）和视觉语言模型（VLM）设计。它旨在提供低延迟和高吞吐量的推理服务，支持从单个 GPU 到大型分布式集群的各种设置。

## 主要功能

- **快速后端运行时**：
  - RadixAttention 用于前缀缓存
  - 零开销 CPU 调度器
  - 预填充-解码分离
  - 推测解码
  - 连续批处理
  - 分页注意力
  - 张量/管道/专家/数据并行
  - 结构化输出
  - 分块预填充
  - 量化支持（FP4/FP8/INT4/AWQ/GPTQ）
  - 多 LoRA 批处理

- **广泛的模型支持**：
  - 生成模型：Llama、Qwen、DeepSeek、Kimi、GLM、GPT、Gemma、Mistral 等
  - 嵌入模型：e5-mistral、gte、mcdse
  - 奖励模型：Skywork
  - 兼容大多数 Hugging Face 模型和 OpenAI API

- **广泛的硬件支持**：
  - NVIDIA GPU（GB200/B300/H100/A100/Spark）
  - AMD GPU（MI355/MI300）
  - Intel Xeon CPU
  - Google TPU
  - Ascend NPU 等

- **灵活的前端语言**：
  - 直观的接口用于编程 LLM 应用
  - 支持链式生成调用、高级提示、控制流、多模态输入、并行和外部交互

## 使用方法

### 安装

参考官方文档：[Install SGLang](https://docs.sglang.ai/get_started/install.html)

### 快速开始

1. 启动服务：

   ```bash
   python -m sglang.launch_server --model-path meta-llama/Llama-2-7b-chat-hf
   ```

2. 发送请求：

   ```python
   import requests

   response = requests.post(
       "http://localhost:30000/v1/chat/completions",
       json={
           "model": "meta-llama/Llama-2-7b-chat-hf",
           "messages": [{"role": "user", "content": "Hello!"}]
       }
   )
   print(response.json())
   ```

### 前端编程示例

```python
import sglang as sgl

@sgl.function
def multi_turn_question(s, question_1, question_2):
    s += sgl.user(question_1)
    s += sgl.assistant(sgl.gen("answer_1", max_tokens=256))
    s += sgl.user(question_2)
    s += sgl.assistant(sgl.gen("answer_2", max_tokens=256))

# 运行
state = multi_turn_question.run(
    question_1="What is the capital of France?",
    question_2="What's another name for it?"
)
```

更多用法请参考：[Backend Tutorial](https://docs.sglang.ai/basic_usage/openai_api_completions.html) 和 [Frontend Tutorial](https://docs.sglang.ai/references/frontend/frontend_tutorial.html)

## 性能基准

SGLang 在各种模型和硬件上提供卓越的性能，包括：

- 比其他框架更快的前缀缓存和解码
- 支持大规模专家并行
- 在 NVIDIA 和 AMD GPU 上优化 DeepSeek 模型

详细基准测试：[Benchmark](https://docs.sglang.ai/benchmark_and_performance.html)

## 社区和支持

- 文档：[docs.sglang.ai](https://docs.sglang.ai/)
- Slack：[slack.sglang.ai](https://slack.sglang.ai/)
- GitHub：[github.com/sgl-project/sglang](https://github.com/sgl-project/sglang)

SGLang 由活跃的社区支持，已在生产环境中部署，服务于数万 GPU。
