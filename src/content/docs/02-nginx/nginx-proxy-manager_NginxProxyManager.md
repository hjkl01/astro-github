---
title: nginx-proxy-manager
---

# Nginx Proxy Manager

**GitHub项目地址:** [https://github.com/NginxProxyManager/nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

## 主要特性

Nginx Proxy Manager (NPM) 是一个基于 Web 界面的开源工具，用于简化 Nginx 反向代理的管理。它将复杂的 Nginx 配置转化为用户友好的图形界面，支持 Docker 部署，适用于家庭实验室、服务器或云环境。主要特性包括：

- **Web 界面管理**：无需命令行，直接通过浏览器配置代理、SSL 证书和访问控制。
- **自动 SSL 支持**：集成 Let's Encrypt，提供免费的自动 HTTPS 证书颁发和续期。
- **反向代理**：轻松设置 HTTP/HTTPS 代理，支持自定义域名和路径路由。
- **访问列表和认证**：内置基本认证、IP 白名单/黑名单，以及 OAuth 支持。
- **负载均衡**：支持多个后端服务器的负载均衡配置。
- **自定义 Nginx 配置**：允许高级用户注入自定义 Nginx 规则。
- **Docker 友好**：官方提供 Docker 镜像，支持一键部署和数据库集成（SQLite 或 MySQL）。
- **多语言支持**：界面支持多种语言，包括中文。
- **开源免费**：基于 MIT 许可，社区活跃。

## 主要功能

- **代理主机管理**：创建和管理反向代理主机，支持 HTTP 到 HTTPS 重定向、WebSocket 支持和自定义错误页面。
- **SSL 证书管理**：一键申请、上传或导入证书，支持通配符证书。
- **重定向和流媒体**：配置 URL 重定向、301/302 跳转，以及流媒体代理。
- **访问控制**：设置访问限制，包括基本 HTTP 认证和 IP 过滤。
- **日志和监控**：查看代理访问日志和实时状态。
- **备份与恢复**：支持数据导出/导入，便于迁移。

## 用法指南

### 1. 部署
- **使用 Docker（推荐）**：
  运行以下命令部署（需预先创建 `data`、`letsencrypt` 目录）：
  ```
  docker run -d \
    --name nginx-proxy-manager \
    -p 80:80 -p 443:443 -p 81:81 \
    -v data:/data \
    -v letsencrypt:/etc/letsencrypt \
    --restart unless-stopped \
    jc21/nginx-proxy-manager:latest
  ```
  - 访问 `http://你的服务器IP:81` 进入 Web 界面。
  - 默认登录：邮箱 `admin@example.com`，密码 `changeme`（首次登录后修改）。

- **手动安装**：从 GitHub 下载源码，安装 Node.js 和 Nginx 依赖，然后运行 `npm install` 和 `npm run build` 构建。

### 2. 配置代理
- 登录 Web 界面后，导航到 “Hosts” > “Proxy Hosts”。
- 点击 “Add Proxy Host”：
  - 输入域名（如 example.com）。
  - 指定后端服务器 IP 和端口（如 192.168.1.100:3000）。
  - 启用 SSL：选择 “Request a new SSL certificate” 并配置 Let's Encrypt。
  - 保存后，NPM 会自动生成 Nginx 配置并重载服务。

### 3. 管理 SSL
- 在 “SSL Certificates” 部分，点击 “Add SSL Certificate”。
- 选择 Let's Encrypt，输入域名和邮箱，系统自动处理颁发。
- 为现有代理主机应用证书，实现 HTTPS。

### 4. 高级用法
- **自定义配置**：在代理主机设置中添加 “Advanced” 标签，输入自定义 Nginx 指令。
- **访问列表**：在 “Access Lists” 创建规则，然后应用到代理主机。
- **更新**：使用 `docker pull jc21/nginx-proxy-manager:latest` 更新镜像。
- **故障排除**：检查 Docker 日志 (`docker logs nginx-proxy-manager`) 或 Nginx 错误日志。

更多细节请参考 GitHub 仓库的 README 和 Wiki。