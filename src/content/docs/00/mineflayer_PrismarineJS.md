
---
title: mineflayer
---

# PrismarineJS/mineflayer

**项目地址**  
https://github.com/PrismarineJS/mineflayer

## 主要特性

- **基于 Node.js** – 通过 JavaScript 编写，可直接在服务器端或桌面端运行。  
- **Minecraft Bot** – 能够模拟玩家在多种 Minecraft 版本（1.7 以上）中的行为。  
- **事件驱动** – 通过事件系统实现对聊天、方块、实体等的监听与响应。  
- **插件化** – 通过子模块（ plugins 目录）可快速扩展功能，例如：聊天机器人、自动挖矿、钓鱼、裁龙等。  
- **网络协议** – 完整实现 Minecraft 的原始网络协议，支持自定义数据包。  
- **跨平台支持** – 兼容 Windows、macOS、Linux，依赖 **LibMCGame** 或 **node-forge** 等原生模块。  

## 功能概述

- **连接与身份验证** – 支持用户名/密码、Mojang 账号（凭 `authlib-injector`）以及基于 Microsoft 的 OAuth2 登录。  
- **世界交互** – 读取/修改方块、实体状态，支持手动或自动挖掘、放置、旋转。  
- **聊天管理** – 监听 `chat` 事件，输出聊天信息，并可通过 `bot.chat()` 发送消息。  
- **路径寻找** – 内置 A* 路径算法，可用 `bot.pathfinder` 进行移动规划。  
- **视线追踪** – 能检测目标方块/实体，实现自动点选/破坏。  
- **插件接口** – 通过 `mineflayer-plugin` 模块快速编写插件，或使用现成的如 `mineflayer-scaffold`、`mineflayer-craft` 等。  
- **高度可定制** – 通过插件或原始回调轻松覆盖默认行为，编写复杂机器人脚本。  

## 如何使用

1. **安装**  
   ```bash
   npm install mineflayer
   ```

2. **创建 Bot**  
   ```js
   const mineflayer = require('mineflayer')

   const bot = mineflayer.createBot({
     host: 'play.com',  // 服务器地址
     port: 25565,               // 端口
     username: 'BotName',       // Minecraft 账号
     auth: 'mojang',            // 账号类型（mojang/legacy/microsoft）
   })
   ```

3. **事件监听**  
   ```js
   bot.on('chat', (username, message) => {
     console.log(`[${username}]: ${message}`)
   })

   bot.on('spawn', () => {
     console.log('Bot 已进入世界')
   })
   ```

4. **发送消息**  
   ```js
   bot.chat('Hello, world!')
   ```

5. **使用插件**（可选）  
   ```bash
   npm install mineflayer-scaffold
   ```
   ```js
   const bot = mineflayer.createBot({ ... })
   const scaffold = require('mineflayer-scaffold')(bot)
   bot.on('spawn', () => scaffold.start())
   ```

6. **路径寻找**（示例）  
   ```js
   const { pathfinder, Movements } = require('mineflayer-pathfinder')
   bot.loadPlugin(pathfinder)

   const ms = new Movements(bot)
   const goal = new GoalBlock(100, 65, 200)
   bot.pathfinder.setMovements(ms)
   bot.pathfinder.setGoal(goal, true)
   ```

> 详细文档请访问官方 wiki 或查看源码中的示例。

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL