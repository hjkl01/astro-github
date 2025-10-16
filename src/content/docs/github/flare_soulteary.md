
---
title: flare
---

# Flare 项目

## 项目地址
[https://github.com/soulteary/flare](https://github.com/soulteary/flare)

## 主要特性
Flare 是一个基于 Rust 开发的命令行工具，主要用于处理和转换 Markdown 文件。它支持高效的 Markdown 解析、渲染和导出功能，具有以下核心特性：
- **高性能解析**：利用 Rust 的速度优势，快速处理大型 Markdown 文件。
- **自定义模板**：支持用户定义 HTML/CSS 模板，实现灵活的输出样式。
- **多格式导出**：可将 Markdown 转换为 HTML、PDF 等格式。
- **插件扩展**：内置插件系统，支持数学公式（KaTeX）、代码高亮（Highlight.js）等扩展。
- **CLI 友好**：简洁的命令行界面，便于集成到工作流中。
- **跨平台支持**：兼容 Windows、macOS 和 Linux 系统。

## 主要功能
- **Markdown 渲染**：将 Markdown 转换为结构化的 HTML，支持标题、列表、图像、链接等标准元素。
- **主题定制**：内置多种预设主题，并允许用户自定义 CSS 样式。
- **批量处理**：支持目录扫描，一次性转换多个 Markdown 文件。
- **集成工具**：可与 Git、Pandoc 等工具结合使用，实现自动化文档生成。
- **错误处理**：提供详细的日志和错误反馈，便于调试。

## 用法
Flare 通过命令行安装和使用。首先，使用 Cargo（Rust 的包管理器）安装：
```
cargo install flare
```

### 基本命令
- **渲染单个文件**：
  ```
  flare input.md -o output.html
  ```
  这会将 `input.md` 转换为 `output.html`。

- **使用自定义模板**：
  ```
  flare input.md -t custom_template.html -o output.html
  ```
  指定模板文件 `custom_template.html`。

- **批量转换目录**：
  ```
  flare process ./docs/ -o ./output/
  ```
  处理 `docs` 目录下的所有 `.md` 文件，输出到 `output` 目录。

- **启用插件**：
  ```
  flare input.md --katex --highlight -o output.html
  ```
  启用 KaTeX（数学公式）和代码高亮插件。

### 高级选项
- `--theme <name>`：应用预设主题，如 `--theme default`。
- `--watch`：监视文件变化，自动重新渲染（适用于开发）。
- `--pdf`：直接导出为 PDF（需安装额外依赖，如 WeasyPrint）。

详细文档请参考项目 README。