
---
title: jan
---

**src/content/docs/00/jan_janhq.md**

```markdown
# Jan (janhq/jan)

> 项目地址: <https://github.com/janhq/jan>

Jan 是一个轻量级、跨平台的本地 AI 聊天框架，旨在让开发者和最终用户都能快速搭建并体验基于大语言模型（LLM）的聊天机器人。它的核心目标是低耦合、高性能、易于扩展。

## 主要特性

| 功能 | 说明 |
|------|------|
| **本地推理** | 支持主流 LLM（如 LLaMA、Vicuna、Mistral、ChatGLM 等）在本地运行，免签名、无网络延时。 |
| **统一接口** | 提供统一的 `ChatClient` 接口，简化不同模型、不同后端（CPU/GPU/FP16/INT8）的调用。 |
| **插件体系** | 通过插件机制可以灵活扩展：
  * 对话管理器（记忆、上下文裁剪）
  * 预/后处理插件（文本格式化、逻辑校正）
  * 可视化插件（故事板、思维导图）
  * 第三方服务集成（语音、翻译、代码生成） |
| **多模态支持** | 原生支持文本、图片到图片、生成音频、短视频等多模态输入输出。 |
| **跨平台** | Rust+Tauri 构建的桌面客户端，支持 Windows、macOS、Linux；CLI 与 Python SDK 兼容。 |
| **易于部署** | 镜像一键启动（Docker），也可自建 Dockerfile；内置模型检索/下载工具。 |
| **安全与隐私** | 所有处理均在本地完成，完全不向外部服务发送任何文本。 |
| **可视化配置** | 提供 GUI 配置窗口，支持热拖拽、即时预览。 |
| **社区协作** | 开源、MIT 许可，提供示例、教程、API 文档，方便团队使用。 |

## 快速开始

> **前置条件**：已安装 Rust（for 源码编译）、Python 3.8+（可选）以及适配的 GPU 驱动（可选）。

### 1. 克隆仓库

```bash
git clone https://github.com/janhq/jan.git
cd jan
```

### 2. 安装依赖

```bash
# For building the Rust core
cargo build --release

# Optional: Build the Tauri desktop app
pnpm install   # (若未安装 pnpm, 可用 npm 或 yarn)
pnpm run tauri dev
```

### 3. 下载模型

```bash
# Jan 自带 CLI，支持下载预训练模型
./jan model -u https://hf.ai/janhq/llama3-8b  -o ./models/llama3-8b
```

> 也可以直接通过 `hf.ai` 或 HuggingFace Hub 下载到指定目录。

### 4. 启动聊天

```bash
# CLI 启动
./jan chat --model ./models/llama3-8b

# 或者使用 Python SDK
python - <<'PY'
from jan import ChatClient
client = ChatClient(model_path='./models/llama3-8b')
print(client.send("你好，Jan!"))
PY
```

### 5. 插件与页面

插件（如记忆、语音识别）在 `plugins/` 目录，使用 Cargo 或 npm 安装后按文档配置即可。

## 典型用例

| 场景 | 示例命令 / 代码 |
|------|----------------|
| **本地客服助手** | `jan chat --model ./models/chatglm-6b` |
| **短篇故事创作** | `jan chat --model ./models/mistral-7b` |
| **多模态生成** | `jan chat --model ./models/koala-13b --image banner.jpg` |
| **语音对话** | `jan chat -p voice` (启用 Whisper + TTS) |

## 文档与支持

- 官方文档：[docs.janhq.ai](https://docs.janhq.ai)
- 代码仓库 Wiki：查看 issue `docs` 标签
- 社区支持：可在 GitHub Issues、Discord 或 Telegram 频道寻求帮助

> Jan 通过“无需网络、零成本、全本地”的理念，让 AI 成为个人和企业的数字助理，轻松帮助你完成文本、代码、设计及更多创意任务。祝你玩得开心 🚀
