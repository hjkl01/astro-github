---
title: loki
---

# Loki

## 功能

Loki 是一个水平可扩展、高可用、多租户的日志聚合系统，受 Prometheus 启发。它专为日志而设计，非常经济有效且易于操作。与其他日志聚合系统不同，Loki 不对日志内容进行全文索引，而是存储压缩的非结构化日志，并仅索引一组标签作为元数据。

Loki 的主要特点包括：

- **成本效益**：通过仅索引元数据而非日志内容，Loki 更简单、更便宜。
- **标签驱动**：使用与 Prometheus 相同的标签来索引和分组日志流，实现指标和日志的无缝切换。
- **云原生友好**：特别适合存储 Kubernetes Pod 日志，自动抓取和索引 Pod 标签等元数据。
- **Grafana 集成**：原生支持 Grafana（需要 Grafana v6.0 及以上版本）。

Loki 基于的日志堆栈包括三个组件：

- **Alloy**：代理，负责收集日志并发送到 Loki。
- **Loki**：主服务，负责存储日志和处理查询。
- **Grafana**：用于查询和显示日志。

Loki 不同于 Prometheus，它专注于日志而非指标，并通过推送而非拉取的方式交付日志。

## 用法

### 安装 Loki

参考官方文档：[Installing Loki](https://grafana.com/docs/loki/latest/installation/)

### 安装 Alloy

参考官方文档：[Installing Alloy](https://grafana.com/docs/loki/latest/send-data/alloy/)

### 入门指南

参考官方文档：[Getting Started](https://grafana.com/docs/loki/latest/get-started/)

### 升级

参考官方文档：[Upgrading Loki](https://grafana.com/docs/loki/latest/upgrading/)

### 文档

- [最新版本文档](https://grafana.com/docs/loki/latest/)
- [即将发布版本文档](https://grafana.com/docs/loki/next/)

常用部分：

- [API 文档](https://grafana.com/docs/loki/latest/api/)：用于将日志导入 Loki。
- [标签](https://grafana.com/docs/loki/latest/getting-started/labels/)
- [操作](https://grafana.com/docs/loki/latest/operations/)
- [Promtail](https://grafana.com/docs/loki/latest/clients/promtail/)：代理，用于跟踪日志文件并推送至 Loki。
- [管道](https://grafana.com/docs/loki/latest/clients/promtail/pipelines/)：日志处理管道详情。
- [Docker 驱动客户端](https://grafana.com/docs/loki/latest/clients/docker-driver/)：Docker 插件，直接从 Docker 容器发送日志到 Loki。
- [LogCLI](https://grafana.com/docs/loki/latest/query/logcli/)：命令行界面，用于查询日志。
- [Loki Canary](https://grafana.com/docs/loki/latest/operations/loki-canary/)：监控 Loki 安装以检测缺失日志。
- [故障排除](https://grafana.com/docs/loki/latest/operations/troubleshooting/)：处理错误消息的帮助。
- [Grafana 中的 Loki](https://grafana.com/docs/loki/latest/operations/grafana/)：在 Grafana 中设置 Loki 数据源。

### 从源码构建

Loki 可以在单主机、无依赖模式下运行。需要最新版本的 Go。

```bash
# 检出源码
git clone https://github.com/grafana/loki
cd loki

# 构建二进制文件
go build ./cmd/loki

# 运行可执行文件
./loki -config.file=./cmd/loki/loki-local-config.yaml
```

或者使用 make：

```bash
# 构建二进制文件
make loki

# 运行可执行文件
./cmd/loki/loki -config.file=./cmd/loki/loki-local-config.yaml
```

构建 Promtail：

```bash
go build ./clients/cmd/promtail
```

### 获取帮助

- 在 Grafana Labs 社区论坛搜索 Loki 相关话题：[https://community.grafana.com](https://community.grafana.com/c/grafana-loki/)
- 在 Loki Slack 频道提问：[https://slack.grafana.com/](https://slack.grafana.com/) 并加入 #loki 频道。
- [提交问题](https://github.com/grafana/loki/issues/new) 用于报告 bug、问题和功能建议。
- 发送邮件至 [lokiproject@googlegroups.com](mailto:lokiproject@googlegroups.com) 或使用 [网页界面](https://groups.google.com/forum/#!forum/lokiproject)。
