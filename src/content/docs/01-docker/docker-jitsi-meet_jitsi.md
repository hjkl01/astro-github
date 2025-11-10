---
title: docker-jitsi-meet
---


# Docker Jitsi Meet

**项目地址**  
[https://github.com/jitsi/docker-jitsi-meet](https://github.com/jitsi/docker-jitsi-meet)

## 项目概述
Docker Jitsi Meet 是一个基于 Docker Compose 的完整 Jitsi Meet 部署方案。它将 Jitsi Videobridge、Jicofo、Prosody、Jitsi Meet 前端等组件打包成可直接运行的容器，方便快速搭建安全、可扩展的视频会议服务。

## 主要特性
- **一键部署**：只需 `docker-compose up -d` 即可完成所有服务的安装与启动。  
- **自定义配置**：通过 `.env` 文件或 `docker-compose.yml` 中的环境变量，轻松调整域名、TLS、音视频参数、授权方式等。  
- **HTTPS/Let’s Encrypt**：内置 Let’s Encrypt 自动获取与续期 TLS 证书。  
- **多域/多实例**：支持同一机器部署不同域名的多实例。  
- **可扩展的网络**：使用 Docker 网络，容器间通信简洁可靠。  
- **日志与监控**：所有容器日志统一输出，易于集成监控系统。  
- **更新与维护**：提供 `docker-compose pull` 与 `docker-compose up -d` 的方式快速升级镜像。  

## 核心功能
| 组件 | 作用 |
|------|------|
| **Jitsi Videobridge** | 负责多方视频转发，支持 WebRTC。 |
| **Jicofo** | 会议控制器，管理会议信息与会议室。 |
| **Prosody** | XMPP 服务器，处理身份验证与信令。 |
| **Jitsi Meet** | 前端网页，提供用户界面与交互。 |
| **nginx** | 反向代理，处理 HTTPS 与域名映射。 |
| **letsencrypt** | 自动颁发与续期 TLS 证书。 |

## 用法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/jitsi/docker-jitsi-meet.git
   cd docker-jitsi-meet
   ```

2. **配置环境变量**  
   - 复制示例文件  
     ```bash
     cp env.example .env
     ```
   - 根据需求编辑 `.env`，至少需要设置：
     - `DOMAIN`：部署域名（如 `meet.example.com`）
     - `ENABLE_LETSENCRYPT`：`1` 或 `0`（是否启用 Let’s Encrypt）
     - `JVB_AUTH_USER` & `JVB_AUTH_PASSWORD`：Jitsi Videobridge 的身份验证
     - `JICOFO_AUTH_USER` & `JICOFO_AUTH_PASSWORD`：Jicofo 的身份验证
     - `PROSODY_PASSWORD`：Prosody 的管理员密码

3. **启动服务**  
   ```bash
   docker-compose up -d
   ```

4. **访问会议**  
   打开浏览器访问 `https://<DOMAIN>`，即可使用 Jitsi Meet 进行视频会议。  

5. **升级镜像**  
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

## 常见命令
- 查看容器日志  
  ```bash
  docker logs -f <容器名>
  ```
- 重启某个服务  
  ```bash
  docker-compose restart <服务名>
  ```
- 停止并移除所有容器  
  ```bash
  docker-compose down
  ```

> 详细配置与高级用法请参考官方 README 与 Docker Compose 文件。  
