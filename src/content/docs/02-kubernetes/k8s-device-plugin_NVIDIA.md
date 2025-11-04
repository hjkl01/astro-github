
---
title: k8s-device-plugin
---


# NVIDIA k8s-device-plugin

**项目地址**: https://github.com/NVIDIA/k8s-device-plugin

---

## 主要特性

- **GPU 资源管理**  
  为 NVIDIA GPU 提供统一的 Kubernetes 资源管理器，允许 Pod 通过 `nvidia.com/gpu` 资源请求显卡。

- **GPU 设备插件（Device Plugin）**  
  容器运行时可通过 `Device Plugin` 读取 GPU 信息，实现 GPU 热插拔、自动发现与管理。

- **多租户 & 资源隔离**  
  支持在同一节点上不同 Pod 使用不同数量的 GPU，并保证资源隔离。

- **性能监控与指标**  
  提供 GPU 使用率、内存占用、温度等监控指标，便于与 Prometheus 等监控系统集成。

- **兼容性**  
  支持 NVIDIA Driver 450.x 及更高版本、CUDA 10+，并兼容多种 GPU 型号（Tesla, GeForce, A100 等）。

---

## 功能概要

| 功能 | 描述 |
|------|------|
| **Device Allocation** | 根据 Pod 的 GPU 请求量动态分配 /dev/nvidiaX 设备。 |
| **Resource Discovery** | 通过 `apiVersion: deviceplugin.k8s.io/v1alpha2` 发现 GPU 资源。 |
| **GPU Partitioning** | 通过 `nvidia.com/gpu` 资源标签实现显存分区（GPU子分配）。 |
| **Driver & Runtime Checks** | 自动检查 NVIDIA Driver 和 Container Runtime 的兼容性。 |
| **Metrics Export** | 通过 `/metrics` 暴露 Prometheus 可拉取指标。 |
| **Health Checks** | 对 GPU 和插件运行状态进行健康监测。 |
| **多节点支持** | 在多节点集群中同步 GPU 资源信息，确保调度一致性。 |

---

## 用法

### 1. 安装 NVIDIA Device Plugin

```bash
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.12.0/nvidia-device-plugin.yml
```

> 确保集群中的每个节点都已安装 NVIDIA 驱动与 CUDA。

### 2. 在 Pod 中请求 GPU

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-pod
spec:
  containers:
  - name: cuda-container
    image: nvidia/cuda:11.8.0-base-ubuntu22.04
    resources:
      limits:
        nvidia.com/gpu: 1   # 请求 1 张 GPU
```

### 3. 通过 GPU 标签限制托管

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    dagster/*: "true"   # Example label
spec:
  containers:
  - name: gpu-app
    image: my-gpu-app
    resources:
      limits:
        nvidia.com/gpu: 2   # 请求 2 张 GPU
```

### 4. 监控 GPU 指标

在 Prometheus 配置中添加：

```yaml
- job_name: "k8s-nvidia-device-plugin"
  static_configs:
  - targets: ["<node-ip>:9101"]
```

### 5. 诊断与排障

| 命令 | 用途 |
|------|------|
| `kubectl get pods -o yaml | grep nvidia.com/gpu` | 查看 GPU 分配信息 |
| `kubectl describe node <node-name>` | 检查 GPU 资源列表 |
| `kubectl logs <plugin-pod>` | 查看插件错误日志 |

---

## 常见问题

- **GPU 驱动未安装**  
  插件会在启动时失败，请确认节点上已安装匹配的驱动版本。

- **CPU 与 GPU 资源不匹配**  
  Kubernetes 规划时可能出现错误，建议检查节点可用 CPU 与 GPU 的对应关系。

- **多租户隔离问题**  
  使用 `nodeSelector` 或 `affinity` 进一步限制 Pod 调度范围。

---

> 以上内容为 NVIDIA k8s-device-plugin 的核心特性、功能与使用方式。请根据自身集群环境进行相应调整。