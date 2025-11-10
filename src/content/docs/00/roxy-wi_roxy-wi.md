---
title: Roxy Wi
---

# roxy-wi

## 项目简介

roxy-wi 是一个用于管理 HAProxy、Nginx、Apache 和 Keepalived 服务器的用户友好 Web 界面。它提供了监控、警报和安全功能，帮助用户轻松管理负载均衡和代理服务器。

## 主要功能

- **安装和更新服务**：支持通过系统服务或 Docker 安装和更新 HAProxy、Nginx、Apache 和 Keepalived。
- **动态配置管理**：实时更改 Maxconn、黑白名单、添加/编辑后端服务器 IP 和端口，并保存到配置文件。
- **服务器状态监控**：从单一控制面板查看和分析所有前端/后端服务器的状态。
- **服务器控制**：通过状态页面启用/禁用服务器，无需重启 HAProxy。
- **日志分析**：直接从 Web 界面查看和分析 HAProxy、Nginx、Apache 和 Keepalived 的日志。
- **工作流可视化**：创建和可视化 HAProxy 工作流。
- **配置推送**：一键推送更改到所有服务器。
- **历史管理**：查看过去更改、评估配置文件，并一键恢复到稳定配置。
- **多用户角色**：支持基于权限的查看和编辑配置。
- **通知系统**：通过 Telegram、Slack、Email、PagerDuty、Mattermost 发送通知。
- **高可用性**：确保主从服务器的正常运行。
- **SSL 支持**：包括 Let's Encrypt。
- **SSH 密钥管理**：使用 SSH 密钥管理多个服务器。
- **安全功能**：SYN flood 保护、Web 应用防火墙 (WAF)、警报系统。
- **监控和指标**：收集连接指标、Web 加速设置。
- **其他**：LDAP 支持、移动端设计、SMON 监控服务、配置备份。

## 用法

### 安装

#### RPM 安装

参考官方站点：[https://roxy-wi.org/installation#rpm](https://roxy-wi.org/installation#rpm)

#### DEB 安装

参考官方站点：[https://roxy-wi.org/installation#deb](https://roxy-wi.org/installation#deb)

#### 手动安装

适用于其他 Linux 发行版。参考官方文档。

支持的操作系统：

- EL7/8/9 (RPM 或手动)
- Amazon Linux 2 (RPM 或手动)
- Ubuntu (DEB 或手动)
- 其他 Linux (手动)

### 数据库设置

默认使用 SQLite。如需 MySQL，启用配置并创建数据库。参考：[https://roxy-wi.org/installation#database](https://roxy-wi.org/installation#database)

### 初始设置

1. 登录 [https://roxy-wi-server/admin](https://roxy-wi-server/admin)，默认用户名/密码：admin/admin。
2. 添加用户、组和服务器。
3. 参考设置指南：[https://roxy-wi.org/settings](https://roxy-wi.org/settings)

### 故障排除

如果遇到 "Internal Server Error"，运行：

```
cd /var/www/haproxy-wi/app
./create_db.py
```

更多信息：[https://roxy-wi.org/troubleshooting](https://roxy-wi.org/troubleshooting)

## 演示站点

访问 [https://demo.roxy-wi.org](https://demo.roxy-wi.org)，登录：admin/admin。服务器每小时重置。

## 社区

- Telegram 频道：[https://t.me/roxy_wi_channel](https://t.me/roxy_wi_channel)
