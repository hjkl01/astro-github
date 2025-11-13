---
title: moonlight-qt
---

# Moonlight-Qt 项目

## 项目地址
[GitHub 项目地址](https://github.com/moonlight-stream/moonlight-qt)

## 主要特性
Moonlight-Qt 是一个开源的游戏流媒体客户端，基于 NVIDIA GameStream 协议实现。它允许用户从 PC 上流式传输游戏到其他设备，如手机、平板或低功耗设备。主要特性包括：
- **低延迟流传输**：支持高帧率（高达 120 FPS）和低延迟的游戏流媒体。
- **多平台支持**：兼容 Windows、macOS、Linux、Android 和 iOS 等操作系统。
- **高质量视频**：支持 H.264 和 HEVC (H.265) 编码，提供 4K 分辨率和 HDR 内容。
- **音频支持**：包括立体声、多声道音频和麦克风回声消除。
- **输入设备兼容**：支持游戏手柄、键盘和触摸屏输入。
- **自定义设置**：可调整比特率、分辨率、帧率和网络优化选项。
- **开源免费**：完全开源，社区驱动开发，无需额外费用。

## 主要功能
- **游戏流传输**：从主机 PC（运行 NVIDIA GeForce Experience）实时流式传输游戏到客户端设备。
- **远程控制**：通过客户端设备控制主机上的游戏，支持虚拟手柄和键盘映射。
- **多显示器支持**：在主机上选择特定显示器进行流传输。
- **网络优化**：内置 UDP 传输和错误校正机制，适用于家庭网络或远程连接（需端口转发）。
- **应用扩展**：不仅限于游戏，还可流传输桌面或特定应用程序。
- **安全连接**：使用 PIN 码认证和加密传输，确保数据安全。

## 用法
1. **安装主机端**：
   - 在主机 PC 上安装 NVIDIA GeForce Experience（需 NVIDIA GPU 支持）。
   - 启用 GameStream 功能：在 GeForce Experience 设置中添加游戏并开启流媒体。

2. **安装客户端**：
   - 从 GitHub Releases 下载适用于你的平台的 Moonlight-Qt 二进制文件或源代码。
   - 对于源代码编译：使用 Qt Creator 或 CMake 构建项目（依赖 Qt 5/6 和其他库）。

3. **设置连接**：
   - 启动 Moonlight-Qt 客户端。
   - 添加主机：输入主机 PC 的 IP 地址和 PIN 码（从 GeForce Experience 获取）。
   - 配对设备：首次连接时输入 PIN 完成认证。

4. **开始流传输**：
   - 在客户端选择游戏或桌面。
   - 调整设置（如分辨率 1080p、比特率 10 Mbps、60 FPS）。
   - 点击“流式传输”开始游戏。使用连接的控制器或键盘输入控制游戏。

5. **高级用法**：
   - 对于远程访问，配置路由器端口转发（UDP 47998-48010）。
   - 使用 Sunshine（开源 GameStream 服务器）替代 GeForce Experience，支持 AMD/Intel GPU。
   - 社区插件可扩展功能，如自定义输入映射。

更多详情请参考 GitHub 仓库的 README 和 Wiki。