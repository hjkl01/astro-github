
---
title: mermaid
---

# Mermaid 项目

## 项目地址
[GitHub 项目地址](https://github.com/mermaid-js/mermaid/blob/develop/README.zh-CN.md)

## 主要特性
Mermaid 是一个基于 JavaScript 的工具，用于通过简单的文本语法生成图表和流程图。它支持多种图表类型，包括流程图、序列图、甘特图、饼图、类图、状态图、实体关系图和用户旅程图等。主要特性包括：
- **文本驱动**：使用 Markdown-like 的语法定义图表，无需图形编辑工具。
- **实时渲染**：集成到 Markdown 编辑器或网页中，支持实时预览和渲染。
- **开源免费**：基于 MIT 许可，支持浏览器、Node.js 等环境。
- **主题自定义**：提供内置主题，并允许用户自定义样式。
- **导出支持**：可导出为 SVG、PNG 等格式。
- **插件扩展**：易于集成到各种框架，如 GitHub、Notion、Typora 等。

## 主要功能
- **流程图（Flowchart）**：描述过程或算法的步骤，支持从上到下、从左到右等方向。
- **序列图（Sequence Diagram）**：展示对象间的交互序列，常用于 API 设计。
- **甘特图（Gantt Chart）**：项目管理中的时间线表示，支持任务依赖和里程碑。
- **饼图（Pie Chart）**：简单的数据比例可视化。
- **类图（Class Diagram）**：UML 类图，用于软件设计。
- **状态图（State Diagram）**：展示状态机或有限状态机的转换。
- **实体关系图（ER Diagram）**：数据库设计中的实体和关系表示。
- **用户旅程图（User Journey）**：用户体验流程的映射。
- **其他**：包括 Git 图、要求图、包图等高级功能。

## 用法
### 安装
- **浏览器使用**：通过 CDN 引入脚本，例如：
  ```html
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({startOnLoad:true});</script>
  ```
- **Node.js**：使用 npm 安装 `npm install mermaid`，然后导入并渲染。
- **集成工具**：在 Markdown 编辑器中启用 Mermaid 插件，如 VS Code 的 Mermaid Preview 扩展。

### 基本语法示例
使用代码块语法 ````mermaid` 定义图表。

**流程图示例**：
```
graph TD
    A[开始] --> B{决策?}
    B -->|是| C[操作1]
    B -->|否| D[结束]
    C --> D
```

在支持的环境中，此代码将渲染为流程图。更多语法详见官方文档中的各章节。