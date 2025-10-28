
---
title: rook
---


# Rook

Rook 是一个开源的 Kubernetes 原生存储操作系统，旨在简化在 Kubernetes 集群中运行分布式存储的过程。该项目为 Ceph、MinIO、EdgeFS、Elastic File System (EFS) 等多种存储后端提供统一的部署、运维、监控和扩展体验。

## 主要特性

| 特性 | 说明 |
|------|------|
| **Kubernetes 原生** | 通过 Operators 与自定义资源（Custom Resource Definition, CRD）完整管理存储集群生命周期，所有操作可在 `kubectl`、CI/CD 或 Helm 中完成。 |
| **多后端支持** | 原生支持 Ceph (RBD, CephFS), MinIO, EdgeFS, 云厂商 NAS 以及本地存储方案。 |
| **零停机升级** | 通过滚动升级、热迁移、快照与克隆等功能实现无中断升级与数据迁移。 |
| **自动化运维** | 监控、告警、备份/恢复、节点自愈等功能内置，可与 Prometheus、Grafana、Alertmanager 集成。 |
| **高度可扩展** | 支持水平扩容，支持单节点/多节点/集群间跨域部署。 |
| **简易安装** | 通过 Helm charts、OperatorDeployment 或直接`kubectl apply`一次即可完成安装。 |

## 核心功能

| 功能 | 说明 |
||------|
| **卷创建与管理** | 通过 `RookCephBlockPool`、`CephFileSystem`、`CephBlockPool` 等 CRD 创建块、文件存储。 |
| **快照与克隆** | 支持快照恢复、克隆对象，支持 Ceph RBD、CephFS 与 MinIO 的快照。 |
| **备份/恢复** | 支持使用 Rook Backupservice 与 `rook-backup-service` 实现备份/恢复。 |
| **监控** | 自动将监控数据导出至 Prometheus。可通过 `ceph dashboard` 访问 Web UI。 |
| **面向对象存储** | 通过 S3、Swift 或 Ceph RadosGW 接口提供对象存储。 |
| **安全** | 支持 TLS 加密、RBAC、机密管理 (Secret) 等。 |

## 用法

### 1. 安装 Rook Operator```bash
# 安装 Helm（若已安装可忽略）
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 添加 Rook Helm 仓库
helm repo add rook-release https://charts.rook.io/release
helm repo update

# 安装 Operator
helm install rook-ceph rook-release/rook-ceph --namespace rook-ceph-system --create-namespace
```

### 2. 部署 Ceph 集群

```bash
# 创建 Ceph cluster CRD
kubectl apply -f - <<EOF
apiVersion: ceph.rook.io/v1
kind: CephCluster
metadata:
  name: ceph
  namespace: rook-ceph
spec:
  cephVersion:
    image: ceph/ceph:v15.2.8
  dataPool:
    replicated:
      size: 3
  monitorCount: 3
  osdDeployments:
  - name: osd
    count: 3
EOF
```

> **提示**  
> - `count` 表示 OSD 节点数。  
> - `monitorCount` 通常是奇数（3、5、7）。  
> - OSD 节点需在同一 namespace 下。

### 3. 创建块存储

```yaml
apiVersion: rook.io/v1
kind: CephBlockPool
metadata:
  name: replicapool
  namespace: rook-ceph
spec:
  replicated:
    size: 3

---
apiVersion: k8s.io/v1
kind: PersistentVolumeClaim
metadata:
  name: rook-ceph-pvc
spec:
  storageClassName: rook-ceph-block
  resources:
    requests:
      storage: 10Gi
```

Apply:

```bash
kubectl apply -f block-pool.yaml
kubectl apply -f pvc.yaml
```

### 4. 对象存储

```bash
kubectl apply -f - <<EOF
apiVersion: ceph.rook.io/v1
kind: CephObjectStore
metadata:
  name: rook-ceph-object
  namespace: rook-ceph
spec:
  metadataPool:
    replicated:
      size: 3
  dataPool:
    replicated:
      size: 3
  gateway:
    replicas: 3
    sslCertificateRef:
      key: tls.key
      name: tls
      namespace: rook-ceph
EOF
```

访问入口信息：

```bash
kubectl get cephobjectstore -n rook-ceph
```

### 5. 日志与监控

```bash
# 查看 Ceph 监控
curl http://<dashboard-ip>:7000

# Prometheus 指标
kubectl get pod -n rook-ceph-system -l app=rook-ceph-mon
```

## 资源

- 官方文档: https://rook.io/docs/rook/latest/
- Helm chart: https://github.com/rook/rook/tree/main/cluster/examples/kubernetes/ceph
- 贡献指南: https://github.com/rook/rook/blob/master/CONTRIBUTING.md

---

- **项目地址**: https://github.com/rook/rook
