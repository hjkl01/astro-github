---
title: wechat-selkies
---

# WeChat Selkies 项目简介

## 项目描述

WeChat Selkies 是一个基于 Docker 的微信/QQ Linux 客户端项目，利用 Selkies WebRTC 技术实现浏览器直接访问，无需本地安装客户端。适用于服务器部署、远程办公等场景。

## 主要功能特性

- 🌐 **浏览器访问**：通过 Web 浏览器直接使用微信，无需本地安装
- 🐳 **Docker化部署**：简单的容器化部署，环境隔离
- 🔒 **数据持久化**：支持配置和聊天记录持久化存储
- 🎨 **中文支持**：完整的中文字体和本地化支持，支持本地中文输入法
- 🖼️ **图片复制**：支持通过侧边栏面板开启图片复制
- 📁 **文件传输**：支持通过侧边栏面板进行文件传输
- 🖥️ **多架构支持**：兼容 AMD64 和 ARM64 架构
- 🔧 **硬件加速**：可选的 GPU 硬件加速支持
- 🪟 **窗口切换器**：左上角增加切换悬浮窗，方便切换到后台窗口
- 🤖 **自动启动**：可配置自动启动微信和 QQ 客户端

## 使用方法

### 环境要求

- Docker
- Docker Compose
- 支持 WebRTC 的现代浏览器（Chrome、Firefox、Safari 等）

### 快速部署

1. 使用 Docker 命令直接运行：
   ```bash
   docker run -it -p 3001:3001 -v ./config:/config --device /dev/dri:/dev/dri nickrunning/wechat-selkies:latest
   ```
2. 或使用 Docker Compose：
   创建 `docker-compose.yml` 文件并运行 `docker-compose up -d`
3. 在浏览器中访问 `https://localhost:3001` 或 `https://<服务器IP>:3001`

更多配置详情请参考项目 README。
