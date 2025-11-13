---
title: docker-jitsi-meet
---

# Docker Jitsi Meet

**项目地址**  
[https://github.com/jitsi/docker-jitsi-meet](https://github.com/jitsi/docker-jitsi-meet)

## 项目概述

Docker Jitsi Meet 是一个基于 Docker Compose 的完整 Jitsi Meet 部署方案。它将 Jitsi Videobridge、Jicofo、Prosody、Jitsi Meet 前端等组件打包成可直接运行的容器，方便快速搭建安全、可扩展的视频会议服务。

## 主要特性

- **一键部署**：只需 `docker-compose up -d` 即可完成所有服务的安装与启动。
- **自定义配置**：通过 `.env` 文件或 `docker-compose.yml` 中的环境变量，轻松调整域名、TLS、音视频参数、授权方式等。
- **HTTPS/Let’s Encrypt**：内置 Let’s Encrypt 自动获取与续期 TLS 证书。
- **多域/多实例**：支持同一机器部署不同域名的多实例。
- **可扩展的网络**：使用 Docker 网络，容器间通信简洁可靠。
- **日志与监控**：所有容器日志统一输出，易于集成监控系统。
- **更新与维护**：提供 `docker-compose pull` 与 `docker-compose up -d` 的方式快速升级镜像。

## 核心功能

Docker 上的 Jitsi Meet

## 用法

请参考项目文档获取详细用法。
