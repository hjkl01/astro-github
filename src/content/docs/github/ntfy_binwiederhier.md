
---
title: ntfy
---

# ntfy 项目描述

## 项目地址
[https://github.com/binwiederhier/ntfy](https://github.com/binwiederhier/ntfy)

## 主要特性
ntfy 是一个简单、灵活的推送通知服务，支持通过 HTTP、WebSocket 等协议发送实时通知。它类似于 Pushover 或 Gotify，但更注重开源和自托管。核心特性包括：
- **实时推送**：支持 Android、iOS 和桌面设备接收通知。
- **主题订阅**：用户可以通过订阅主题（topic）接收特定通知。
- **自托管**：可以轻松部署在自己的服务器上，无需依赖第三方服务。
- **多协议支持**：兼容 HTTP POST、WebSocket 和 MQTT。
- **扩展性**：内置缓存、访问控制和 webhook 支持。
- **轻量级**：使用 Go 语言开发，资源占用低。

## 主要功能
- **发送通知**：通过 API 发送消息到指定主题，通知会推送到订阅设备。
- **接收通知**：移动 App 或 Web 客户端订阅主题，实时接收推送。
- **消息管理**：支持消息缓存、过期时间设置和过滤。
- **集成**：易于集成到脚本、自动化工具（如 cron 任务）中，用于监控或警报。
- **安全**：支持认证、HTTPS 和访问控制列表 (ACL)。

## 用法
### 1. 安装与部署
- **Docker 部署**（推荐）：
  ```
  docker run -it --rm -p 80:80 -v ntfy:/var/cache/ntfy binwiederhier/ntfy serve
  ```
  这会启动服务器，默认监听 80 端口。

- **二进制安装**：
  下载预编译二进制文件（如从 GitHub Releases），运行 `ntfy serve` 启动服务器。

- **配置**：
  编辑配置文件 `ntfy.yml` 设置缓存路径、认证等：
  ```yaml
  server:
    listen-http: :80
  cache-file: /var/cache/ntfy/ntfy.db
  auth-file: /etc/ntfy/user.db
  ```

### 2. 发送通知
使用 curl 发送 HTTP POST 请求：
```
curl -d "Your message here" ntfy.sh/mytopic
```
- `mytopic` 是通知主题。
- 支持标题、标签、优先级等参数，例如：
  ```
  curl -H "Title: Alert" -H "Priority: 5" -d "High priority alert!" ntfy.sh/mytopic
  ```

### 3. 接收通知
- **移动 App**：下载 ntfy App（Android/iOS），订阅主题如 `ntfy.sh/mytopic`。
- **Web 客户端**：访问 `https://ntfy.sh` 订阅主题。
- **自托管**：在 App 中输入服务器 URL 如 `http://your-server:80/mytopic`。

### 4. 高级用法
- **订阅管理**：使用 App 或 API 管理订阅。
- **Webhook 集成**：服务器支持 webhook 端点，用于自定义处理。
- **CLI 工具**：使用 `ntfy` CLI 发送通知：
  ```
  ntfy publish mytopic "Hello from CLI"
  ```

更多细节请参考项目 README。