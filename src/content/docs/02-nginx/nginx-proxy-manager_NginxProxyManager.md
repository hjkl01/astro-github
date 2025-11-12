---
title: nginx-proxy-manager
---

# Nginx Proxy Manager

**GitHub项目地址:** [https://github.com/NginxProxyManager/nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

## 主要特性

Nginx Proxy Manager 是一个基于 Web 的界面，用于管理 Nginx 代理主机。它通过用户友好的 Web UI 简化了 Nginx 反向代理、SSL 证书和访问控制的管理。主要特性包括：

- 基于 Web 的管理界面
- 通过 Let's Encrypt 自动 SSL 证书配置
- HTTP/HTTPS 反向代理配置
- 主机的访问列表和基本 HTTP 认证
- 负载均衡支持
- 自定义 Nginx 配置注入
- 支持 Docker，提供官方镜像
- 多语言支持
- 开源且免费

## 主要功能

- Proxy Hosts: Create and manage reverse proxy hosts with HTTP to HTTPS redirects, WebSocket support, custom error pages
- SSL Certificates: One-click certificate requests, uploads, and wildcard support
- Redirection & Streaming: URL redirects, 301/302, streaming proxy
- Access Control: Access restrictions with basic auth and IP filtering
- Logs & Monitoring: View access logs and real-time status
- Backup & Restore: Export/import configurations for migration

## 用法指南

### 1. 部署

- **Docker (recommended)**:

  ```
  docker run -d \
    --name nginx-proxy-manager \
    -p 80:80 -p 443:443 -p 81:81 \
    -v /path/to/data:/data \
    -v /path/to/letsencrypt:/etc/letsencrypt \
    --restart unless-stopped \
    jc21/nginx-proxy-manager:latest
  ```

  Access at `http://your-server-ip:81`, default login: `admin@example.com` / `changeme`.

- **Manual install**: Download source, install Node.js/Nginx, run `npm install` and `npm run build`.

### 2. 配置代理

- Login, go to Hosts > Proxy Hosts.
- Add Proxy Host: Enter domain, backend IP/port, enable SSL with Let's Encrypt.
- Save, NPM generates nginx config and reloads.

### 3. 管理 SSL

- SSL Certificates > Add SSL Certificate.
- Choose Let's Encrypt, enter domain/email, auto-provision.
- Apply to proxy hosts for HTTPS.

### 4. 高级用法

- Custom config in Advanced tab.
- Access Lists for rules.
- Update: `docker pull jc21/nginx-proxy-manager:latest`.
- Troubleshoot: Check logs.

See GitHub README/Wiki for more.
