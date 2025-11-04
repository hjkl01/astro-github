
---
title: mimir
---

# Mimir – Grafana Mimir

**GitHub 地址**  
[https://github.com/grafana/mimir](https://github.com/grafana/mimir)

## 主要特性

| 功能 | 说明 |
|------|------|
| **分布式时序数据库** | 兼容 Prometheus，支持大规模数据写入与查询。 |
| **多租户支持** | 每个租户拥有独立的数据隔离与配额控制。 |
| **高可用** | 支持 Cassandra、 DynamoDB 、 MySQL / PostgreSQL 的存储后端，支持异地多副本。 |
| **可扩展存储** | 支持行内或落地存储，可按需配置冷热分层。 |
| **查询与拉取** | 兼容 PromQL（查询），支持 Prometheus remote_write 与 remote_read 接口。 |
| **复制与灾备** | 支持水平扩容、异地复制与灾备恢复。 |
| **门限报警** | 与 Grafana 等监控工具集成，输出 PromQL 查询结果。 |
| **多协议集成** | 支持 OpenTelemetry、Jaeger、Zipkin 等多种遥测协议。 |

## 核心功能

1. **写入（remote_write）**  
   Prometheus、Grafana Tempo、OpenTelemetry 等可直接向 Mimir 写入。
2. **查询（remote_read）**  
   支持 PromQL、InstantVector、RangeVector 等查询模式。
3. **降采样**  
   自动或手动对历史数据进行降采样，节省存储空间。
4. **控制台**  
   通过 `madmin` 命令行工具管理任意配置与命令行交互。
5. **分片与持久化**  
   数据按 TSID 分片，写入时自动在多个后端存储持久化。

## 快速上手

### 1. 安装

```bash
# 使用 Docker Compose
docker compose -f docker-compose.yml up -d

# 或直接使用发行版
brew install grafana/mimir/mimir
```

### 2. 配置

编辑 `mimir.yaml`（或使用环境变量）：

```yaml
# Mimir 配置示例
storage:
  type: s3
  s3:
    bucket_name: my-bucket
    endpoint: s3.example.com
    access_key_id: ...
    secret_access_key: ...
```

### 3. 运行

```bash
mimir -config.file=mimir.yaml
```

### 4. 与 Prometheus 集成

在 `prometheus.yml` 添加：

```yaml
remote_write:
  - url: http://localhost:9009/api/v1/remote_write
remote_read:
  - url: http://localhost:9009/api/v1/remote_read
```

### 5. 通过 Grafana 查询

在 Grafana 创建数据源：

- Type: Prometheus
- URL: http://localhost:9009

即可使用 PromQL 进行查询与监控。

## 常用命令

```bash
# 重载配置
mimirctl reload

# 查看状态
mimirctl status

# 清理旧数据
mimirctl compact

# 统计信息
mimirctl metrics
```

## 资源与文档

- 官方文档: https://grafana.com/docs/mimir
- 代码仓库: https://github.com/grafana/mimir

---