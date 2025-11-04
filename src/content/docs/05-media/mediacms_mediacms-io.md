
---
title: mediacms
---


# MediCMS

**项目地址**  
<https://github.com/mediacms-io/mediacms>

## 项目简介  
MediCMS 是一款基于 Node.js、React 与 ffmpeg 的开源媒体中心平台。它提供完整的多媒体内容管理、转码、分发以及权限控制，支持直播与点播，兼容 HLS、DASH、RTMP 等主流流媒体协议。

---

## 主要特性

| # | 功能 | 说明 |
|---|------|------|
| 1 | **多媒体内容管理** | 支持视频、音频、图片、文档等文件的上传、编辑、分类、标签、搜索与批量操作。 |
| 2 | **自动转码** | 使用 ffmpeg 将原始文件转码为 MP4、HLS、DASH、WebM 等多种格式，并可按需求生成多分辨率、字幕、音轨。 |
| 3 | **直播与点播** | 兼容 RTMP 推流，自动生成 HLS/DASH 播放地址；支持点播播放、播放列表、章节分割。 |
| 4 | **权限与用户管理** | 基于角色的访问控制（管理员、编辑、观众），支持多租户与 API Key 授权。 |
| 5 | **响应式前端** | React + Redux，支持桌面与移动端浏览器。 |
| 6 | **RESTful API** | 提供完整的 API 接口，便于与第三方系统（CMS、CRM、支付等）集成。 |
| 7 | **插件架构** | 通过插件机制可轻松扩展功能（例如 DRM、字幕下载、统计分析等）。 |
| 8 | **监控与日志** | 内置日志系统、性能监控与错误告警，支持 Grafana、Prometheus 等工具。 |

---

## 功能概述

1. **媒体库**：可视化管理所有媒体资源，支持批量上传与多字段筛选。  
2. **转码工作流**：上传后自动触发 ffmpeg 转码，支持任务队列与重试机制。  
3. **流媒体服务**：提供 HLS/DASH 播放地址，兼容 JW Player、Video.js 等播放器。  
4. **直播推流**：接收 RTMP 推流，实时转码并推送给 CDN。  
5. **权限控制**：基于 JWT 或 Session 的身份验证，细粒度权限配置。  
6. **API 文档**：Swagger UI 自动生成，方便前后端协同开发。  
7. **插件开发**：通过 `plugin` 目录添加自定义功能，插件可独立发布。  

---

## 安装与使用

### 先决条件

- Node.js ≥ 14  
- npm 或 yarn  
- ffmpeg（已安装在 PATH）  
- PostgreSQL / MySQL / SQLite（根据需求选择）  

### 克隆源码

```bash
git clone https://github.com/mediacms-io/mediacms.git
cd mediacms
```

### 安装依赖

```bash
# 使用 npm
npm install

# 或者使用 yarn
yarn install
```

### 配置环境

复制示例配置文件并根据实际情况修改：

```bash
cp .env.example .env
# 编辑 .env
# 例如：
# DATABASE_URL=postgres://user:pass@localhost:5432/mediacms
# FFMP4_PATH=/usr/bin/ffmpeg
```

### 初始化数据库

```bash
# 运行迁移
npm run migrate
# 或者
yarn migrate
```

### 启动项目

```bash
# 开发模式 (热重载)
npm run dev
# 或者
yarn dev

# 打包后启动
npm run build
npm start
# 或者
yarn build
yarn start
```

### 访问

浏览器打开 `http://localhost:3000`，即可访问前端管理界面。  
API 接口默认在 `http://localhost:3000/api`。

---

## 部署建议

- **Docker**：项目已提供 `Dockerfile` 与 `docker-compose.yml`，适合快速部署。  
- **CI/CD**：可结合 GitHub Actions 自动构建与发布。  
- **CDN**：将 HLS/DASH 片段推送至 CDN，提升播放性能。  

---

## 贡献

欢迎提交 Issue 与 PR。请遵循项目的 [CONTRIBUTING](https://github.com/mediacms-io/mediacms/blob/main/CONTRIBUTING.md) 指南。

---

> *本文件仅包含项目核心信息，供快速了解与使用。*
