---
title: Velero
---

# Velero

## 功能介绍

Velero（前身为Heptio Ark）是一个用于备份和恢复Kubernetes集群资源和持久卷的工具。它支持在公有云平台或本地环境中运行。

Velero的主要功能包括：

- **备份和恢复**：在集群丢失的情况下备份集群并进行恢复。
- **迁移**：将集群资源迁移到其他集群。
- **复制**：将生产集群复制到开发和测试集群。

Velero由两个主要组件组成：

- 在集群上运行的服务器。
- 本地运行的命令行客户端。

## 用法

### 安装

1. 下载并安装Velero CLI：

   ```bash
   # 使用包管理器或从GitHub releases下载
   ```

2. 在Kubernetes集群中安装Velero：

   ```bash
   velero install --provider <provider> --bucket <bucket> --secret-file <secret-file>
   ```

   其中`<provider>`可以是AWS、GCP、Azure等。

### 创建备份

```bash
velero backup create <backup-name> --include-namespaces <namespaces>
```

### 恢复备份

```bash
velero restore create --from-backup <backup-name>
```

### 更多用法

详细的安装和使用指南请参考[官方文档](https://velero.io/docs/)。
