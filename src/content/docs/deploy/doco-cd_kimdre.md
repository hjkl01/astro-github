---
title: doco-cd
---

# doco-cd

## 功能

Doco-CD 是一个轻量级的 GitOps 工具，用于自动化部署和更新 Docker Compose 项目和 Swarm stacks。它通过轮询（polling）和 webhooks 来实现自动化部署，是 Portainer 或 ArgoCD 的简单替代方案，专为 Docker 环境设计。

主要功能包括：

- **自动化部署**：通过 Git 仓库的变更自动触发 Docker Compose 或 Swarm 栈的部署。
- **多服务支持**：支持单仓库多服务（monorepo）部署，每个服务可配置独立的目录、超时和 Compose 文件。
- **外部密钥管理**：集成 1Password、AWS Secrets Manager、Bitwarden 等外部密钥提供商。
- **Webhook 和轮询**：支持 Git 提供商的 webhook 触发，或定期轮询仓库变更。
- **健康检查**：提供 API 端点检查服务状态。
- **通知**：支持通过 Apprise 发送部署通知。
- **私有仓库认证**：支持私有 Docker 仓库的认证配置。
- **分支/标签过滤**：可配置仅在特定分支或标签上触发部署。

## 用法

### 安装和配置

1. **运行 Doco-CD**：
   使用 Docker Compose 启动 Doco-CD 服务：

   ```yaml
   services:
     doco-cd:
       image: ghcr.io/kimdre/doco-cd:latest
       environment:
         GIT_ACCESS_TOKEN: your_git_token
         WEBHOOK_SECRET: your_webhook_secret
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
         - data:/data
   ```

2. **配置部署**：
   在 Git 仓库根目录创建 `.doco-cd.yml` 文件定义服务：

   ```yaml
   name: myapp
   working_dir: . # 可选，默认当前目录
   compose_files:
     - docker-compose.yml
   timeout: 300 # 可选，默认 300 秒
   ```

   对于多服务（monorepo）：

   ```yaml
   name: frontend
   working_dir: frontend/
   ---
   name: backend
   working_dir: backend/
   timeout: 600
   ```

3. **外部密钥**：
   在 `.doco-cd.yml` 中配置外部密钥：

   ```yaml
   name: myapp
   external_secrets:
     DB_PASSWORD: 'op://production/database/password' # 1Password
     API_KEY: 'arn:aws:secretsmanager:region:account:secret:name' # AWS
   ```

   在 `docker-compose.yml` 中使用：

   ```yaml
   services:
     app:
       environment:
         DATABASE_PASSWORD: $DB_PASSWORD
   ```

4. **Webhook 设置**：
   - 生成 webhook secret：`openssl rand -base64 40`
   - 在 Git 提供商中配置 webhook 到 `http://your-doco-cd:port/v1/webhook`
   - 对于 monorepo，可使用 `http://your-doco-cd:port/v1/webhook/<target>` 并创建 `.doco-cd.<target>.yml`

5. **轮询配置**：
   在 `docker-compose.yml` 中设置 `POLL_CONFIG`：

   ```yaml
   environment:
     POLL_CONFIG: |
       - url: https://github.com/user/repo.git
         reference: refs/heads/main
         interval: 120  # 秒
   ```

6. **健康检查**：
   - API 端点：`GET /v1/health`
   - 响应：`{"details": "healthy"}`

7. **私有仓库认证**：
   创建 `docker-config.json`：

   ```json
   {
     "auths": {
       "registry.example.com": {
         "auth": "base64_encoded_credentials"
       }
     }
   }
   ```

   挂载到容器：`- ./docker-config.json:/root/.docker/config.json`

### 高级配置

- **分支过滤**：在 `.doco-cd.yml` 中添加 `webhook_filter: "^refs/heads/main$"`
- **通知**：集成 Apprise 服务发送部署状态通知。
- **代理**：设置 `HTTP_PROXY` 环境变量使用代理。
- **Docker 客户端**：配置 `DOCKER_HOST` 等连接远程 Docker daemon。

Doco-CD 适合小型到中型 Docker 部署场景，提供简单易用的 GitOps 自动化。
