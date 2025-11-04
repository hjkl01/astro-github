
---
title: mkdocs-material
---

# mkdocs-material（squidfunk）

> **GitHub 地址**: <https://github.com/squidfunk/mkdocs-material>

## 项目概述
mkdocs-material 是一个基于 **MkDocs** 的主题，专为技术文档、博客和项目手册设计。它提供了现代化、响应式的 UI、可自定义的导航、搜索与主题切换等功能，帮助开发者快速构建美观且易用的文档站点。

## 主要特性
- **响应式布局**：在桌面、平板和移动设备上均表现优秀。
- **主题切换**：默认支持明暗模式，可通过自定义 CSS 或 JavaScript 进一步扩展。
- **侧边栏导航**：支持多层级导航、自动生成目录、可配置 `nav`。
- **搜索功能**：集成 `mkdocs-search`，支持全文搜索、主题高亮。
- **插件生态**：可与 MkDocs 官方插件（如 `mkdocs-minify-plugin`、`mkdocs-redirects`）无缝配合。
- **自定义页面**：支持 Markdown、HTML、Jinja2 模板，方便扩展页面内容。
- **图表与代码高亮**：内置 `mermaid`、`plantuml`、`kroki` 支持；使用 Pygments 进行代码高亮。
- **多语言支持**：通过 `mkdocs-i18n` 或自定义配置实现多语言站点。
- **部署简易**：可通过 GitHub Pages、Netlify、ReadTheDocs 等平台一键部署。

## 功能与使用

### 1. 安装
```bash
pip install mkdocs-material
```

### 2. 配置文件 `mkdocs.yml`
```yaml
site_name: 我的文档
theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
    - scheme: slate
      primary: indigo
      accent: indigo
  icon:
    repo: fontawesome/brands/github
nav:
  - Home: index.md
  - Guides:
      - Getting Started: guides/getting-started.md
      - Advanced: guides/advanced.md
plugins:
  - search
```

### 3. 创建 Markdown 文件
```markdown
# 欢迎
欢迎使用 mkdocs-material。
```

### 4. 预览 & 生成
```bash
mkdocs serve          # 本地预览
mkdocs build          # 生成静态文件
```

### 5. 部署
- **GitHub Pages**：将 `site/` 目录推送至 `gh-pages` 分支。
- **Netlify**：直接部署 `site/` 或配置 `build` 选项。
- **ReadTheDocs**：在 `docs/` 目录下放置 `conf.py`，使用 MkDocs 构建。

## 进一步阅读
- 官方文档: <https://squidfunk.github.io/mkdocs-material/>
- 插件列表: <https://squidfunk.github.io/mkdocs-material/plugins/>

---