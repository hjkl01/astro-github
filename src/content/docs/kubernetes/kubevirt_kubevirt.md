---
title: Kubevirt
---

# KubeVirt

## 项目简介

KubeVirt 是 Kubernetes 的虚拟机管理附加组件，旨在为 Kubernetes 提供虚拟化解决方案。它通过 Kubernetes 的 Custom Resource Definitions (CRD) API 添加额外的虚拟化资源类型（如 `VM` 类型），从而允许使用 Kubernetes API 来管理这些虚拟机资源。

## 主要功能

KubeVirt 允许在 Kubernetes 集群中声明式地进行以下操作：

- 创建预定义的虚拟机 (VM)
- 在 Kubernetes 集群上调度虚拟机
- 启动虚拟机
- 停止虚拟机
- 删除虚拟机

## 用法

### 快速开始

要开始使用 KubeVirt，请访问 [kubevirt.io](https://kubevirt.io/get_kubevirt/) 的快速入门指南。

### 用户文档

详细的用户文档可在 [kubevirt.io/docs](https://kubevirt.io/user-guide) 找到。

### 示例用法

KubeVirt 允许您像管理其他 Kubernetes 资源一样管理虚拟机。例如，您可以创建一个 VM 资源，然后使用标准的 Kubernetes 命令来管理它。

更多信息和最新功能，请查看：

- [KubeVirt 博客](https://kubevirt.io/blogs/)
- [KubeVirt YouTube 频道](https://www.youtube.com/channel/UC2FH36TbZizw25pVT1P3C3g)

## 架构

KubeVirt 通过运行额外的控制器和代理来扩展现有 Kubernetes 集群的功能。这些组件提供虚拟机管理的业务逻辑，而不修改 Kubernetes 核心本身。

## 社区和支持

- Slack: [#virtualization @ kubernetes.slack.com](https://kubernetes.slack.com/?redir=%2Farchives%2FC8ED7RKFE)
- 邮件列表: [kubevirt-dev Google Group](https://groups.google.com/forum/#!forum/kubevirt-dev)
- Twitter: [@kubevirt](https://twitter.com/kubevirt)

## 许可证

KubeVirt 采用 Apache License, Version 2.0 许可证。
