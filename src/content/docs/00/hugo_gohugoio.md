
---
title: hugo
---

# Hugo: 静态网站生成器

**GitHub 项目地址:** <https://github.com/gohugoio/hugo>

## 主要特性

- **快速生成**：使用 Go 语言编译，构建速度快，生成大型站点时仅需几秒或几分钟。
- **多主题支持**：内置主题系统，支持自定义主题。通过目录结构 `themes/` 加载或直接在项目根目录放置主题文件。
- **多语言（i18n）**：自带多语言支持，可配置每个页面和内容的语言版本。
- **内容类型**：支持 Markdown、Org、Asciidoc 等多种写作格式。数据文件（YAML、TOML、JSON）用于存储结构化内容。
- **模板**：基于 Go text/template，实现灵活的模板继承和标签功能。
- **资源处理**：图片优化、压缩、WebP 生成等，提供资源管道（Asset Pipeline）。
- **本地服务器**：内置 `hugo server`，支持热重载，实时预览。
- **部署**：输出静态文件，适合直接托管于 GitHub Pages、Netlify、Vercel 等静态托管平台。
- **插件系统**：通过 Shortcodes 和 Render Hooks 可扩展功能和页面内容。

## 核心功能

1. **内容管理**  
   - **内容文件**：放在 `content/` 目录下，以目录分层方式组织。  
   - **Front Matter**：每篇文章顶部的 YAML/TOML/JSON 块，用于设置标题、日期、标签、分类等元数据。  

2. **模板渲染**  
   - **布局文件**：位于 `layouts/`，包含 `baseof.html`（布局骨架），各种页面类型（`single.html`、`list.html`）和组件（`partials/`）。  
   - **主题**：选择 `themes/` 下的主题目录，自动落库。

3. **搜索与导航**  
   - 通过多站点、分页、分类/标签列表、RSS 订阅实现网站导航。  
   - 支持 Hugo 自带的短代码 `[<a href="...">link](...), [<img src="...">]` 等。

4. **多站点**  
   - 一个仓库中可有多个 `site`，共享内容、主题、静态资源，适合多语言、多范畴的站点。

5. **Asset Pipeline**  
   - `resources` 支持 CSS、JS、图片的组合、压缩、转换。  
   - 用 `{{ .Resources.Get "style.scss" | resources.ToCSS | minify }}` 简单调用。

## 使用方法

```bash
# 安装 Hugo (示例：Homebrew)
brew install hugo

# 创建新站点
hugo new site mywebsite

# 进入站点目录
cd mywebsite

# 添加主题（以ananke为例）
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo 'theme = "ananke"' >> config.toml

# 添加内容
hugo new posts/hello-world.md

# 编辑 posts/hello-world.md，添加 Front Matter 和 Markdown 内容

# 本地预览
hugo server --listen 1313

# 生成静态文件
hugo
```

- **配置文件**：`config.toml`（或 `config.yaml` / `config.json`）中设置 URL、语言、主题、菜单等。  
- **自定义**：复制 `themes/{theme}/layouts/` 到项目根目录 `layouts/` 进行覆盖。  
- **部署**：运行 `hugo` 生成 `public/` 目录，全部内容为静态文件，可直接上传至任何 Web 服务器或静态托管平台。

## 典型工作流程

| 步骤 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `hugo new site myproject` | 创建站点骨架 |
| 选择主题 | 添加子模块或直接复制 | 设置 `theme` |
| 编写内容 | `hugo new posts/XXX.md` | 在 `content/` 写文章 |
| 预览 | `hugo server` | 实时热重载 |
|  `hugo` | 输出 `public/` |
| 部署 | `git push origin master` + CI/CD 或手动上传 | 发布到生产环境 |

---

> 以上是对 Hugo 项目的简要中文概述，便于快速了解其核心特性、功能与基本使用流程。