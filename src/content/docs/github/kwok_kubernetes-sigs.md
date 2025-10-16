
---
title: kwok
---

# KWOK 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/kubernetes-sigs/kwok)

## 主要特性
KWOK（Kubernetes WithOut Kubelet）是一个轻量级的 Kubernetes 集群模拟工具，由 Kubernetes SIGs 维护。它旨在提供一个高效的 Kubernetes 环境模拟器，而无需实际运行完整的 Kubernetes 集群。主要特性包括：
- **轻量级模拟**：模拟 Kubernetes API 服务器和节点行为，而不启动真实的 kubelet 或容器运行时，资源消耗极低。
- **快速启动**：允许开发者在几秒钟内启动一个模拟的 Kubernetes 集群，用于测试、开发和 CI/CD 流程。
- **节点模拟**：支持模拟多个节点的状态、Pod 调度和资源分配，行为接近真实 Kubernetes。
- **插件支持**：可扩展插件系统，用于自定义模拟行为，如模拟资源限制或网络延迟。
- **兼容性**：与标准 Kubernetes API 兼容，支持 kubectl 等工具无缝集成。
- **跨平台**：支持 Linux、macOS 和 Windows 环境，便于本地开发。

## 主要功能
- **集群模拟**：创建虚拟 Kubernetes 集群，模拟 API 服务器、etcd 和节点生命周期。
- **Pod 管理和调度**：模拟 Pod 的创建、调度、就绪和终止过程，支持自定义阶段（如 Pending、Running、Succeeded）。
- **资源监控**：提供模拟的资源使用情况报告，帮助调试 Kubernetes 应用。
- **测试集成**：适用于单元测试、集成测试和 e2e 测试场景，加速 Kubernetes 应用开发。
- **自定义扩展**：通过 YAML 配置或插件自定义节点和 Pod 的行为，例如模拟故障注入或负载均衡。

## 用法
### 安装
1. 从 GitHub Releases 下载预编译二进制文件，或使用 Go 构建：
   ```
   go install github.com/kubernetes-sigs/kwok/cmd/kwok@latest
   ```
2. 对于 Kubernetes 环境，确保安装 kubectl。

### 基本用法
1. **启动模拟集群**：
   ```
   kwok start --kubeconfig ~/.kube/kwok.config
   ```
   这将启动一个默认的单节点模拟集群，并生成 kubeconfig 文件。

2. **创建模拟节点**：
   使用 YAML 定义节点：
   ```yaml
   apiVersion: v1
   kind: Node
   metadata:
     name: simulated-node
   spec:
     # 节点规格
   ```
   然后应用：
   ```
   kubectl apply -f node.yaml
   ```

3. **部署 Pod**：
   模拟 Pod 调度：
   ```
   kubectl apply -f pod.yaml
   ```
   KWOK 会自动模拟 Pod 在节点上的运行状态。

4. **停止集群**：
   ```
   kwok stop
   ```

### 高级用法
- **多节点模拟**：使用 `kwok node create` 命令添加多个节点。
- **配置自定义**：编辑 `kwok.yaml` 文件调整模拟参数，如节点容量或调度策略。
- **插件集成**：运行 `kwok plugin load <plugin>` 来加载扩展插件。

更多细节请参考项目文档：[https://github.com/kubernetes-sigs/kwok](https://github.com/kubernetes-sigs/kwok)。