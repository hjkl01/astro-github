
---
title: docker-wechat
---

# Docker WeChat 项目

## 项目地址
[https://github.com/huan/docker-wechat](https://github.com/huan/docker-wechat)

## 主要特性
- **基于Docker的WeChat实现**：使用Docker容器化技术封装WeChat（微信）功能，支持在Linux、macOS和Windows等平台上运行，无需安装原生WeChat客户端。
- **跨平台兼容**：通过Docker确保在不同操作系统上的一致性运行，适合服务器部署或开发环境。
- **开源与模块化**：项目采用开源许可，基于Node.js和WeChaty框架构建，便于扩展和自定义。
- **轻量级部署**：无需图形界面，支持命令行操作，资源占用低，适用于自动化脚本和机器人开发。
- **集成WeChaty**：内置WeChaty puppet支持，可实现消息监听、发送、群管理等自动化功能。

## 主要功能
- **WeChat登录与会话管理**：支持扫描二维码登录WeChat账号，维护会话状态，实现持久化连接。
- **消息处理**：监听和发送文本、图片、文件等消息，支持事件回调，如好友添加、群聊消息等。
- **机器人开发**：提供API接口，用于构建WeChat机器人，例如自动回复、群公告推送或数据同步。
- **多账号支持**：可配置多个WeChat实例，适用于企业级应用或多用户场景。
- **日志与监控**：内置日志记录和错误处理，便于调试和监控运行状态。

## 用法
1. **环境准备**：
   - 安装Docker和Docker Compose（推荐）。
   - 确保系统有足够的权限运行Docker容器。

2. **克隆项目**：
   ```
   git clone https://github.com/huan/docker-wechat.git
   cd docker-wechat
   ```

3. **配置**：
   - 编辑`docker-compose.yml`文件，设置环境变量如`WECHATY_PUPPET`（指定puppet类型，例如`wechaty-puppet-padlocal`）。
   - 配置WeChat账号相关参数（如token或二维码路径）。

4. **运行**：
   - 使用Docker Compose启动：
     ```
     docker-compose up -d
     ```
   - 或直接运行Docker命令：
     ```
     docker run -it --rm \
       -e WECHATY_PUPPET=wechaty-puppet-padlocal \
       -e WECHATY_PUPPET_PADLOCAL_TOKEN=your_token \
       huan/docker-wechat
     ```

5. **登录与使用**：
   - 容器启动后，查看日志获取二维码（或通过浏览器访问暴露端口）。
   - 使用手机WeChat扫描二维码登录。
   - 通过项目提供的API或脚本接口开发自定义功能，例如监听消息：
     ```javascript
     const { Wechaty } = require('wechaty');
     const bot = new Wechaty();
     bot.on('message', async msg => {
       console.log(`Message: ${msg}`);
     });
     bot.start();
     ```

6. **停止与清理**：
   - 停止容器：`docker-compose down`。
   - 查看日志：`docker-compose logs -f`。

更多细节请参考项目README文档。