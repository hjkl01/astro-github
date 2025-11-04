
---
title: document
---


# Ranuts 文档生成工具

- **项目地址**：<https://github.com/ranuts/document>

## 项目概览
Ranuts 文档生成工具是一个基于 **VuePress** 的轻量级静态文档生成器，专为 **ranuts** 生态提供高质量、可维护的项目文档。它能够自动扫描源码、提取注释、生成结构化文档，并支持多语言、主题自定义、插件扩展等功能。

## 主要特性
| 特性 | 说明 |
|------|------|
| **自动化文档生成** | 通过解析源码注释（JSDoc、TSDoc）自动生成 API 文档、组件使用说明、示例代码。 |
| **多语言支持** | 内置 i18n 模块，可在同一站点展示多语言文档（如中文、英文）。 |
| **主题定制** | 支持官方主题、暗黑模式及自定义 CSS，满足品牌视觉需求。 |
| **插件生态** | 可通过插件扩展功能，例如 Markdown 语法扩展、图表渲染、搜索增强等。 |
| **持续集成友好** | 与 CI/CD 流水线（GitHub Actions、GitLab CI 等）无缝集成，自动部署到 GitHub Pages、Vercel、Netlify 等。 |
| **易于维护** | 文档结构基于文件夹/Markdown，易于团队协作，支持 Pull Request 直接更新文档。 |

## 安装与使用

```bash
# 1. 克隆仓库
git clone https://github.com/ranuts/document.git
cd document

# 2. 安装依赖
npm install   # 或者 yarn

# 3. 生成静态站点
npm run docs:build   # 生成 dist/docs

# 4. 本地预览
npm run docs:dev
```

### 配置说明
- `docs/.vuepress/config.js`：全局配置文件，支持主题、导航、侧边栏、插件等设置。
- `docs/.vuepress/public`：放置静态资源（图片、字体等）。
- `docs/.vuepress/locales`：多语言翻译文件夹。

### 文档结构
```
docs/
├─ README.md            # 项目概览
├─ guide/
│  ├─ introduction.md   # 入门指南
│  └─ advanced.md       # 高级使用
├─ api/
│  ├─ component.md      # 组件 API
│  └─ service.md        # 服务 API
└─ assets/
   └─ logo.png
```

## 贡献指南
1. Fork 本仓库并创建 Feature 分支。  
2. 编写或修改 Markdown 文档，保持语法一致。  
3. 提交 Pull Request，附上简短说明。  
4. 维护者将会在 24 小时内进行评审。

## 常见问题
| 问题 | 解决办法 |
|------|----------|
| 页面加载慢 | 检查 `config.js` 中的 `head` 标签，移除不必要的脚本。 |
| 文档中文乱码 | 确认文件编码为 UTF-8，且 `head` 中 `<meta charset="utf-8">` 正确。 |
| 主题不生效 | 清除浏览器缓存或强制刷新；检查 `themeConfig` 是否正确。 |

---

> **提示**：若想将文档部署到 GitHub Pages，请在仓库 `settings → Pages` 中将源设置为 `gh-pages` 分支，或使用 `npm run docs:deploy` 自动部署。

``` 
