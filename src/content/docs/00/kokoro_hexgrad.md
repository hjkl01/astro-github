
---
title: kokoro
---


---
title: Kokoro - Hexgrad 项目概览
link: https://github.com/hexgrad/kokoro
---

# Kokoro

**Kokoro** 是一个轻量级、易用的容器集群管理工具，基于 Docker 和 Go 开发，旨在简化多主机容器部署、扩缩容及服务发现。它将 Docker 的强大生态与集群编排的需求相结合，提供了一套简洁的 API 与命令行工具，适合中小型项目快速落地及生产环境的日常运维。

## 主要特性

| 特性 | 说明 |
| ---- | ---- |
| **多主机支持** | 自动发现并管理 Kubernetes 之外的物理/虚拟机节点，支持 Heterogeneous 环境。 |
| **动态服务发现** | 通过基于一致性哈希的负载均衡实现跨节点服务发现，支持环境变量注入。 |
| **弹性扩缩容** | 支持基于 CPU/内存阈值或自定义策略的自动扩容/缩容，保证服务可用性。 |
| **自定义健康检查** | 可配置 HTTP、TCP、Exec 等多种健康检查方式，失败自动重启容器。 |
| **多租户与权限管理** | 通过 OAuth2/LDAP 进行身份认证，支持细粒度资源访问控制。 |
| **插件化设计** | 支持插件接口，用户可自行编写插件（如监控、日志聚合、网络插件）扩展功能。 |
| **命令行与 REST API** | 提供 `kokoro` CLI 与 RESTful 接口，兼容 CI/CD 工作流。 |
| **轻量级运行时** | 基于 Docker 的 natively 容器网络，无需额外代理，启动速度快。 |

## 功能列表

| 功能 | 说明 |
| ---- | ---- |
| 节点注册/注销 | 节点加入集群后自动注册，离线后及时注销。 |
| 容器编排 | 根据 YAML/JSON 配置文件快速部署多容器应用。 |
| 网络策略 | 支持 overlay 网络、静态路由与网络插件统一管理。 |
| 日志与监控 | 与 Prometheus、Grafana、ELK 等集成，统一收集日志与指标。 |
| 迁移与升级 | 通过 rolling update 或蓝绿部署零停机升级。 |
| 资源配额 | 通过 CPU/内存配额控制单容器资源使用。 |
| 文件卷管理 | 采用 Docker local / NFS / Ceph 等多种存储后端。 |

## 用法

### 1. 安装

```bash
# 直接下载二进制
curl -L https://github.com/hexgrad/kokoro/releases/latest/download/kokoro_linux_amd64.tar.gz | tar xz
mv kokoro /usr/local/bin
```

### 2. 初始化集群

```bash
# 初始化主节点，创建一个空集群
kokoro init --name=mycluster --listen=0.0.0.0:8500

# 加入从节点
kokoro join http://<master-ip>:8500
```

### 3. 配置 `kokoro.yaml`

```yaml
global:
  log_level: info
  image_pull: always

services:
  web:
    image: nginx:latest
    replicas: 3
    ports:
      - 80:80
    healthcheck:
      http_get:
        path: /healthz
        port: 80
    env:
      - ENV=prod
  db:
    image: mysql:5.7
    replicas: 1
    ports:
      - 3306:3306
    env:
      - MYSQL_ROOT_PASSWORD=secret
```

### 4. 部署

```bash
kokoro deploy -f kokoro.yaml
```

### 5. 查看状态

```bash
kokoro ps          # 查看所有服务的容器状态
kokoro logs web    # 查看 `web` 服务日志
kokoro top web     # CPU/内存占用
```

### 6. 停止/删除服务

```bash
kokoro stop web
kokoro rm db
```

### 7. 滚动升级

```bash
kokoro upgrade nginx:latest -f kokoro.yaml
```

## 集成 CI/CD

```bash
kokoro deploy -f kokoro.yaml -t mytoken
```

> 通过 `--token` 参数可直接在 GitHub Actions、GitLab CI 等流水线中使用。

## 文档与社区

- 官方文档：<https://kokohexgrad.io/docs>  
- 交流群：微信/Telegram（扫描下方二维码）  
- Issue 反馈：<https://github.com/hexgrad/kokoro/issues>  

---

> 以上示例以最常见的部署方式为例，具体参数请参考官方文档。祝您使用愉快！