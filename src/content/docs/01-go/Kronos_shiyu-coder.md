
---
title: Kronos
---


# Kronos (shiyu-coder/Kronos)

**项目地址**：<https://github.com/shiyu-coder/Kronos>

---

## 项目概述  
Kronos 是一款开源分布式任务调度系统，基于 Go 语言实现。它可以将任何需要按规则执行的任务（如定时执行脚本、接口调用、数据备份等）统一管理、调度与监控，并支持多租户、多节点弹性伸缩。

---

## 主要特性  

| 特色 | 说明 |
|------|------|
| **Cron 语法支持** | 兼容标准 cron 表达式，可计算切分、增量调度等 |
| **分布式调度** | 采用 Redis + Redlock 进行节点间锁竞争，避免任务重复执行 |
| **高可用** | 通过一致性 Hash 分区与故障转移实现节点无单点故障 |
| **多租户** | 通过命名空间隔离，同一集群可同时接管不同业务的调度需求 |
| **插件化执行** | 支持自定义执行器（HTTP、Script、Message Queue 等） |
| **监控与告警** | 集成 Prometheus 指标，提供 Web UI 与 API 监控结果 |
| **视图化管理** | 内置 Web UI，支持任务 CRUD、执行日志、调度规则配置 |
| **安全性** | 基于 Token/PKI 的鉴权与访问控制 |

---

## 功能模块  

| 模块 | 关键职责 |
|------|----------|
| **API Server** | 处理调度规则 CRUD、查询日志、节点管理等 REST/GRPC 接口 |
| **Scheduler Worker** | 核心调度引擎，周期性扫描任务、获取执行锁、触发执行器 |
| **Executor** | 一个或多个插件实现实际任务执行（HTTP 请求、内部脚本、MQ 任务等） |
| **UI** | 前端页面提供可视化配置与监控，支持标签与搜索 |
| **Store** | 支持 Redis + MySQL 作为持久化后端，存储任务元数据与执行日志 |
| **Metrics** | 采集调度统计（成功率、失败率、耗时）并导出给 Prometheus |

---

## 快速开始

> **前提**：已安装 Go 1.20+, Docker (可选)

```bash
# 克隆仓库
git clone https://github.com/shiyu-coder/Kronos.git
cd Kronos

# 预 1：使用本地编译运行
go build ./...
./kronos-server
# 默认会跑在 http://localhost:8080

# 预 2：使用 Docker Compose (推荐)
docker compose up -d
# 服务启动后可访问 http://localhost:8080

# 预 3：使用 Helm (Kubernetes)
helm repo add kronos https://shiyu-coder.github.io/kronos-helm/
helm install kronos kronos/kronos
```

---

## 使用示例

### 新建定时任务

```bash
curl -X POST http://localhost:8080/api/v1/tasks \
  -H 'Content-Type: application/json' \
  -d '{
        "name":   "daily_backup",
        "cron":   "0 2 * * *",
        "type":   "http",
        "config": {
          "method": "POST",
          "url":    "https://backup.example.com/v1/backup",
          "headers": {
            "Authorization": "Bearer ____"
          }
        }
      }'
```

### 查询运行日志

```
GET http://localhost:8080/api/v1/tasks/daily_backup/logs?limit=20
```

### 通过 UI 进行管理  
访问 `http://localhost:8080` → `任务管理` → `新增` → 填写 Cron、类型、配置 → `保存`。

---

## 文档与社区支持  

- **官方文档**：<https://github.com/shiyu-coder/Kronos/blob/main/docs/README_zh.md>
- **示例项目**：<https://github.com/shiyu-coder/kronos-demo>
- **Issue Tracker**：<https://github.com/shiyu-coder/Kronos/issues>
- **讨论社区**：QQ群/Discord（请在 issue 中提出）

---

> *本文件为 `src/content/docs/00/Kronos_shiyu-coder.md` 的内容。*