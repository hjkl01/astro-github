---
title: casdoor
---

# Casdoor 项目

## 项目地址

[GitHub 项目地址](https://github.com/casdoor/casdoor)

## 主要特性

Casdoor 是一个开源的身份和访问管理 (IAM) 平台，基于 Go 语言开发，支持现代化的身份认证和授权机制。主要特性包括：

- **多协议支持**：兼容 OAuth 2.0、OIDC、SAML 等标准协议，便于与其他系统集成。
- **用户管理**：提供用户注册、登录、权限管理和角色分配功能，支持多租户架构。
- **访问控制**：基于 RBAC (Role-Based Access Control) 和 ABAC (Attribute-Based Access Control) 的细粒度权限控制。
- **多因素认证 (MFA)**：集成 TOTP 和 WebAuthn 等安全认证方式，提升安全性。
- **前端友好**：内置响应式 Web UI，支持自定义主题和多语言（包括中文）。
- **可扩展性**：模块化设计，支持插件扩展和 API 驱动的集成。
- **数据存储**：支持 MySQL、PostgreSQL 等数据库，以及 Casbin 作为权限引擎。

## 主要功能

- **身份提供商 (IdP)**：作为身份提供商，支持单点登录 (SSO) 和联合身份认证。
- **应用集成**：快速配置 OAuth 客户端，支持 Web、移动和 API 应用。
- **组织管理**：支持多组织、多部门的用户分组和权限隔离。
- **审计日志**：记录用户操作和访问事件，便于合规审计。
- **API 网关**：内置网关功能，实现 API 认证和限流。
- **自托管**：完全开源，可部署在私有云或本地环境中。

## 在线演示

- 只读站点：https://door.casdoor.com（任何修改操作将失败）
- 可写站点：https://demo.casdoor.com（原始数据每 5 分钟恢复一次）

## 文档

https://casdoor.org

## 安装

- 通过源代码：https://casdoor.org/docs/basic/server-installation
- 通过 Docker：https://casdoor.org/docs/basic/try-with-docker
- 通过 Kubernetes Helm：https://casdoor.org/docs/basic/try-with-helm

## 如何连接到 Casdoor？

https://casdoor.org/docs/how-to-connect/overview

## Casdoor 公共 API

- 文档：https://casdoor.org/docs/basic/public-api
- Swagger：https://door.casdoor.com/swagger

## 集成

https://casdoor.org/docs/category/integrations

## 用法

1. **安装部署**：
   - 克隆仓库：`git clone https://github.com/casdoor/casdoor.git`
   - 安装依赖：使用 Docker 快速启动（推荐），运行 `docker-compose up`。
   - 或者本地构建：安装 Go 环境，运行 `go build` 并启动服务器。

2. **配置**：
   - 编辑 `conf/app.conf` 文件，设置数据库连接、JWT 密钥等参数。
   - 通过 Web 界面初始化管理员账户。

3. **使用**：
   - 访问 Web UI (默认端口 8000)，创建应用和用户。
   - 集成到其他项目：使用 OAuth 流程，客户端重定向到 Casdoor 登录页面。
   - API 调用：通过 RESTful API 管理用户，例如 `/api/login` 进行认证。
   - 扩展：自定义适配器或插件以集成第三方服务如 LDAP 或微信登录。

更多详情请参考项目文档：[Casdoor 文档](https://casdoor.org/docs/overview)。

## 贡献

对于 Casdoor，如果您有任何问题，可以提出 Issues，或者也可以直接发起 Pull Requests（但我们推荐先提出 issues 与社区沟通）。

### I18n 翻译

如果您为 casdoor 贡献，请注意我们使用 [Crowdin](https://crowdin.com/project/casdoor-site) 作为翻译平台和 i18next 作为翻译工具。当您在 `web/` 目录中使用 i18next 添加一些单词时，请记得将添加的内容添加到 `web/src/locales/en/data.json` 文件中。

## 如何联系？

- Discord：https://discord.gg/5rPsrAzK7S
- 联系：https://casdoor.org/help
