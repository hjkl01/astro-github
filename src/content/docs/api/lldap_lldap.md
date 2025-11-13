---
title: lldap
---

**lldap**（Link-local login – Lightweight Access and Auth Service）  
项目地址: https://github.com/lldap/lldap  

### 主要特性  
- **自托管身份认证与授权**：使用 HTTPS + LDAP + OIDC 统一管理用户、组、权限。  
- **轻量级部署**：容器化 Docker + Docker‑Compose，或直接 `pip install`，文件式配置（`config.yaml`）。  
- **多协议兼容**：LDAP(目录服务)、OpenID Connect(单点登录）、SAML（可通过中间件支持）。  
- **静态网站+社会化登录**：支持 GitHub、Gitea、GitLab、Bitbucket OAuth。  
- **多租户**：通过域名/子域名分隔不同组织。  
- **内置后台 UI**：轻量 Web UI 用于账号、组、组织管理。  
- **访问控制**：基于 ACL 或权限组细粒度控制应用访问。  
- **高安全**：TLS 终端配置、密码哈希 Argon2id、JWT 规范。  
- **扩展性**：支持自定义鉴权插件、日志插件，Webhooks 可用于自动化。

### 功能概览  
| 功能 | 描述 |
|------|------|
| 用户管理 | 账号 CRUD，密码策略，双因素验证（TOTP） |
| 组管理 | 组成员管理，继承权限 |
| 组织/租户 | 支持多租户模式，组织知晓的域或子域 |
| OpenID Connect | 认证流程、Token 发行、Refresh Token |
| LDAP 兼容 | 传统 LDAP 查询、认证可直接与现有 LDAP 客户端兼容 |
| OAuth 统一 | GitHub、GitLab、Gitea 等外部 OAuth 提供者统一登录 |
| 权限控制 | ACL（基于资源路径） 或 Scope（针对 API） |
| UI 管理 | 账号、组、组织、许可证的可视化管理 |
| 日志 & 监控 | 访问日志、错误日志，支持 Loki/Prometheus 集成 |

### 用法示例  

1. **Docker 部署**  
```bash
# 克隆项目
git clone https://github.com/lldap/lldap.git
cd lldap
# 创建配置文件（可通过 UI 初次配置）
cp conf.sample.yaml conf.yaml

# 启动
docker-compose up -d
```

2. **配置 (`conf.yaml`)**  
```yaml
server:
  host: 0.0.0.0
  port: 8000
  tls:
    enabled: true
    cert: /path/to/fullchain.pem
    key: /path/to/privkey.pem

database:
  url: postgres://user:pass@postgres:5432/lldap

authorization:
  - pattern: /api/*
    methods: [GET, POST]
    scopes: [read, write]
```

3. **访问管理 UI**  
打开浏览器访问 `https://<域名>/admin`，使用管理员账号登录，进行用户、组、组织的增删改。  

4. **使用 OIDC**  
使用客户端（如前端或浏览器插件）配置：
- **Redirect URI**: `https://<域名>/auth/callback`
- **Client ID** / **Secret** 从 UI 生成  
前端示例（JavaScript）：
```js
import { UserManager } from 'oidc-client';
const mgr = new UserManager({
  authority: 'https://<域名>/auth',
  client_id: 'myapp',
  redirect_uri: 'https://myapp.com/callback',
  response_type: 'code',
  scope: 'openid profile email'
});
mgr.signinRedirect();
```

5. **LDAP 查询示例**  
```bash
ldapsearch -H ldap://<域名> -D "cn=admin,dc=lldap,dc=org" -w adminpwd -b "dc=lldap,dc=org" "(uid=alice)"
```

6. **权限控制**  
在 `conf.yaml` 中配置 `authorization`，例如：
```yaml
authorization:
  - pattern: /repos/*
    methods: [GET]
    groups: [devs, managers]
```
用户归入 `devs` 或 `managers` 的组即可访问该路径。

7. **Docker Compose 现场配置**  
```yaml
services:
  lldap:
    image: ghcr.io/lldap/lldap:latest
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/lldap
      - LLDAP_HOST=0.0.0.0
      - LLDAP_PORT=80
    ports:
      - "80:80"
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=lldap
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
```

### 进一步资源  
- 官方文档: `https://lldap.io/docs/`  
- API 参考: `https://lldap.io/docs/api/`  

> 所有配置、部署和使用示例均以中文记录，项目可在 GitHub 仓库获取更完整说明。