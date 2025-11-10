---
title: calico
---

# Calico 项目简介

> GitHub 地址: https://github.com/projectcalico/calico

## 主要特性

- **容器网络插件**  
  兼容 Kubernetes、OpenShift、Docker、Rkt 等多种容器平台，负责 Pod/VM 的 IP 分配、路由与安全策略执行。

- **BGP 路由**  
  通过邻居节点间的 BGP 对等来交换路由，支持跨云、公有网络与外部网络的透明通信。

- **网络安全策略 (NetworkPolicy)**  
  以 IP 组为核心，实现细粒度、基于标签的入站/出站流量控制。支持 Kubernetes NetworkPolicy、Calico 自有扩展等。

- **IP 地址管理 (IPAM)**  
  支持多种 IPAM 模式（Pod、Node、OpenStack、AWS 等），提供可扩展的地址池管理。

- **多租户 & 多集群**  
  通过 Calico `Overlay` 或 `VXLAN`,`IPIP` 等技术实现逻辑隔离，支持管理多集群或多租户环境。

- **高性能 & 零内存开销**  
  Calico 直接在宿主机网卡层处理转发，避免网络层侵占 CPU 与内存，使集群保持超低延迟。

- **丰富的监控与日志**  
  与 Prometheus、Grafana、ELK 等生态系统集成，提供链路追踪、指标收集与日志聚合。

## 核心功能

| 功能 | 说明 |
|------|------|
| `calicoctl` | 命令行工具，用于管理 Calico 配置、IPAM、路由等。 |
| `calico-node` | 代理进程，负责 BGP 对等、规则编写、链路监控。 |
| `calico-cni` | CNI 插件，负责容器 IP 分配与网络规则插桩。 |
| `calico-typha` | (可选) 进行 BGP 对等聚合，在大规模集群中提高可伸缩性。 |
| `calico-kube-controllers` | 监控 Kubernetes 资源，产生 Calico 对象映射。 |
| `calico-cloud-controllers` | 针对私有云/公有云集成实现 IPAM、路由等平滑迁移。 |

## 用法示例

1. **安装** (以 Kubernetes 为例)

   ```bash
   kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
   ```

2. **启动代理**

   ```bash
   docker run -d --privileged --net=host \
       --name calico-node \
       -v /var/run/calico:/var/run/calico \
       -v /proc:/host/proc:ro \
       -v /lib/modules:/host/lib/modules:ro \
       calico/node:latest
   ```

3. **配置网络策略**

   ```yaml
   # 只允许同一 namespace 内的 Pod 互联
   apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: allow-same-namespace
   spec:
     podSelector: {}
     ingress:
     - from:
       - podSelector: {}
   ```

4. **查看 BGP 统计**  

   ```bash
   calicoctl node status
   ```

5. **监控**  

   - 在 `metrics.enabled` 后端部署 Prometheus。  
   - 使用 Grafana 预设仪表盘查看延迟、吞吐量与失效率。

## 快速启动

```bash
# 1. 克隆代码
git clone https://github.com/projectcalico/calico.git

# 2. 进入目录
cd calico

# 3. 生成系统运行时所需的服务文件
make manifests

# 4. 部署到 Kubernetes
kubectl apply -f manifests

# 5. 验证
kubectl get pods -n calico-system
```

> 以上示例基于 Calico 3.x 版本，详情请查看官方文档（https://docs.projectcalico.org/）。

---
