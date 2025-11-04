
---
title: Baileys
---


# Baileys (WhiskeySockets)

**项目地址:** https://github.com/WhiskeySockets/Baileys

## 主要特性

- **现代化 WhatsApp Web 协议实现**：基于 `@adiwajshing/baileys` 的改进与扩展。
- **TypeScript 支持**：完整的类型定义，便于静态检查和 IDE 自动补全。
- **可扩展插件体系**：轻松集成自定义插件，实现多种功能。
- **高性能与低延迟**：使用 `node:worker_threads` 和异步 I/O，确保实时性。
- **多账号管理**：一次启动即可同时管理多个 WhatsApp 账号。
- **自动重连与错误恢复**：内置智能重连策略，提升稳定性。

## 核心功能

| 功能 | 描述 |
|------|------|
| **消息收发** | 支持文本、图片、视频、语音、文件、位置、群聊、直播等多种消息类型。 |
| **事件监听** | 通过 `on('message')` 等事件监听各种业务逻辑。 |
| **联系人管理** | 获取联系人、群组、广播列表，支持搜索与筛选。 |
| **多媒体处理** | 自动下载、上传、转码，支持自定义媒体转换器。 |
| **群组管理** | 创建/解散群聊、邀请/踢除成员、修改群信息、设置管理员。 |
| **多设备同步** | 通过 WebSocket 与多个客户端保持同步。 |
| **插件生态** | `plugins/` 目录可放置自定义插件，支持 `onCommand`、`onEvent` 等钩子。 |

## 安装与使用

```bash
# 克隆仓库
git clone https://github.com/WhiskeySockets/Baileys.git
cd Baileys

# 安装依赖
npm install

# 编译 TypeScript
npm run build

# 运行示例
npm start
```

### 示例代码

```ts
import { default, useSingleFileAuthState } from '@whiskeysockets/baileys';
import * as pino from 'pino';

const { state, saveState } = useSingleFileAuthState('./auth_info.json');

const client = await default({
  logger: pino({ level: 'silent' }),
  auth: state,
});

client.ev.on('messages.upsert', async ({ messages }) => {
  const msg = messages[0];
  if (msg.message?.conversation) {
    console.log(`收到消息: ${msg.message.conversation}`);
  }
});

client.ev.on('connection.update', ({ connection, lastDisconnect }) => {
  if (connection === 'close' && lastDisconnect.error) {
    console.log('连接已断开，尝试重连...');
  }
});
```

### 运行

```bash
# 运行编译后的代码
node dist/index.js
```

## 文档与支持

- 官方文档: https://github.com/WhiskeySockets/Baileys#documentation
- 示例与教程: `examples/` 目录

---

> 以上内容基于 `WhiskeySockets/Baileys` 项目 README 与源码概览整理，供快速上手与了解项目核心特性。