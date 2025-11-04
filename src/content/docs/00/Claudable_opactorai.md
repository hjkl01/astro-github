
---
title: Claudable
---

**GitHub项目地址**  
https://github.com/opactorai/Claudable  

---

### 主要特性  
- **Claude API 封装**：提供一套简洁的 Python 接口，直接调用 Anthropic 的 Claude 系列模型（如 `claude-3-haiku`, `claude-3-sonnet` 等）。  
- **流式响应**：支持 `stream=True`，可按 token 或字节实时获取生成结果。  
- **内置缓存**：使用 `attachment_cache` 自动缓存同一次请求的结果，降低重复成本与延迟。  
- **错误重试**：内置指数退避重试机制，自动处理网络或 API 限速异常。  
- **可插拔的工具集**：支持通过 `claudable/tools` 目录快速添加自定义工具，满足多种功能调用需求。  
- **CLI 与 SDK 双用**：内置命令行工具 `claudable`，可以在终端直接调用；同时提供公开的 Python SDK，方便集成到自己的项目。  

### 功能概览  
1. **基本聊天**  
   ```bash
   claudable --prompt "写一段 Python 代码，实现快速排序"
   ```  
2. **流式聊天**  
   ```bash
   claudable --stream --prompt "讲解一下量子力学"
   ```  
3. **保存上下文**  
   ```python
   from claudable import Client
   client = Client()
   response = client.chat("帮我写一份简历", conversation_id="resume")
   ```  
4. **工具调用**  
   - 自动加载 `tools/` 目录下的自定义工具；  
   - 在 prompt 中使用 `{"name":"weather","arguments":{...}}` 触发工具。  
5. **批量请求**  
   ```python
   client.batch([{"prompt":"..."}], concurrency=4)
   ```  
6. **多线程与异步**  
   ```python
   import asyncio
   async def fetch():
       async for token in client.stream("让我们一起探索宇宙"):
           print(token, end='')
   asyncio.run(fetch())
   ```  

### 安装与使用  
```bash
# 安装
pip install claudable

# 直接在命令行使用
claudable --prompt "翻译成中文：" --model claude-3-sonnet
```  

```python
# 在 Python 中使用
from claudable import Client

client = Client()
result = client.chat(
    prompt="写一篇关于机器学习的博客文章",
    model="claude-3-sonnet",
    max_tokens=512,
    temperature=0.7,
)
print(result)
```  

**环境变量**  
- `CLAUDE_API_KEY`：必填，Anthropic API Key。  
- `CLAUDE_CACHE_DIR`（可选）：自定义缓存文件路径。  

---

以上即为 **Claudable** 项目的核心特性、功能与使用方法。后续细节可参考项目 README 与源码。