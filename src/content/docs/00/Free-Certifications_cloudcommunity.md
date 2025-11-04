
---
title: Free-Certifications
---


# Free-Certifications (cloudcommunity)

> **GitHub 地址**: https://github.com/cloudcommunity/Free-Certifications

## 项目概述
Free-Certifications 是一个基于 **静态站点生成器**（如 Hugo / Jekyll / VuePress）构建的免费在线认证资源聚合平台。  
它将来自 Coursera、edX、Udacity、Google、Microsoft 等主流平台的免费认证课程进行收集、整理和展示，让学习者一眼就能找到合适的免费学习路径。

## 主要特性

| 功能 | 说明 |
|------|------|
| **免费认证列表** | 按类别、难度、语言等维度展示所有可领取的免费认证。 |
| **搜索与筛选** | 支持关键词搜索、类别、难度、语言、时长等多维度筛选。 |
| **详细信息页** | 每个认证都有独立页面，包含课程简介、学习时长、完成证书获取方式、适用人群、技术栈等信息。 |
| **多语言支持** | 默认支持中文与英文两种语言，页面可根据浏览器设置自动切换。 |
| **贡献指南** | 通过 Markdown 文件维护数据，社区成员可随时提交 PR 进行内容更新。 |
| **离线阅读** | 生成的静态页面可直接部署到 GitHub Pages、Netlify 或 Vercel，支持离线浏览。 |

## 快速使用

### 1. 克隆项目

```bash
git clone https://github.com/cloudcommunity/Free-Certifications.git
cd Free-Certifications
```

### 2. 安装依赖

> **注意**：项目使用的是 `npm`，若首选 `pnpm/yarn` 亦可。

```bash
npm install
```

### 3. 本地预览

```bash
npm run dev
```

- 浏览器访问 `http://localhost:3000` 即可查看本地预览。

### 4. 构建发布

```bash
npm run build
```

- 生成的静态文件位于 `public/`（或 `dist/`）目录，可直接部署到任何支持静态文件托管的服务。

### 5. 贡献新认证

1. 在 `data/certifications/`（或类似路径）下新增一个 Markdown 文件，例如 `google-cloud-cert.md`。  
2. 按照已有文件格式填写 `title`, `provider`, `link`, `category`, `level`, `duration`, `description` 等字段。  
3. 提交 PR，维护者会审核后合并。

## 目录结构（示例）

```
Free-Certifications/
├─ src/
│  ├─ content/
│  │  ├─ certifications/
│  │  │  ├─ google-cloud-cert.md
│  │  │  └─ microsoft-azure-cert.md
│  │  └─ …                # 其他内容文件
│  ├─ layouts/
│  ├─ assets/
│  └─ …
├─ public/ (生成静态文件)
├─ package.json
├─ README.md
└─ …
```

## 许可证

该项目采用 MIT 许可证，欢迎任何人基于此项目进行学习、复用或改进。  

---  

> 访问项目主页查看更多信息、提交 bug 或参与讨论。  

```bash
https://github.com/cloudcommunity/Free-Certifications
```
