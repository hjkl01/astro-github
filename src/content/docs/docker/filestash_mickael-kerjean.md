
---
title: filestash
---

# Filestash 项目

## 项目地址
[GitHub 项目地址](https://github.com/mickael-kerjean/filestash)

## 主要特性
Filestash 是一个开源的文件管理器和 WebDAV 服务器，支持多种存储后端（如本地文件系统、SFTP、FTP、S3、Dropbox 等）。它提供了一个现代化的 Web 界面，用于远程文件访问、管理和同步。主要特性包括：
- **多协议支持**：兼容 WebDAV、SFTP、FTP 等协议，便于集成到各种环境中。
- **文件管理功能**：支持文件上传、下载、编辑、重命名、删除、压缩/解压等操作。
- **跨平台访问**：通过浏览器访问，无需安装客户端，支持移动设备。
- **安全特性**：内置用户认证、加密传输（HTTPS），并支持 LDAP 和 OAuth 集成。
- **插件扩展**：可自定义插件，支持如 Office Online 编辑器集成。
- **轻量级部署**：容器化支持（Docker），易于在服务器、NAS 或云环境中运行。

## 主要功能
- **文件浏览器**：直观的界面浏览目录结构，支持预览图片、视频、文档等文件。
- **同步与备份**：实现文件同步，支持版本控制和自动备份。
- **协作工具**：多人共享文件夹，权限管理，便于团队协作。
- **API 接口**：提供 RESTful API，用于自动化脚本或第三方应用集成。
- **性能优化**：支持大文件传输、断点续传，适用于企业级文件存储。

## 用法
1. **安装部署**：
   - 使用 Docker：运行命令 `docker run -d -p 8334:8334 -v /path/to/data:/data filesh/filestash`（替换 `/path/to/data` 为本地数据目录）。
   - 手动安装：从 GitHub 下载源码，安装 Node.js 和依赖，然后运行 `npm install && npm start`。
   - 支持其他方式如 Helm（Kubernetes）或直接在 Linux/Mac/Windows 上部署。

2. **配置**：
   - 访问 `http://your-server:8334`，设置管理员账户。
   - 在界面中添加存储后端（如 SFTP 服务器的 IP、端口、凭证）。
   - 配置 WebDAV 路径和用户权限。

3. **日常使用**：
   - 登录后，选择存储源，浏览文件。
   - 上传文件：拖拽或点击上传按钮，支持批量操作。
   - 编辑文件：集成如 OnlyOffice 或 LibreOffice Online。
   - 共享：生成临时链接或设置权限共享给他人。
   - 监控：查看日志和使用统计。

项目适合个人云存储、NAS 管理或企业文件服务器使用，文档详见 GitHub 仓库的 README。