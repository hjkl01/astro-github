---
title: jellyfin
---

# Jellyfin 项目

## 项目地址
[https://github.com/jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)

## 主要特性
Jellyfin 是一个开源的媒体服务器软件，旨在为用户提供免费、无需订阅的媒体管理和流媒体解决方案。它基于 .NET Core 构建，支持跨平台运行，包括 Windows、Linux、macOS 和 Docker 等环境。主要特性包括：
- **开源免费**：完全开源，无需付费订阅或云服务依赖。
- **多媒体支持**：支持视频、音频、照片和书籍等多种媒体类型，包括 4K、HDR 和 Dolby Vision 等高品质格式。
- **用户友好界面**：提供现代化的 Web 界面、移动 App 和智能电视支持，便于管理和播放。
- **隐私保护**：所有数据存储在本地服务器上，不上传到第三方云端，确保用户隐私。
- **插件扩展**：支持丰富的插件系统，可扩展功能如字幕下载、元数据抓取和硬件转码。
- **硬件加速**：集成 NVIDIA、Intel Quick Sync 和 AMD 等硬件解码支持，优化流媒体性能。
- **多用户管理**：支持多用户账户、权限控制和家长控制。

## 主要功能
- **媒体库管理**：自动扫描和组织本地媒体文件，获取元数据、海报和字幕。
- **流媒体播放**：支持直接播放、转码和字幕同步，可通过 DLNA、Chromecast 或内置播放器在各种设备上流式传输。
- **实时转码**：根据客户端设备能力动态转码媒体，避免兼容性问题。
- **远程访问**：通过反向代理或 VPN 实现安全的远程访问。
- **API 和集成**：提供 RESTful API，支持与其他工具如 Home Assistant 或 Kodi 的集成。
- **后台服务**：包括通知、日志记录和备份功能，确保服务器稳定运行。

## 用法
1. **安装**：
   - 下载最新版本的 Jellyfin 从 GitHub Releases 页面，或使用包管理器（如 apt、yum）安装。
   - 对于 Docker 用户：运行 `docker run -d -p 8096:8096 --name jellyfin jellyfin/jellyfin` 命令启动容器。
   - 安装后，访问 `http://your-server-ip:8096` 进行初始设置。

2. **配置**：
   - 在 Web 界面中添加媒体库路径，Jellyfin 会自动扫描文件。
   - 设置用户账户、启用 HTTPS（推荐使用 Let's Encrypt 证书）和配置元数据提供商（如 TMDb、TVDB）。

3. **使用**：
   - 通过 Web 浏览器或官方 App（Android/iOS、Roku、Fire TV 等）登录并浏览媒体库。
   - 播放媒体时，选择字幕和音频轨道；服务器会自动处理转码。
   - 管理插件：在仪表板中搜索并安装扩展，如 Intro Skipper（跳过片头）或 Fanart（增强海报）。

4. **高级用法**：
   - 编辑 `system.xml` 配置硬件加速选项。
   - 使用 Jellyfin CLI 工具进行自动化任务，或通过 API 开发自定义应用。

更多详情请参考官方文档：https://jellyfin.org/docs