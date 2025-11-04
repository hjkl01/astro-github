
---
title: litellm
---


# LiteLLM

**项目地址**: <https://github.com/BerriAI/litellm>

## 主要特性

- **轻量级**：为本地部署的 LLM 提供快速、低资源占用的接口。  
- **兼容多模型**：支持 Hugging Face、OpenAI、Anthropic 等多种 LLM 提供商。  
- **易集成**：使用 Python `pip install litellm`，无缝集成到现有项目。  
- **安全与隐私**：支持本地推理，避免将数据发送到外部服务器。  
- **可扩展**：通过插件机制可以轻松添加自定义模型或后处理逻辑。  

## 功能概览

| 功能 | 说明 |
|------|------|
| **文本生成** | 使用 `completion` 接口生成自然语言文本。 |
| **聊天** | `chat_completion` 接口支持多轮对话。 |
| **嵌入** | `embedding` 接口返回文本向量，可用于检索或相似度计算。 |
| **检索增强生成 (RAG)** | 配合向量数据库实现内容检索后再生成回答。 |
| **多语言支持** | 内置多语言模型，支持中文、英文等常见语言。 |
| **模型管理** | 通过配置文件或环境变量快速切换模型。 |
| **监控与日志** | 内置日志系统，可记录请求、响应及错误信息。 |

## 快速使用

```bash
# 安装
pip install litellm

# 简单文本生成
python - <<'PY'
import litellm

response = litellm.completion(
    model="gpt-4o-mini",
    prompt="写一段关于大数据的简介。",
    max_tokens=150
)
print(response.choices[0].text)
PY
```

### 通过配置文件切换模型

```yaml
# litellm_config.yaml
model: "gpt-4o-mini"
temperature: 0.7
max_tokens: 200
```

```python
import litellm
litellm.set_default_config("litellm_config.yaml")

response = litellm.completion(prompt="请解释一下区块链的工作原理。")
print(response.choices[0].text)
```

### 使用本地模型

```python
import litellm

response = litellm.completion(
    model="local-model-path/ggml-model.bin",
    prompt="给我一个Python列表的例子。",
    max_tokens=50
)
print(response.choices[0].text)
```

## 进阶功能

- **RAG**：结合向量数据库（如 Pinecone、FAISS）实现检索增强生成。  
- **插件**：实现自定义插件（如自定义 token 计数、后处理等）。  
- **多线程**：`litellm.AsyncClient` 支持异步并发请求。  

---

> 以上内容为项目核心特性与使用示例，更多细节请参阅官方文档或源码。  
