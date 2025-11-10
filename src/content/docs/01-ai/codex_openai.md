---
title: codex
---


# OpenAI Codex

- **项目地址**：<https://github.com/openai/codex>

## 主要特性

| 特色 | 描述 |
|------|------|
| **自然语言到代码转换** | 通过 GPT-3 的代码生成模型，将自然语言描述直接转化为多种编程语言（Python、JavaScript、Java、C++ 等）的代码段。 |
| **智能补全与建议** | 在编程时自动补全函数、变量、类等，同时给出语法、逻辑或性能改进建议。 |
| **跨语言翻译** | 支持将一种语言编写的代码转换为另一种语言，帮助快速迁移或学习。 |
| **代码审阅与重构** | 对现有代码进行分析，提出可读性、可维护性或安全性的提升建议。 |
| **集成插件** | 提供 VS Code/JetBrains 等集成开发环境（IDE）插件，直接在编辑器中调用 Codex。 |
| **快速原型** | 通过一句“创建一个登录表单”快速生成前端/后端代码，极大提升原型设计速度。 |

## 功能概览

1. **代码生成**  
   ```bash
   # 直接调用 Codex 生成示例
   curl -X POST https://api.openai.com/v1/engines/davinci-codex/completions \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $OPENAI_API_KEY" \
     -d '{
           "prompt": "用Python实现快速排序",
           "max_tokens": 150,
           "temperature": 0
         }'
   ```

2. **IDE 插件**  
   * 通过 VS Code 扩展插件 `OpenAI Codex`，在代码编辑区按下快捷键即可自动补全或生成代码片段。  
   * 支持上下文感知：插件会分析当前光标位置前后的代码段，为生成结果提供更精准的上下文。  

3. **代码翻译**  
   ```bash
   # 把 JavaScript 代码转换为 Python
   prompt = "将下面 JavaScript 函数转换为等价的 Python 函数:\n\nfunction greet(name) { return 'Hello, ' + name; }"
   # 调用 Codex 完成代码翻译
   ```

4. **自动重构与提示**  
   * Codex 能够识别冗余代码、循环反复出现的逻辑，并给出提取函数或使用更合适数据结构的建议。  
   * 同时可提供单元测试代码、错误处理方式等改进建议。  

## 如何使用

1. **获取 API Key**  
   - 访问 [OpenAI API](https://platform.openai.com/) 注册账号并生成 `OPENAI_API_KEY`。  

2. **安装依赖（示例：Python）**  
   ```bash
   pip install openai
   ```

3. **编写脚本调用 Codex**  
   ```python
   import openai

   openai.api_key = "YOUR_API_KEY"

   response = openai.Completion.create(
       engine="davinci-codex",
       prompt="用JavaScript实现一个事件总线（EventBus）",
       max_tokens=200,
       temperature=0.2,
   )

   print(response.choices[0].text.strip())
   ```

4. **IDE 集成**  
   - 在 VS Code 市场搜索 “Codex”，安装后按快捷键 `Ctrl+Alt+Space` 即可使用。  

5. **使用 Chrome 扩展**  
   - 安装 “Codex for Chrome” 或 “GitHub Copilot” 等扩展，可在浏览器中直接生成代码片段，支持代码片段粘贴到 IDE、文本编辑器中。  

## 适用场景

| 场景 | 说明 |
|------|------|
| 初学者 | 自动生成标注清晰的代码，帮助学习语法和最佳实践。 |
| 快速原型 | 只需一句“构建一个 RESTful API”，即可得到完整后端框架代码。 |
| 多语言迁移 | 将大型项目从一种语言迁移到另一种语言，显著降低工作量。 |
| 代码审查 | 在 CI 流程中自动检查代码质量、潜在 bug。 |

---
> **文档来源**：<https://github.com/openai/codex>
