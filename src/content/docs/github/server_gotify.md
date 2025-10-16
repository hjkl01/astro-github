
---
title: server
---

# Gotify Server 项目

## 项目地址
[GitHub 项目地址](https://github.com/gotify/server)

## 主要特性
Gotify 是一个开源的自托管通知服务器，专注于简单、高效的推送通知服务。它支持多种平台和设备，提供 RESTful API 接口，便于与其他应用集成。主要特性包括：
- **自托管**：用户可以轻松在自己的服务器上部署，无需依赖第三方服务，确保数据隐私。
- **多平台支持**：兼容 Android、iOS 和 Web 客户端，支持推送文本、标题、优先级等通知类型。
- **API 驱动**：提供完整的 REST API，用于发送、接收和管理通知，支持 Webhook 集成。
- **用户管理和权限**：支持多用户账户、应用令牌（App Token）和访问控制。
- **插件扩展**：内置插件系统，可扩展功能，如邮件集成或自定义通知处理。
- **轻量级**：基于 Go 语言开发，资源占用低，易于部署在 Raspberry Pi 等设备上。
- **加密传输**：支持 HTTPS，确保通知传输安全。

## 主要功能
- **推送通知**：通过 API 发送实时推送，支持优先级（低、中、高）和过期时间设置。
- **客户端应用**：官方提供 Android 和 iOS 应用，以及 Web 界面，用于接收和查看通知。
- **Webhook 支持**：可与 GitHub、CI/CD 工具（如 Jenkins）或其他服务集成，实现自动化通知。
- **消息管理**：支持消息历史记录、搜索、删除和批量操作。
- **主题和自定义**：用户可自定义通知声音、振动和显示方式。
- **健康检查**：内置监控端点，用于检查服务器状态。

## 用法
### 部署服务器
1. **前提条件**：安装 Go 1.17+ 或使用 Docker。
2. **从源代码构建**（推荐）：
   - 克隆仓库：`git clone https://github.com/gotify/server.git`
   - 进入目录：`cd server`
   - 构建：`go build -o gotify-server`
   - 配置：编辑 `config.json` 文件，设置端口、数据库（SQLite 默认）、HTTPS 等。
   - 运行：`./gotify-server`
3. **使用 Docker**：
   - 拉取镜像：`docker pull gotify/server`
   - 运行容器：`docker run -p 80:80 -v /path/to/data:/app/data gotify/server`
   - 访问 Web 界面：`http://your-server-ip:80`

### 发送通知
- 使用 cURL 示例：
  ```
  curl -X POST -F "message=Hello World" -F "title=Test" -F "priority=10" \
  -H "Content-Type: multipart/form-data" \
  "http://your-server-ip:80/message?token=YOUR_APP_TOKEN"
  ```
- 集成到应用：使用官方客户端库（Go、Java 等）或直接调用 API。

### 客户端使用
1. 下载官方 App（Android/iOS）或访问 Web 界面。
2. 注册账户：使用服务器 URL 和用户名/密码创建账户。
3. 创建应用：生成 App Token 用于接收通知。
4. 配置推送：设置服务器地址和 Token，即可接收通知。

更多详情请参考项目 README 和文档。