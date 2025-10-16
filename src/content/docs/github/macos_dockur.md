
---
title: macos
---

# macOS 项目描述

## 项目地址
[https://github.com/dockur/macos](https://github.com/dockur/macos)

## 主要特性
- **基于 Docker 的 macOS 虚拟化**：该项目允许用户在 Linux 主机上通过 Docker 容器运行 macOS 系统，实现轻量级虚拟机体验，而无需完整的虚拟化软件如 VirtualBox 或 VMware。
- **支持多种 macOS 版本**：兼容 macOS Ventura、Monterey 等主流版本，用户可根据需求选择安装。
- **图形界面支持**：提供完整的 macOS 桌面环境，包括 Finder、Safari 等原生应用，支持音频、视频和外设映射。
- **资源高效**：Docker 容器化设计使资源占用更低，启动速度更快，适合开发测试或日常使用。
- **开源免费**：基于开源工具构建，易于自定义和扩展。

## 主要功能
- **安装 macOS**：一键下载并安装 macOS 镜像，支持从 Apple 官方源获取。
- **运行和管理**：通过命令行或 Web 界面启动、停止和监控 macOS 容器，支持端口转发以访问图形界面。
- **自定义配置**：允许调整 CPU、内存、磁盘大小等资源分配；支持共享文件夹、USB 设备直通。
- **网络和安全**：内置网络桥接，支持 VPN 和防火墙配置；确保容器隔离以保护主机系统。
- **扩展支持**：可集成其他 Docker 服务，如运行 macOS 上的开发环境（Xcode、iOS 模拟器）。

## 用法
1. **前提条件**：确保主机为 Linux 系统（推荐 Ubuntu），已安装 Docker 和 Docker Compose。需要 KVM 支持（对于 x86 架构）。
2. **克隆仓库**：
   ```
   git clone https://github.com/dockur/macos.git
   cd macos
   ```
3. **配置**：编辑 `docker-compose.yml` 文件，设置 macOS 版本（如 `macos-13` 为 Ventura）和资源参数（e.g., `cpus: 4`, `memory: 8G`）。
4. **启动安装**：
   ```
   docker compose up -d
   ```
   首次运行会自动下载 macOS 镜像（需数小时，视网络而定）。通过 VNC 客户端（如 `vncviewer localhost:5900`）连接图形界面，完成 macOS 安装向导。
5. **日常使用**：启动容器后，使用 VNC 或 RDP 访问 macOS 桌面。停止容器：`docker compose down`。
6. **高级用法**：参考仓库的 `README.md` 文档自定义脚本、添加共享卷或集成其他服务。注意：项目仅限教育/测试用途，遵守 Apple 许可协议。