
---
title: whatsapp-web.js
---

# whatsapp-web.js（pedroslopez）

> 项目地址: <https://github.com/pedroslopez/whatsapp-web.js>

## 项目概述  
`whatsapp-web.js` 是一个基于 Node.js 的开源库，封装了 WhatsApp Web 的协议，允许开发者通过 JavaScript 与 WhatsApp 进行交互。它提供了完整的 API 来发送/接收消息、管理群组、处理媒体文件、获取会话状态等功能，适用于聊天机器人、自动化脚本、监控工具等场景。

## 安装
```bash
npm install whatsapp-web.js
```

## 主要特性
- **自动登录**：支持二维码扫码登录、使用会话文件保持登录状态。
- **消息收发**：支持文本、图片、视频、音频、文件、表情、贴纸、位置、联系人卡片等多种消息类型。
- **群组管理**：创建、解散、修改群组信息；邀请/踢除成员；获取群组成员列表。
- **事件监听**：监听 `message`、`message_create`、`message_revoke_everyone`、`group_join`、`group_leave`、`presence_change` 等事件。
- **媒体处理**：下载、上传媒体文件，支持自定义缓存策略。
- **多实例**：可在同一台机器上运行多个实例，分别登录不同账号。
- **WebSocket 连接**：使用 WebSocket 实时接收事件，支持 `proxy`、`timeout` 等配置。

## 用法示例
```js
const { Client, LocalAuth } = require('whatsapp-web.js');
const client = new Client({
    authStrategy: new LocalAuth()   // 保存会话信息
});

client.on('qr', qr => {
    console.log('扫描二维码: ', qr);
});

client.on('ready', () => {
    console.log('WhatsApp 已准备就绪！');
    client.sendMessage('123456789@c.us', 'Hello, World!');
});

client.on('message', msg => {
    console.log(`收到消息: ${msg.body}`);
});

client.initialize();
```

## 快速开始
1. **创建项目**  
   ```bash
   mkdir my-whatsapp-bot && cd my-whatsapp-bot
   npm init -y
   npm install whatsapp-web.js
   ```

2. **编写脚本**  
   保存上述示例为 `bot.js`。

3. **运行**  
   ```bash
   node bot.js
   ```

4. **扫码登录**  
   扫描终端打印的二维码，即可登录。

## 文档与支持  
- 官方文档: <https://github.com/pedroslopez/whatsapp-web.js/wiki>
- 示例代码: <https://github.com/pedroslopez/whatsapp-web.js/tree/master/examples>
- 社区支持: 在 GitHub Issues 或 Discord 讨论组中提问。

## 贡献
欢迎提交 Pull Request、Issue 与讨论。请遵循项目的编码规范与贡献指南。

## 许可证  
MIT © 2023 Pedro Lopez

---