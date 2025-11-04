
---
title: notifuse
---


# Notifuse

**项目地址**  
<https://github.com/Notifuse/notifuse>

## 简介  
Notifuse 是一个轻量级的通知代理，主要用于在 Linux 系统上统一接收和转发来自不同应用的通知。它实现了 `org.freedesktop.Notifications` DBus 接口，并提供命令行工具和 REST API，方便开发者在自己的程序中发送通知。

## 主要特性  
- **DBus 接口**：兼容 `org.freedesktop.Notifications`，可直接替代系统默认的通知服务。  
- **命令行发送**：`notifuse send` 可从终端直接发送通知，支持标题、正文、图标、超时等参数。  
- **REST API**：提供 `/notify` 接口，支持 HTTP POST 方式发送通知，便于与其他语言或服务集成。  
- **自定义图标与动作**：支持在通知中嵌入自定义图标、音效以及可执行的操作按钮。  
- **配置文件**：支持通过 `config.yaml` 或环境变量自定义默认超时、日志级别等。  
- **跨语言**：提供 Go SDK，方便在 Go 项目中直接调用。  

## 功能列表  
| 功能 | 描述 |
|------|------|
| 接收 DBus 通知 | 监听系统 DBus，捕获所有通知消息。 |
| 转发通知 | 将接收到的通知转发给客户端或通过 REST API 发送。 |
| 命令行工具 | `notifuse send` 用于手动触发通知。 |
| REST API | `POST /notify` 接受 JSON 格式的通知请求。 |
| 配置管理 | 通过 `config.yaml` 或环境变量进行全局设置。 |
| 日志系统 | 支持 `debug`、`info`、`error` 等日志级别。 |

## 用法

### 1. 安装  
```bash
# 通过 Go 安装
go install github.com/Notifuse/notifuse@latest

# 或下载预编译二进制文件
curl -L https://github.com/Notifuse/notifuse/releases/latest/download/notifuse-linux-amd64 -o notifuse
chmod +x notifuse
```

### 2. 启动服务  
```bash
# 默认使用 config.yaml（如果存在）
notifuse

# 指定配置文件
notifuse -config /path/to/config.yaml
```

### 3. 命令行发送通知  
```bash
# 基本用法
notifuse send --title "测试" --message "这是一个通知"

# 指定图标、超时和动作
notifuse send \
  --title "警告" \
  --message "磁盘空间不足" \
  --icon "/usr/share/icons/alert.png" \
  --timeout 5000 \
  --action "open" "打开磁盘管理"
```

### 4. 通过 REST API 发送  
```bash
curl -X POST http://localhost:8080/notify \
  -H "Content-Type: application/json" \
  -d '{
        "title": "API 通知",
        "message": "这是通过 REST API 发送的通知",
        "icon": "/usr/share/icons/info.png",
        "timeout": 3000
      }'
```

## 配置示例（config.yaml）
```yaml
port: 8080          # REST API 监听端口
timeout: 5000       # 默认通知显示时间（毫秒）
log_level: info     # 日志级别
```

## 贡献  
欢迎提交 Issue 与 PR，详细说明请参阅 `CONTRIBUTING.md`。

## 许可证  
MIT © Notifuse
```
