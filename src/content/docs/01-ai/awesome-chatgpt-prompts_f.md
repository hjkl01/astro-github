
---
title: awesome-chatgpt-prompts
---

# awesome-chatgpt-prompts（f 维护版）

> 项目地址: <https://github.com/f/awesome-chatgpt-prompts>

## 项目简介
`awesome-chatgpt-prompts` 是一个由社区维护的 ChatGPT 提示词集合，涵盖了从日常对话、编程、写作、翻译到专业领域的多种场景。每个提示词都以 Markdown 文件形式存放，附带标签、分类和使用示例，方便快速检索与使用。

## 主要特性
- **海量提示词**：数百条经过筛选、更新的 Prompt，涵盖多语言与多功能场景。  
- **结构化存储**：每条 Prompt 存为单独 Markdown 文件，包含 `tags`、`category`、`description` 等元信息。  
- **标签过滤**：通过 `tags`（如 `python`、`writing`、`translation`）快速定位所需 Prompt。  
- **贡献友好**：开放 Issue 与 Pull Request，支持添加新 Prompt 或改进已有 Prompt。  
- **社区维护**：定期更新，已移除不再适用或错误的 Prompt，保证质量。  

## 功能概览
| 功能 | 说明 |
|------|------|
| Prompt 分类 | 按 `category`（如 `developer`、`writer`、`translator`）分组 |
| 标签搜索 | 使用 `tags` 进行多维度检索 |
| Markdown 结构 | 每条 Prompt 包含 `title`、`description`、`prompt`、`usage` |
| 贡献指南 | `CONTRIBUTING.md` 提供提交 Prompt 的规范 |
| 示例与说明 | 每条 Prompt 附带使用示例，帮助快速上手 |
| 兼容多语言 | 支持中文、英文等多语言 Prompt |
| 细粒度更新 | 只更新有变动的 Prompt，避免全量重建 |

## 用法
1. **克隆仓库**  
   ```bash
   git clone https://github.com/f/awesome-chatgpt-prompts.git
   cd awesome-chatgpt-prompts
   ```

2. **浏览 Prompt**  
   目录结构如 `prompts/<category>/<prompt_file>.md`，打开对应 Markdown 文件查看 Prompt 内容。

3. **复制 Prompt**  
   直接复制文件中 `prompt` 字段的文本，粘贴到 ChatGPT 的输入框即可。

4. **使用标签搜索**  
   在项目页面使用 “Find file” 或 `tags` 过滤器快速定位所需 Prompt。

5. **贡献新 Prompt**  
   - 在对应类别文件夹下新建 Markdown 文件，遵循已有模板。  
   - 提交 Pull Request，遵循 `CONTRIBUTING.md` 说明。

## 示例
```markdown
## Prompt 示例: 代码审查

**Description:**  
对给定的 Python 代码进行审查，指出潜在问题、改进建议及最佳实践。

**Prompt:**
```
Please review the following Python code and provide a detailed critique, including potential bugs, performance issues, and suggestions for improvement.  
[Insert code here]
```
```

---