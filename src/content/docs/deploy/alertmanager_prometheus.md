---
title: alertmanager
---


# Prometheus Alertmanager

> **项目地址**: https://github.com/prometheus/alertmanager

## 主要特性

- **Alert routing**  
  根据标签（label）将收到的警报按自定义规则分派到不同的接收器（receiver）或通道。支持多层路由、优先级和重试。

- **Alert grouping & throttling**  
  同一主体的多个警报会被合并成一个通知，避免信息冗余；可通过 `time_interval` 或 `group_wait` 控制发送频率。

- **Inhibition（抑制）**  
  通过 `inhibit_rules` 配置，设定若某类警报已存在时，抑制其他关联警报的通知，减少误报。

- **多渠道通知**  
  原生支持：slack、hipchat、teams、email、webhook、Opsgenie、PagerDuty、Pushover、victorops、wechat、wechatbot、opsgenie-sns、redis、influxdb 等。

- **Silences（静默）**  
  完全禁止特定警报标签组合的通知，可临时设置或通过 Web UI 持久化。

- **RESTful API & UI**  
  提供 `GET /api/v1/alerts`、`POST /api/v1/silences` 等 API，配合友好的 Web UI 进行监控与管理。

- **High Availability**  
  支持多实例部署，配置文件共享、/tmp/alertmanager/clustering 目录实现故障转移。

- **丰富的配置语法**  
  YAML 配置文件 `alertmanager.yml` 包含 `global`, `route`, `receivers`, `inhibit_rules`, `templates` 等块。

## 主要功能概览

| 功能 | 说明 |
| ---- | ---- |
| **警报接收** | Prometheus `alertmanager` 通过 push 或 pull 的方式接收 `Alert`。 |
| **警报分组** | 同余标签的警报合并后一次发送。 |
| **路由** | 自定义 `path`、`continue`、`group_by` 等字段，实现多级路由。 |
| **抑制** | 配置 `source_match`、`target_match` 规则，筛选抑制目标。 |
| **通知** | 多个通知渠道并行发送，支持自定义模板。 |
| **静默** | 使用 `Alertmanager` UI 或 API 创建 `silence`，可设置过期时间。 |
| **模板** | 支持 Handlebars/Jinja 等语法，用于自定义通知正文。 |
| **监控** | 内置 `-/metrics`，pgprometheus 采集指标。 |

## 用法实例

### 1. 本地启动 (Docker)

```bash
docker run -d \
  --name alertmanager \
  -p 9093:9093 \
  -v /path/to/alertmanager.yml:/etc/alertmanager/alertmanager.yml \
  prom/alertmanager
```

### 2. 基础配置示例 `alertmanager.yml`

```yaml
global:
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alertmanager@example.com'
  smtp_auth_username: 'user'
  smtp_auth_password: 'pass'

route:
  receiver: 'team-X-prod-alerts'
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 3h
  group_by: ['alertname', 'priority']

receivers:
- name: 'team-X-prod-alerts'
  email_configs:
  - to: 'ops+teamX@example.com'
    send_resolved: true

inhibit_rules:
- source_match:
    severity: 'critical'
  target_match:
    severity: 'warning'
  equal: ['alertname', 'dev', 'instance']
```

### 3. Prometheus 与 Alertmanager 集成

在 Prometheus 配置文件中添加：

```yaml
alerting:
  alertmanagers:
  - static_configs:
    - targets: ['alertmanager:9093']
```

### 4. 通过 UI 管理警报和静默

访问 `http://<alertmanager-host>:9093`  
- 查看当前激活的警报  
- 创建/删除静默  
- 编辑路由规则（仅限通过 API 或编辑 `alertmanager.yml`）

### 5. 使用 API 创建静默

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "matchers":[{"name":"alertname","value":"HighCPUUsage","isRegex":false}],
    "startsAt":"2024-11-01T00:00:00Z",
    "endsAt":"2024-11-01T01:00:00Z",
    "createdBy":"admin",
    "comment":"临时静默"
  }' \
  http://<alertmanager-host>:9093/api/v1/silences
```

## 结语

Alertmanager 为 Prometheus 提供了完整的警报生命周期管理：从接收、分组、抑制到多渠道通知，兼顾可配置性与扩展性。通过精细化标签匹配与灵活的路由规则，能够在大规模分布式环境下高效处置警报，减少噪声并保持团队关注点。