---
title: prometheus
---

# Prometheus 项目

**项目地址:** [https://github.com/prometheus/prometheus](https://github.com/prometheus/prometheus)

## 主要特性

Prometheus 是一个开源的监控系统和时间序列数据库，专为云原生环境设计。它具有以下主要特性：

- **多维数据模型**：基于标签（labels）的键值对，支持动态和灵活的查询。
- **PromQL 查询语言**：强大的表达式语言，用于查询和分析时间序列数据。
- **无需外部存储**：内置高效的时间序列数据库，支持本地存储和查询。
- **拉取式（Pull）模型**：通过 HTTP 定期从目标端点拉取指标，支持服务发现。
- **警报系统**：集成 Alertmanager，支持基于规则的警报通知。
- **高可用性和可扩展性**：支持联邦（federation）和分片部署，适用于大规模环境。
- **生态系统丰富**：与 Kubernetes、Grafana 等工具无缝集成，提供 exporter 用于各种系统监控。

## 主要功能

Prometheus 的核心功能包括：

- **指标采集**：从 HTTP 端点（如 /metrics）拉取指标，支持文本格式（text-based）和二进制暴露。
- **存储和查询**：高效存储时间序列数据，支持 PromQL 进行实时查询、聚合和可视化。
- **警报管理**：定义规则触发警报，并通过 Alertmanager 发送通知（如邮件、Slack、PagerDuty）。
- **服务发现**：自动发现监控目标，支持文件、Consul、DNS、Kubernetes 等后端。
- **仪表盘集成**：可与 Grafana 结合创建自定义仪表盘。
- **推入网关（Pushgateway）**：处理短期任务的指标推送。
- **远程读写**：支持与 Thanos 或 Cortex 等远程存储集成，实现长期存储。

## 用法

### 安装

1. **下载二进制文件**：从 GitHub Releases 下载适合操作系统的二进制包。
   ```bash
   wget https://github.com/prometheus/prometheus/releases/download/v2.XX.X/prometheus-2.XX.X.linux-amd64.tar.gz
   tar xvfz prometheus-2.XX.X.linux-amd64.tar.gz
   cd prometheus-2.XX.X.linux-amd64
   ```

2. **使用 Docker**：
   ```bash
   docker run -p 9090:9090 prom/prometheus
   ```

3. **Kubernetes 部署**：使用 Helm Chart 安装。
   ```bash
   helm install prometheus prometheus-community/kube-prometheus-stack
   ```

### 配置和运行

- 编辑 `prometheus.yml` 配置文件，定义抓取目标（scrape_configs）和规则。
  示例配置：
  ```yaml
  global:
    scrape_interval: 15s

  scrape_configs:
    - job_name: 'prometheus'
      static_configs:
        - targets: ['localhost:9090']
  ```

- 启动 Prometheus：
  ```bash
  ./prometheus --config.file=prometheus.yml
  ```

- 访问 Web UI：打开浏览器访问 http://localhost:9090，执行 PromQL 查询，如 `up` 查看目标状态。

### 基本用法示例

1. **暴露指标**：在应用中集成 Prometheus 客户端库（如 Go 的 prom/client_golang），暴露 /metrics 端点。
2. **查询数据**：在 UI 的 Graph 页面输入 PromQL，如 `rate(http_requests_total[5m])` 计算请求速率。
3. **设置警报**：在 `rules.yml` 中定义规则，然后在 prometheus.yml 中加载。
   示例规则：
   ```yaml
   groups:
   - name: example
     rules:
     - alert: InstanceDown
       expr: up == 0
       for: 5m
   ```
4. **集成 Alertmanager**：配置 prometheus.yml 中的 alerting 部分，并启动 Alertmanager 服务。

更多详情请参考官方文档：https://prometheus.io/docs/introduction/overview/