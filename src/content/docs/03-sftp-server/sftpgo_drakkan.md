---
title: sftpgo
---

# SFTPGo 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/drakkan/sftpgo)

## 主要特性
SFTPGo 是一个功能丰富的、完全功能化的、基于 Go 语言编写的 SFTP 服务器实现。它支持多种协议，包括 SFTP、FTP/S 和 WebDAV，并提供灵活的存储后端选项。核心特性包括：
- **多协议支持**：支持 SFTP（SSH 文件传输协议）、FTP/S（文件传输协议与安全扩展）和 WebDAV（Web 分布式创作和版本控制），允许用户通过多种方式访问文件。
- **虚拟文件系统**：支持本地文件系统、S3 兼容对象存储（如 AWS S3、MinIO）、加密存储和外部 SFTP 服务器作为后端，提供虚拟化文件管理。
- **用户管理和认证**：内置用户管理，支持内部用户、外部认证（如 LDAP、OAuth2、OIDC）和多因素认证（2FA）。用户可以有独立的配额、权限和元数据。
- **安全性**：支持 TLS/SSL 加密、IP 白名单/黑名单、速率限制、证书管理，以及对常见攻击的防护（如暴力破解）。
- **Web 管理界面**：提供现代化的 Web 界面，用于管理用户、配置服务器和监控活动，支持 API 集成。
- **扩展性和可移植性**：跨平台支持（Linux、Windows、macOS），支持 Docker 部署，轻量级且易于扩展。
- **其他特性**：事件钩子（webhooks）、日志记录、数据加密、备份/恢复功能，以及与外部工具的集成。

## 主要功能
- **文件传输与管理**：用户可以通过 SFTP、FTP 或 WebDAV 上传、下载、删除和重命名文件，支持大文件传输和断点续传。
- **存储后端灵活性**：可以配置本地磁盘、云存储（如 Google Cloud Storage、Azure Blob）或数据库（如 SQLite、PostgreSQL、MySQL）作为元数据存储。
- **权限控制**：细粒度权限设置，包括读/写/执行权限、目录遍历限制和路径映射。
- **监控与报告**：实时监控连接、传输日志和审计报告，支持导出日志到外部系统。
- **自动化集成**：通过 REST API 和 webhooks 实现自动化脚本和第三方集成，例如与 CI/CD 管道结合。

## 用法指南
### 安装
1. **二进制安装**（推荐简单环境）：
   - 从 GitHub Releases 下载适用于你的平台的预编译二进制文件。
   - 解压并运行：`./sftpgo serve`（默认监听端口 2022 for SFTP，8080 for Web UI）。

2. **Docker 安装**（推荐生产环境）：
   - 拉取镜像：`docker pull drakkan/sftpgo:latest`。
   - 运行容器：`docker run -d -p 2022:2022 -p 8080:8080 -v /path/to/config:/srv/sftpgo drakkan/sftpgo:latest`。
   - 配置卷挂载以持久化数据。

3. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/drakkan/sftpgo.git`。
   - 安装 Go（1.18+），然后运行 `go build` 和 `go install`。

### 配置
- 编辑配置文件 `sftpgo.json` 或使用环境变量。
- 关键配置项：
  - `bind_port`：设置 SFTP 监听端口。
  - `httpd.bind_port`：Web 界面端口。
  - `data_provider`：选择数据存储（如 "sqlite"）。
  - `s3fs`：配置 S3 后端凭证。
- 初始化数据库：首次运行时自动创建，或手动使用 `sftpgo initprovider`。

### 使用步骤
1. **启动服务器**：运行 `sftpgo serve`，访问 `http://localhost:8080` 登录 Web 界面（默认 admin/admin）。
2. **创建用户**：
   - 在 Web 界面中添加用户，设置用户名、密码、家庭目录和权限。
   - 示例：用户名 "testuser"，密码 "password"，目录 "/home/testuser"。
3. **连接客户端**：
   - SFTP：使用工具如 FileZilla 或命令行 `sftp testuser@localhost -P 2022`。
   - FTP：`ftp localhost:2121`（需启用 FTP）。
   - WebDAV：通过浏览器或客户端连接 `http://localhost:8090/webdav`。
4. **管理文件**：通过客户端上传/下载文件，服务器会根据配置处理存储和权限。
5. **高级用法**：
   - 配置外部认证：编辑 `external_auth_hook` 以集成 LDAP。
   - 监控：查看日志文件或使用 API 查询 `/api/v2/connections`。
   - 更新：定期拉取新版本并重启服务。

更多细节请参考项目文档：[官方文档](https://github.com/drakkan/sftpgo/wiki)。