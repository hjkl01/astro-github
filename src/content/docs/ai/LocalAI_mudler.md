---
title: LocalAI
---

## 项目简介

LocalAI 是一个免费、开源的 OpenAI 替代品，由 Ettore Di Giacinto 创建和维护。它是一个自托管、本地优先的 AI 推理平台，可以作为 OpenAI API 的直接替代品运行在消费级硬件上，无需 GPU 支持。LocalAI 支持多种模型格式，如 gguf、transformers、diffusers 等，并提供丰富的功能，包括文本生成、音频、视频、图像生成、语音克隆、分布式和 P2P 去中心化推理。

## 主要功能

- **文本生成**：支持多种语言模型后端，如 llama.cpp、transformers、vLLM 等，用于生成高质量文本。
- **音频处理**：包括文本转音频（TTS）和音频转文本（ASR），支持 Whisper 等模型。
- **图像生成**：支持 Stable Diffusion 等图像生成模型。
- **多模态支持**：包括视觉 API、对象检测、重新排序等。
- **工具集成**：兼容 OpenAI 工具 API，支持函数调用。
- **嵌入生成**：用于向量数据库的嵌入生成。
- **分布式推理**：支持 P2P 和分布式推理模式。
- **模型上下文协议 (MCP)**：提供代理能力，与外部工具集成。
- **WebUI**：内置用户友好的 Web 界面。

## 支持的后端和加速

LocalAI 支持多种 AI 后端，并提供硬件加速选项：

### 文本生成和语言模型

- llama.cpp：支持 CUDA、ROCm、Intel SYCL、Vulkan、Metal、CPU
- vLLM：支持 CUDA、ROCm、Intel
- transformers：支持 CUDA、ROCm、Intel、CPU
- exllama2：支持 CUDA
- MLX：支持 Apple Metal（M1/M2/M3+）
- MLX-VLM：支持 Apple Metal

### 音频和语音处理

- whisper.cpp、faster-whisper：音频转文本
- bark、bark-cpp、coqui、kokoro、chatterbox、piper、kitten-tts：文本转音频
- silero-vad：语音活动检测
- neutts：语音克隆

### 图像和视频生成

- stablediffusion.cpp：支持 CUDA、Intel SYCL、Vulkan、CPU
- diffusers：支持 CUDA、ROCm、Intel、Metal、CPU

### 其他任务

- rfdetr：对象检测
- rerankers：文档重新排序
- local-store：向量数据库

## 使用方法

### 快速开始

1. **使用安装脚本**：

   ```bash
   curl https://localai.io/install.sh | sh
   ```

2. **使用 Docker**：
   - CPU 版本：
     ```bash
     docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
     ```
   - NVIDIA GPU 版本：
     ```bash
     docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-12
     ```
   - AMD GPU 版本：
     ```bash
     docker run -ti --name local-ai -p 8080:8080 --device=/dev/kfd --device=/dev/dri --group-add=video localai/localai:latest-gpu-hipblas
     ```

3. **加载模型**：
   - 从模型库加载：
     ```bash
     local-ai run llama-3.2-1b-instruct:q4_k_m
     ```
   - 从 Hugging Face 加载：
     ```bash
     local-ai run huggingface://TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf
     ```
   - 从 Ollama 注册表加载：
     ```bash
     local-ai run ollama://gemma:2b
     ```

### 高级用法

- **模型管理**：LocalAI 支持从模型库自动下载和管理模型，支持多种来源如 Hugging Face、Ollama 等。
- **API 使用**：LocalAI 提供与 OpenAI API 兼容的 REST API，可以直接替换 OpenAI 客户端。
- **分布式模式**：支持 P2P 推理和分布式计算，提高性能和可扩展性。
- **集成**：与 LangChain、Home Assistant、Discord/Slack 机器人等工具集成。

## 注意事项

- LocalAI 自动检测系统 GPU 能力并下载相应后端，无需手动配置。
- 支持多种硬件加速，包括 NVIDIA CUDA、AMD ROCm、Intel oneAPI、Apple Metal 等。
- 项目活跃维护，社区贡献丰富，支持多种模型和用例。
- 许可证：MIT，由 Ettore Di Giacinto 维护。

更多详细信息请参考 [官方文档](https://localai.io)。
