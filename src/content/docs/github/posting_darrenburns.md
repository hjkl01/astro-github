
---
title: posting
---

# darrenburns/posting

> 项目地址：[https://github.com/darrenburns/posting](https://github.com/darrenburns/posting)

## 主要特性

- **轻量级静态博客生成器**：用 Markdown + front‑matter 写作，自动生成整合网站
- **Command‑line 工具**：`posting new`、`posting build`、`posting serve` 等命令一键完成开发与发布
- **支持标签、分类、目录**：在前置信息中声明，生成归档页面
- **自动 RSS/Atom 订阅**：更新后即时同步
- **可自定义主题**：通过 CSS & 模板配置自定义展示风格
- **发布至 GitHub Pages**：打包后直接推送到指定仓库，零成本托管
- **缓存与压缩优化**：自动缓存已生成文件，并可开启 Minify
- **跨平台**：兼容 Windows / macOS / Linux，Python 3+ 运行

## 用法示例

```bash
# 安装
pip install posting

# 初始化项目
posting init

# 新建文章
posting new "我的第一篇文章"

# 本地预览
posting serve

# 生成静态文件
posting build

# 推送到 GitHub Pages（需配置 .yml）
posting deploy
```

> **提示**：配置文件默认位于 `.posting.yml`，包括 `output_dir`、`baseurl`、`theme` 等常用参数。

---

> 举例配置片段 (`.posting.yml`)

```yaml
output_dir: "_site"
baseurl: "/blog"
theme: "default"
collections:
  posts:
    path: "posts"
    template: "post.html"
```
