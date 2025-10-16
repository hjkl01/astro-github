
---
title: Cloudreve
---

# Cloudreve 项目

## 项目地址
[GitHub 项目地址](https://github.com/cloudreve/Cloudreve)

## 主要特性
Cloudreve 是一个开源的云盘系统，支持多种存储后端（如本地存储、阿里云 OSS、腾讯云 COS、OneDrive 等），具有高性能、易部署和可扩展性强的特点。主要特性包括：
- **多存储支持**：兼容本地文件系统、对象存储服务和云存储 API，灵活配置存储策略。
- **用户管理**：支持多用户注册、权限控制、文件夹共享和访问限制。
- **文件操作**：上传、下载、预览、分享、搜索和批量管理文件，支持断点续传和大文件处理。
- **安全机制**：文件加密、访问日志、IP 白名单和防盗链功能，确保数据安全。
- **界面友好**：响应式 Web 界面，支持移动端访问，内置主题和自定义选项。
- **扩展性**：支持插件系统和 API 接口，便于二次开发和集成。

## 主要功能
- **文件存储与同步**：用户可上传文件到云端，支持实时同步和版本控制。
- **分享与协作**：生成分享链接，支持密码保护、有效期设置和外链下载。
- **预览与编辑**：内置 Office、PDF、图片和视频预览，支持在线编辑集成（如 OnlyOffice）。
- **管理员面板**：监控系统资源、用户行为和存储使用情况，提供备份和恢复功能。
- **API 支持**：RESTful API 接口，可与第三方应用集成，如 WebDAV 协议支持。

## 用法
### 部署步骤
1. **环境准备**：确保服务器安装 Go 1.15+、MySQL 5.7+ 或 SQLite，以及 Nginx/Apache 等 Web 服务器。推荐使用 Docker 快速部署。
2. **下载与安装**：
   - 从 GitHub Releases 下载最新二进制文件或使用 `go install github.com/cloudreve/Cloudreve/v3@latest` 编译。
   - 配置 `cloudreve.ini` 文件，设置数据库连接、存储策略和监听端口。
3. **启动服务**：
   - 运行 `./cloudreve -p 8020`（默认端口 8020）。
   - 使用 Docker：`docker run -d -p 8020:8020 --name cloudreve cloudreve/cloudreve`。
4. **Web 访问**：浏览器打开 `http://your-server-ip:8020`，初始用户名/密码为 `admin/123456`，立即修改密码。
5. **配置存储**：在管理面板中添加存储策略（如阿里云 OSS），测试连接后启用。
6. **用户使用**：
   - 注册新用户，登录后上传文件。
   - 创建文件夹、分享文件或通过 API 集成。
   - 管理员可在后台管理用户和策略。

更多详情请参考项目 Wiki：https://github.com/cloudreve/Cloudreve/wiki