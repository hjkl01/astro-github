---
title: gitea
---

# Gitea 项目

**项目地址：** [https://github.com/go-gitea/gitea](https://github.com/go-gitea/gitea/blob/master/README_ZH.md)

## 主要特性

Gitea 是一个轻量级的 Git 服务端实现，使用 Go 语言开发，旨在提供一个自托管的 Git 仓库管理平台。它类似于 GitHub 或 GitLab，但更注重简洁、高效和低资源消耗。主要特性包括：

- **自托管和开源**：完全开源（MIT 许可），可以轻松部署在个人服务器、NAS 或 VPS 上，支持 Docker 和二进制安装。
- **Git 仓库管理**：支持创建、克隆、推送和拉取 Git 仓库，提供完整的版本控制功能。
- **Web 界面**：直观的 Web UI，支持代码浏览、提交历史、分支管理、合并请求（Pull Requests）和问题跟踪（Issues）。
- **用户和权限管理**：支持多用户注册、组织/团队协作、细粒度权限控制（如读/写/管理权限）。
- **集成与扩展**：内置 CI/CD 支持（通过 Actions）、Wiki、标签、里程碑、通知系统；可集成 LDAP、OAuth、邮件服务器等外部服务。
- **多语言支持**：包括完整的中文界面和文档。
- **轻量高效**：资源占用低，可在 Raspberry Pi 等低端设备上运行，支持 SQLite、MySQL、PostgreSQL 等数据库后端。
- **移动端友好**：响应式设计，支持手机访问。

## 主要功能

- **代码托管**：托管无限数量的 Git 仓库，支持私有和公共仓库。
- **协作工具**：问题跟踪、合并请求、代码审查、@提及通知、评论系统。
- **自动化**：Gitea Actions 提供 GitHub Actions 兼容的 CI/CD 管道，支持自定义工作流。
- **附加功能**：文件上传、代码搜索、钩子（Hooks）支持、API 接口（RESTful API）、主题自定义、Fediverse 集成（ActivityPub）。
- **安全特性**：两因素认证（2FA）、CSRF 保护、签名提交验证。

## 用法

### 安装
1. **二进制安装**（推荐简单环境）：
   - 下载最新发布版：从 GitHub Releases 下载适用于你的系统的二进制文件。
   - 解压并运行：`./gitea web` 启动服务，默认监听 3000 端口。
   - 配置数据库：在 `app.ini` 文件中设置数据库连接。

2. **Docker 安装**：
   ```
   docker run -d -p 3000:3000 -p 222:22 --name gitea -v /path/to/data:/data gitea/gitea:latest
   ```
   - 访问 `http://localhost:3000` 初始化管理员账户。

3. **从源码构建**：
   - 安装 Go（1.19+）和 Git。
   - 克隆仓库：`git clone https://github.com/go-gitea/gitea.git`。
   - 构建：`make build`。
   - 运行：`./gitea web`。

### 基本用法
1. **初始化**：首次访问 Web 界面，设置站点标题、数据库、管理员账户。
2. **创建仓库**：登录后，点击“新建仓库”，选择类型（Git 或迁移现有仓库）。
3. **克隆和推送**：
   - 克隆：`git clone http://your-server:3000/username/repo.git`。
   - 推送：使用标准 Git 命令推送代码。
4. **协作**：创建 Issue 或 Pull Request，通过 Web UI 审查和合并。
5. **配置**：编辑 `custom/conf/app.ini` 文件自定义设置，如 SMTP 邮件通知或 SSH 密钥支持。
6. **升级**：备份数据后，从 Releases 下载新版替换二进制文件，或使用 `make build` 重新构建。

更多详细用法请参考官方文档：[Gitea 文档](https://docs.gitea.com/zh-cn/)。