
---
title: go2rtc
---


# go2rtc (AlexxIT)

> **项目地址**: https://github.com/AlexxIT/go2rtc

## 项目简介  
go2rtc 是一款用 Go 编写的轻量级 WebRTC 流媒体服务器。它支持将多种流媒体协议（RTSP、RTMP、HTTP、SRT 等）转换为 WebRTC，也可将 WebRTC 流转发为 HLS/MPEG‑DASH、RTSP/RTMP 等协议，实现一次部署多协议互通。项目目标是“**让所有摄像头、流媒体协议无缝互通**”，并提供 Docker 镜像、CLI 与 HTTP API 等多种使用方式。

---

## 主要特性

| 序号 | 特性 | 说明 |
|------|------|------|
| 1 | **多协议互通** | RTSP / RTMP / HTTP SRT / RTSP-RTMP 等协议皆可作为输入，输出为 WebRTC、HLS、MPEG‑DASH、RTSP、RTMP 等。 |
| 2 | **WebRTC 接入** | 支持多轨音视频、SDP、ICE、DTLS、SRTP、SIMULCAST 等，兼容 Chrome / Firefox / Safari / Edge，并可通过浏览器直接预览。 |
| 3 | **Docker 官方镜像** | `ghcr.io/alexxit/go2rtc:latest`（或 `docker pull alexxit/go2rtc`）。为一键部署提供便利。 |
| 4 | **HTTP API 与 Web UI** | `/api/...` 接口可查询、配置摄像头；Web UI 通过 WebRTC 观看、控制摄像头。 |
| 5 | **多路流合并与分流** | 可将多个 RTSP 画面合并为多路 WebRTC，或单一路 RTSP 切分成多个 WebRTC 流。 |
| 6 | **自动重连与 RTSP 预热** | 对失效连接自动重连；支持 RTSP 预热以降低延迟。 |
| 7 | **视频录制与转码** | 直接录制为文件，或使用 FFmpeg 进行码，支持多种编解码器（H.264, H.265, VP8, VP9 等）。 |
| 8 | **安全与鉴权** | 支持 Basic Auth、JWT、CAPTCHA、模拟 HTTPS、密钥加密等多种鉴权方式。 |
| 9 | **插件化路由** | 支持自定义 `rtspproxy`, `httprecv`, `rtc`, `relay`, `record`, `auth`, `cors`, `rewrite` 等插件。 |
| 10 | **跨平台** | 可直接在 Linux、macOS、Windows 上编译运行。 |

---

## 如何安装

### 1. 使用 Docker 部署（推荐）

```bash
docker run -d \
  --name go2rtc \
  -p 1984:1984 -p 8080:8080 -p 8554:8554 -p 8765:8765 \
  -v /path/to/config.yaml:/etc/go2rtc/config.yaml \
  ghcr.io/alexxit/go2rtc:latest
```

> *默认监听：*
> - 1984 作为 WebRTC 接口（`rtc://`）  
> - 8080 作为 HTTP API / Web UI  
> - 8554 作为 RTSP/RTMP 监听  
> - 8765 作为插件 WebSocket 端口

### 2. 本地编译

```bash
go install github.com/AlexxIT/go2rtc/v2@latest
go2rtc -config /path/to/config.yaml
```

---

## 核心配置示例（`config.yaml`）

```yaml
# ================== 全局通用 ==================
stream:
  rtsp:                # RTSP 摄像头列表
    rtsp://10.0.0.10:554/axis-cgi/mjpg/video.cgi?resolution=640p:rtsp://10.0.0.10:554/axis-cgi/mjpg/video.cgi?resolution=640p
  rtmp:                # RTMP 推流列表
    rtmp://myserver:1935/app/stream:rtmp://myserver:1935/app/stream

# =================  WebRTC 入口 =================
rtc:
  run: true
  bind-ts: localhost:1984
  bind-us: localhost:1984

# ===================== HTTP API ==================
http:
  bind: localhost:8080
  auth:  # 简单的 Basic Auth
    basic: alice:passwd
  cors:  "*"

# ===================== PLUGINS ===================
plugin:
  record:
    run: true
    path: "/var/records/{{ .Beacon.uuid }}/{{ .Now '20060102150405' }}.mp4"

# ====================== 其他 =====================
log: stdout
```

> **说明**  
> - `{{ .Beacon.uuid }}` 会被替换为流唯一标识。  
> - `{{ .Now '20060102150405' }}` 生成文件名的时间戳。  
> - 通过 `bind` 设定监听地址；`auth` 可设定 Basic 或 JWT。  

---

## 常用命令行参数

```bash
go2rtc -h
```

- `-config`      指定配置文件路径（默认 `/etc/go2rtc/config.yaml`）  
- `-debug`       打印调试日志  
- `-http`        指定 HTTP 服务地址（如果想快速测试）  
- `-rtc`         指定 WebRTC 接口地址  
- `-no-ui`       禁用 Web UI（只保留 API）  

---

## 使用示例

### 1. 通过浏览器观看

打开 `http://<host>:8080`，使用 Web UI 登录。  
或直接打开 WebRTC 地址： `rtc://<host>:1984/<stream-id>` (可通过命令行 `go2rtc` 自动生成 `rtc://` 连接内容)。

> **提示**：在 Chrome 中可通过 DevTools 中的「Network」选项卡查看 SDP 与 RTCPeerConnection 详细过程。

### 2. 观看 RTSP/RTMP 推流（HLS/MPEG-DASH）

```bash
curl http://<host>:8080/api/hls/<stream-id>   # HLS M3U8
curl http://<host>:8080/api/dash/<stream-id>  # MPEG‑DASH MPD
```

随后将得到的 URL 直接放到 VLC/ffmpeg/浏览器中。

### 3. 观看 RTSP 摄像头

```bash
rtsp://<host>:8554/<stream-id>
```

### 4. 通过 FFmpeg 推流

```bash
ffmpeg -i input.mp4 -vcodec libx264 -f rtsp rtsp://<host>:8554/stream
```

---

## 进阶使用

### ① 通过自定义插件过滤 RTSP 篇

在 `config.yaml`：

```yaml
plugin:
  filter:
    run: true
    option:
      regex: ".*\\.jpg$"   # 只获取 jpg
```

> **更多插件**：[`relay`, `auth`, `cors`, `auto`, etc.`](https://github.com/AlexxIT/go2rtc/wiki/Plugins)

### ② 将 3 路 RTSP 合并为 1 路 WebRTC

```yaml
stream:
  udp: rtsp://cam1:554;rtsp://cam2:554;rtsp://cam3:554
```

此配置将 3 条 RTSP 源按时间同步合成 1 路 WebRTC。

### ③ 安全配置（加密 HTTPS）

```bash
go2rtc -config config.yaml -https 0.0.0.0:8443 \
       -cert /path/tls.pem -key /path/tls.key
```

> HTTPS 只用于 API/Web UI，WebRTC（`rtc://`）仍为清晰地址。

---

## 文档与社区

- 官方 README: https://github.com/AlexxIT/go2rtc  
- Wiki / API 参考: https://github.com/AlexxIT/go2rtc/wiki  
- Docker Hub / GHCR: https://github.com/AlexxIT/go2rtc/pkgs/container/go2rtc  
- 讨论群 / Issues: 在 GitHub Issues 或 Discord `#go2rtc` 频道。

--- 

> *环境要求：Go 1.20+；Docker 20+；或将 `go2rtc` 直接运行在任意支持 x86_64 / arm64 的系统。*

```



```
// 文件路径: src/content/docs/00/go2rtc_AlexxIT.md
