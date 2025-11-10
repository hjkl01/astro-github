---
title: aliyunpan
---

# AliyunPan 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/liupan1890/aliyunpan)

## 主要特性
AliyunPan 是一个开源的阿里云盘客户端项目，主要用于实现对阿里云盘（Aliyun Drive）的 WebDAV 协议支持和文件管理功能。它具有以下主要特性：
- **WebDAV 支持**：允许通过 WebDAV 协议访问和管理阿里云盘文件，支持与第三方工具（如文件管理器、同步软件）集成。
- **多平台兼容**：支持 Windows、macOS 和 Linux 等操作系统，提供命令行和图形界面选项。
- **文件同步与传输**：实现文件上传、下载、同步和分享功能，支持大文件处理和断点续传。
- **开源与自定义**：基于 Go 语言开发，代码开源，便于用户自定义扩展和二次开发。
- **安全机制**：集成阿里云盘的 OAuth 认证，支持加密传输，确保数据安全。

## 主要功能
- **认证与登录**：通过阿里云账号登录，支持 Refresh Token 持久化，避免频繁登录。
- **文件操作**：浏览目录、上传/下载文件、创建文件夹、删除/重命名文件、搜索文件。
- **分享管理**：生成分享链接、设置分享密码和过期时间。
- **同步功能**：双向同步本地文件与云盘，支持实时监控和冲突解决。
- **API 集成**：提供 RESTful API 接口，便于与其他应用集成。
- **日志与监控**：内置日志记录和错误处理，支持性能监控。

## 用法
1. **安装**：
   - 下载最新 Release 版本的二进制文件，或通过 Go 安装：`go install github.com/liupan1890/aliyunpan@latest`。
   - 对于 WebDAV 模式，确保安装 WebDAV 客户端（如 Cyberduck 或 Windows 资源管理器）。

2. **配置**：
   - 运行 `aliyunpan config` 初始化配置。
   - 使用 `aliyunpan login` 通过浏览器登录阿里云账号，获取 Access Token。
   - 编辑配置文件（通常在 `~/.aliyunpan/config.json`），设置 WebDAV 端口（如 8080）和根目录。

3. **基本命令**：
   - **启动 WebDAV 服务**：`aliyunpan webdav --port=8080`。然后在 WebDAV 客户端连接 `http://localhost:8080/dav`。
   - **文件上传**：`aliyunpan upload /local/path /cloud/path`。
   - **文件下载**：`aliyunpan download /cloud/path /local/path`。
   - **列出文件**：`aliyunpan ls /cloud/path`。
   - **同步文件夹**：`aliyunpan sync /local/folder /cloud/folder`。

4. **高级用法**：
   - 支持 Docker 部署：使用官方 Dockerfile 构建镜像。
   - 对于图形界面，可结合第三方工具如 rclone 配置阿里云盘后端。
   - 详细文档参考项目 README 和 Wiki 页面。

注意：使用前确保遵守阿里云服务条款，避免滥用导致账号限制。