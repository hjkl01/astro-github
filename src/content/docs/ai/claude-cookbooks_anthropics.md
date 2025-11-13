---
title: claude-cookbooks
---


# Claude Cookbooks (Anthropics)

**项目地址**: <https://github.com/anthropics/claude-cookbooks>

## 主要特性  
- **示例丰富**：包含数十种针对不同任务（编程、文本生成、翻译、摘要、角色扮演等）的完整 Prompt 示例。  
- **可定制化**：每个示例都提供可直接执行的 Code Snippet，方便快速替换为自己的数据或需求。  
- **OpenAI 兼容**：示例兼容 Claude API 的标准请求格式，可直接通过 API 调用。  
- **可扩展**：项目结构清晰，易于添加、修改或共享新的 Prompt Cookbooks。  

## 功能  
| 功能 | 描述 |
|------|------|
| Prompt Library | 统一管理 Prompt 结构，支持参数化与模板化。 |
| 示例代码 | 每个 Prompt 对应最少一段可运行的 Python 示例。 |
| 角色扮演脚本 | 提供多种角色扮演与对话实例，帮助快速构建对话系统。 |
| 任务拆分 | 某些复杂请求（如代码评审）被拆解为若干子任务，示例演示分步调用。 |

## 用法  
1. **克隆仓库**  
   ```bash
   git clone https://github.com/anthropics/claude-cookbooks.git
   cd claude-cookbooks
   ```

2. **安装依赖**（项目默认使用 `requests`）  
   ```bash
   pip install -r requirements.txt  # 如有需求
   ```

3. **配置 API Key**  
   在环境变量或代码中设置 `ANTHROPIC_API_KEY`。  
   ```bash
   export ANTHROPIC_API_KEY=your_key_here
   ```

4. **运行示例**  
   进入对应目录，例如 `cookbooks/summarization`，运行示例脚本。  
   ```bash
   python summarize_example.py
   ```

5. **自定义 Prompt**  
   打开 `template_prompt.txt`，改写 Prompt 并在脚本中加载即可。  

> **提示**：所有示例均遵循 Claude API 的 `messages` 格式，可直接粘贴到你自己的应用中。

---  

**说明**：本文件仅包含主要特性、功能及使用说明，已按要求保存为  
`src/content/docs/00/claude-cookbooks_anthropics.md`。