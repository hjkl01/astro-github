
---
title: open-tv
---


# Open TV（Open-TV）

> GitHub 地址: https://github.com/Fredolx/open-tv

## 项目简介
Open TV 是一个轻量级、易于部署的 IPTV/直播流服务器，支持多种流媒体协议（RTMP、HLS、DASH、RTSP），并提供 Web UI 与 REST API，方便用户快速配置频道、观看直播、录制节目。

## 主要特性
- **多协议支持**：RTMP、HLS、DASH、RTSP 等，兼容主流播放器。
- **频道管理**：通过 `config/channels.yaml` 或 Web UI 一键添加/编辑频道地址与元数据。
- **录制与回看**：实时录制，文件按时间分区存储；可通过 Web UI 或 API 进行回看。
- **Docker 一键部署**：提供 `docker-compose.yml`，即可在任何 Docker 环境快速启动。
- **RESTful API**：查询频道列表、获取节目单、控制录制等。
- **Web UI**：直观的界面，支持直播观看、节目单浏览、录制管理。

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/Fredolx/open-tv.git
cd open-tv

# 2. 配置频道
# 编辑 config/channels.yaml，添加频道信息

# 3. 启动
# 方式一：Docker
docker compose up -d

# 方式二：直接运行
go run main.go

# 4. 访问
浏览器访问 http://<服务器IP>:8000 即可观看直播或管理频道
```

## 示例频道配置

```yaml
# config/channels.yaml
- name: "央视新闻"
  url: "rtmp://live.cctv.com/live"
  type: "rtmp"
- name: "BBC"
  url: "http://stream.bbc.co.uk/live"
  type: "hls"
```

## 贡献与支持
- Fork 本仓库并提交 Pull Request。
- 如需功能建议或 bug 报告，请在 GitHub Issues 页面提出。

--- 
