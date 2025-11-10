---
title: How-To-Ask-Questions-The-Smart-Way
---


# How to Ask Questions: The Smart Way

**项目地址**  
[https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)

## 主要特性

| 功能 | 说明 |
|------|------|
| **完整的提问指南** | 以 Markdown 形式提供的系统化提问流程，涵盖标题、描述、代码、错误信息等关键要素。 |
| **可复用模板** | `templates/` 目录下的预设模板，可直接复制粘贴到问答平台（如 Stack Overflow、GitHub Issues 等）。 |
| **示例与案例** | `examples/` 目录收录多种常见场景（编程语言、工具、框架）下的提问示例，帮助快速定位问题。 |
| **交互式测验** | `quiz/` 目录提供基于 `quiz.js` 的命令行测验，检验用户对提问要点的掌握。 |
| **多语言支持** | 除英文外，还提供简体中文、繁体中文等多语言版本，便于不同读者使用。 |
| **可视化思维导图** | `diagrams/` 中的 Mermaid 图表展示提问流程的可视化结构，适合教学与演示。 |

## 功能说明

1. **提问流程**  
   - **标题**：简洁、明确、包含关键词。  
   - **描述**：完整背景、已尝试的解决方案、具体错误。  
   - **代码**：最小可复现例子，使用代码块格式。  
   - **标签**：为问题添加合适的标签，提升可见性。  

2. **模板使用**  
   ```bash
   # 复制模板到当前目录
   cp templates/question.md .
   # 编辑后直接粘贴到 Q&A 平台
   ```

3. **交互式测验**  
   ```bash
   npm install
   node quiz/quiz.js
   ```
   通过测验，快速检验并巩固提问技巧。  

4. **多语言切换**  
   - 通过 `i18n/` 目录下的 `*.json` 文件切换语言。  
   - 例如：`i18n/zh-CN.json` 为简体中文版本。  

5. **演示与分享**  
   - 在 Markdown 文件中嵌入 Mermaid 图表：  
     ```mermaid
     graph TD;
         A[Title] --> B[Description];
         B --> C[Code];
         C --> D[Tags];
     ```  

## 用法示例

```markdown
**标题**：JavaScript 中如何在 Promise 链中捕获错误？

**描述**：我正在使用 async/await 处理异步请求，但在某些情况下会出现未捕获的错误。请问应该如何在 Promise 链中添加错误处理？

**代码**：
```js
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}

fetchData()
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

**标签**：javascript, async-await, promise
```

> 复制上述内容，粘贴到 Stack Overflow 或其他 Q&A 平台，即可获得更高质量的回答。  

---
> 以上是对 **How to Ask Questions: The Smart Way** 项目的简要说明。请根据自身需求，结合 `README.md` 进一步探索和使用。