---
title: caddy
---


# Caddy 服务器

> **项目地址**: https://github.com/caddyserver/caddy

Caddy 是一款用 Go 语言编写的现代化、功能强大的 Web 服务器，主打易用性、自动 HTTPS 与插件化设计。它适用于静态文件托管、反向代理、负载均衡、内容分发网络(CDN)等多种场景。

## 主要特性

| 特性 | 说明 |
|------|------|
| **自动 HTTPS** | 通过 Caddyfile 或 WebDAV/JSON API 自动获取并续订 Let’s Encrypt 证书，无需手动配置。 |
| **零配置** | 默认配置已开启 HTTPS、HTTP/2、压缩、缓存、访问日志；只需最小化配置即可快速上线。 |
| **插件化架构** | 通过官方与社区插件扩展功能，例如：WebSocket、Rate Limiting、OAuth2 验证、JWT、GraphQL、数据库集成等。 |
| **多协议支持** | 支持 HTTP/1.1、HTTP/2、QUIC / HTTP/3、HTTPS、H2C、WebSocket、TCP、UDP 等。 |
| **高性能** | 采用 Go 并行模型，适合高并发场景；内置缓存、压缩、重写、重定向等中间件。 |
| **动态配置** | 通过 Caddyfile、JSON 或 REST API 实时更新配置；支持热重载。 |
| **安全** | 内置 CSP、HSTS、XSS 过滤、自动更新、最小权限运行。 |
| **可视化仪表盘** | Caddy Admin API 可与 Grafana、Prometheus 等监控系统集成。 |
| **跨平台** | 支持 Linux、macOS、Windows、FreeBSD、OpenBSD、Android 等操作系统。 |

## 基本使用

### 1. 安装

```bash
# 通过官方脚本安装
curl -sfL https://getcaddy.com | bash -s personal

# 或者手动下载
wget https://github.com/caddyserver/caddy/releases/download/v2.6.4/caddy_v2.6.4_linux_amd64.tar.gz
tar -xzf caddy_v2.6.4_linux_amd64.tar.gz
sudo mv caddy /usr/local/bin/
```

> 版本号会随时间更新，访问官方 Releases 页面获取最新版本。

### 2. 简单的 Caddyfile 示例

```nginx
{
    # 全局设置
    email you@example.com
    acme_ca https://acme-v02.api.letsencrypt.org/directory
}

# 监听 80/443 并自动 HTTPS
example.com

# 静态文件托管
/static {
    root * /var/www/static
    file_server
}

# 反向代理
api.example.com {
    reverse_proxy localhost:8080
}

# HTTP/3（QUIC）支持
https://quic.example.com {
    reverse_proxy localhost:9090
}
```

> 只需将上述内容保存为 `Caddyfile`，然后执行 `caddy run` 即可启动。

### 3. 通过 JSON API 配置

```bash
curl -X POST http://localhost:2019/load \
     -H "Content-Type: application/json" \
     -d '{
           "apps": {
             "http": {
               "servers": {
                 "srv1": {
                   "listen": ["*:80"],
                   "routes": [
                     {
                       "handle": [
                         { "handler": "static_response", "body": "Hello, world!" }
                       ]
                     }
                   ]
                 }
               }
             }
           }
         }'
```

> 通过 API 可在运行时动态添加/修改站点，无需重启。

### 4. 插件使用示例

```bash
# 安装官方插件：caddy-dns-cloudflare
caddy add-package github.com/caddyserver/caddy-dns-cloudflare@v1.0.2

# 配置插件
{
    dns cloudflare {email your-email@example.com; api_token YOUR_TOKEN}
}
```

> 插件可以通过 `caddy plugin` 命令管理，支持官方插件与社区插件。

## 常用命令

| 命令 | 说明 |
|------|------|
| `caddy run` | 启动服务器，默认读取当前目录 `Caddyfile` |
| `caddy run --config /path/to/Caddyfile --adapter caddyfile` | 指定配置文件与适配器 |
| `caddy version` | 查看版本信息 |
| `caddy reload` | 热重载配置（支持 Caddyfile、JSON） |
| `caddy stop` | 停止服务器 |
| `caddy health` | 检查健康状态 |
| `caddy token` | 生成或显示 Access Token（用于 API） |

## 进一步阅读

- 官方文档: https://caddyserver.com/docs/
- 插件生态: https://caddyserver.com/docs/plugins
- 示例项目: https://github.com/caddyserver/caddy/tree/master/examples

---
> 以上内容为对 Caddy 服务器核心功能与基本使用的简要概述，帮助快速上手。祝使用愉快！
