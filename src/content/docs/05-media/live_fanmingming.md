---
title: live
---

# Live 项目

**GitHub 项目地址:** [https://github.com/fanmingming/live](https://github.com/fanmingming/live)

## 主要特性
- **实时视频流支持**: 项目基于 FFmpeg 和 WebRTC 技术，实现低延迟的视频直播传输，支持多种协议如 RTMP、HLS 和 WebRTC。
- **跨平台兼容**: 支持 Windows、Linux 和 macOS 等操作系统，易于部署在服务器环境中。
- **模块化设计**: 包括推流端（publisher）和拉流端（player），便于扩展和自定义。
- **高性能处理**: 优化了视频编码/解码，支持 H.264/H.265 等格式，适用于大规模并发直播场景。
- **开源免费**: 使用 MIT 许可，允许自由修改和商用。

## 主要功能
- **推流功能**: 允许用户从摄像头或文件源推送视频流到服务器，支持实时编码和多路输出。
- **拉流播放**: 通过 Web 界面或 API 拉取直播流，支持浏览器直接播放，无需插件。
- **录制与回放**: 内置录制功能，可保存直播内容为 MP4 文件，并支持点播回放。
- **监控与管理**: 提供简单的 Web 管理面板，用于监控流状态、统计观众数和日志查看。
- **API 接口**: 暴露 RESTful API，便于集成到其他应用中，如移动端或第三方平台。

## 用法
1. **安装依赖**:
   - 克隆仓库: `git clone https://github.com/fanmingming/live.git`
   - 安装 FFmpeg: 根据系统下载并配置环境变量。
   - 运行 `make` 或 `npm install`（如果适用）来构建项目。

2. **配置**:
   - 编辑 `config.json` 文件，设置服务器端口、RTMP 地址和密钥等参数。
   - 示例配置:
     ```
     {
       "rtmp_port": 1935,
       "http_port": 8080,
       "hls_path": "./hls"
     }
     ```

3. **启动服务器**:
   - 在项目根目录运行 `./bin/live` 或 `node server.js`。
   - 服务器启动后，默认监听 RTMP 端口 1935 和 HTTP 端口 8080。

4. **推流**:
   - 使用 OBS Studio 或 FFmpeg 命令推流，例如:
     ```
     ffmpeg -re -i input.mp4 -c:v libx264 -f flv rtmp://localhost/live/stream_key
     ```

5. **拉流播放**:
   - 在浏览器访问 `http://localhost:8080/player.html?stream=live/stream_key`。
   - 或使用 HLS: `http://localhost:8080/hls/stream_key.m3u8`。

6. **高级用法**:
   - 集成 WebRTC: 修改配置启用 WebRTC 模块，实现 P2P 低延迟传输。
   - 部署到云服务器: 使用 Docker 容器化，例如 `docker build -t live .` 和 `docker run -p 1935:1935 -p 8080:8080 live`。

更多细节请参考项目 README 和示例代码。