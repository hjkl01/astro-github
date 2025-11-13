---
title: Cloudreve
---

## 项目简介

Cloudreve 是一个自托管的文件管理和分享系统，支持多种存储提供商。它允许用户通过 Web 界面管理文件、上传下载、分享链接，并提供丰富的预览和编辑功能。

## 主要功能

- **多存储支持**：支持本地存储、远程节点、OneDrive、S3 兼容 API、七牛云 Kodo、阿里云 OSS、腾讯云 COS、华为云 OBS、金山云 KS3、又拍云等。
- **直接传输**：客户端直接与存储提供商进行上传/下载，提高效率。
- **后台下载**：集成 Aria2/qBittorrent，支持后台下载，使用多个下载节点分担负载。
- **文件操作**：压缩/解压/预览归档文件，支持批量下载。
- **WebDAV 支持**：覆盖所有存储提供商的 WebDAV 协议。
- **上传功能**：支持拖拽上传文件或文件夹，并行断点续传。
- **元数据提取**：从文件中提取媒体元数据，按元数据或标签搜索文件。
- **用户管理**：支持多用户和多组管理。
- **分享功能**：创建文件和文件夹的分享链接，支持设置过期日期。
- **在线预览**：预览视频、图片、音频、ePub 文件。
- **在线编辑**：编辑文本、图表、Markdown、图片、Office 文档。
- **自定义界面**：自定义主题颜色、暗模式、PWA 应用、单页应用 (SPA)、国际化 (i18n)。
- **开箱即用**：一体化打包，所有功能无需额外配置。

## 使用方法

### 部署

1. **快速测试部署**：参考 [快速开始](https://docs.cloudreve.org/overview/quickstart) 进行本地部署测试。
2. **生产环境部署**：参考 [部署指南](https://docs.cloudreve.org/overview/deploy/) 进行完整部署。

### 构建

从源码构建 Cloudreve，请参考 [构建指南](https://docs.cloudreve.org/overview/build/)。

### 贡献

如果您想为 Cloudreve 贡献代码，请参考 [贡献指南](https://docs.cloudreve.org/api/contributing/)。

## 技术栈

- 后端：Go + Gin + ent
- 前端：React + Redux + Material-UI

## 许可证

GPL V3
