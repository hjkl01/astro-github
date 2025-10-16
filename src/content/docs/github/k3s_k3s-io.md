
---
title: k3s
---

# K3s 项目

## 项目地址
https://github.com/k3s-io/k3s

## 主要特性
K3s 是 Kubernetes 的轻量级发行版，由 Rancher Labs 开发，专为资源受限的环境设计，如边缘计算、IoT 设备和开发测试场景。它在保持 Kubernetes 核心功能的同时，显著减少了资源消耗和复杂性。主要特性包括：
- **轻量级**：单一二进制文件（小于 40MB），启动时间快，内存占用低（通常小于 512MB）。
- **简化安装**：无需外部依赖（如 etcd），内置 SQLite 或嵌入式 etcd，支持 ARM64 和 x86_64 架构。
- **高可用性**：支持多节点集群，内置负载均衡和自动故障转移。
- **安全性**：默认启用 RBAC、TLS 和 Pod 安全策略，集成 Flannel CNI 网络插件。
- **易于维护**：支持自动更新、Helm 图表管理和 Traefik Ingress Controller。
- **兼容性**：完全兼容 Kubernetes API，支持标准工具如 kubectl 和 Helm。

## 主要功能
K3s 提供了一个完整的 Kubernetes 环境，但进行了优化：
- **集群管理**：快速部署单节点或多节点集群，支持服务器（server）和代理（agent）模式。
- **容器编排**：运行 Pod、Deployment、Service 等 Kubernetes 资源，支持 CRI 容器运行时（如 containerd）。
- **网络与存储**：内置 CNI 插件（Flannel）和 CSI 驱动，支持持久卷。
- **监控与日志**：易于集成 Prometheus 和 Fluentd 等工具。
- **边缘支持**：适用于远程位置的部署，具有低延迟和离线能力。

## 用法
### 安装
1. **单节点快速安装**（Linux/macOS/Windows with WSL）：
   ```
   curl -sfL https://get.k3s.io | sh -
   ```
   这将安装 K3s 并启动一个单节点集群。安装后，kubectl 命令可用（位于 `/usr/local/bin/kubectl`）。

2. **多节点集群**：
   - 在主节点（server）运行：
     ```
     curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--cluster-init" sh -
     ```
     获取 token：`cat /var/lib/rancher/k3s/server/node-token`。
   - 在工作节点（agent）运行：
     ```
     curl -sfL https://get.k3s.io | K3S_URL=https://<server-ip>:6443 K3S_TOKEN=<token> sh -
     ```

3. **卸载**：
   ```
   /usr/local/bin/k3s-uninstall.sh
   ```

### 基本操作
- **检查集群状态**：`kubectl get nodes`。
- **部署应用**：使用 YAML 文件或 Helm，例如：
  ```
  kubectl apply -f deployment.yaml
  ```
- **配置**：编辑 `/etc/rancher/k3s/config.yaml` 以自定义设置，如禁用 Traefik 或指定数据存储。
- **更新**：运行安装脚本并添加 `--upgrade` 标志。

更多细节请参考官方文档：https://docs.k3s.io。