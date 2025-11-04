
---
title: github-mcp-server
---


# GitHub MCP Server

**GitHub仓库地址:** https://github.com/github/github-mcp-server

---

## 项目概述
GitHub MCP Server 是一个为内部微服务提供统一配置查询与管理的 HTTP 服务。它实现了简单的 REST API，支持多种配置来源（文件、环境变量等），并可在运行时热更新配置。该服务主要用于在 GitHub 内部网络中让各个微服务快速获取所需的配置信息。

---

## 主要特性

| 特色 | 说明 |
|------|------|
| **统一配置服务** | 所有微服务通过统一接口获取配置，减少重复配置与代码。 |
| **支持多源配置** | 配置可来自 JSON/YAML 文件、环境变量、或内部配置中心。 |
| **热更新** | 通过 `/reload` 接口或文件系统事件即时更新配置，无需重启服务。 |
| **健康检查** | 提供 `/health` 接口，返回服务运行状态。 |
| **监控指标** | 通过 `/metrics` 暴露 Prometheus 监控指标。 |
| **安全认证** | 支持基于 token 的身份验证，确保只有授权服务能访问配置。 |
| **日志与监控** | 集成标准日志输出，支持结构化日志，方便排查。 |

---

## API 说明

| 路径 | 方法 | 描述 | 示例 |
|------|------|------|------|
| `/config/{service}` | GET | 获取指定服务的配置 | `GET http://localhost:8080/config/auth-service` |
| `/reload` | POST | 触发配置热更新 | `POST http://localhost:8080/reload` |
| `/health` | GET | 健康检查 | `GET http://localhost:8080/health` |
| `/metrics` | GET | Prometheus 指标 | `GET http://localhost:8080/metrics` |

---

## 如何使用

1. **克隆仓库**

   ```bash
   git clone https://github.com/github/github-mcp-server.git
   cd github-mcp-server
   ```

2. **安装依赖**

   ```bash
   go mod download
   ```

3. **配置环境变量**（可选）

   - `MCP_PORT`：监听端口（默认 `8080`）
   - `MCP_CONFIG_PATH`：配置文件路径（默认 `./config.yaml`）
   - `MCP_AUTH_TOKEN`：服务访问 token

4. **启动服务**

   ```bash
   go run main.go
   ```

5. **查询配置**

   ```bash
   curl http://localhost:8080/config/my-service
   ```

6. **热更新配置**

   ```bash
   curl -X POST http://localhost:8080/reload
   ```

---

## 部署

- **容器化**：仓库提供 `Dockerfile`，可直接构建镜像。

  ```bash
  docker build -t github-mcp-server .
  docker run -p 8080:8080 -e MCP_CONFIG_PATH=/etc/mcp/config.yaml github-mcp-server
  ```

- **Kubernetes**：示例 `deployment.yaml` 可在 `deploy/k8s` 目录查看。

---

## 贡献

如需贡献代码或报告问题，请查看仓库中的 `CONTRIBUTING.md` 与 `ISSUE_TEMPLATE.md`。

---