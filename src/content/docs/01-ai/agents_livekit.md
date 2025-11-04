
---
title: agents
---


# LiveKit Agents

项目地址: https://github.com/livekit/agents

## 功能概述
LiveKit Agents 是一个开源框架，专为在 LiveKit 视频/音频会议中实时部署 AI 助手和多智能体系统而设计。它将多模态输入（文本、音频、图像）与大型语言模型（LLM）结合，实现自然语言交互、实时语音识别、文本生成以及语音合成。

## 主要特性
- **实时语音到文本**：内置 Whisper 或其他转写模型，实时将会议音频转为文本。
- **LLM 接口抽象**：支持 OpenAI、Anthropic、DeepMind 等多种 LLM，可通过 `LLMProvider` 轻松切换。
- **文本到语音**：使用 TTS 引擎（如 Whisper TTS、gTTS 等）将生成文本转为合成语音。
- **多智能体协作**：AgentManager 可管理多位 AI 代理，支持任务分配、并发处理、上下文共享。
- **上下文管理**：提供 `ChatContext`、`Memory`、`Summarizer` 等模块，自动维护对话记录与要点摘要。
- **可插拔架构**：所有功能都以插件形式实现，方便扩展或替换（如自定义 Transcriber、LLMProvider）。
- **异常处理与重试**：内置回退机制，保证在网络/服务异常时机器仍能继续运行。
- **示例与演示**：提供多种快照脚本（如 `quickstart.py`、`multi_agent_demo.py`）作为参考。

## 用法示例
```bash
# 克隆并进入项目
git clone https://github.com/livekit/agents.git
cd agents

# 安装依赖
pip install -r requirements.txt

# 配置环境变量（示例：OpenAI）
export OPENAI_API_KEY="sk-...YOUR_KEY..."

# 启动一个示例 AI 代理
python agents/quickstart.py
```

> 进一步使用请查阅项目的 `docs/` 目录，或直接查看 `agents/` 包内的具体模块与示例。