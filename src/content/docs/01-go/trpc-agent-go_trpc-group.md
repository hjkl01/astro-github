
---
title: trpc-agent-go
---


# trpc-agent-go（trpc-group/trpc-agent-go）

**项目地址**  
[https://github.com/trpc-group/trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)

## 主要特性
- **服务注册与发现**：支持将 trpc 服务注册到 Agent，并通过 Agent 进行服务发现。  
- **健康检查**：自动对已注册的服务进行定期健康检查，失效服务会被自动下线。  
- **负载均衡**：提供多种负载均衡策略（如轮询、加权轮询、一致性哈希等）。  
- **监控与可观测性**：内置 Prometheus 指标导出，支持对请求数、错误率、延迟等进行监控。  
- **可配置**：支持 YAML/JSON 配置文件，支持动态热更新。  
- **CLI 与 HTTP API**：提供简易的命令行工具启动 Agent，同时提供 HTTP API 用于查询服务状态、手动注册/注销服务。  
- **轻量级 & 易部署**：单个二进制文件，适合容器化部署与 sidecar 方案。

## 核心功能
| 功能 | 说明 |
|------|------|
| **服务注册** | 通过 HTTP API 或在启动时配置文件自动注册服务。 |
| **服务发现** | 客户端可通过 Agent 获取可用服务实例列表。 |
| **健康检查** | 支持自定义健康检查脚本或 HTTP/GRPC 检查。 |
| **负载均衡** | 内置多种策略，可在客户端或 Agent 层配置。 |
| **指标采集** | 自动生成 `trpc_agent_*` 系列 Prometheus 指标。 |
| **配置热更新** | 监听配置文件变化，支持动态加载新配置。 |
| **CLI** | `agent start`, `agent stop`, `agent status` 等常用命令。 |

## 用法

### 1. 安装
```bash
go install github.com/trpc-group/trpc-agent-go@latest
```

### 2. 配置
创建 `config.yaml`（示例）：

```yaml
port: 8080
services:
  - name: user-service
    address: 127.0.0.1:50051
    weight: 1
    health_check:
      type: http
      url: http://127.0.0.1:50051/health
```

### 3. 启动 Agent
```bash
trpc-agent-go -c config.yaml
```

Agent 将监听 `8080` 端口，自动完成服务注册与健康检查。

### 4. 通过 HTTP API 查询服务
```bash
curl http://127.0.0.1:8080/v1/services/user-service
```

返回已注册且健康的实例列表。

### 5. Docker 部署
```bash
docker pull ghcr.io/trpc-group/trpc-agent-go:latest
docker run -p 8080:8080 -v /path/to/config.yaml:/etc/trpc-agent/config.yaml ghcr.io/trpc-group/trpc-agent-go:latest
```

### 6. 在 trpc 客户端中使用
```go
import (
    "github.com/trpc-group/trpc-go"
    "github.com/trpc-group/trpc-agent-go/client"
)

func main() {
    // 使用 Agent 作为服务发现中心
    trpc.SetDiscoverer(client.NewAgentDiscoverer("http://127.0.0.1:8080"))
    // 之后 trpc 调用会自动通过 Agent 获取实例
}
```

## 运行示例

```bash
# 启动 Agent
trpc-agent-go -c config.yaml

# 在另一终端启动 trpc 服务
go run main.go

# 调用服务
go run client.go
```

## 贡献与维护

- 代码托管在 GitHub，欢迎 issue 与 PR。  
- 项目使用 Go 1.22+ 编译。  
- CI/CD 通过 GitHub Actions 自动构建与发布 Docker 镜像。

---

> 本文档摘自项目 README，已作精简与中文化，供快速上手与部署参考。