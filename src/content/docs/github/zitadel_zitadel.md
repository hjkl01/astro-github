
---
title: zitadel
---

# Zitadel

## 项目地址  
[https://github.com/zitadel/zitadel](https://github.com/zitadel/zitadel)

## 主要特性  
- **开源身份与访问管理（IAM）**：提供统一身份、会话、权限与多因素认证。  
- **标准兼容**：支持 OAuth2、OpenID Connect、SAML、SCIM 等行业标准。  
- **多租户与可插拔**：支持多租户架构，身份源、协议、权限策略可插拔。  
- **高可用与可扩展**：基于 Kubernetes 原生，水平扩展、滚动升级。  
- **审计与合规**：完整审计日志，满足 GDPR、HIPAA 等合规要求。  

## 核心功能  
- **用户管理**：自助注册、登录、密码重置、用户信息同步。  
- **多因素认证**：OTP、WebAuthn、短信、邮件等多种 MFA。  
- **权限与角色**：细粒度 RBAC、资源级权限配置。  
- **应用集成**：OAuth2 客户端、OIDC 代理、SAML SP/IDP。  
- **API 网关**：自动生成、统一鉴权、速率限制。  
- **审计日志**：可查询、导出、满足合规需求。  

## 快速上手  

```bash
# 克隆仓库
git clone https://github.com/zitadel/zitadel.git
cd zitadel

# 安装官方 Helm Chart
helm repo add zitadel https://charts.zitadel.io
helm install zitadel zitadel/zitadel --namespace zitadel --create-namespace

# 端口转发访问 UI
kubectl port-forward svc/zitadel-ui 8080:80 -n zitadel
```

浏览器访问 `http://localhost:8080`，按向导完成管理员账户创建。

## 文档与支持  
- 官方文档: https://zitadel.com/docs  
- 社区讨论: https://github.com/zitadel/zitadel/discussions  
- 贡献指南: https://github.com/zitadel/zitadel/blob/master/CONTRIBUTING.md