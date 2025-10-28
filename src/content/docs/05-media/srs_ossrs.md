
---
title: srs
---

# SRS 项目介绍

## 项目地址
[https://github.com/ossrs/srs](https://github.com/ossrs/srs)

## 主要特性
SRS (Simple Realtime Server) 是一个开源的实时多媒体服务器，支持多种流媒体协议和实时传输技术。主要特性包括：
- **高性能**：基于C++开发，支持高并发、低延迟的流媒体处理。
- **多协议支持**：兼容RTMP、HLS、HTTP-FLV、WebRTC、SRT等协议，实现直播推流和拉流。
- **实时能力**：内置WebRTC支持，实现毫秒级延迟的低时延直播。
- **集群与扩展**：支持边缘节点、负载均衡和自动发现，适用于大规模分布式部署。
- **安全性**：集成HTTPS、鉴权和加密机制，确保传输安全。
- **易集成**：提供API和SDK，便于与其他系统（如OBS、FFmpeg）集成。
- **开源免费**：采用MIT许可证，社区活跃，支持商业和个人使用。

## 主要功能
SRS 主要用于实时视频/音频直播和点播场景，核心功能包括：
- **推流与拉流**：支持从推流端（如OBS、FFmpeg）接收RTMP流，并转换为HLS或HTTP-FLV分发给播放端。
- **实时通信**：通过WebRTC实现双向实时音视频传输，适用于视频会议、游戏直播等。
- **转码与录制**：内置转码模块，支持格式转换、画质调整；可自动录制直播流为文件。
- **监控与管理**：提供HTTP API用于流状态监控、统计和配置管理。
- **边缘计算**：支持源站-边缘架构，实现全球CDN-like的低延迟分发。
- **兼容性**：无缝支持移动端、Web端和桌面播放器。

## 用法
SRS 的部署和使用简单，以下是基本步骤（假设在Linux环境下）：

1. **安装依赖**：
   - 安装GCC、Make等构建工具。
   - 示例命令：`sudo apt update && sudo apt install build-essential git libssl-dev`

2. **克隆并编译**：
   ```
   git clone https://github.com/ossrs/srs.git
   cd srs/trunk
   ./configure && make
   ```

3. **配置**：
   - 编辑`conf/full.conf`文件，设置服务器端口、Vhost等参数。
   - 示例配置RTMP推流：`listen 1935;`（默认RTMP端口）。

4. **启动服务器**：
   ```
   ./objs/srs -c conf/full.conf
   ```

5. **推流测试**：
   - 使用FFmpeg推流：`ffmpeg -re -i input.mp4 -c copy -f flv rtmp://your-server:1935/live/stream`
   - 或使用OBS软件配置RTMP URL为`rtmp://your-server/live`，流键为`stream`。

6. **播放测试**：
   - RTMP播放：使用VLC打开`rtmp://your-server/live/stream`。
   - HLS播放：浏览器访问`http://your-server:8080/live/stream.m3u8`。
   - WebRTC：通过SRS提供的WebRTC页面或API集成。

更多高级用法详见项目Wiki和文档，支持Docker一键部署和云环境集成。