---
title: mediamtx
---


# MediaMTX（bluenviron/mediamtx）

> 项目地址：<https://github.com/bluenviron/mediamtx>

## 概述

MediaMTX 是一款轻量级、低延迟的多媒体流服务器，支持 RTMP、RTSP、HLS、SRT、WebRTC 等协议。它以 Go 语言实现，跨平台部署，适合用于直播、录像、转码、转发等场景。

## 主要特性

| 特性 | 说明 |
|------|------|
| **多协议支持** | 同时兼容 RTMP、RTSP(v1/v2)、SRT、HLS、WebRTC、MPEG‑DASH 等。 |
| **低延迟** | 对 RTMP/RTSP 采用流式传输，延迟可低至 200 ms（取决于网络）。 |
| **高性能** | Go 并发模型，CPU 与内存占用低，单实例即可处理数百流。 |
| **转码与转发** | 内置 FFmpeg 自动转码，可实时将流转发至多路输出。 |
| **安全** | 支持 TLS、SRT 证书、IP 白名单、基本身份验证等。 |
| **可配置** | 通过 YAML 或环境变量全方位定制服务器行为。 |
| **监控** | 提供 `/stats` JSON 接口，支持 Grafana、Prometheus。 |
| **插件化** | 可通过 Lua 脚本扩展功能。 |
| **容器友好** | 官方 Docker 镜像，轻松部署在 Kubernetes、Docker Compose 等。 |

## 功能细节

- **推流**：可使用 OBS、ffmpeg、gstreamer 等推送 RTMP/RTSP/SRT。
- **拉流**：支持 HLS（m3u8）和 DASH（mpd）播放，亦可拉取 RTMP/RTSP 作为中继。
- **录制**：自动将流保存为文件，支持按时间或事件切割。
- **转码**：基于 FFmpeg 的转码管线，可实现分辨率、码率、编码器转换。
- **转发**：将一个源流多路推送到不同协议或目标地址。
- **管理**：通过 `/admin` 接口实现动态添加/删除流、修改转码参数等。
- **监控**：`/stats` 输出 JSON，包含连接数、带宽、延迟等指标。

## 快速使用

### 1. 运行 Docker 镜像

```bash
docker run -d \
  -p 8554:8554 -p 1935:1935 -p 8080:8080 \
  -v /data/mediamtx:/data \
  bluenviron/mediamtx
```

- `8554`：RTSP 默认端口  
- `1935`：RTMP 默认端口  
- `8080`：管理/监控接口

### 2. 推流示例（ffmpeg）

```bash
ffmpeg -re -i input.mp4 -c copy -f rtsp rtsp://localhost:8554/stream
```

### 3. 拉取 HLS

```bash
ffplay http://localhost:8080/hls/stream.m3u8
```

### 4. 查看服务器状态

```bash
curl http://localhost:8080/stats
```

## 配置文件示例

```yaml
# mediamtx.yml

# 服务器基本信息
listen:
  rtsp: 8554
  rtmp: 1935
  http:
    addr: 0.0.0.0:8080
    root: /web

# 推流源
sources:
  mylive:
    rtsp:
      auth: none
      path: /mylive
    rtmp:
      path: /mylive

# 转码/录制
transcodes:
  mylive:
    ffmpeg:
      cmd: -i {src} -c:v libx264 -crf 23 -pix_fmt yuv420p -f flv {dst}
    dst: rtsp://localhost:8554/encoded

# 监控
stats:
  enable: true
  endpoint: /stats
```

> 具体配置项详见官方文档。

## 参考链接

- 官方仓库：<https://github.com/bluenviron/mediamtx>
- 文档与示例：<https://bluenviron.github.io/mediamtx/>
- Docker Hub：<https://hub.docker.com/r/bluenviron/mediamtx>
- 社区讨论：<https://github.com/bluenviron/mediamtx/discussions>
