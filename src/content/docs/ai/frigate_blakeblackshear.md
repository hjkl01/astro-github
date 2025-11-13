---
title: frigate
---

# Frigate

## 项目简介

Frigate 是一个完整的本地 NVR（网络视频录像机），专为 [Home Assistant](https://www.home-assistant.io) 设计，具有 AI 对象检测功能。它使用 OpenCV 和 TensorFlow 在本地对 IP 摄像头进行实时对象检测。

## 主要功能

- **与 Home Assistant 的紧密集成**：通过自定义组件实现无缝集成。
- **高效资源管理**：仅在必要时和必要位置进行对象检测，最大化性能并最小化资源使用。
- **多进程架构**：重度使用多进程，强调实时性而非处理每一帧。
- **低开销运动检测**：使用运动检测来确定运行对象检测的位置。
- **独立对象检测进程**：TensorFlow 对象检测在单独进程中运行，以获得最大 FPS。
- **MQTT 通信**：便于集成到其他系统。
- **智能录制**：根据检测到的对象记录视频，并设置保留设置。
- **24/7 录制**：支持全天候录制。
- **RTSP 重新流式传输**：减少摄像头连接数。
- **低延迟实时视图**：支持 WebRTC 和 MSE。

## 推荐硬件

强烈推荐使用 GPU 或 AI 加速器，如 [Google Coral](https://coral.ai/products/) 或 [Hailo](https://hailo.ai/)。AI 加速器即使在最佳 CPU 上也能以极低开销实现卓越性能。

## 用法

1. **安装**：通过 Docker 或其他方式部署 Frigate。
2. **配置**：设置摄像头和检测参数。
3. **集成**：与 Home Assistant 或其他系统通过 MQTT 集成。
4. **监控**：使用内置 Web 界面查看实时流和录制。

详细文档请查看：[https://docs.frigate.video](https://docs.frigate.video)

## 捐赠

如果您想支持开发，请使用 [GitHub Sponsors](https://github.com/sponsors/blakeblackshear)。
