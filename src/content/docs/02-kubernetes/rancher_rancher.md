
---
title: rancher
---

# Rancher 项目

**项目地址：** [https://github.com/rancher/rancher](https://github.com/rancher/rancher)

## 主要特性
Rancher 是一个开源的 Kubernetes 管理平台，专为企业级容器编排而设计。它提供了一个简化的界面和工具来部署、管理和扩展 Kubernetes 集群。主要特性包括：
- **多集群管理**：支持同时管理多个 Kubernetes 集群，包括本地、云端和混合环境。
- **用户友好的 UI**：直观的 Web 界面，便于监控、配置和故障排除。
- **安全与访问控制**：集成 RBAC（基于角色的访问控制）和多租户支持，确保安全隔离。
- **自动化与扩展**：内置 CI/CD 集成、监控（Prometheus）、日志（Fluentd）和自动缩放功能。
- **开源与社区支持**：基于 Apache 2.0 许可，活跃的社区贡献和企业级支持选项。
- **兼容性强**：支持 Kubernetes 的所有版本，并与 Docker、Helm 等工具无缝集成。

## 主要功能
- **集群部署**：快速创建和管理 Kubernetes 集群，支持从零开始或导入现有集群。
- **应用管理**：通过 Rancher 的应用目录（Catalog）部署和管理容器化应用，如数据库、Web 服务等。
- **监控与日志**：实时监控资源使用、节点健康和 Pod 状态，提供警报和可视化仪表板。
- **网络与存储**：集成 Ingress、Load Balancer 和持久化存储解决方案。
- **备份与恢复**：自动化备份集群配置和数据，支持灾难恢复。
- **集成与 API**：RESTful API 和 CLI 工具，便于自动化脚本和第三方集成。

## 用法
1. **安装 Rancher**：
   - 在 Kubernetes 集群上部署 Rancher Server：使用 Helm 命令 `helm install rancher rancher-stable/rancher --namespace cattle-system --set hostname=<your-domain>`。
   - 或者在 Docker 上运行：`docker run -d --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher:latest`。

2. **访问界面**：
   - 通过浏览器访问 Rancher 的 URL（默认 HTTPS），首次登录需设置管理员密码。

3. **创建和管理集群**：
   - 在 UI 中选择“集群” > “创建”，选择提供商（如 AWS、GCP 或自定义），跟随向导配置节点和网络。
   - 导入现有集群：生成 kubeconfig 并使用 `kubectl` 应用 Rancher 的代理。

4. **部署应用**：
   - 导航到“应用” > “启动”，从目录中选择应用（如 Nginx），配置参数并部署。

5. **监控与维护**：
   - 使用内置仪表板查看指标，设置警报。
   - 通过 CLI：安装 `rancher` CLI 并使用命令如 `rancher clusters ls` 来管理资源。

更多详细用法，请参考官方文档：[Rancher 文档](https://rancher.com/docs)。