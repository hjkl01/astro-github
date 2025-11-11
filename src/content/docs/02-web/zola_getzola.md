---
title: zola
---

# Zola

Zola 是一个快速的静态站点生成器，用 Rust 编写，所有功能都内置在一个单一的二进制文件中。它旨在提供一个简单、高效的方式来构建静态网站，而无需复杂的设置或外部依赖。

## 主要功能

- **单二进制**：无需安装多个组件，一切都包含在一个可执行文件中。
- **语法高亮**：支持代码块的语法高亮。
- **Sass 编译**：内置 Sass/SCSS 编译器，用于样式处理。
- **资产共置**：允许将静态资产与内容文件放在一起。
- **多语言站点支持**：基本支持多语言网站。
- **图像处理**：内置图像处理功能，如调整大小和优化。
- **主题**：支持可重用的主题系统。
- **短代码**：允许在 Markdown 中使用自定义短代码。
- **内部链接**：智能处理内部链接。
- **外部链接检查器**：检查外部链接的有效性。
- **目录自动生成**：自动为页面生成目录。
- **自动标题锚点**：为标题添加锚点链接。
- **别名**：支持页面别名。
- **分页**：内置分页支持。
- **自定义分类法**：允许定义自定义分类和标签。
- **搜索**：无需服务器或第三方服务的内置搜索功能。
- **实时重载**：开发时支持实时重载。
- **易于部署**：支持部署到 Netlify、Vercel、Cloudflare Pages 等平台。

## 用法

### 安装

从 [GitHub Releases](https://github.com/getzola/zola/releases) 下载最新版本的二进制文件，或从源码构建：

```bash
cargo install zola
```

### 创建新站点

```bash
zola init my_site
cd my_site
```

这将创建一个基本的站点结构，包括 `config.toml`、`content/` 和 `templates/` 目录。

### 添加内容

在 `content/` 目录中添加 Markdown 文件。例如，创建一个 `content/_index.md` 作为首页，或 `content/posts/my-post.md` 作为博客文章。

### 构建站点

```bash
zola build
```

这将在 `public/` 目录中生成静态文件。

### 本地预览

```bash
zola serve
```

启动本地服务器，默认在 `http://127.0.0.1:1111` 运行，支持实时重载。

### 配置

编辑 `config.toml` 文件来自定义站点设置，如标题、描述、主题等。

更多详细信息，请参考 [官方文档](https://www.getzola.org/documentation/getting-started/overview/)。
