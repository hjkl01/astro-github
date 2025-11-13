---
title: Spotifyd/spotifyd
---

# Spotifyd

Spotifyd 是一个开源的 Spotify 客户端，以 UNIX 守护进程的形式运行。它可以像官方客户端一样流式播放音乐，但更加轻量级，并支持更多平台。此外，它还支持 Spotify Connect 协议，使其作为设备出现在官方客户端中，可以通过官方客户端进行控制。

**注意：** Spotifyd 需要 Spotify Premium 账户。

## 功能特性

- **轻量级播放**：提供与官方客户端相同的音乐流式播放体验，但资源占用更少。
- **跨平台支持**：支持 Linux、macOS 和 Windows 等多个平台。
- **Spotify Connect 协议**：允许从其他设备（如手机或桌面客户端）控制播放。
- **后台运行**：作为守护进程运行，无需图形界面。

## 用法

1. **安装**：根据你的操作系统，从 [GitHub Releases](https://github.com/Spotifyd/spotifyd/releases) 下载最新版本，或使用包管理器安装（如 `apt`、`brew` 等）。
2. **配置**：创建配置文件，通常位于 `~/.config/spotifyd/spotifyd.conf`，设置用户名、密码或其他选项。
3. **运行**：启动守护进程，例如 `spotifyd --config-path ~/.config/spotifyd/spotifyd.conf`。
4. **控制**：使用 Spotify 官方客户端连接到设备，或通过命令行工具控制。

详细的安装和配置指南请参考 [官方 Wiki](https://spotifyd.github.io/spotifyd/)。
