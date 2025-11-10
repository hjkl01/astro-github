---
title: sealos
---

# Sealos 项目

## 项目地址
[GitHub 项目地址](https://github.com/labring/sealos)

## 主要特性
Sealos 是一个开源的云原生操作系统，专注于简化 Kubernetes 集群的部署、管理和运维。它基于 Sealos 的核心引擎，提供了高效的容器编排和应用分发能力。主要特性包括：
- **一键部署 Kubernetes**：支持快速创建和管理 Kubernetes 集群，兼容多种云环境。
- **应用商店与分发**：内置应用市场，用户可以轻松安装和管理流行应用，如数据库、Web 服务等。
- **多云支持**：兼容 AWS、Azure、阿里云等主流云提供商，以及本地部署。
- **自动化运维**：集成 CI/CD 管道、监控和日志收集，减少手动操作。
- **高可用性与扩展性**：支持自动缩放、负载均衡和故障恢复，确保系统稳定。
- **开源与社区驱动**：基于 Apache 2.0 许可，鼓励社区贡献和插件扩展。

## 主要功能
Sealos 的核心功能围绕云原生基础设施展开：
- **集群管理**：创建、升级、销毁 Kubernetes 集群，支持多节点配置。
- **应用部署**：通过 YAML 或 UI 界面部署 Helm Charts、Docker 镜像或自定义应用。
- **资源调度**：优化 CPU、内存和存储资源的分配，支持 GPU 和边缘计算。
- **安全与合规**：集成 RBAC、NetworkPolicy 和镜像扫描，确保环境安全。
- **监控与调试**：内置 Prometheus、Grafana 等工具，提供实时监控和问题诊断。
- **备份与恢复**：支持数据备份、快照和灾难恢复功能。

## 用法
### 安装 Sealos
1. **前提条件**：确保系统为 Linux（推荐 Ubuntu 20.04+），安装 Docker 和 kubectl。
2. **下载安装**：
   ```bash
   curl -fsSL https://get.sealos.io | sh
   ```
   或从 GitHub Releases 下载二进制文件。

### 基本用法
1. **初始化集群**：
   ```bash
   sealos init --cloud-provider aliyun  # 以阿里云为例
   ```
   这将创建一个基本的 Kubernetes 集群。

2. **部署应用**：
   ```bash
   sealos app install nginx  # 从应用商店安装 Nginx
   ```
   或使用自定义 YAML：
   ```bash
   sealos apply -f my-app.yaml
   ```

3. **管理集群**：
   - 查看集群状态：`sealos status`
   - 扩展节点：`sealos add node --count 2`
   - 升级版本：`sealos upgrade kubernetes:v1.25.0`

4. **访问 UI**（可选）：
   安装后，通过 `sealos dashboard` 启动 Web 界面，在浏览器中访问 `http://localhost:8080` 进行图形化管理。

更多详细用法，请参考官方文档：https://sealos.io/docs。