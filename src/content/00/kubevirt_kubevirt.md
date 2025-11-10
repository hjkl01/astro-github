# KubeVirt

## 项目简介

KubeVirt 是一个虚拟机管理插件，用于 Kubernetes。它通过 Kubernetes 的 Custom Resource Definitions (CRD) API 添加额外的虚拟化资源类型（特别是 `VM` 类型），从而允许使用 Kubernetes API 来管理这些 `VM` 资源与其他 Kubernetes 资源。

## 主要功能

- **虚拟化扩展**：在 Kubernetes 上提供虚拟化解决方案的通用基础。
- **声明式管理**：允许声明式地：
  - 创建预定义的虚拟机 (VM)
  - 在 Kubernetes 集群上调度 VM
  - 启动 VM
  - 停止 VM
  - 删除 VM

## 用法

### 安装和开始使用

1. **快速开始**：访问 [kubevirt.io](https://kubevirt.io/get_kubevirt/) 进行快速入门。
2. **用户文档**：查看 [kubevirt.io/docs](https://kubevirt.io/user-guide/) 获取详细使用指南。

### 基本用法示例

KubeVirt 通过 Kubernetes API 管理 VM 资源。以下是一个简单的 VM 定义示例：

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: testvm
spec:
  running: false
  template:
    metadata:
      labels:
        kubevirt.io/size: small
        kubevirt.io/os: linux
    spec:
      domain:
        devices:
          disks:
            - name: containerdisk
              disk:
                bus: virtio
            - name: cloudinitdisk
              disk:
                bus: virtio
        resources:
          requests:
            memory: 64M
      volumes:
        - name: containerdisk
          containerDisk:
            image: kubevirt/fedora-cloud-container-disk-demo:latest
        - name: cloudinitdisk
          cloudInitNoCloud:
            userData: |
              #cloud-config
              password: fedora
              chpasswd: { expire: False }
```

### 开发和贡献

- **开发环境设置**：参考 [Getting Started Guide](https://github.com/kubevirt/kubevirt/blob/main/docs/getting-started.md)。
- **贡献指南**：阅读 [CONTRIBUTING.md](https://github.com/kubevirt/kubevirt/blob/main/CONTRIBUTING.md)。

## 相关资源

- [官方网站](https://kubevirt.io)
- [博客](https://kubevirt.io/blogs/)
- [YouTube 频道](https://www.youtube.com/channel/UC2FH36TbZizw25pVT1P3C3g)
- [社区 Slack](https://kubernetes.slack.com/?redir=%2Farchives%2FC8ED7RKFE)
- [邮件列表](https://groups.google.com/forum/#!forum/kubevirt-dev)

## 许可证

KubeVirt 采用 [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt) 许可证。
