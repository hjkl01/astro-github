
---
title: jitsi-meet
---

# Jitsi Meet 项目

## 项目地址
[https://github.com/jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet)

## 主要特性
Jitsi Meet 是一个开源的视频会议解决方案，具有以下核心特性：
- **端到端加密**：支持 E2EE，确保会议通信安全。
- **无限制参与者**：支持无限数量的参与者加入会议，无需付费。
- **屏幕共享**：允许用户实时共享屏幕内容，便于演示和协作。
- **实时聊天**：内置文本聊天功能，支持表情符号和文件共享。
- **录制与直播**：可录制会议或通过 YouTube 等平台直播。
- **移动端支持**：兼容 Web、iOS 和 Android 设备，提供原生应用。
- **集成性强**：易于集成到其他应用中，支持 API 和 SDK。
- **自托管**：完全开源，可部署在自己的服务器上，避免第三方依赖。
- **多语言支持**：界面支持多种语言，包括中文。
- **高性能**：基于 WebRTC 技术，提供低延迟、高质量的视频和音频传输。

## 主要功能
- **视频会议**：创建或加入视频会议，支持高清视频和音频。
- **白板协作**：内置白板工具，用于实时绘图和标注。
- **会议管理**：支持密码保护、等待室和主持人控制。
- **插件扩展**：可添加自定义插件，如字幕、虚拟背景等。
- **API 接口**：提供 RESTful API 用于自动化会议管理和集成。
- **安全性**：支持 JWT 认证和角色-based 访问控制。

## 用法
1. **快速启动**：
   - 访问 [meet.jit.si](https://meet.jit.si)，输入会议名称即可创建或加入会议。
   - 无需注册，直接使用浏览器（推荐 Chrome 或 Firefox）。

2. **自托管部署**：
   - 克隆仓库：`git clone https://github.com/jitsi/jitsi-meet.git`。
   - 安装依赖：使用 Docker 或手动配置 Prosody、Jicofo 和 JVB（Jitsi Videobridge）。
   - 配置域名和 SSL 证书，然后启动服务。
   - 详细部署指南见仓库的 `doc/` 目录或官方文档。

3. **集成到应用**：
   - 使用 iframe 嵌入：`<iframe src="https://your-domain.com/room-name" allow="camera; microphone"></iframe>`。
   - 通过 JavaScript API 控制会议，如启动/停止录制或管理参与者。
   - 对于移动端，使用 Jitsi Meet SDK 集成到原生应用。

4. **高级用法**：
   - 配置自定义 UI：修改 React 组件以适应品牌需求。
   - 启用 E2EE：在设置中激活端到端加密模式。
   - 监控与扩展：使用 Jigasi 集成 SIP 或其他桥接功能。

更多细节请参考 GitHub 仓库的 README 和文档。