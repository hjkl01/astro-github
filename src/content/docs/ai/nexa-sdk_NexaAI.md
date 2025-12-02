---
title: nexa-sdk
---

# NexaSDK - 在任何后端运行任何AI模型

NexaSDK 是一个易用的开发者工具包，用于在本地运行任何AI模型，支持NPU、GPU和CPU。它由NexaML引擎驱动，该引擎完全从零开始构建，以在每个硬件栈上实现最佳性能。与依赖现有运行时的包装器不同，NexaML是一个统一的推理引擎，在内核级别构建。它使NexaSDK能够实现对新模型架构（LLM、多模态、音频、视觉）的Day-0支持。NexaML支持3种模型格式：GGUF、MLX和Nexa AI自己的.nexa格式。

## 功能特点

- **NPU优先支持**：专为NPU设计，支持Qualcomm、Intel、AMD等NPU
- **跨平台支持**：桌面、移动端、汽车、物联网设备
- **多模态支持**：图像、音频、文本
- **多种模型格式**：GGUF、MLX、.nexa格式
- **低级控制**：提供对模型的精细控制
- **OpenAI兼容API**：支持函数调用
- **一键运行**：一行代码即可运行模型

## 快速开始

### 步骤1：下载Nexa CLI

#### macOS

- [arm64 for Apple Neural Engine](https://nexa-model-hub-bucket.s3.us-west-1.amazonaws.com/public/nexa_sdk/downloads/nexa-cli_macos_arm64_ane.pkg)
- [arm64 for MLX](https://public-storage.nexa4ai.com/nexa_sdk/downloads/nexa-cli_macos_arm64.pkg)
- [x86_64](https://public-storage.nexa4ai.com/nexa_sdk/downloads/nexa-cli_macos_x86_64.pkg)

#### Windows

- [arm64 with Qualcomm NPU support](https://public-storage.nexa4ai.com/nexa_sdk/downloads/nexa-cli_windows_arm64.exe)
- [x86_64 with Intel / AMD NPU support](https://public-storage.nexa4ai.com/nexa_sdk/downloads/nexa-cli_windows_x86_64.exe)

#### Linux

对于x86_64：

```bash
curl -fsSL https://github.com/NexaAI/nexa-sdk/releases/latest/download/nexa-cli_linux_x86_64.sh -o install.sh && chmod +x install.sh && ./install.sh && rm install.sh
```

对于arm64：

```bash
curl -fsSL https://github.com/NexaAI/nexa-sdk/releases/latest/download/nexa-cli_linux_arm64.sh -o install.sh && chmod +x install.sh && ./install.sh && rm install.sh
```

### 步骤2：运行模型

使用 `nexa infer <完整仓库名>` 运行任何兼容的GGUF、MLX或nexa模型。

#### GGUF模型

运行LLM，如Qwen3：

```bash
nexa infer ggml-org/Qwen3-1.7B-GGUF
```

运行多模态模型，如Qwen3-VL-4B：

```bash
nexa infer NexaAI/Qwen3-VL-4B-Instruct-GGUF
```

#### MLX模型（仅macOS Apple Silicon）

运行LLM，如Qwen3：

```bash
nexa infer NexaAI/Qwen3-4B-4bit-MLX
```

运行多模态模型，如Gemma3n：

```bash
nexa infer NexaAI/gemma-3n-E4B-it-4bit-MLX
```

#### Qualcomm NPU模型（Windows arm64，Snapdragon X Elite）

首先设置许可证令牌：

```bash
nexa config set license '<your_token_here>'
```

然后运行模型：

```bash
nexa infer NexaAI/OmniNeural-4B
nexa infer NexaAI/Granite-4-Micro-NPU
nexa infer NexaAI/Qwen3-VL-4B-Instruct-NPU
```

## CLI参考

- `nexa -h`：显示所有CLI命令
- `nexa pull <repo>`：交互式下载并缓存模型
- `nexa infer <repo>`：本地推理
- `nexa list`：显示所有缓存的模型及其大小
- `nexa remove <repo>` / `nexa clean`：删除一个/所有缓存的模型
- `nexa serve --host 127.0.0.1:8080`：启动OpenAI兼容的REST服务器
- `nexa run <repo>`：通过现有服务器与模型聊天

对于多模态模型，您可以直接将照片或音频剪辑拖入CLI，甚至可以一次拖入多个图像！

## 支持的模型

NexaSDK支持最新的LLM和VLM，包括：

- OpenAI gpt-oss
- Granite4
- Qwen3VL
- Gemma 3n
- 以及更多

访问 [Nexa Wishlist](https://sdk.nexa.ai/wishlist) 来请求和投票您想要在设备上运行的模型。
