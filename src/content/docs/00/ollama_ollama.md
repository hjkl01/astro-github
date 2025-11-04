
---
title: ollama
---


# Ollama

**GitHub 项目地址**  
<https://github.com/ollama/ollama>

## 1. 项目概述  
Ollama 是一款轻量级、可本地部署的大型语言模型（LLM）框架，专注于让开发者能够在本地机器上快速上手、运行、调试各种 LLM。它实现了跨平台的命令行工具、HTTP API 以及 Docker‑style 容器化执行环境，支持多种模型形式（chat、embeddings、text生成等），兼容常见的 LLM 模型文件（例如模型权重、tokenizer、config 等）。

## 2. 主要特性  

| 特色 | 说明 |
|-----|-----|
| **本地化推理** | 无需联网即可完成文本生成、归纳、检索等任务。 |
| **多模型支持** | 通过 `ollama pull <model>` 支持下载、安装、切换多种模型。 |
| **统一 API** | `ollama serve` 启动 HTTP API，提供 `/api/chat`, `/api/embeddings` 等端点，兼容 OpenAI API 规范。 |
| **命令行工具** | 提供 `ollama` CLI，包含 **pull / run / list / rm / serve** 等常用命令。 |
| **轻量开销** | 采用 Rust + LLama +自己实现的推理引擎，内存占用低，速度快。 |
| **扩展与自定义** | 可通过 `config.yml` 与环境变量自定义模型路径、GPU/CPU 选项、并发等参数。 |
| **Docker‑style 运行** | `ollama run <model>` 启动临时容器级服务，方便多实例测试。 |

## 3. 功能说明  

| 功能 | 说明 |
|------|------|
| **安装模型** | `ollama pull <model-name>` – 从官方仓库或自定义远程拉取模型文件。 |
| **运行实例** | `ollama run <model-name>` – 在本地启动模型推理服务。 |
| **查询已安装模型** | `ollama list` – 查看已下载模型。 |
| **删除模型** | `ollama rm <model-name>` – 删除本地模型文件。 |
| **启动后台服务** | `ollama serve` – 启动默认运行地址 `localhost:11434`，支持持续推理。 |
| **聊天交互** | `ollama chat <model>` – 通过终端交互式对话；`api` 通道可通过 HTTP POST 交互。 |
| **生成嵌入** | `ollama embedding <model>` – 生成向量嵌入，支持检索与向量数据库集成。 |
| **配置自定义** | 通过 `config.yml` 或环境变量 (E.g. `OLLAMA_MODELS_PATH`, `OLLAMA_HOST`) 进行本地化与性能调优。 |

## 4. 使用示例  

```bash
# 安装模型
ollama pull llama3.1:latest

# 查看已安装模型
ollama list

# 启动服务器
ollama serve

# 终端交互式聊天
ollama chat llama3.1

# 通过 curl 调用 API
curl -X POST http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"llama3.1","messages":[{"role":"user","content":"你好"}]}'
```

### 自定义配置（config.yml 示例）

```yaml
# ~/.ollama/config.yml
models:
  - name: llama3.1
    path: /custom/models/llama3.1
    # 仅当有多 GPU 集群时使用
    gpu: true
server:
  host: "0.0.0.0"
  port: 11434
  max_conns: 100
```

> 配置文件位于 `~/.ollama/config.yml` 或 `$XDG_CONFIG_HOME/ollama/config.yml`。  
> 采用环境变量优先级可覆盖配置文件中对应字段。

## 5. 进一步阅读  
- 官方文档: <https://github.com/ollama/ollama/blob/main/docs>  
- 示例项目与代码控制台: <https://github.com/ollama/ollama/tree/main/example>  

---

> 以上内容为最新的项目概要与指南，按需使用即可。