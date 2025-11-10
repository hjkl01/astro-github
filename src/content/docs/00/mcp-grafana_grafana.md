---
title: Mcp Grafana
---

# mcp-grafana

## 项目简介

mcp-grafana 是 Grafana 的 Model Context Protocol (MCP) 服务器，为 Grafana 实例及其周边生态系统提供访问接口。它允许通过 MCP 客户端与 Grafana 进行交互，支持本地 Grafana 实例和 Grafana Cloud。

## 主要功能

### 仪表板 (Dashboards)

- 搜索仪表板
- 通过 UID 获取完整仪表板详情
- 获取仪表板摘要（标题、面板数量、面板类型、变量、元数据）
- 使用 JSONPath 表达式提取仪表板特定部分
- 更新或创建仪表板
- 修补仪表板（部分修改）
- 获取面板查询和数据源信息

### 数据源 (Datasources)

- 列出和获取数据源信息
- 支持 Prometheus 和 Loki 数据源

### Prometheus 查询

- 执行 PromQL 查询（即时和范围查询）
- 获取 Prometheus 元数据（指标名称、标签名称、标签值）

### Loki 查询

- 执行 LogQL 查询（日志和指标查询）
- 获取 Loki 元数据（标签名称、标签值、流统计）

### 事件管理 (Incidents)

- 搜索、创建和更新 Grafana Incident 中的事件
- 添加活动到事件

### Sift 调查

- 列出 Sift 调查
- 获取特定调查详情
- 获取调查分析
- 在 Loki 日志中检测错误模式
- 检测慢请求（使用 Tempo）

### 告警 (Alerting)

- 列出和获取告警规则信息及其状态
- 列出联系点

### Grafana OnCall

- 列出和管理值班计划
- 获取班次详情
- 获取当前值班用户
- 列出团队和用户
- 列出告警组

### 管理 (Admin)

- 列出团队
- 列出组织用户

### 导航 (Navigation)

- 生成 Grafana 资源的准确 deeplink URL
- 支持仪表板、面板、Explore 链接
- 时间范围和自定义参数支持

### 注解 (Annotations)

- 查询注解（支持时间范围、仪表板 UID、标签、匹配模式）
- 创建注解
- 创建 Graphite 格式注解
- 更新和修补注解
- 获取注解标签

## 要求

- Grafana 版本 9.0 或更高（完整功能）
- 某些数据源相关功能可能在早期版本中不可用

## 安装和使用

### 安装方式

1. **Docker 镜像**：

   ```bash
   docker pull mcp/grafana
   ```

2. **下载二进制文件**：
   从 [releases 页面](https://github.com/grafana/mcp-grafana/releases) 下载最新版本

3. **从源码构建**：

   ```bash
   GOBIN="$HOME/go/bin" go install github.com/grafana/mcp-grafana/cmd/mcp-grafana@latest
   ```

4. **Kubernetes Helm**：
   ```bash
   helm repo add grafana https://grafana.github.io/helm-charts
   helm install --set grafana.apiKey=<Grafana_ApiKey> --set grafana.url=<GrafanaUrl> my-release grafana/grafana-mcp
   ```

### 配置

创建服务账户并生成令牌，确保具有适当的 RBAC 权限。

#### Claude Desktop 配置示例

```json
{
  "mcpServers": {
    "grafana": {
      "command": "mcp-grafana",
      "args": [],
      "env": {
        "GRAFANA_URL": "http://localhost:3000",
        "GRAFANA_SERVICE_ACCOUNT_TOKEN": "<your service account token>",
        "GRAFANA_ORG_ID": "1"
      }
    }
  }
}
```

#### Docker 配置示例

```json
{
  "mcpServers": {
    "grafana": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        "GRAFANA_URL",
        "-e",
        "GRAFANA_SERVICE_ACCOUNT_TOKEN",
        "mcp/grafana",
        "-t",
        "stdio"
      ],
      "env": {
        "GRAFANA_URL": "http://localhost:3000",
        "GRAFANA_SERVICE_ACCOUNT_TOKEN": "<your service account token>"
      }
    }
  }
}
```

### 传输方式

- **stdio**: 默认，用于直接集成 AI 助手
- **sse**: HTTP 服务器模式，客户端连接到服务器
- **streamable-http**: 支持多个客户端连接的独立进程

### 工具配置

可以使用 `--disable-<category>` 标志禁用特定类别的工具，例如：

- `--disable-write`: 启用只读模式
- `--disable-dashboard`: 禁用仪表板工具
- `--disable-prometheus`: 禁用 Prometheus 工具

### TLS 配置

支持客户端和服务器 TLS 配置，用于安全连接。

### 调试模式

使用 `--debug` 标志启用详细的 HTTP 请求/响应日志。

## RBAC 权限

每个工具需要特定的 RBAC 权限。建议为服务账户分配适当的权限范围，或使用内置角色如 `Editor`。

## 故障排除

- 确保 Grafana 版本 >= 9.0 以支持所有功能
- 检查服务账户权限
- 使用调试模式排查连接问题

## 许可证

Apache License, Version 2.0
