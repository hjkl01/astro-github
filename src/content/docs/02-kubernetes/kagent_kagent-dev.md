
---
title: kagent
---


# kagent

## 项目地址
[https://github.com/kagent-dev/kagent](https://github.com/kagent-dev/kagent)

## 主要特性
- **Kubernetes 资源监控**：实时采集节点、Pod、Container 的各种指标（CPU、内存、磁盘 I/O、网络流量等）。  
- **Prometheus 兼容**：以标准 metric 格式暴露数据，方便直接被 Prometheus 抓取。  
- **端口转发与 API 代理**：在同一容器内运行 `kagent` 与 k8s API 代理，简化网络访问。  
- **轻量级 DaemonSet**：可直接部署为 DaemonSet，保证每个节点都被监控。  
- **可扩展插件体系**：支持自定义插件，快速接入第三方监控源或业务指标。  
- **低资源占用**：采用 Go 原生编译，二进制体积小、启动慢，运行时 CPU & 内存消耗低。  

## 关键功能
| 功能 | 说明 |
|------|------|
| **Metrics 采集** | 通过 kubelet、container runtime API 采集多维度指标。 |
| **Events 监听** | 监听 Kubernetes 事件，将重要告警转化为 Prometheus alert。 |
| **日志收集** | 可配置将容器日志通过 webhook 推送到远程日志系统。 |
| **Discovery** | 自动发现新增 Namespace、Pod、Service 等资源，无需手动配置。 |
| **安全性** | 支持使用 ServiceAccount 与 RBAC，使用最小权限原则。 |

## 用法示例

### 1. 使用 Docker 镜像直接运行
```bash
docker run -d --name kagent \
  --hostname $(hostname) \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /var/lib/kagent:/data \
  -p 9100:9100 \
  kagent/kagent:latest
```

### 2. 作为 DaemonSet 部署（最常用方式）
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: kagent
  labels:
    app: kagent
spec:
  selector:
    matchLabels:
      app: kagent
  template:
    metadata:
      labels:
        app: kagent
    spec:
      serviceAccount: kagent-sa
      containers:
      - name: kagent
        image: kagent/kagent:latest
        ports:
        - containerPort: 9100
          name: metrics
        volumeMounts:
        - name: docker-sock
          mountPath: /var/run/docker.sock
        - name: data
          mountPath: /data
      volumes:
      - name: docker-sock
        hostPath:
          path: /var/run/docker.sock
      - name: data
        hostPath:
          path: /var/lib/kagent
```

### 3. 配置例子（config.yaml）
```yaml
global:
  scrape_interval: 15s
  log_level: info

kube:
  host: https://kubernetes.default.svc:443
  ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
  token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
  skip_verify: false

metrics:
  enable_container: true
  enable_node: true
  enable_pod: true
  enable_service: false
```

将上述 `config.yaml` 挂载到容器（例如 `-v ./config.yaml:/etc/kagent/config.yaml`），即可自定义采集范围和 Prometheus 抓取频率。  

## 参考文件
- `README.md` – 项目简介与安装文档  
- `docs/` – 详细使用手册与 API 说明  
- `charts/kagent/` – Helm Chart，用于快速部署  

---

> 以上内容已转换为 Markdown，可直接保存至 `src/content/docs/00/kagent_kagent-dev.md`。