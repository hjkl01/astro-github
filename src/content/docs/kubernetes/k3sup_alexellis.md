---
title: k3sup
---

# k3sup 项目

**GitHub 项目地址**: [https://github.com/alexellis/k3sup](https://github.com/alexellis/k3sup)

## 主要特性
k3sup 是一个轻量级的 Kubernetes 安装工具，专为快速部署 K3s（轻量级 Kubernetes 发行版）而设计。其主要特性包括：
- **简单易用**：通过单个命令即可在远程服务器上安装和管理 K3s，无需复杂的配置。
- **跨平台支持**：支持 Linux、macOS 和 Windows 环境，通过 SSH 连接远程主机。
- **自动化管理**：自动处理 K3s 的安装、加入集群、卸载等操作，支持单节点和多节点集群。
- **轻量高效**：基于 Go 语言开发，体积小巧，便于集成到 CI/CD 管道或脚本中。
- **安全性**：使用 SSH 密钥认证，确保安装过程安全可靠。

## 主要功能
- **安装 K3s**：快速在服务器上部署 K3s 服务器或代理节点。
- **集群管理**：支持添加新节点到现有 K3s 集群，或从集群中移除节点。
- **配置导出**：生成 kubeconfig 文件，便于本地 kubectl 访问集群。
- **卸载支持**：轻松移除 K3s 安装，清理系统资源。
- **自定义选项**：允许指定 K3s 的额外参数，如数据目录、端口等。

## 用法
k3sup 的用法简单，通过命令行工具操作。以下是基本示例（假设已安装 k3sup 二进制文件）：

### 1. 安装 K3s 服务器（单节点集群）
```bash
k3sup install --ip <服务器IP> --user <用户名> --ssh-key <SSH密钥路径>
```
- 这将在指定服务器上安装 K3s，并生成 kubeconfig 文件。

### 2. 加入集群（添加代理节点）
```bash
k3sup join --ip <服务器IP> --server-ip <主服务器IP> --user <用户名> --ssh-key <SSH密钥路径>
```
- 用于将新节点加入现有 K3s 集群。

### 3. 导出 kubeconfig
```bash
k3sup install --ip <服务器IP> --user <用户名> --k3s-extra-args "--cluster-init" --local-path ./kubeconfig
```
- 安装后导出配置到本地文件。

### 4. 卸载 K3s
```bash
k3sup uninstall --ip <服务器IP> --user <用户名>
```

更多高级用法和选项，请参考项目文档。k3sup 适合开发者和运维人员快速搭建 Kubernetes 测试环境。