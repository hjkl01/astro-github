
---
title: flyctl
---

# Flyctl 项目

## 项目地址
[https://github.com/superfly/flyctl](https://github.com/superfly/flyctl)

## 主要特性
Flyctl 是 Fly.io 平台的官方命令行工具（CLI），专为开发者设计，用于简化云部署和应用管理。它支持容器化应用的快速部署、全球分布式网络配置，以及高效的资源管理。主要特性包括：
- **无缝集成 Docker**：自动构建和部署 Docker 镜像，支持多架构构建。
- **全球边缘部署**：利用 Fly.io 的全球数据中心网络，实现低延迟应用分发。
- **自动缩放和负载均衡**：内置支持应用自动扩展、路由管理和 SSL 证书自动配置。
- **多应用管理**：支持创建、监控和管理多个应用实例，包括日志查看和秘密管理。
- **插件扩展**：可扩展的架构，支持自定义插件和集成其他工具。
- **跨平台支持**：兼容 macOS、Linux 和 Windows 系统，提供简洁的命令行界面。

## 主要功能
Flyctl 提供了一系列核心功能，覆盖从应用部署到运维的全生命周期：
- **应用部署**：使用 `fly deploy` 命令一键部署应用，支持 Git 集成和 CI/CD 管道。
- **资源配置**：管理虚拟机（VM）大小、持久卷（Volumes）和数据库（如 Postgres）实例。
- **网络与安全**：配置自定义域名、IPv4/IPv6 支持、WireGuard VPN 和访问控制。
- **监控与调试**：实时查看应用日志（`fly logs`）、指标和性能数据，支持 SSH 访问 VM。
- **团队协作**：支持多用户组织管理和权限控制。
- **其他工具**：包括证书管理（`fly certs`）、代理设置（`fly proxy`）和状态检查（`fly status`）。

## 用法
### 安装
1. 从 GitHub Releases 下载二进制文件，或使用包管理器安装：
   - macOS: `brew install flyctl`
   - Linux: `curl -L https://fly.io/install.sh | sh`
   - Windows: 通过 Scoop 或直接下载 EXE 文件。
2. 验证安装：运行 `flyctl version` 检查版本。

### 基本用法
1. **认证和初始化**：
   - 登录：`flyctl auth login`（使用 GitHub 或 email 登录 Fly.io 账户）。
   - 初始化应用：`flyctl launch`（在项目目录中运行，自动检测 Dockerfile 并创建应用）。

2. **部署应用**：
   - 构建并部署：`flyctl deploy`（默认使用本地 Dockerfile，或指定远程镜像）。
   - 示例：`flyctl deploy --image myapp:latest`。

3. **管理应用**：
   - 查看状态：`flyctl status`。
   - 缩放实例：`flyctl scale count 3`（设置 3 个实例）。
   - 查看日志：`flyctl logs`（实时日志流）。
   - 打开应用：`flyctl open`（在浏览器中打开应用 URL）。

4. **高级命令**：
   - 创建卷：`flyctl volumes create myvol --size 10`（创建 10GB 卷）。
   - 配置秘密：`flyctl secrets set API_KEY=yourkey`。
   - SSH 到 VM：`flyctl ssh console`。

更多详细用法，请参考官方文档：https://fly.io/docs/flyctl/。Flyctl 的设计注重简洁性和自动化，适合现代云原生开发。