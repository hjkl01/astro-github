---
title: cloudreve-docker
---

# Cloudreve Docker 项目

## 项目地址
[https://github.com/justxuewei/cloudreve-docker](https://github.com/justxuewei/cloudreve-docker)

## 主要特性
- **基于 Docker 的部署**：提供一键式 Docker 容器化部署方案，支持快速安装和运行 Cloudreve 文件管理服务。
- **多存储后端支持**：兼容本地存储、阿里云 OSS、腾讯云 COS、七牛云、OneDrive 等多种云存储，提供灵活的文件存储选项。
- **用户友好界面**：内置 Web 管理面板，支持多用户管理、文件分享、权限控制和在线预览。
- **安全性增强**：集成 SSL 支持、登录验证码和访问控制，确保数据安全。
- **轻量级与可扩展**：容器化设计，便于扩展和维护，支持自定义配置。

## 主要功能
- **文件上传与管理**：支持大文件分片上传、批量操作、文件夹管理。
- **分享与协作**：生成分享链接，支持密码保护和有效期设置，实现文件协作。
- **在线编辑与预览**：内置 Office Online、PDF 查看器等，支持文档直接编辑和预览。
- **策略配置**：自定义存储策略、用户组权限、回收站功能。
- **API 接口**：提供 RESTful API，便于集成到其他应用中。

## 用法
1. **环境准备**：确保系统安装 Docker 和 Docker Compose。
2. **克隆仓库**：运行 `git clone https://github.com/justxuewei/cloudreve-docker.git` 下载项目。
3. **配置**：编辑 `docker-compose.yml` 文件，设置数据库（SQLite/MySQL）、存储后端和端口等参数。
4. **启动服务**：在项目目录执行 `docker-compose up -d` 启动容器。
5. **访问管理面板**：浏览器打开 `http://localhost:5212`（默认端口），默认用户名/密码为 `admin/123456`，立即修改密码。
6. **高级配置**：通过环境变量或卷挂载自定义数据持久化、SSL 证书等。参考仓库 README 获取详细命令和故障排除。