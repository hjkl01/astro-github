---
title: stf
---

# STF 项目描述

## 项目地址
[https://github.com/DeviceFarmer/stf](https://github.com/DeviceFarmer/stf)

## 主要特性
STF（Smartphone Test Farm）是一个开源的Android设备农场工具，主要用于管理和远程访问Android设备。它支持多设备并行管理、实时屏幕镜像和交互，适用于测试、调试和自动化场景。核心特性包括：
- **设备农场管理**：集中管理多个Android设备，支持Web界面监控设备状态。
- **远程访问**：通过浏览器实时查看和控制设备屏幕，支持触摸、输入和文件传输。
- **自动化支持**：集成ADB（Android Debug Bridge），便于脚本自动化测试。
- **可扩展性**：支持Docker部署，易于扩展到云环境或本地集群。
- **开源免费**：基于Node.js和WebSocket构建，社区活跃。

## 主要功能
- **设备监控**：实时显示连接设备的电池、CPU、内存等信息。
- **屏幕镜像与控制**：使用WebRTC技术实现低延迟的远程屏幕共享和输入模拟。
- **会话管理**：支持多用户会话，权限控制和会话记录。
- **插件集成**：可扩展插件用于日志捕获、截屏和APK安装。
- **跨平台支持**：服务器端支持Linux/macOS/Windows，客户端通过浏览器访问。

## 用法
1. **安装依赖**：确保安装Node.js（v8+）、ADB和Android SDK。克隆仓库：`git clone https://github.com/DeviceFarmer/stf.git`。
2. **启动服务器**：进入项目目录，运行`npm install`，然后`./bin/stf local`启动本地模式（需启用设备USB调试）。
3. **部署生产环境**：使用Docker：`docker-compose up`（需配置docker-compose.yml）。访问Web界面：http://localhost:7100。
4. **连接设备**：通过ADB连接Android设备，STF会自动检测并列出可用设备。
5. **远程使用**：在浏览器中选择设备，启动会话进行屏幕查看和操作。支持API调用如`/api/v1/devices`获取设备列表。
6. **高级用法**：配置rethinkdb数据库持久化数据；集成Jenkins用于CI/CD测试流程。详细文档见项目README。