
---
title: chanify
---

# Chanify 项目

**GitHub 项目地址:** [https://github.com/chanify/chanify](https://github.com/chanify/chanify/blob/main/README-zh_CN.md)

## 主要特性

Chanify 是一个简单、安全的通信工具，旨在帮助用户快速、安全地发送消息和文件。它支持跨平台使用，包括 iOS、Android、macOS、Windows 和 Linux 等系统。主要特性包括：

- **端到端加密**：所有消息传输均采用端到端加密，确保数据隐私和安全。
- **跨平台支持**：提供移动端（iOS 和 Android）和桌面端（macOS、Windows、Linux）应用，以及 Web 版本，便于多设备同步。
- **推送通知**：支持实时推送消息通知，类似于短信或即时消息。
- **文件附件**：允许发送图片、文件等附件，支持预览和下载。
- **自定义服务器**：用户可以自建服务器，实现私有化部署，避免依赖第三方服务。
- **简单易用**：无需注册账号，通过设备 ID 或二维码快速连接设备。
- **开源免费**：基于 MIT 许可，完全开源，用户可自由修改和贡献。

## 主要功能

- **消息发送与接收**：用户可以通过 Chanify 发送文本消息、位置信息或文件，并实时接收来自其他设备的消息。
- **设备管理**：支持添加和管理多个设备，实现消息在设备间的同步。
- **服务器部署**：提供 Docker、Go 等方式快速部署服务器，支持 HTTPS 和自定义域名。
- **API 接口**：内置 RESTful API，允许开发者集成到其他应用中发送消息。
- **离线消息**：服务器可存储离线消息，当设备上线时自动推送。
- **插件扩展**：支持 Webhook 和脚本插件，扩展功能如集成其他服务。

## 用法

### 1. 安装客户端
- **iOS**：从 App Store 下载 Chanify App。
- **Android**：从 Google Play 或 GitHub Releases 下载 APK。
- **桌面端**：从 GitHub Releases 下载对应平台的安装包（如 .dmg、.exe 或 .deb）。
- **Web 版**：通过浏览器访问自建服务器的 Web 界面。

### 2. 连接设备
- 打开 App，扫描二维码或输入设备 ID 连接到服务器。
- 对于自建服务器，先部署服务器（详见下文），然后在 App 中输入服务器地址。

### 3. 发送消息
- 在 App 中选择联系人或设备，输入文本、添加附件或位置，然后发送。
- 通过 API 发送：使用 curl 或其他工具调用服务器 API，例如：
  ```
  curl -X POST "https://your-server.com/v1/message" \
  -H "Content-Type: application/json" \
  -d '{"device_token": "your_token", "title": "标题", "content": "消息内容"}'
  ```

### 4. 部署服务器
- **使用 Docker**（推荐）：
  ```
  docker run -d -p 8000:8000 -v /path/to/data:/data chanify/chanify
  ```
- **直接运行 Go 二进制**：下载二进制文件，配置 `chanify.conf`，然后执行 `./chanify server`。
- 访问 `http://your-server:8000` 配置 HTTPS 和域名。
- 详细部署指南见项目 README。

Chanify 适用于个人隐私通信、企业内部通知或自动化脚本，操作简单且高效。