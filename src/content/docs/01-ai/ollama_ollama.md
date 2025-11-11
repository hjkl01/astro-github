---
title: Ollama
---

# Ollama

## 项目描述

Ollama 是一个用于在本地机器上构建和运行大型语言模型的轻量级、可扩展框架。它提供了一个简单的 API，用于创建、运行和管理模型，以及一个预构建模型库，可以轻松用于各种应用程序。

## 主要功能

- **模型库**：支持多种模型，如 Gemma 3、DeepSeek-R1、Llama 3 等。
- **自定义模型**：允许从 GGUF 或 Safetensors 导入模型，并自定义提示。
- **多模态支持**：支持图像和文本的模型，如 LLaVA。
- **REST API**：提供 API 用于生成响应、聊天和管理模型。
- **社区集成**：与多种工具和平台集成，如 WebUI、Discord 机器人等。

## 用法

### 安装

- **macOS**：下载 [Ollama.dmg](https://ollama.com/download/Ollama.dmg)
- **Windows**：下载 [OllamaSetup.exe](https://ollama.com/download/OllamaSetup.exe)
- **Linux**：运行 `curl -fsSL https://ollama.com/install.sh | sh`

### 运行模型

1. 拉取模型：`ollama pull llama3.2`
2. 运行模型：`ollama run llama3.2`
3. 与模型聊天：输入提示并回车。

### 自定义模型

创建 `Modelfile`：

```
FROM llama3.2
PARAMETER temperature 1
SYSTEM "You are Mario from Super Mario Bros."
```

然后：`ollama create mario -f Modelfile` 和 `ollama run mario`

### REST API 示例

生成响应：

```bash
curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "prompt":"Why is the sky blue?"}'
```

聊天：

```bash
curl http://localhost:11434/api/chat -d '{"model": "llama3.2", "messages": [{"role": "user", "content": "why is the sky blue?"}]}'
```

更多信息请访问 [ollama.com](https://ollama.com)。
