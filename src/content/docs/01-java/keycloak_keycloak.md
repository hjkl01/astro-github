---
title: keycloak
---

# Keycloak 项目

**GitHub 项目地址:** [https://github.com/keycloak/keycloak](https://github.com/keycloak/keycloak)

## 主要特性

Keycloak 是一个开源的身份和访问管理（IAM）解决方案，主要用于为现代应用程序和微服务提供认证、授权和用户管理功能。它基于 Java 开发，支持多种协议和标准，具有以下核心特性：

- **单点登录 (SSO)**: 支持 SAML 2.0 和 OpenID Connect (OIDC) 协议，实现跨应用的无缝登录体验。
- **用户管理**: 内置用户注册、登录、密码管理、角色和权限分配，支持多租户（realm）架构。
- **社交登录集成**: 支持 Google、Facebook、GitHub 等社交提供商的身份验证。
- **联邦身份管理**: 可以与 LDAP、Active Directory 等外部身份提供商集成，实现身份联邦。
- **OAuth 2.0 支持**: 提供令牌端点（token endpoint），支持客户端凭证、授权码等授权流程。
- **多因素认证 (MFA)**: 支持 OTP（一次性密码）等额外的安全层。
- **管理控制台**: 提供 Web-based 管理界面，便于配置 realm、客户端和用户。
- **可扩展性**: 支持自定义主题、SPI（服务提供者接口）扩展，以及容器化部署（如 Docker）。
- **安全性**: 内置 CSRF 保护、会话管理、事件日志和审计功能。
- **社区支持**: 开源项目，由 Red Hat 维护，活跃的社区和文档。

## 主要功能

Keycloak 的功能聚焦于安全身份管理，适用于 Web 应用、移动应用、API 和微服务架构。具体包括：

- **认证服务**: 处理用户登录、会话管理和注销，支持浏览器和 REST API 认证。
- **授权服务**: 基于角色（RBAC）和基于属性的访问控制（ABAC），管理资源和作用域。
- **用户联合**: 与外部 IdP（如 Kerberos）集成，实现单一身份源。
- **客户端适配器**: 提供 Java、JavaScript、.NET 等语言的适配器，便于集成到现有应用。
- **报告和监控**: 内置事件监听器，支持导出事件到外部系统如 Elasticsearch。
- **主题和 UI 自定义**: 允许修改登录页面和电子邮件模板。
- **离线令牌支持**: 用于长期访问的刷新令牌机制。

## 用法

### 安装和部署

1. **下载和运行**: 从 [官方网站](https://www.keycloak.org/downloads.html) 下载最新版本。解压后运行：
   ```
   bin/kc.sh start-dev
   ```
   或使用 Maven 从源码构建：`mvn clean install`。
2. **Docker 部署**: 使用官方 Docker 镜像快速启动开发模式：
   ```
   docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev
   ```
   访问 `http://localhost:8080` 配置管理控制台。
3. **生产部署**: 配置数据库（如 PostgreSQL），启用 HTTPS，并使用 OptaPlanner 优化性能。参考官方文档进行集群模式设置。

### 配置和使用

1. **创建 Realm**: 在管理控制台中创建一个新的 realm（领域），用于隔离不同应用的用户和配置。
2. **注册客户端**: 为你的应用添加客户端（Client），配置重定向 URI、协议（OIDC/SAML）和访问类型（public/confidential）。
3. **用户管理**: 添加用户、组和角色。启用用户自注册和密码策略。
4. **集成应用**:
   - **Web 应用**: 使用 Keycloak JavaScript 适配器在前端集成登录按钮。
   - **API 保护**: 配置客户端凭证流程，应用使用 Keycloak 令牌验证 API 请求。
   - 示例（Java Spring Boot 集成）：
     ```xml
     <dependency>
         <groupId>org.keycloak</groupId>
         <artifactId>keycloak-spring-boot-starter</artifactId>
     </dependency>
     ```
     在 `application.yml` 中配置 Keycloak 服务器 URL 和 realm。
5. **测试**: 使用管理控制台的“测试”功能验证认证流程，或运行端到端测试。

更多细节请参考官方文档：[Keycloak Documentation](https://www.keycloak.org/docs/latest/)。项目适用于企业级身份管理场景，支持从开发到生产的完整生命周期。
