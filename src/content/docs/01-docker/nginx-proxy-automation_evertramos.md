---
title: nginx-proxy-automation
---

# NGINX Proxy Automation 项目

## 项目地址
[GitHub 项目地址](https://github.com/evertramos/nginx-proxy-automation)

## 主要特性
- **自动化代理管理**：通过脚本自动配置和管理 NGINX 反向代理，支持动态添加和更新代理规则。
- **Docker 集成**：专为 Docker 环境设计，支持与 Docker Compose 结合，实现容器化部署和热重载。
- **环境变量驱动**：使用环境变量简化配置，避免手动编辑 NGINX 配置文件，提高可维护性。
- **SSL/TLS 支持**：内置 Let's Encrypt 集成，实现自动证书获取和续期，确保 HTTPS 安全访问。
- **负载均衡与健康检查**：支持后端服务的负载均衡和健康检查机制，提高系统可用性。
- **日志与监控**：提供详细的访问日志和错误日志，支持集成监控工具如 Prometheus。

## 主要功能
- **代理规则生成**：根据域名和后端服务自动生成 NGINX 配置文件，支持虚拟主机、多站点代理。
- **动态更新**：监听 Docker 容器事件，实现代理配置的实时更新，无需重启 NGINX。
- **证书管理**：自动化处理 SSL 证书的申请、安装和续期，使用 Certbot 工具。
- **自定义扩展**：允许用户通过模板自定义代理行为，支持添加自定义头、缓存和限流规则。
- **一键部署**：提供预配置的 Docker 镜像和脚本，支持快速启动代理服务。

## 用法
1. **克隆仓库**：
   ```
   git clone https://github.com/evertramos/nginx-proxy-automation.git
   cd nginx-proxy-automation
   ```

2. **配置环境**：
   - 编辑 `docker-compose.yml` 文件，设置域名、后端服务地址和环境变量（如 `VIRTUAL_HOST`、`LETSENCRYPT_HOST`）。
   - 示例环境变量：
     ```
     VIRTUAL_HOST=example.com
     LETSENCRYPT_HOST=example.com
     LETSENCRYPT_EMAIL=admin@example.com
     ```

3. **启动服务**：
   ```
   docker-compose up -d
   ```
   这将启动 NGINX 代理容器，并自动配置规则。

4. **添加新服务**：
   - 在 Docker Compose 中添加新容器，并设置相应的环境变量。
   - 脚本将自动检测并更新 NGINX 配置，重载服务。

5. **证书管理**：
   - 首次启动时，系统会自动申请 Let's Encrypt 证书。
   - 证书续期由 cron 任务处理，通常每 12 小时检查一次。

6. **停止与清理**：
   ```
   docker-compose down
   ```
   注意：停止前备份证书文件以避免丢失。

更多细节请参考项目 README 文件。