
---
title: parlant
---


# Parlant 项目
**GitHub 地址**  
[https://github.com/emcie-co/parlant](https://github.com/emcie-co/parlant)

## 主要特性

| # | 特性 | 简介 |
|---|------|------|
| 1 | **轻量级结构** | 仅依赖核心 Node.js 与标准插件，体积小，启动快。 |
| 2 | **模块化插件体系** | 通过 `parlant-plugin-*` 依赖，轻松扩展功能。 |
| 3 | **命令行工具** | `parlant-cli` 支持项目初始化、构建、启动、插件管理等。 |
| 4 | **支持多语言** | 通过 `i18n` 模块，项目内文案可多语言切换。 |
| 5 | **主题与布局可定制** | 采用 Handlebars/HTML 模板，可自由更换主题或开发自定义布局。 |
| 6 | **静态资源快速构建** | 内置 Gulp/rollup，支持 Sass/ES6/ES Module 的编译和压缩。 |
| 7 | **服务器端渲染(SSR)** | 可配置为纯静态或 SSR，适配 Vercel、Netlify 等平台部署。 |

## core 功能

- **项目结构生成**： `parlant init <project-name>` 自动生成文件夹、`package.json` 等基础文件。  
- **开发服务器**： `parlant dev` 开启热重载模式，实时预览。  
- **构建发布**： `parlant build` 生成 `dist/`，可直接上传至 CDN。  
- **插件管理**： `parlant plugin add <name>`, `parlant plugin remove <name>`，插件按需下载。  
- **多主题切换**：`parlant theme list`, `parlant theme switch <theme>`。  
- **i18n 渲染**：通过 `#lang {key}` 语法在模板中插入多语言字符串。  

## 快速上手

```bash
# 1. 安装 CLI（全局或项目内部）
npm install -g parlant-cli          # 全局安装
# 或者
npm i -D parlant-cli                # 项目内部安装

# 2. 创建新项目
parlant init my-awesome-site

# 3. 进入项目目录
cd my-awesome-site

# 4. 开发调试
parlant dev

# 5. 构建发布
parlant build

# 6. 本地预览构建产物
parlant preview
```

### 插件使用示例

```bash
# 添加 Markdown 处理插件
parlant plugin add parlant-plugin-md

# 删除插件
parlant plugin remove parlant-plugin-md
```

### 主题切换示例

```bash
# 查看可用主题
parlant theme list

# 切换主题
parlant theme switch dark-mode
```

---

> 该项目的详细使用说明已在根目录的 `README.md` 和 `docs/` 目录下说明，包含 API 文档、主题开发教程与插件开发规范。若需进一步了解插件架构与自定义功能，请参考官方文档。 

