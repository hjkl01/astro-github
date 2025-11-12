---
title: sftpgo
---

# SFTPGo 项目概述

使用 SFTPGo，您可以利用本地和云存储后端，使用您已经熟悉的相同工具和流程，在内部或与业务伙伴交换和存储文件。

## 项目地址

[GitHub 项目地址](https://github.com/drakkan/sftpgo)

## 主要特性

SFTPGo 是一个功能丰富的、完全功能化的、基于 Go 语言编写的 SFTP 服务器实现。它是一个高度可配置的事件驱动文件传输解决方案，支持多种协议，包括 SFTP、HTTP/S、FTP/S 和 WebDAV，并提供灵活的存储后端选项。核心特性包括：

- **多协议支持**：支持 SFTP（SSH 文件传输协议）、HTTP/S、FTP/S（文件传输协议与安全扩展）和 WebDAV（Web 分布式创作和版本控制），允许用户通过多种方式访问文件。
- **虚拟文件系统**：支持本地文件系统、加密本地文件系统、S3 兼容对象存储（如 AWS S3、MinIO）、Google Cloud Storage、Azure Blob Storage 和外部 SFTP 服务器作为后端，提供虚拟化文件管理。
- **用户管理和认证**：内置用户管理，支持内部用户、外部认证（如 LDAP、OAuth2、OIDC）和多因素认证（2FA）。用户可以有独立的配额、权限和元数据。
- **安全性**：支持 TLS/SSL 加密、IP 白名单/黑名单、速率限制、证书管理，以及对常见攻击的防护（如暴力破解）。
- **Web 管理界面**：提供现代化的 Web 界面，用于管理用户、配置服务器和监控活动，支持 API 集成。

- **Web 客户端界面**：允许最终用户在浏览器中更改凭据、浏览和管理文件，并设置与 Microsoft Authenticator、Google Authenticator、Authy 等兼容应用配合使用的两因素认证。
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

更多细节请参考项目文档：[官方文档](https://docs.sftpgo.com/)。

## 赞助商

SFTPGo 致力于开源。核心功能免费提供并维护。如果您在项目中依赖 SFTPGo，请考虑成为[赞助商](https://github.com/sponsors/drakkan)，以帮助确保其长期可持续性。

您的赞助有助于覆盖维护、安全更新和开源版本的持续开发。

### 感谢我们的赞助商

#### 白金赞助商

[![Aledade logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/Aledade_logo.png)](https://www.aledade.com/)

[![Jump Trading logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/jumptrading.png)](https://www.jumptrading.com/)

[![WP Engine logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/wpengine.png)](https://wpengine.com/)

#### 白银赞助商

[![IDCS logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/IDCS.png)](https://idcs.ip-paris.fr/)

#### 青铜赞助商

[![7digital logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/7digital.png)](https://www.7digital.com/)

[![servinga logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/servinga.png)](https://servinga.com/)

[![ReUI logo](https://raw.githubusercontent.com/drakkan/sftpgo/main/img/reui.png)](https://www.reui.io/)

## 支持

开源版本的 SFTPGo 是免费使用的，遵循其许可证条款。我们致力于提供强大且功能完整的版本，以满足许多生产环境的需求。

虽然我们不提供免费的直接支持，但社区支持可通过 [GitHub Discussions](https://github.com/drakkan/sftpgo/discussions) 获得，您可以在那里提问、分享反馈并与其他用户互动。

如果您需要保证的支持、专家指导或高级功能，请考虑使用 SFTPGo Enterprise：SFTPGo 的商业许可版本，扩展了开源版本，具有企业专用功能和完整支持。

SFTPGo Enterprise 以两种部署选项提供：

- 本地部署：在您自己的基础设施上部署，具有完全控制和商业级支持。更多详情：[sftpgo.com/on-premises](https://sftpgo.com/on-premises)
- 完全托管 SaaS：让我们处理基础设施。理想选择，用于安全、可扩展和维护-free 设置，并包含完整支持。更多详情：[sftpgo.com/saas](https://sftpgo.com/saas)

## 国际化

翻译通过 [Crowdin](https://crowdin.com/project/sftpgo) 提供，他们为我们提供了开源许可证。

在开始翻译之前，请查看我们的贡献 [指南](https://sftpgo.github.io/latest/web-interfaces/#internationalization)。

## 发布节奏

SFTPGo 遵循功能驱动的发布周期，而不是固定的时间-based 调度。目前，我们的主要开发工作集中在 [Enterprise edition](https://docs.sftpgo.com/enterprise/#enterprise-edition)，它从更快的发布节奏中受益，并接收主要新功能（参见 [changelog](https://docs.sftpgo.com/enterprise/changelog/)）。

这个开源版本的 SFTPGo 保持维护，并将继续接收错误修复和基本更新。但是，不是所有在 Enterprise edition 中引入的增强功能都将在此处可用。

## 致谢

SFTPGo 使用 go.mod 中列出的第三方库。

我们非常感谢所有通过想法和/或拉取请求贡献的人。

感谢 [ysura](https://www.ysura.com/) 为我们提供稳定的 AWS S3 测试账户访问。

感谢 [KeenThemes](https://keenthemes.com/) 为我们提供自定义许可证，以使用他们的优秀 [themes](https://keenthemes.com/bootstrap-templates) 用于 SFTPGo WebAdmin 和 WebClient 用户界面，在开源和开源核心版本中。

感谢 [Crowdin](https://crowdin.com/) 为我们提供开源许可证。

感谢 [Incode](https://www.incode.it/) 帮助我们改进 UI/UX。
