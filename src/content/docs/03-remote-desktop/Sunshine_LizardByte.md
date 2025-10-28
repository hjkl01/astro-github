
---
title: Sunshine
---

# Sunshine 项目

**GitHub 项目地址:** [https://github.com/LizardByte/Sunshine](https://github.com/LizardByte/Sunshine/blob/master/docs/getting_started.md)

## 主要特性
Sunshine 是一个开源的自托管游戏流媒体服务器，专为 Moonlight 等客户端设计。它允许用户将 PC 上的游戏或桌面内容流式传输到其他设备上，支持低延迟、高质量的远程游戏体验。主要特性包括：
- **开源免费**：基于 GPLv3 许可，完全开源，用户可以自由修改和分发。
- **跨平台支持**：兼容 Windows、Linux 和 macOS 等操作系统。
- **高性能编码**：集成 NVIDIA NVENC、AMD AMF 和 Intel Quick Sync 等硬件加速编码，支持 H.264 和 HEVC (H.265) 视频编码，提供高质量视频流。
- **低延迟传输**：优化网络协议，支持 UDP 和 TCP，确保游戏流媒体的实时性。
- **多设备兼容**：与 Moonlight 客户端无缝集成，支持 Android、iOS、Raspberry Pi 等设备作为接收端。
- **自定义配置**：支持 JSON 配置文件调整分辨率、比特率、帧率等参数。
- **安全性**：内置 HTTPS 支持和证书管理，保护流媒体传输安全。
- **扩展性**：可作为 NVIDIA GameStream 的开源替代品，支持虚拟显示和多显示器配置。

## 主要功能
- **游戏流媒体**：将 PC 游戏实时传输到远程设备，支持键盘、鼠标、游戏手柄输入。
- **桌面镜像**：不仅仅限于游戏，还可流式传输整个桌面或特定应用程序。
- **硬件加速**：利用 GPU 进行视频编码，减少 CPU 负载，提高性能。
- **网络优化**：自动调整比特率以适应网络条件，支持局域网和广域网传输。
- **输入映射**：客户端输入（如触摸屏或控制器）映射到主机端，实现远程控制。
- **日志和调试**：提供详细日志记录，便于故障排除和性能优化。

## 用法
1. **安装**：
   - 从 GitHub Releases 下载适用于您操作系统的预编译二进制文件，或从源代码构建。
   - Windows：运行安装程序，启用 Sunshine 服务。
   - Linux：使用包管理器安装依赖（如 NVIDIA 驱动），然后运行可执行文件。
   - macOS：通过 Homebrew 或手动编译安装。

2. **配置**：
   - 首次运行时，Sunshine 会生成配置文件（通常在 `~/.config/sunshine/sunshine.conf` 或 Windows 的 `%APPDATA%\Sunshine`）。
   - 编辑配置文件设置用户名、密码、端口（默认 47989）、视频分辨率等。
   - 对于 NVIDIA/AMD GPU，确保驱动已安装并启用硬件编码。

3. **运行服务器**：
   - 启动 Sunshine（命令行：`sunshine` 或通过服务管理器）。
   - 访问 Web UI（通常 `https://localhost:47990`）进行图形化配置和应用授权。

4. **客户端连接**：
   - 在接收设备上安装 Moonlight 客户端。
   - 添加主机 IP，输入 Sunshine 配置的凭据。
   - 选择游戏或桌面开始流媒体会话。

5. **高级用法**：
   - 使用 Docker 部署：拉取官方镜像并映射端口。
   - 自定义输入：通过配置文件映射控制器。
   - 故障排除：检查防火墙设置，确保端口开放；查看日志文件诊断问题。

更多细节请参考官方文档：[Getting Started](https://github.com/LizardByte/Sunshine/blob/master/docs/getting_started.md)。