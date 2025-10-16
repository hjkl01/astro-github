
---
title: aiortc
---

# aiortc 项目

## 项目地址
[https://github.com/aiortc/aiortc](https://github.com/aiortc/aiortc)

## 主要特性
aiortc 是一个 Python 库，实现了 WebRTC 协议栈。它基于 asyncio 异步框架，支持实时音视频通信。核心特性包括：
- **WebRTC 协议支持**：完整实现 RTP/RTCP、ICE、DTLS 等 WebRTC 标准协议。
- **异步设计**：利用 Python 的 asyncio 实现非阻塞 I/O，适合高并发场景。
- **媒体处理**：内置支持音频/视频编解码（如 VP8、H.264、Opus），并可集成 FFmpeg 等工具。
- **跨平台兼容**：支持 Linux、macOS 和 Windows，无需浏览器环境。
- **轻量级**：纯 Python 实现，易于扩展和集成到其他应用中。

## 主要功能
- **P2P 通信**：启用设备间直接的点对点音视频传输，减少延迟。
- **信令处理**：支持自定义信令服务器，实现会话建立和媒体协商。
- **媒体流管理**：处理本地/远程媒体轨道，包括捕获、渲染和流传输。
- **NAT 穿越**：通过 STUN/TURN 服务器处理网络地址转换。
- **数据通道**：支持可靠/不可靠的数据通道，用于传输任意数据（如聊天消息）。

## 用法
### 安装
```bash
pip install aiortc
```

### 基本示例：简单视频通话
1. **服务器端（信令）**：使用 aiortc-examples 中的示例设置信令服务器。
2. **客户端代码**（发送端）：
   ```python
   import asyncio
   from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
   from aiortc.contrib.media import MediaPlayer

   pc = RTCPeerConnection()
   player = MediaPlayer("video.mp4")  # 或使用摄像头
   pc.addTrack(player.video)

   # 创建 Offer
   offer = await pc.createOffer()
   await pc.setLocalDescription(offer)

   # 通过信令发送 offer 到远程端
   ```

3. **远程端（接收端）**：
   ```python
   # 接收 offer 并创建 Answer
   await pc.setRemoteDescription(RTCSessionDescription(sdp=offer_sdp, type="offer"))
   answer = await pc.createAnswer()
   await pc.setLocalDescription(answer)

   # 处理事件
   @pc.on("track")
   def on_track(track):
       print(f"Received track: {track.kind}")
   ```

更多用法参考项目中的 `examples` 目录，包括 WebSocket 信令、浏览器集成等。文档详见项目 README 和官方 API 参考。