# roxy-wi

## 项目描述

roxy-wi 是一个用于管理 HAProxy、Nginx、Apache 和 Keepalived 服务器的 Web 界面。它提供了用户友好的 Web GUI、警报、监控和安全功能，帮助用户轻松管理负载均衡器和相关服务。

## 主要功能

1. 安装和更新 HAProxy、Nginx、Apache 和 Keepalived 作为系统服务或 Docker 服务。
2. 下载、更新和格式化 GeoIP 数据以适用于 HAProxy 和 Nginx。
3. 动态更改 Maxconn、黑白名单、添加/编辑/删除后端服务器的 IP 和端口，并保存到配置文件。
4. 通过 Web 界面快速配置 HAProxy、Nginx、Apache 和 Keepalived。
5. 查看和分析所有前端/后端服务器的状态。
6. 通过状态页面启用/禁用服务器，无需重启 HAProxy。
7. 查看和分析 HAProxy、Nginx、Apache 和 Keepalived 日志。
8. 创建和可视化 HAProxy 工作流。
9. 一键推送更改到服务器。
10. 查看历史更改、评估配置文件并恢复到之前的稳定配置。
11. 通过 Web 界面添加/编辑前端或后端服务器。
12. 编辑配置并一键同步到所有主/从服务器。
13. 支持多服务器配置同步。
14. 自动管理前端端口。
15. 评估最近推送的配置更改。
16. 支持多用户角色和权限管理。
17. 创建组并管理服务器集群。
18. 通过 Telegram、Slack、Email、PagerDuty、Mattermost 发送通知。
19. 支持高可用性。
20. 支持 SSL（包括 Let's Encrypt）。
21. 支持 SSH 密钥管理。
22. SYN 洪水保护。
23. 警报后端状态变化和 Maxconn 限制。
24. 警报服务状态。
25. 收集连接指标。
26. Web 加速设置。
27. Web 应用防火墙 (WAF)。
28. LDAP 支持。
29. 保持服务活跃。
30. 支持隐藏配置块以限制访客用户访问。
31. 移动端友好设计。
32. SMON 服务：检查 Ping、TCP/UDP、HTTP(s)、SSL 到期、HTTP 响应体、DNS 记录、状态页面。
33. 备份配置文件。

## 用法

### 安装

#### RPM 安装

参考官方站点：[https://roxy-wi.org/installation#rpm](https://roxy-wi.org/installation#rpm)

#### DEB 安装

参考官方站点：[https://roxy-wi.org/installation#deb](https://roxy-wi.org/installation#deb)

#### 手动安装

适用于其他 Linux 发行版。参考官方文档。

### 支持的操作系统

- EL7、EL8、EL9（RPM 和手动安装）
- Amazon Linux 2（RPM 和手动安装）
- Ubuntu（DEB 和手动安装）
- 其他 Linux 发行版（手动安装，仅 x86_64）

### 数据库支持

默认使用 SQLite。如需 MySQL，参考：[https://roxy-wi.org/installation#database](https://roxy-wi.org/installation#database)

### 设置

1. 访问 [https://roxy-wi-server/admin](https://roxy-wi-server/admin)，默认登录：admin/admin。
2. 添加用户、组和服务器。
3. 参考官方设置指南：[https://roxy-wi.org/settings](https://roxy-wi.org/settings)

### 故障排除

如果遇到 "Internal Server Error"，运行：

```
$ cd /var/www/haproxy-wi/app
$ ./create_db.py
```

更多信息：[https://roxy-wi.org/troubleshooting](https://roxy-wi.org/troubleshooting)

## 演示站点

访问 [https://demo.roxy-wi.org](https://demo.roxy-wi.org)，登录：admin/admin（每小时重置）。

## 许可证

Apache-2.0
