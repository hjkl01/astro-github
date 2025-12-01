---
title: kite
---

# Kite - 现代 Kubernetes 仪表板

Kite 是一个轻量级、现代的 Kubernetes 仪表板，提供直观的界面来管理和监控您的 Kubernetes 集群。它提供实时指标、全面的资源管理、多集群支持和美观的用户体验。

## 功能特性

### 🎯 现代用户体验

- 🌓 **多主题支持** - 深色/浅色/彩色主题，支持系统偏好检测
- 🔍 **高级搜索** - 跨所有资源的全局搜索
- 🌐 **国际化** - 支持英语和中文语言
- 📱 **响应式设计** - 针对桌面、平板和移动设备优化

### 🏘️ 多集群管理

- 🔄 **无缝集群切换** - 在多个 Kubernetes 集群之间切换
- 📊 **每集群监控** - 为每个集群独立配置 Prometheus
- ⚙️ **Kubeconfig 集成** - 从您的 kubeconfig 文件自动发现集群
- 🔐 **集群访问控制** - 细粒度的集群访问权限管理

### 🔍 全面资源管理

- 📋 **完整资源覆盖** - Pods、Deployments、Services、ConfigMaps、Secrets、PVs、PVCs、Nodes 等
- 📄 **实时 YAML 编辑** - 内置 Monaco 编辑器，支持语法高亮和验证
- 📊 **详细资源视图** - 深入信息，包括容器、卷、事件和条件
- 🔗 **资源关系** - 可视化相关资源之间的连接（例如 Deployment → Pods）
- ⚙️ **资源操作** - 直接从 UI 创建、更新、删除、缩放和重启资源
- 🔄 **自定义资源** - 完全支持 CRDs（自定义资源定义）
- 🏷️ **快速镜像标签选择器** - 基于 Docker 和容器注册表 API 轻松选择和更改容器镜像标签
- 🎨 **可自定义侧边栏** - 自定义侧边栏可见性和顺序，并添加 CRDs 以便快速访问
- 🔌 **Kube Proxy** - 通过 Kite 直接访问 pods 或服务，无需 `kubectl port-forward`

### 📈 监控与可观测性

- 📊 **实时指标** - 由 Prometheus 驱动的 CPU、内存和网络使用图表
- 📋 **集群概览** - 全面的集群健康和资源统计
- 📝 **实时日志** - 实时流式传输 pod 日志，支持过滤和搜索
- 💻 **Web/Node 终端** - 通过浏览器直接在 pods/nodes 中执行命令
- 📈 **节点监控** - 详细的节点级性能指标和利用率
- 📊 **Pod 监控** - 单个 pod 资源使用和性能跟踪

### 🔐 安全性

- 🛡️ **OAuth 集成** - 在 UI 中支持 OAuth 管理
- 🔒 **基于角色的访问控制** - 在 UI 中支持用户权限管理
- 👥 **用户管理** - 在 UI 中全面的用户管理和角色分配

## 用法

### Docker 运行

使用预构建的镜像运行 Kite：

```bash
docker run --rm -p 8080:8080 ghcr.io/zxh326/kite:latest
```

### 在 Kubernetes 中部署

#### 使用 Helm（推荐）

1. **添加 Helm 仓库**

   ```bash
   helm repo add kite https://zxh326.github.io/kite
   helm repo update
   ```

2. **使用默认值安装**
   ```bash
   helm install kite kite/kite -n kube-system
   ```

#### 使用 kubectl

1. **应用部署清单**

   ```bash
   kubectl apply -f deploy/install.yaml
   # 或在线安装
   kubectl apply -f https://raw.githubusercontent.com/zxh326/kite/refs/heads/main/deploy/install.yaml
   ```

2. **通过端口转发访问**
   ```bash
   kubectl port-forward -n kube-system svc/kite 8080:8080
   ```

### 从源码构建

1. **克隆仓库**

   ```bash
   git clone https://github.com/zxh326/kite.git
   cd kite
   ```

2. **构建项目**

   ```bash
   make deps
   make build
   ```

3. **运行服务器**
   ```bash
   make run
   ```

有关详细说明，请参考[文档](https://kite.zzde.me)。
