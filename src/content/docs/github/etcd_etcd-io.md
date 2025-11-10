---
title: etcd
---


# etcd
> 项目地址: [https://github.com/etcd-io/etcd](https://github.com/etcd-io/etcd)

## 主要特性
- **分布式一致性键值存储**：采用 Raft 共识协议，保证 99.9% 的一致性与线性读写。
- **高可用与弹性伸缩**：节点可以随时加入或离开集群，自动重新选主并复制数据。
- **灵活的数据模型**：键值对、目录、TTL、事务 (compare, set, get) 等。
- **Watch 机制**：可实时监听键值变更，用于事件驱动与状态同步。
- **多租户（Namespace）**：隔离不同业务空间的数据。
- **安全性**：TLS 加密、SASL 认证、RBAC 权限控制。
- **原子锁与计数器**：支持基于键的分布式锁和计数。
- **快照与日志滚动**：支持数据快照、日志压缩，支持恢复与备份。

## 核心功能
| 功能 | 描述 |
|------|------|
| **存储** | GET/PUT/DELETE 单或批量操作。 |
| **事务** | Compare‑Swap、CAS、事务原子性。 |
| **Watch** | 监听键/前缀变更。 |
| **租约 (Lease)** | TTL 后自动失效，适用于注册中心。 |
| **分布式锁** | 基于租约实现互斥。 |
| **快照** | `etcdctl snapshot save` 与 `restore`。 |
| **复制** | 将集群数据复制到另一个集群（`etcdctl migrate`）。 |

## 用法示例

### 1. 启动单节点集群
```bash
./etcd
```

### 2. 基础命令
```bash
# 设置键值
etcdctl put /app/config/db "postgres://user:pass@host/db"

# 获取键值
etcdctl get /app/config/db

# 删除键
etcdctl del /app/config/db

# 监听键变更
etcdctl watch /app/config/db
```

### 3. 事务示例
```bash
etcdctl tx \
  put /counter 1 \
  put /config/active 1
```

### 4. 利用租约实现服务注册
```bash
# 创建租约并绑定键
LEASE_ID=$(etcdctl lease grant 5s | awk '/ID:/ {print $2}')
etcdctl put /services/web --lease=$LEASE_ID "10.0.0.1:8080"

# 续租以保持注册
etcdctl lease keep-alive $LEASE_ID
```

### 5. 分布式锁
```bash
# 加锁
etcdctl lock /locks/db

# 解锁
etcdctl unlock /locks/db
```

### 6. 集群扩容
```bash
# 在新节点上执行
etcd \
  --name node2 \
  --data-dir /var/lib/etcd/data \
  --initial-advertise-peer-urls https://node2:2380 \
  --listen-peer-urls https://0.0.0.0:2380 \
  --listen-client-urls https://0.0.0.0:2379 \
  --advertise-client-urls https://node2:2379 \
  --initial-cluster-token etcd-cluster-1 \
  --initial-cluster node1=https://node1:2380,node2=https://node2:2380 \
  --initial-cluster-state new
```

## 与 Kubernetes 的集成
- **CoreDNS** 与 **kube-apiserver** 使用 etcd 作为后端存储。
- **Kubernetes API Server** 将 etcd 视为持久化存储，所有对象均存入 etcd。
- `kubeadm` 安装 Kubernetes 时默认使用 etcd。  

## 结语
etcd 是一个成熟、稳健的分布式键值存储，凭借 Raft 协议和丰富的 API，广泛应用于服务发现、任务调度、分布式锁、配置管理等领域。它被多家开源平台（Kubernetes、CoreDNS、Docker Swarm）亲自使用并拿来做核心组件。  

``` 

保存路径: `src/content/docs/00/etcd_etcd-io.md