
---
title: meshery
---


# Meshery

**GitHub 地址**: [https://github.com/meshery/meshery](https://github.com/meshery/meshery)

---

## 项目简介

Meshery 是一个开源的**服务网格管理平台**，旨在帮助企业和开发者统一管理多云与多集群环境中的多种服务网格（如 Istio、Linkerd、Cons、Kuma 等）。它提供了一套完整的可视化界面、自动化运营工具、模型驱动的配置方法以及丰富的 API，支持服务网格的安装、升级、性能调优、运维以及安全管控。

---

## 核心特性

1. **多网格支持**  
   - 同时管理 Istio、Linkerd、Consul、Kuma 等 10+ 服务网格。  
   - 支持多 Kubernetes 集群（单集群、本地、云端、跨云端）下的统一操作。

2. **可视化与监控**  
   - 直观的 Service Mesh 结构图（Service Mesh Diagram）。  
   - 运行时状态监控、指标聚合与告警。  
   - 通过 Prometheus、Grafana、Jaeger、OpenTelemetry 集成实时报表。

3. **模型驱动配置**  
   - **Meshery Operator**：通过自定义资源（CRD）生成和管理网格配置。  
   - 使用 **Service Mesh Protocols (SMP)** 或 **Open Service Mesh SDK** 进行统一配置。  
   - 支持业务场景模板（Istio VirtualService、DestinationRule 等）回调和自动化部署。

4. **服务网格生命周期管理**  
   - 自动升（升级）/降级（回退）网格版本。  
   - 灾难恢复、滚动升级与灰度发布。  
   - 业务服务蓝绿/金丝雀发布、流量镜像、熔断器。

5. **安全与合规**  
   - 统一证书管理与自动续签（CertManager）。  
   - 策略审计、访问控制、加密流量、证书失效监控。  
   - 侧信道（Sidecar Injection）与多租户隔离。

6. **API 与集成**  
   - RESTful API 与 OpenAPI 规范。  
   - SDK（Go、Node.js、Python）及 CLI（meshery-cli）访问。  
   - 与 CI/CD、GitOps 集成（ArgoCD、Flux）实现自动化部署。

7. **插件生态**  
   - 支持自定义插件（Meshery Adapter）对接第三方工具。  
   - Meshery Catalog：在线插件、社区共享模板与资源。

---

## 主要功能

| 功能 | 说明 |
|------|------|
| **安装 & 升级** | 使用 Helm chart 或 `kubectl apply -f operator.yaml` 安装 Meshery。支持版本回滚、自动升级。 |
| **Dashboard** | Web UI 直观展示集群状态、服务拓扑、健康度、资源使用。 |
| **Meshery Adapter** | 统一网格生态，适配不同网格的细节配置与监控。 |
| **Data Harvest** | 使用 sidecar 采集应用数据，融合到 Meshery 平台做运营与排障。 |
| **Policies** | 统一授权策略（基于 Istio RBAC），安全与访问控制。 |
| **Traffic Management** | 流量镜像、全链路路由、熔断器、重试、超时、优先级。 |
| **Observability** | 通过 Prometheus + Grafana + Tempo 监控链路、指标与日志。 |
| **Service Mesh Catalog** | 一键下载、部署多网格组件与模板。 |
| **CLI** | `mesheryctl` 用于查询、创建、同步配置。 |

---

## 用法

### 1. 安装 Meshery

```bash
# 下载安装 Helm
helm repo add meshery https://meshery.github.io/helm
helm repo update

# 安装 Meshery Operator 和 Dashboard
helm upgrade --install meshery meshery/meshery \
  --namespace meshery-system \
  --create-namespace \
  --set mesheryOperator.enabled=true \
  --set dashboard.enabled=true
```

> 也可以直接使用 `kubectl` 部署 Operator：

```bash
kubectl apply -f https://raw.githubusercontent.com/meshery/meshery/main/deploy/meshery-operator.yaml
```

### 2. 注册服务网格

在 Dashboard 内部或通过 CLI 向 Meshery 发送网格配置。

```bash
# 使用 Meshery Adapter 连接 Istio
kubectl apply -f https://raw.githubusercontent.com/meshery/meshery/main/deploy/istio-operator.yaml
```

Meshery 通过自动探测方式把网格加入到管理列表。

### 3. 创建与同步网格配置

```bash
# 通过 CLI 导入 Meshery 模板
mesheryctl registry download meshery/istio:control_plane.yaml

# 本地编辑
mesheryctl registry edit meshery/istio:control_plane.yaml

# 同步到目标集群
mesheryctl registry sync cluster1
```

### 4. 监控与告警

- 访问 `https://<meshery-host>/login` 查看 Dashboard。  
- 配置 Prometheus Grafana，开启 Meshery 监控面板。  
- 通过 `mesheryctl context` 切换集群。

### 5. 自动化与 CI/CD

在 GitHub Action 或 ArgoCD 中：

```yaml
# 示例：ArgoCD 自动化
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: meshery-operator
spec:
  project: default
  source:
    repoURL: 'https://github.com/meshery/meshery.git'
    path: 'deploy'
  destination:
    server: 'https://kubernetes.default.svc'
    namespace: meshery-system
```

### 6. 插件与扩展

- 访问 Meshery Catalog 下载插件模板。  
- 使用 `mesheryctl` 安装自定义 Meshery Adapter。

```bash
mesheryctl registry install-plugin <plugin-repo-url>
```

---

## 常见命令

| 命令 | 作用 |
|------|------|
| `mesheryctl version` | 查看 Meshery 版本 |
| `mesheryctl create mesh` | 创建 Meshery Mesh CRD |
| `mesheryctl edit mesh <name>` | 编辑 Meshery Mesh |
| `mesheryctl delete mesh <name>` | 删除 Meshery Mesh |
| `mesheryctl registry list` | 列出已下载的配置/插件 |
| `mesheryctl registry pull <name>` | 拉取最新配置 |
| `mesheryctl jobs list` | 查看运行中的 Meshery 任务 |

---

## 开源协议

MIT © Meshery Contributors

---

> 保存文件到 `src/content/docs/00/meshery_meshery.md` 即可。