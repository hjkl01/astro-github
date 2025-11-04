
---
title: juicefs
---


# JuiceFS

> 项目地址: [https://github.com/juicedata/juicefs](https://github.com/juicedata/juicefs)

## 1. 概述
JuiceFS 是一款基于云存储的分布式文件系统，兼容 POSIX API，支持高并发读写，适用于大数据、机器学习、容器化等场景。

## 2. 主要特性
- **云原生**：直接挂载 S3、Azure Blob、Google Cloud Storage 等对象存储，无需额外对象存储层。
- **高性能**：采用分布式元数据服务（Meta Server）与统一缓存，IO 性能可与本地文件系统媲美。
- **可伸缩**：支持水平扩容，Meta Server 可水平扩展，存储容量随对象存储扩容。
- **快照与备份**：支持快照、点检镜像，便于数据恢复与版本管理。
- **多租户**：支持 ACL、配额、用户分隔，满足多租户场景。
- **兼容 POSIX**：可以直接在 Linux、k8s、Docker、Spark、Hadoop 等环境下使用。

## 3. 核心功能
| 功能 | 说明 |
|------|------|
| **挂载** | `juicefs mount` 支持多种后端，使用 FUSE 挂载到本地文件系统。 |
| **元数据服务** | Meta Server 负责文件目录、权限、快照等元数据，支持多实例部署。 |
| **缓存层** | 支持 Redis、Memcached 或内存缓存，降低对象存储延迟。 |
| **CLI 管理** | `juicefs` 命令行工具，可查询状态、管理元数据、创建快照、同步等。 |
| **集成** | 与 Docker、Kubernetes、Spark、Hadoop、TensorFlow 等生态无缝对接。 |

## 4. 安装与配置

```bash
# 安装 JuiceFS
curl -s https://juicedata.com/install.sh | bash

# 创建文件系统并挂载
juicefs format -i <instance_id> <s3://bucket/path>
juicefs mount -o allow_other <s3://bucket/path> /mnt/juicefs
```

> **Meta Server 部署**（示例）
```bash
juicefs meta-server start -p 8080 -c /etc/juicefs/meta.conf
```

## 5. 使用示例

```bash
# 创建目录
mkdir /mnt/juicefs/data

# 上传文件
cp local_file.txt /mnt/juicefs/data/

# 查看元数据
juicefs stat /mnt/juicefs/data/local_file.txt

# 创建快照
juicefs snapshot create snapshot1

# 恢复快照
juicefs snapshot restore snapshot1
```

## 6. 典型场景

| 场景 | 说明 |
|------|------|
| **大数据处理** | 在 Spark、YARN、Hadoop 生态中直接读取/写入 JuiceFS，避免数据搬运。 |
| **容器卷** | 通过 `juicefs` 作为 Kubernetes PersistentVolume，支持多副本共享。 |
| **机器学习** | 训练模型时使用 JuiceFS 共享数据集，支持多节点并行。 |
| **日志归档** | 将日志写入 JuiceFS，利用快照实现灰度回滚。 |

## 7. 资源
- 官方文档: https://juicefs.com/docs/
- GitHub: https://github.com/juicedata/juicefs
- 社区: https://github.com/juicedata/juicefs/discussions
