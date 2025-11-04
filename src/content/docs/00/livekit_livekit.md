
---
title: livekit
---

# LiveKit

> 项目地址: <https://github.com/livekit/livekit>

## 项目简介

LiveKit 是一套开源的实时音视频通讯框架，基于 WebRTC 构建，支持 1:n / n:n 场景，适用于 Web、iOS、Android、桌面以及服务器端应用。它提供低延迟、可扩展、可自托管的视频会议、直播、AR/VR 以及远程协作的完整生态。

## 主要特性

| 特性 | 说明 |
|------|------|
| **低延迟高性能** | 采用分布式架构，0.3~0.5s 之间的时延，支持高并发（10k+ 并发通话）。 |
| **多方实时通信** | 支持 1:n、n:n 场景，可自动做转发、路由，支持多路复用、Simulcast、SVC 等。 |
| **多平台 SDK** | 提供 Web (`JavaScript`), iOS (`Swift`), Android (`Java/Kotlin`), Flutter, Unity, Typescript, Go, Python, Rust 等多语言 SDK。 |
| **录制 & 录制转码** | 支持会话录制、录制转码，可将音视频流保存为 MP4、HLS、DASH。 |
| **白板 & 共享屏幕** | 内置白板、屏幕共享、共享摄像头/麦克风，支持协同编辑。 |
| **混音 & 声音处理** | 支持混响、噪声抑制、回声消除、增益控制等音频处理功能。 |
| **弹性伸缩** | 可通过 Kubernetes、Docker Swarm 等编排自动扩容，支持全栈扩容（RTC、SFU、Redis、PostgreSQL 等）。 |
| **安全与合规** | 端到端加密传输、JWT 认证、意外断开重连、信令加密。 |
| **插件化扩展** | 自定义插件可实现云端录制、转码、AI字幕等业务。 |
| **易部署** | 提供 Docker Compose、Helm chart、Kubernetes YAML，亦可直接构建源码部署。 |

## 核心功能

- **Signal Server**：信令服务器负责房间、通道、用户管理，基于 WebSocket 实现低延迟交互。
- **SFU (Selective Forwarding Unit)**：转发媒体流，压缩负载，支持多路复用。
- **Recording (RecordServer)**：实时录制会议，支持 HLS、DASH 等拆分格式，提供 API 可实时获取录制进度。
- **WorkingSpark Host**：可在几秒内创建一个音视频房间，支持 WebRTC 随机匹配、双向通讯等。
- **Dashboard**：提供可视化监控与管理面板，查看房间状态、参与者、流量等。

## 用法指南

### 1. 安装与启动

```bash
# Docker 启动（推荐）
docker run -d \
  -e LIVEKIT_TOKEN_SECRET="super-secret" \
  -e LIVEKIT_DATABASE_URL="postgresql://username:password@localhost:5432/livekit" \
  -p 7880:7880 \
  livekit/livekit:latest

# 或者使用 docker compose
docker-compose up -d
```

### 2. 创建房间

```javascript
import { connect, Room } from 'livekit-client';

(async () => {
  const room = new Room();
  await room.connect(
    'https://demo.livekit.io',
    'YOUR_ACCESS_TOKEN',
    { name: 'my-room' } // 允许同事加入
  );
})();
```

### 3. 添加媒体轨道

```javascript
const mediaStream = await navigator.mediaDevices.getUserMedia({
  audio: true,
  video: { width: 1280, height: 720 }
});
mediaStream.getTracks().forEach(track => room.localParticipant.publishTrack(track));
```

### 4. 监听远程流

```javascript
room.on('participantConnected', participant => {
  participant.videoTracks.forEach(publication => {
    if (publication.track?.isSubscribed) {
      document.body.appendChild(publication.track.attach());
    }
  });
});
```

### 5. 录制与回放

```bash
# 录制
curl -X POST "http://localhost:7880/api/v1/recording" \
 -H "Authorization: Bearer YOUR_TOKEN" \
 -H "Content-Type: application/json" \
 -d '{"roomName":"my-room","targets":["my-room"]}'

# 回放 (HLS)
http://localhost:7880/video/my-room.mp4
```

### 6. 自定义插件

```go
// example_plugin.go
package main

import (
  "github.com/livekit/livekit-server/pkg/recording"
  "github.com/livekit/livekit-server/pkg/plugins"
)

type MyRecorder struct{}
func (*MyRecorder) RecordSession(ctx context.Context, recorder *recording.Session) error {
  // 自定义录制逻辑
  return nil
}

func main() {
  plugins.Register(MyRecorder{})
}
```

## 开发与贡献

- Fork → 克隆 → `make build`（需要 Go、Docker）  
- 编写单元测试：`make test`  
- PR 时请遵循 [Contributing.md](https://github.com/livekit/livekit/blob/main/CONTRIBUTING.md)

### 常见问题

- **鉴权失败**：确保 `LIVEKIT_TOKEN_SECRET` 与访问令牌对应，或使用 `livekit_token` CLI。  
- **多房间同步**：使用 `room=roomName` 参数在同一服务器上避免调度冲突。  
- **网络不稳定**：可开启 [WebRTC ICE/TURN]，或使用 TURN 服务器进行穿透。

## 参考文档

- 官方文档: <https://docs.livekit.io>  
- API 参考: <https://github.com/livekit/livekit-client>  
- 示例代码: <https://github.com/livekit/examples>  

> 更多详细信息请访问项目仓库中的 `docs/`，或查看 `README.md` 与 `CHANGELOG.md`。

---