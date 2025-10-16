
---
title: redroid-doc
---

# Redroid 项目文档

## 项目地址
[GitHub 项目地址](https://github.com/remote-android/redroid-doc)

## 主要特性
Redroid 是一个开源的 Android 云端模拟器项目，支持在服务器上运行多个 Android 实例，并通过 WebRTC 等技术实现远程访问。主要特性包括：
- **容器化部署**：基于 Docker 容器运行 Android 系统，支持 ARM 和 x86 架构。
- **多实例管理**：可以同时运行多个 Android 实例，每个实例独立隔离。
- **远程访问**：通过 Web 界面或 API 实现远程控制，支持屏幕镜像、输入操作（如触摸、键盘）。
- **高性能**：利用 WebRTC 提供低延迟的实时流媒体传输，适用于游戏、测试等场景。
- **开源与可扩展**：提供详细的文档和 API，支持自定义 Android 镜像和插件扩展。
- **跨平台支持**：服务器端支持 Linux 环境，客户端可在浏览器中访问，无需安装额外软件。

## 主要功能
- **Android 实例启动与管理**：创建、启动、停止和管理多个 Android 虚拟设备（AVD）。
- **远程控制**：支持触摸屏输入、键盘输入、摄像头和麦克风访问，实现完整的远程操作。
- **屏幕录制与截图**：实时捕获屏幕，支持录制视频或截取图片。
- **API 接口**：提供 RESTful API 用于自动化脚本集成，适用于 CI/CD 测试或批量管理。
- **WebRTC 流传输**：使用 WebRTC 协议实现 P2P 或服务器中转的视频流，低延迟且安全。
- **自定义配置**：支持修改 Android 系统配置、安装 APK、调试模式等。

## 用法
### 1. 环境准备
- 安装 Docker 和 Docker Compose（服务器端）。
- 确保服务器有足够的 CPU、内存和 GPU（可选，用于加速）。
- 下载 Redroid 镜像：从 GitHub Releases 获取最新的 Docker 镜像。

### 2. 快速启动
- 克隆仓库：`git clone https://github.com/remote-android/redroid-doc.git`
- 进入目录：`cd redroid-doc`
- 配置 `docker-compose.yml` 文件，设置端口、Android 版本等参数。
- 启动服务：`docker-compose up -d`
- 访问 Web 界面：打开浏览器，输入 `http://your-server-ip:8080`（默认端口）。

### 3. 创建和管理实例
- 在 Web 界面点击“创建实例”，选择 Android 版本和分辨率。
- 实例启动后，通过 WebRTC 连接远程访问，支持拖拽、点击等操作。
- 使用 API 示例（需启用 API 端口）：
  - 创建实例：`POST /api/instances` with JSON body `{ "image": "redroid/redroid:11.0.0-latest" }`
  - 连接实例：`GET /api/instances/{id}/connect` 返回 WebRTC 配置。

### 4. 高级用法
- **自定义镜像**：构建自己的 Android 镜像，添加预装应用或修改系统设置。
- **集成测试**：结合 Appium 或 ADB 工具进行自动化测试。
- **安全配置**：启用 HTTPS 和认证，限制访问 IP。
- 详细文档请参考项目仓库中的 README 和 docs 目录。

更多细节请查看项目仓库的官方文档。