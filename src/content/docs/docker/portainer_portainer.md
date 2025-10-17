
---
title: portainer
---

# Portainer 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/portainer/portainer)

## 主要特性
Portainer 是一个开源的、轻量级的 Docker 管理用户界面（UI），旨在简化 Docker 环境的监控和管理。它支持多平台部署，包括 Docker、Docker Swarm、Kubernetes 和 Nomad 等容器编排系统。主要特性包括：
- **直观的用户界面**：提供 Web 基于的仪表板，易于可视化管理容器、镜像、卷和网络。
- **多环境支持**：兼容单节点 Docker、集群模式（如 Swarm）和 Kubernetes 集群，允许跨环境统一管理。
- **访问控制**：内置角色-based 访问控制（RBAC），支持用户和团队管理，确保安全访问。
- **实时监控**：实时显示资源使用情况，如 CPU、内存和网络指标。
- **自动化与扩展**：支持模板部署、栈（Stack）管理（Compose 文件），以及与外部工具集成。
- **开源与社区驱动**：免费开源（MIT 许可），有活跃社区和企业版扩展。

## 主要功能
- **容器管理**：创建、启动、停止、重启和删除容器，支持日志查看和控制台访问。
- **镜像管理**：拉取、构建、推送和管理 Docker 镜像，支持私有仓库集成。
- **网络与卷管理**：配置容器网络、持久化卷，并管理存储。
- **栈部署**：使用 Docker Compose 或 Kubernetes YAML 文件一键部署多容器应用。
- **用户与安全**：管理用户权限、API 密钥，并支持 OAuth/SSO 集成。
- **警报与事件**：监控事件日志和设置警报通知。

## 用法
1. **安装**：
   - 使用 Docker 运行：`docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`
   - 对于 Kubernetes：使用 Helm 图表或 YAML 清单部署。
   - 访问 `http://localhost:9000`（默认端口），设置管理员账户。

2. **基本操作**：
   - 登录后，选择环境（本地 Docker 或远程端点）。
   - 在仪表板浏览容器列表，点击容器查看详情、日志或执行命令。
   - 使用“镜像”部分拉取新镜像，或“栈”部分上传 Compose 文件部署应用。
   - 配置用户：在“用户”菜单添加新用户并分配角色。

3. **高级用法**：
   - 连接远程环境：添加端点 URL 和凭据。
   - 自定义模板：上传自定义 YAML/Compose 文件作为部署模板。
   - 监控：启用 Prometheus 集成以获取高级指标。

Portainer 适合 DevOps 团队和开发者快速上手容器管理，无需深入 CLI 操作。