---
title: ox
---

# ox_inventory

## 项目简介

ox_inventory 是 Overextended 团队为 FiveM 开发的完整库存系统，提供基于槽位的物品管理，支持元数据、武器、商店、储物箱等功能，无需严格依赖特定框架。

## 主要功能

- **服务器端安全**：所有物品、商店和储物箱的交互均在服务器端验证，确保安全性。
- **日志记录**：记录重要事件，如购买、物品移动、创建或移除。
- **框架支持**：兼容 ox_core、ESX、Qbox、ND_Core 等框架，支持玩家车辆、许可证和群组系统。
- **同步访问**：允许多个玩家同时访问同一库存。

### 物品系统

- 基于槽位的物品存储，支持自定义元数据以实现物品唯一性。
- 武器作为物品，支持附件和弹药系统，包括特殊弹药类型。
- 物品耐久度，支持随时间消耗或移除。
- 内部物品系统，提供安全且易用的物品使用效果。
- 兼容第三方框架的物品注册。

### 商店

- 基于群组和许可证的访问限制。
- 支持不同货币类型（如黑钱、扑克筹码等）。

### 储物箱

- 个人储物箱，可与特定标识符关联或创建玩家实例。
- 基于群组的访问限制。
- 支持从任何资源注册新储物箱。
- 容器物品允许访问储物箱，如纸袋或背包。
- 访问车辆的手套箱和后备箱。
- 垃圾箱和无主车辆中的随机物品生成。

## 安装和使用

1. 从 [GitHub Releases](https://github.com/overextended/ox_inventory/releases/latest/download/ox_inventory.zip) 下载最新版本的 ZIP 文件。
2. 将 `ox_inventory` 文件夹解压到你的 FiveM 服务器的 `resources` 目录中。
3. 在 `server.cfg` 中添加 `ensure ox_inventory` 以启动资源。
4. 根据你的框架配置相关设置（详见文档）。

## 文档

详细文档请访问：[https://overextended.dev/ox_inventory](https://overextended.dev/ox_inventory)

## 许可证

本项目采用 GPL-3.0 许可证。
