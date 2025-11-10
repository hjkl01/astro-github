---
title: Ant-Media-Server
---

# Ant Media Server 项目

## 项目地址
[GitHub 项目地址](https://github.com/ant-media/Ant-Media-Server)

## 主要特性
Ant Media Server 是一个开源的实时视频流媒体服务器，支持 WebRTC、RTMP、HLS 和 DASH 等协议。它以低延迟和高性能著称，适用于实时视频通信、直播和视频会议等场景。主要特性包括：
- **实时低延迟流媒体**：通过 WebRTC 实现亚秒级延迟，支持 P2P 和 SFU（选择性转发单元）模式。
- **多协议支持**：兼容 RTMP（用于推流）、HLS/DASH（用于自适应比特率流）和 WebRTC（用于浏览器实时传输）。
- **集群扩展**：支持水平扩展和负载均衡，可处理数千并发用户。
- **内置录制与转码**：自动录制直播，支持自适应比特率转码和 DVR（数字视频录制）功能。
- **安全性**：集成 SSL/TLS 支持、令牌认证和 IP 过滤。
- **易集成**：提供 REST API 和 SDK，支持与 React、Vue 等前端框架集成。
- **开源与社区**：基于 Java 开发，Apache 2.0 许可，活跃社区支持。

## 主要功能
- **实时视频会议**：支持多方视频通话、屏幕共享和聊天集成。
- **直播推流与拉流**：从 OBS 等工具推流，支持观众通过浏览器观看。
- **自适应流媒体**：根据网络条件自动调整视频质量。
- **数据通道**：WebRTC 数据通道用于传输聊天、文件等非视频数据。
- **监控与分析**：内置仪表盘监控服务器性能、流统计和用户行为。
- **移动端支持**：兼容 iOS 和 Android 设备，通过 WebRTC 实现跨平台。

## 用法
1. **安装**：
   - 下载最新版本的安装包（支持 Ubuntu、CentOS、Windows 等）。
   - 对于 Ubuntu/Debian：运行 `sudo apt install ant-media-server` 或从 GitHub 下载 deb/rpm 包。
   - 启动服务器：`sudo systemctl start ant-media-server`。

2. **配置**：
   - 编辑 `application.properties` 文件设置端口、协议和 API 密钥。
   - 启用 WebRTC：确保端口 5080/5443 开放，并配置防火墙。

3. **使用示例**：
   - **推流直播**：使用 OBS Studio 设置 RTMP URL 为 `rtmp://your-server:1935/live`，流密钥为自定义名称。观众通过浏览器访问 `https://your-server:5443/WebRTCAppEE/websocket` 观看。
   - **WebRTC 应用**：集成 JavaScript SDK，例如：
     ```javascript
     var webRTCAdaptor = new WebRTCAdaptor({
         websocket_url: "wss://your-server:5443/WebRTCAppEE/websocket",
         mediaConstraints: { video: true, audio: true }
     });
     webRTCAdaptor.publish("stream1"); // 发布流
     ```
   - **API 调用**：使用 REST API 创建应用或管理流，例如 POST `/v2/broadcasts/create` 创建直播。
   - **集群部署**：配置 NodeJS 负载均衡器，将多个服务器节点连接到 Redis。

详细文档和示例见 GitHub 仓库的 [Wiki](https://github.com/ant-media/Ant-Media-Server/wiki)。建议在生产环境使用企业版以获得高级支持。