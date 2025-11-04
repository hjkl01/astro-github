
---
title: loki
---


# Loki（Grafana Labs）项目概述

**GitHub 地址**: https://github.com/grafana/loki

---

## 1. 项目简介  
Loki 是一套水平可扩展、受限型的日志聚合系统，专为与 Prometheus 级别的监控场景配合使用。它采用与 Prometheus 相同的标签体系，支持高效存储、索引以及查询日志。

---

## 2. 主要特性  
| 特性 | 说明 |
|------|------|
| **轻量级索引** | 只索引日志标签和时间戳，避免大规模文本索引，节省磁盘与内存 |
| **水平可扩展** | 通过分片、拉取、复制实现多节点扩展 |
| **多租户支持** | 为每个租户隔离数据与资源，适合 SaaS 场景 |
| **与 Grafana 深度集成** | 直接在 Grafana 搭建面板，支持 Loki 查询语言 (LogQL) |
| **弹性存储** | 可使用多种后端：Cassandra、Elasticsearch、BoltDB、S3 等 |
| **高可用** | 支持 Raft 节点复制，保证日志数据的持久性 |

---

## 3. 核心功能  
1. **日志采集**  
   - `promtail`、`fluentd`、`syslog` 等代理程序可将日志推送到 Loki。  
   - 支持通过文件、容器、Kubernetes 事件等多种来源。

2. **查询日志**  
   - **LogQL**：查询语言与 PromQL 类似，支持正则匹配、聚合、行过滤。  
   - 示例：`{app="web"} |~ "error|critical" | line_format "{{.timestamp}} {{.message}}"`

3. **聚合与采样**  
   - 支持 *max-lines* 控制查询返回行数，或者使用 `count_over_time`、`sum_over_time` 等聚合函数。

4. **多租户查询与标签过滤**  
   - 通过 `X-Scope-OrgID` HTTP 头控制租户，或通过 `label_values` 函数获取租户标签。

5. **终端工具与插件**  
   - `grafana-cli` 插件：Grafana 中的 Loki 数据源。  
   - `loki` 命令行：用于查询、导入、诊断。

---

## 4. 典型用法

### 4.1 安装与运行  
```bash
# 拉取仓库
git clone https://github.com/grafana/loki.git
cd loki

# 编译二进制
make build

# 运行 Loki（默认配置示例）
./loki -config.file=conf/loki-local-config.yaml
```

### 4.2 配置采集代理 promtail  
```yaml
# promtail.yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://localhost:3100/loki/api/v1/push

scrape_configs:
  - job_name: system
    static_configs:
      - targets:
          - localhost
        labels:
          job: varlogs
          __path__: /var/log/*log
```
```bash
# 运行 promtail
./promtail -config.file=promtail.yaml
```

### 4.3 在 Grafana 中添加 Loki 数据源  
1. 登录 Grafana。  
2. 进入 *Configuration → Data Sources → Add data source → Loki*.  
3. URL 输入 `http://localhost:3100`.  
4. 保存并测试。

### 4.4 查询示例  
```logql
# 过滤包含 "error" 的日志
{job="varlogs"} |~ "error"

# 计算过去 5 分钟内的错误行数
count_over_time({job="varlogs"}[5m])
```

---

## 5. 参考资源  
- 官方文档: https://grafana.com/docs/loki/latest/  
- 代码仓库: https://github.com/grafana/loki  
- 交流社区: https://github.com/grafana/loki/discussions  

---

**项目地址**: https://github.com/grafana/loki  
