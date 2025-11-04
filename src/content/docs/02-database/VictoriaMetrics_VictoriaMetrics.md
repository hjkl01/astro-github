
---
title: VictoriaMetrics
---


# VictoriaMetrics

**项目地址**: https://github.com/VictoriaMetrics/VictoriaMetrics

## 简介
VictoriaMetrics 是一款高性能、可扩展的时间序列数据库，专为监控系统、日志分析和实时指标收集而设计。它兼容 Prometheus、Graphite、InfluxDB 等常见监控采集格式，并提供 PromQL、InfluxQL 以及自家查询语言，具备高写入速率、低存储开销、优秀的压缩率和查询效率。

## 主要特性
| # | 特性 | 说明 |
|---|------|------|
| 1 | **极高写入/查询吞吐** | 单节点可处理数十万 TPS；集群可水平扩展至亿级 TPS |
| 2 | **压缩存储** | 带有自适应延迟窗口的列式压缩，单行仅占 1~2 字节 |
| 3 | **兼容 Prometheus/Graphite/InfluxDB** | 直接接收其 Remote Write、Line Protocol、PromQL 查询 |
| 4 | **水平可扩展** | 提供 `victoria-metrics`、`vmstorage`、`vmselect`、`vmagent`；支持 3+ 节点集群 |
| 5 | **自带块存储与压缩** | 按天/周/月分块，支持多时间粒度导出 |
| 6 | **零依赖、单二进制** | Go 编写，Linux / Mac / Windows 均可直接执行 |
| 7 | **多查询语言** | 支持 PromQL、InfluxQL、VictoriaMetrics 指标查询语言（语法友好） |
| 8 | **灵活的保留策略** | `-retentionPeriod`, `-dataRetentionPeriod`, `-badDataRetentionPeriod` 等 |
| 9 | **安全** | TLS、BasicAuth、OAuth、JWT 等验证方式 |
|10 | **监控 & CLI** | 通过 `/metrics`, `/v1/tsdb` REST API 监控；CLI 方便数据导入导出 |

## 功能概览
- **数据写入**  
  * 示例: `curl -X POST -d 'http_metric{label="value"} 42 1620000000' http://localhost:8428/api/v1/write`  
  * 远程写入：`# PUSH` 任务或 `gRPC`  
- **数据查询**  
  * PromQL: `SELECT sum(rate(http[5m])) FROM victoriametrics`  
  * InfluxQL: `SELECT * FROM gauge_metric WHERE time>now()-1h`  
  * 自家表达式: `a{job="api"} < 5`  
- **压缩/导出**  
  * `victoria-metrics-tools` 包含 `vmtools`，支持块导出、恢复、索引查看  
- **集群管理**  
  * 配置文件 `vms.yaml`，或命令行参数 `-storageDataPath`、`-replicationFactor`  
  * 简易部署：Docker Compose / Helm chart  

## 使用方法

### 1. 单机快速开始  
```bash
# 下载
wget https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest/download/victoria-metrics-linux-amd64-current.tar.gz
tar xvfz victoria-metrics-linux-amd64-current.tar.gz
cd victoria-metrics*

# 启动，默认端口 8428
./victoria-metrics-prod -storageDataPath="/path/to/data" -retentionPeriod=365d
```
- 访问 `http://localhost:8428/tsdb/query?query=up` 检查是否正常。

### 2. Docker 部署  
```bash
docker pull victoriametrics/victoria-metrics
docker run -d -p 8428:8428 -v /my/data:/data victoriametrics/victoria-metrics-prod \
  -storageDataPath=/data -retentionPeriod=365d
```

### 3. 集群部署  
1. 准备 `victoria-metrics-cluster.yaml`（或使用 Helm chart）  
2. 启动 `vmstorage`、`vmselect`、`vmagent`  
3. 配置 `remote_write` 到 `vmagent`  

```bash
# vmstorage
docker run -d -p 8400:8400 victoriametrics/vmstorage \
  -dataDir=/repo -storageDataPath=/repo

# vmselect
docker run -d -p 8401:8401 victoriametrics/vmselect \
  -storageNode=10.0.0.10:8400

# vmagent
docker run -d -p 8428:8428 victoriametrics/vmagent \
  -remoteWriteUrl=http://10.0.0.12:8428/api/v1/import
```

### 4. Prometheus 配置示例  
```yaml
scrape_configs:
  - job_name: 'victoria-metrics'
    static_configs:
      - targets: ['victoria-metrics:8428']
```

## 文档与资源
- 官方文档: https://victoriametrics.com/  
- GitHub 仓库: https://github.com/VictoriaMetrics/VictoriaMetrics  
- Docker Hub: https://hub.docker.com/r/victoriametrics/victoria-metrics  
- Helm 仓库: https://github.com/VictoriaMetrics/helm-victoriametrics

> 以上内容已整理为 Markdown，可直接保存为 `src/content/docs/00/VictoriaMetrics_VictoriaMetrics.md`。