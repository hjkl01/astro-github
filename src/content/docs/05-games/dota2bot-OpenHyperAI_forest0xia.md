---
title: dota2bot-OpenHyperAI
---

# Dota2 Bot Script (OpenHyperAI)

## 功能

Dota2 Bot Script 是一个 beta 版本的 Dota 2 机器人脚本，旨在提供更好的机器人游戏体验。

- 支持 Dota 2 Patch 7.39。
- 支持所有 126 个英雄，包括新英雄如 Kez、Ringmaster 等。
- 可自定义机器人：ban/picks、名称、物品构建、技能升级等。
- 动态难度（Fretbots mode）：为机器人提供巨大优势以增加挑战。
- 支持大多数游戏模式。
- 改进决策：技能释放、物品使用、游走、农兵、防御。
- AI 聊天机器人：与机器人聊天（需要 Fretbots mode）。
- 机器人可以玩任何角色/位置，具有确定性 laning 分配。
- 修复许多 bug，如空闲机器人、取消通道、卡住状态。

## 用法

1. 创建自定义大厅，选择本地主机作为服务器位置。
2. 要启用 Fretbots mode（更难的机器人、中性物品、聊天机器人等），必须手动安装脚本：[安装说明](https://github.com/forest0xia/dota2bot-OpenHyperAI/discussions/68)。
3. 机器人角色和定位：大厅槽位顺序 = 位置分配（1-5）。
4. 游戏内命令：
   - `!pos X`：与机器人交换车道/角色（例如 `!pos 2`）。
   - `!pick HERO_NAME`：为自己选择英雄。
   - `!Xpos Y`：重新分配其他机器人的位置（例如 `!3pos 5`）。
   - `!ban HERO_NAME`：禁止英雄被选择。
   - `!sp XX`：设置机器人语言（例如 `!sp en`）。
5. 自定义设置：在 Customize 文件夹中调整。

参考 [Steam Workshop Link](https://steamcommunity.com/sharedfiles/filedetails/?id=3246316298) 获取更多信息。
