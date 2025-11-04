
---
title: PathOfBuilding
---


# Path of Building – PathOfBuildingCommunity

**项目地址**  
<https://github.com/PathOfBuildingCommunity/PathOfBuilding>

## 项目简介  
Path of Building 是一款针对《Path of Exile》游戏的高级构建工具，帮助玩家在离线环境下规划、分析和优化角色技能树、被动树、装备配置以及符文阵列。它以可视化界面、丰富的计算功能和高度可扩展性著称，是社区中最受欢迎的构建辅助工具之一。

---

## 主要特性

| 类别 | 功能描述 |
|------|----------|
| **技能树 & 被动树** | 交互式可视化树图，支持节点点击、路径高亮、锁定/解锁、节点统计显示。 |
| **装备/物品数值计算** | 自动读取装备属性，计算属性加成、护甲/闪避/韧性、攻击/防御等数值。 |
| **技能/符文计算** | 支持所有技能和符文的数值、冷却、消耗、命中等计算，并可查看技能树中对应节点。 |
| **构建导入/导出** | 支持导入《Path of Exile》内置的构建链接（POE语法），也支持导出为POE格式或Markdown、图片、JSON。 |
| **模拟与分析** | 提供对抗模拟、伤害输出、持续伤害、生命恢复等多维度分析工具。 |
| **插件与脚本** | 支持用户自定义插件（Lua脚本）扩展功能，插件目录可通过 `Plugins` 目录加载。 |
| **多语言 & 多平台** | 支持中文、英文等多语言，跨平台（Windows、macOS、Linux）运行。 |
| **离线操作** | 所有计算均在本地完成，无需网络连接。 |

---

## 功能与使用方法

### 1. 安装与运行
1. 克隆仓库或下载发布版本（Release）  
   ```bash
   git clone https://github.com/PathOfBuildingCommunity/PathOfBuilding.git
   ```
2. 进入项目根目录，使用 `npm`（或 `yarn`）安装依赖  
   ```bash
   npm install
   ```
3. 编译并启动  
   ```bash
   npm run build
   npm start
   ```
   或者直接运行已发布的可执行文件（`PathOfBuilding.exe`、`PathOfBuilding.app` 等）。

### 2. 导入构建
- 在《Path of Exile》游戏界面中复制构建链接（Prefixed `https://www.pathofexile.com/character-window/...`）。
- 在 Path of Building 主界面点击 **Import**，粘贴链接，点击 **Import**。  
- 工具会解析链接，自动填充技能树、被动树、装备与符文。

### 3. 编辑与优化
- **技能树**：点击技能节点打开属性窗口；右键可锁定/解锁节点。  
- **被动树**：类似技能树，支持多种统计视图。  
- **装备**：在 **Inventory** 面板中拖拽装备，查看属性与合成建议。  
- **符文阵列**：点击符文节点查看对应符文属性，支持符文锁定。  
- **属性窗口**：显示当前角色的综合数值（生命、护甲、攻击等），实时更新。

### 4. 分析与输出
- **Damage Calculator**：输入目标类型、距离、等级等，查看伤害输出。  
- **Stat Tracker**：实时统计技能伤害、冷却、消耗等。  
- **Export**：  
  - `Export to POE` → 生成可直接粘贴到游戏的构建链接。  
  - `Export to Markdown` / `Export to Image` / `Export to JSON` → 用于分享或备份。  
- **Simulation**：使用 `Sim` 模块跑对抗模拟，评估不同装备/技能组合的表现。

### 5. 自定义与插件
- 在 **Plugins** 目录下放置自定义 Lua 脚本，工具会自动加载。  
- 插件可扩展计算逻辑、添加新的图表、实现自定义分析等。

---

## 贡献与社区

- **Issues**：提交 bug、功能需求。  
- **Pull Requests**：加入新功能、修复错误。  
- **Wiki & Docs**：查看详细使用手册、插件开发指南。  
- **Discord / Reddit**：与其他玩家、开发者交流使用经验。

---

> Path of Building 通过强大的离线计算与可视化编辑，帮助玩家快速构建与评估高效的 POE 技能树。无论是新手还是老玩家，都能在其中找到实用的工具与灵感。祝你在暗影森林中玩得开心，打造最强构建！

