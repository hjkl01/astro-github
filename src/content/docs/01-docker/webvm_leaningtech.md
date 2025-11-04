
---
title: webvm
---


# webvm（leaningtech/webvm）

- **项目地址**: [https://github.com/leaningtech/webvm](https://github.com/leaningtech/webvm)

## 主要特性
| # | 特性 | 说明 |
|---|------|------|
| 1 | **Web 前端管理** | 采用 Vue+Vuetify 简洁 UI，支持新增、启动、停止、删除容器，实时查看日志。 |
| 2 | **Docker 容器化** | 通过 Dockerfile 或 `docker-compose.yml` 定义镜像，支持多种部署方式（本地、K8s）。 |
| 3 | **脚本化部署** | `deploy.sh` 脚本一次性构建镜像并启动服务，支持 `--debug` 调试模式。 |
| 4 | **多实例支持** | 同时运行多个隔离容器，支持自定义端口映射与环境变量。 |
| 5 | **API 接口** | 通过 RESTful API 可自动化管理容器，配合 CI/CD 使用。 |
| 6 | **日志与监控** | 集成 `fluentbit` 与 `Grafana`（可选），实时监控容器日志与性能。 |
| 7 | **安全隔离** | 基于 Docker 的命名空间、Seccomp 策略进行最小特权运行。 |
| 8 | **插件化扩展** | 通过 `plugins/` 目录可添加自定义插件，实现业务特定功能。 |

## 功能概览

### 1. 启动与停止容器
```bash
# 启动服务
docker compose up -d

# 停止服务
docker compose down
```

### 2. 创建与管理容器
```bash
# 在 web 前端创建新容器
# 选择 Dockerfile 或 docker-compose.yml，填入名称、端口映射、环境变量
```

### 3. 访问 WebUI
默认端口 `8080`：
```bash
http://localhost:8080
```

### 4. API 示例
```bash
# 获取所有容器：
curl -X GET http://localhost:8080/api/v1/vms

# 启动容器：
curl -X POST http://localhost:8080/api/v1/vms/<id>/start

# 停止容器：
curl -X POST http://localhost:8080/api/v1/vms/<id>/stop
```

### 5. 配置示例 (`config.yml`)
```yaml
server:
  hostname: "webvm.local"
  port: 8080
docker:
  registry: "docker.io"
  default_image: "ubuntu:latest"
logging:
  level: "info"
```

## 使用步骤

1. **克隆项目**  
   ```bash
   git clone https://github.com/leaningtech/webvm.git
   cd webvm
   ```

2. **构建镜像**  
   ```bash
   docker compose build
   ```

3. **运行服务**  
   ```bash
   docker compose up -d
   ```

4. **访问 WebUI**  
   在浏览器打开 `http://localhost:8080`，登录后即可管理容器。

5. **（可选）使用 API 自动化**  
   配置 CI/CD 环境变量，调用上述 RESTful API 实现无交互管理。

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| `docker compose` 找不到 | 安装 `docker compose`（新版 Docker Desktop 默认已安装）或安装 `docker-compose` 命令行工具。 |
| 控制台页面渲染慢 | 检查 `frontend/` 目录的 `node_modules` 是否已正确安装，执行 `npm ci`。 |
| 容器无法访问外部网络 | 确认 Docker 代理已配好，或在容器内手动 `ping` 目标 IP。 |

> **提示**：项目使用 `Docker Swarm` 或 `Kubernetes` 进行大规模部署时，请在 `swarm/` 或 `k8s/` 目录下查阅相应的部署脚本和 Helm Charts。

---

> *以上内容仅为项目功能、特性与基本使用方式的说明，请参考官方仓库的 README 与贡献指南获取更详细信息。*
