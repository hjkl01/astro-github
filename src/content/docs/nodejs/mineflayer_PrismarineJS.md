---
title: mineflayer
---

# Mineflayer

## 项目简介

Mineflayer 是一个强大的、稳定的、高级 JavaScript API，用于创建 Minecraft 机器人。它支持 Minecraft 1.8 到 1.21.8 版本，并可从 Python 中使用。

## 主要功能

- **实体知识和跟踪**：跟踪游戏中的实体。
- **方块知识**：查询周围世界，快速查找任何方块。
- **物理和移动**：处理所有边界框，支持移动。
- **攻击和车辆**：攻击实体和使用车辆。
- **库存管理**：管理物品栏。
- **合成和容器**：支持合成、箱子、发射器、附魔台等。
- **挖掘和建造**：挖掘和建造方块。
- **其他功能**：健康状态、天气、激活方块、使用物品、聊天等。

## 安装

首先安装 Node.js >= 18，然后运行：

```bash
npm install mineflayer
```

## 基本用法

### 简单回声机器人示例

```javascript
const mineflayer = require('mineflayer');

const bot = mineflayer.createBot({
  host: 'localhost', // Minecraft 服务器 IP
  username: 'Bot', // 用户名，如果 auth 为 'offline'，否则为唯一标识符
  auth: 'microsoft', // 对于离线模式服务器，设置为 'offline'
  // port: 25565,              // 如果不是默认端口 25565，需要设置
  // version: false,           // 仅在需要特定版本时设置，否则自动检测
  // password: '12345678'      // 如果使用密码认证，需要设置，username 必须是邮箱
});

bot.on('chat', (username, message) => {
  if (username === bot.username) return;
  bot.chat(message);
});

// 记录错误和踢出原因：
bot.on('kicked', console.log);
bot.on('error', console.log);
```

如果 `auth` 设置为 `microsoft`，你将被提示在浏览器中登录 Microsoft.com。登录后，机器人将自动获取并缓存认证令牌。

## 更多示例

- **查看机器人视角**：使用 prismarine-viewer 在浏览器中显示机器人视角。
- **路径寻找**：使用 pathfinder 插件让机器人自动前往任何位置。
- **箱子操作**：使用箱子、熔炉、发射器等。
- **挖掘**：创建能挖掘方块的机器人。
- **守卫**：让机器人守卫指定区域免受怪物攻击。

更多示例请查看 [examples](https://github.com/PrismarineJS/mineflayer/tree/master/examples) 文件夹。

## 插件

Mineflayer 支持插件，以下是一些第三方插件：

- [pathfinder](https://github.com/Karang/mineflayer-pathfinder)：高级 A\* 路径寻找。
- [prismarine-viewer](https://github.com/PrismarineJS/prismarine-viewer)：简单网页区块查看器。
- [mineflayer-pvp](https://github.com/PrismarineJS/mineflayer-pvp)：易用的 PVP 和 PVE API。

## 文档

- [官方文档](https://prismarinejs.github.io/mineflayer/)
- [API 参考](https://github.com/PrismarineJS/mineflayer/blob/master/docs/api.md)
- [教程](https://github.com/PrismarineJS/mineflayer/blob/master/docs/tutorial.md)
