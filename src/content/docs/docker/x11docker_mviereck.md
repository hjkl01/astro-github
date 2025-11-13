---
title: x11docker
---

# x11docker 项目

**GitHub 项目地址:** [https://github.com/mviereck/x11docker](https://github.com/mviereck/x11docker)

## 主要特性

x11docker 是一个开源工具，用于在 Linux 系统上运行 Docker 容器，并安全地将 X11 图形界面转发到主机。它强调安全性，避免直接暴露 X 服务器给容器，防止潜在的权限提升攻击。主要特性包括：

- **X11 转发安全**：使用多种隔离方法（如 xpra、Xephyr、Xvfb）来运行 GUI 应用，而不授予容器对主机的直接访问权限。
- **硬件加速支持**：可选支持 GPU 加速、音视频设备和 USB 设备透传。
- **容器隔离**：集成 seccomp、AppArmor 和其他安全机制，确保容器运行环境高度隔离。
- **跨平台兼容**：主要针对 Linux，支持 Wayland 和 X11 环境。
- **轻量级**：无需 root 权限运行，支持各种 Docker 镜像。

## 主要功能

Run GUI applications and desktops in docker and podman containers. Focus on security.

## 用法

请参考项目文档获取详细用法。
