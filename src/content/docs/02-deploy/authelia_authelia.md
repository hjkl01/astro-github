
---
title: authelia
---

# Authelia 项目

## 项目地址
[GitHub 项目地址](https://github.com/authelia/authelia)

## 主要特性
Authelia 是一个开源的认证和授权服务器，专为保护应用程序和资源而设计。它提供轻量级、高性能的访问控制解决方案，支持多种身份验证方法。主要特性包括：
- **多因素认证 (MFA)**：支持 TOTP、WebAuthn 和移动应用（如 Authy）等第二因素认证，提升安全性。
- **单点登录 (SSO)**：基于 OpenID Connect (OIDC) 协议，实现跨多个应用的统一登录体验。
- **访问控制**：细粒度的访问策略，支持基于角色 (RBAC) 和属性的访问控制 (ABAC)，可限制特定用户或组的访问。
- **轻量级设计**：无需数据库后端，仅需文件配置或轻量存储，支持高可用部署。
- **集成性强**：无缝集成 Nginx、Traefik、HAProxy 等反向代理，以及 LDAP、SAML 等身份提供商。
- **通知与日志**：内置电子邮件通知、事件日志记录，以及与外部系统的集成（如 Slack、Discord）。

## 主要功能
- **认证流程**：用户通过用户名/密码登录，支持密码策略（如最小长度、复杂性要求）和账户锁定机制防止暴力破解。
- **授权决策**：根据配置文件定义访问规则，例如允许/拒绝特定路径或域名的访问。
- **会话管理**：支持可配置的会话持续时间和重定向逻辑，确保安全注销。
- **身份联邦**：与外部身份提供商集成，实现联邦身份验证。
- **监控与审计**：提供详细的审计日志，便于合规性和故障排查。

## 用法
### 安装与配置
1. **前提条件**：确保系统安装 Go 语言环境（或使用 Docker），并准备配置文件 `configuration.yml`。
2. **快速启动（Docker）**：
   ```
   docker run -d --name authelia authelia/authelia:latest
   ```
   挂载配置文件和 secrets（如 JWT 密钥、SMTP 设置）。

3. **配置文件示例**（configuration.yml）：
   ```yaml
   jwt_secret: your_jwt_secret
   default_redirection_url: https://example.com

   server:
     host: 0.0.0.0
     port: 9091

   authentication_backend:
     file:
       path: /config/users_database.yml
       password:
         argon2id: # 密码哈希配置

   access_control:
     default_policy: deny
     rules:
       - domain: example.com
         policy: two_factor
         subject:
           - "group:admin"

   session:
     secret: your_session_secret
     expiration: 1h
     inactivity: 5m

   storage:
     local:
       path: /config/db.sqlite3

   notifier:
     smtp:
       host: smtp.example.com
       port: 587
   ```

4. **集成反向代理（Nginx 示例）**：
   在 Nginx 配置中添加：
   ```
   location / {
       auth_request /authelia/api/verify;
       error_page 401 =302 /authelia/?rd=$request_uri;
       auth_request_set $user $upstream_http_x_forwarded_user;
       auth_request_set $groups $upstream_http_x_forwarded_groups;
   }

   location /authelia {
       proxy_pass http://authelia:9091;
   }
   ```

5. **部署与运行**：
   - 使用 Docker Compose 启动 Authelia 和反向代理。
   - 访问保护的 URL 时，会自动重定向到 Authelia 登录页面。
   - 用户管理：在 `users_database.yml` 中添加用户和组，例如：
     ```yaml
     users:
       john:
         displayname: "John Doe"
         password: "$argon2id$v=19$m=65536,t=3,p=4$..." # 使用 authelia hash-password 生成
         groups: [users, admin]
     ```

更多详情请参考官方文档：https://www.authelia.com/docs/。