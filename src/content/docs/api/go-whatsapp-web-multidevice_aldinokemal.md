---
title: go-whatsapp-web-multidevice
---

# go-whatsapp-web-multidevice

## 项目简介

go-whatsapp-web-multidevice 是一个用 Golang 构建的 WhatsApp REST API，提供对 UI、Webhooks 和 MCP（Model Context Protocol）的支持。该项目专注于高效的内存使用，支持多设备登录。

## 主要功能

- **REST API**: 通过 HTTP API 发送 WhatsApp 消息，支持文本、图片、音频、文件、视频、贴纸、联系人、链接、位置等
- **MCP 支持**: 作为 MCP 服务器运行，允许 AI 代理和工具通过标准化协议与 WhatsApp 交互
- **多设备支持**: 支持 WhatsApp 多设备登录
- **Webhook**: 支持接收消息的 webhook 通知
- **自动回复**: 可配置自动回复消息
- **媒体处理**: 自动压缩图片和视频，支持发送贴纸（自动转换为 WebP 格式）
- **群组管理**: 创建群组、管理成员、邀请链接等
- **状态发布**: 支持发布 WhatsApp 状态
- **基本认证**: 支持多用户基本认证
- **子路径部署**: 支持在特定路径下部署

## 安装和使用

### 基本使用

1. 克隆仓库：

   ```bash
   git clone https://github.com/aldinokemal/go-whatsapp-web-multidevice
   cd go-whatsapp-web-multidevice/src
   ```

2. 运行 REST API 模式：

   ```bash
   go run . rest
   ```

3. 打开浏览器访问 `http://localhost:3000`

### Docker 使用

```bash
git clone https://github.com/aldinokemal/go-whatsapp-web-multidevice
cd go-whatsapp-web-multidevice
docker-compose up -d --build
```

### 构建二进制

```bash
cd src
go build -o whatsapp
./whatsapp rest
```

### MCP 模式

```bash
./whatsapp mcp
```

## 配置选项

支持命令行参数和环境变量配置：

- `--port`: 设置端口（默认 3000）
- `--debug`: 启用调试模式
- `--os`: 设置设备名称
- `--basic-auth`: 设置基本认证
- `--webhook`: 设置 webhook URL
- `--autoreply`: 设置自动回复消息

## API 概述

### 主要端点

- `GET /app/login` - QR 码登录
- `POST /send/message` - 发送文本消息
- `POST /send/image` - 发送图片
- `POST /send/file` - 发送文件
- `GET /chats` - 获取聊天列表
- `GET /user/my/contacts` - 获取联系人
- `POST /group` - 创建群组

### MCP 工具

提供丰富的 MCP 工具用于 AI 集成，包括连接管理、消息发送、群组管理等。

## 系统要求

- Go 1.24.0+
- FFmpeg（用于媒体处理）
- 支持 Linux、macOS、Windows（推荐 WSL）

## 注意事项

这是一个非官方项目，与 WhatsApp 无关。请注意使用官方 WhatsApp API 以避免问题。
