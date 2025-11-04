
---
title: certificates
---

# smallstep/certificates 项目概览

- **项目地址**: <https://github.com/smallstep/certificates>

---

## 项目简介

`smallstep/certificates` 是一个轻量级的 **ACME**（自动化证书管理协议）实现，旨在为内部环境、CI/CD 流程和自托管平台提供安全、可扩展的证书颁发与续签解决方案。它共包含两个主要组件：

| 组件 | 作用 |
|------|------|
| **`step ca`** | 内置或容器化的 ACME CA，支持自签、交叉签和发布 CA 证书 |
| **`step cert`** | 用于交互式获取、续签和签发证书的 CLI 工具 |

---

## 主要特性

- **ACME 兼容**：支持 RFC 8555 规范，兼容 `certbot`、`acme.sh` 等常见 ACME 客户端。
- **面向内部网**：可在无公网 DNS 或 HTTP 访问的私有网络中使用，支持 HTTP、TLS-ALPN、DNS 等挑战方式。
- **实时证书签发**：支持批量导入 & 预签发、证书模板与属性自定义（如 SAN、重定向规则等）。
- **自签与交叉签**：可生成自签根证书或与外部 CA 进行交叉签署。
- **可扩展插件**：实现了 `step-ca` 通过 hook、模板、存储后端等方式可被轻松定制。
- **轻量级发布**：项目依赖少，支持以 Docker 镜像或二进制直接部署。

---

## 功能概要

1. **证书颁发**  
   - `step ca new`：创建或导入现有根/子 CA。  
   - `step ca issue`：以 ACME 挑战方式签发单个证书。  
   - `step ca issue --dns` / `--tls-alpn` / `--http-01`：支持多种验证方式。

2. **证书续签**  
   - `step ca renew`：批量检查并自动续签即将到期的证书。  
   - 配置 `config.json` 中 `renew_before`、`CRL` 等参数，实现自定义策略。

3. **证书管理**  
   - `step ca backup` / `step ca restore`：备份/恢复 CA 数据库。  
   - `step ca revocation`：吊销证书并更新 CRL。

4. **CLI 工具**  
   - `step cert install`：自动安装并配置证书在 Web 服务器（如 Nginx、Traefik）中。  
   - `step cert fetch`：从 ACME 服务器抓取并验证已有证书。

5. **API & SDK**  
   - RESTful API（`/acme`）符合 ACME 标准。  
   - Go SDK 供企业内部系统集成使用。

---

## 快速上手

1. **安装**  
   ```bash
   # 直接下载二进制
   curl -sL https://code.smallstep.com/step-cli/releases/latest/download/step_$(uname -s)_$(uname -m).tar.gz | tar xz -C /usr/local/bin

   # 或通过 Docker
   docker pull smallstep/step
   ```

2. **初始化 CA**  
   ```bash
   step ca init -- "my-org-ca" \
     --country "US" \
     --locality "San Francisco" \
     --province "California" \
     --organization "MyOrg" \
     --email "admin@myorg.local"
   ```

3. **签发证书**  
   ```bash
   step ca issue \
     --subject "CN=api.myorg.local" \
     --san "DNS:api.myorg.local" \
     api-myorg-local
   ```

4. **部署到服务器**  
   ```bash
   step cert install \
     --endpoint $(step ca endpoint) \
     --ca-bundle /path/to/ca-bundle.pem \
     --result /etc/ssl/api.myorg.local
   ```

5. **自动续签**  
   ```bash
   # cron 任务示例
   0 */12 * * * step ca renew
   ```

---

## 参考资料

- 官方文档: <https://smallstep.com/docs/>
- GitHub Repository: <https://github.com/smallstep/certificates>
- Docker Hub: <https://hub.docker.com/r/smallstep/step>

---

> *本文件保存在 `src/content/docs/00/certificates_smallstep.md`。*