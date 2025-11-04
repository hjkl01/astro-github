
---
title: tinymist
---

# tinymist  
*(https://github.com/Myriad-Dreamin/tinymist)*

---

## 项目简介  
tinymist 是一个小型、轻量级的 Markdown 文档处理工具，旨在快速将 Markdown 文本转化为结构化数据、提供实时预览以及支持内嵌代码片段的执行。它主要用于本地文档编写、教学示例、技术博客的快速渲染及社区内部知识库的构建。

---

## 主要特性  

| 功能 | 说明 |
|------|------|
| **Markdown 解析** | 支持 GitHub Flavored Markdown（GFM），包括表格、任务列表、脚注等扩展。 |
| **实时预览** | 通过内置的 VS Code 插件或 CLI，实时在浏览器/终端中预览渲染结果。 |
| **代码执行** | 识别 `<script lang="js">`、`<script lang="ts">`、`<script lang="python">` 等标签，支持在同一文件内交互式跑代码，输出结果与 Markdown 同步。 |
| **插件化 API** | 通过 `tinymist` API 能自定义 Markdown 渲染器（e.g. Prism.js高亮）或扩展语法。 |
| **轻量部署** | 仅依赖 Node.js / Deno，安装后即能通过命令行或 npm package 直接使用，整个项目体积小于 10 MB。 |
| **跨平台** | 在 Windows、macOS、Linux 上均可正常运行。 |

---

## 用法

### 1. 安装

```bash
# 通过 npm
npm i -g tinymist

# 或者 via yarn
yarn global add tinymist
```

> 依赖 Node 20+ 或 Deno 1.45+。若想在项目中单独使用，可改为本地 devDependency：

```bash
npm i -D tinymist
```

### 2. 基本命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `tinymist serve <docs_dir>` | 启动本地服务器，实时预览 `<docs_dir>` 下所有 markdown | `tinymist serve ./docs` |
| `tinymist build <docs_dir> -o <output>` | 生成静态 HTML 或 JSON，适用于托管 | `tinymist build ./docs -o ./public` |
| `tinymist preview <file>` | 在浏览器单独预览单文件 | `tinymist preview README.md` |
| `tinymist convert <file> --format=html|json` | 仅转换文件 | `tinymist convert chapter1.md --format=html` |

### 3. 运行内嵌代码

在 Markdown 文件中写入：

```md
Here is a quick demo:

```js
function greet(name) {
  return `Hello, ${name}!`;
}
greet('world');
```

The result will be displayed below the code block.
```

`tinymist` 会自动识别 `<js>`、`<ts>`, `<py>` 代码块，并在渲染时执行，输出放在后面。

### 4. 配置文件

在项目根目录放置 `tinymist.yml`（YAML或JSON均可）：

```yaml
# tinymist.yml
serve:
  port: 8080
  open: true
build:
  format: html
  minify: true
plugins:
  - prism  # 安装并使用 Prism.js 高亮
```

> 也可通过 CLI 选项覆盖这些设置。

### 5. 在 VS Code 中使用

1. 安装官方扩展：`TinyMIST Enhancer`  
2. 打开 Markdown 文件，按 `Ctrl+Shift+P` → `Tinymist: Preview`  
3. 在侧边栏实时查看渲染结果，并可直接执行代码块。

---

## 典型使用场景

| 场景 | 说明 |
|------|------|
| **技术博客** | 用 Markdown 写文章，同时插入可执行代码，让读者现场看到结果。 |
| **教学笔记** | 在笔记中插入代码示例，保持可执行性，适合实验课程。 |
| **文档化** | 将 API 文档作为 Markdown 生成 HTML，附带代码演示。 |
| **知识库** | 通过 `tinymist build` 生成静态站点，部署到 GitHub Pages 或 Netlify。 |

---

## 贡献指南

1. Fork → Clone → `npm i`  
2. 新建分支 `feat/xxxx` 或 `fix/xxxx`  
3. 编写代码/测试 → 提交 PR  
4. PR 通过 CI 后即合并

> 详细说明请参见仓库根目录的 `CONTRIBUTING.md`。

---

## 许可证

MIT License – 详情见 `LICENSE` 文件。

---

> **项目地址**：[https://github.com/Myriad-Dreamin/tinymist](https://github.com/Myriad-Dreamin/tinymist)