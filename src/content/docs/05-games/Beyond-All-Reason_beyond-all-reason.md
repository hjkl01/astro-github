
---
title: Beyond-All-Reason
---

**src/content/docs/00/Beyond-All-Reason_beyond-all-reason.md**

# Beyond All Reason

> GitHub项目地址: [https://github.com/beyond-all-reason/Beyond-All-Reason](https://github.com/beyond-all-reason/Beyond-All-Reason)

## 主要特性

- **基于Unity**：使用Unity 2022.x 进行开发，采用 C# 编写脚本，支持 3D 与 2D 场景。
- **模块化设计**：游戏核心逻辑拆分为多个可独立升级的模块，方便后期扩展和替换。
- **多人联网**：集成 UNET / Mirror，实现跨平台多人在线对战。
- **AI 对战**：内置基于状态机的 AI 系统，支持单人 vs AI 的多种玩法。
- **Mod 插件**：提供插件框架，玩家可以通过自定义脚本或资源包实现游戏改动。
- **日常挑战与剧情**：自带多段剧情任务与每日挑战系统，增强游戏趣味性与重玩价值。
- **性能优化**：使用对象池、协程以及 DOTS（Burst+Jobs）等技术，减少 GC 与帧率波动。

## 功能说明

| 功能 | 说明 |
|------|------|
| **宇宙航行** | 通过自由飞行控制器在星系中飞行，支持加速与降落。 |
| **资源采集** | 玩家可在行星表面采集矿物、能源与生物样本，供科技研发使用。 |
| **科技树** | 由玩家制衡不同研究路径，解锁新舰船、武器与等级提升。 |
| **舰队战斗** | 采用轨道投射与实体碰撞，支持多舰作战与策略配置。 |
| **UPnP 直连** | 内置 NAT-PIN/NAT-T 解析，简化玩家间直接连接。 |
| **自定义剧情** | 通过文本与脚本文件驱动剧情节点，可在游戏中随时跳转回调。 |

## 安装与使用

1. **克隆仓库**

   ```bash
   git clone https://github.com/beyond-all-reason/Beyond-All-Reason.git
   ```

2. **打开 Unity 项目**

   - 直接双击 `Beyond-All-Reason/Assets` 文件夹中的 `ProjectSettings` 目录，或在 Unity Hub 中导入该项目。

3. **构建平台**

   - 在 `File → Build Settings` 中设置目标平台（Windows、Mac、Linux、WebGL 等），点击 **Build** 或 **Build And Run**。

4. **运行游戏**

   - 执行生成的可执行文件，或者直接在 Unity Editor 中按 `Play` 进入实验模式。

5. **多人匹配**

   - 在游戏主界面选择 “多人游戏” → 服务器/匹配，输入服务器地址或使用默认 matchmaking。

6. **添加 Mod**

   - 在 `Mods` 文件夹下放置自定义脚本或资源包，然后在主菜单 “Mod 管理器” 中激活。

## 开发者指南

- **代码结构**：核心逻辑分布在 `Assets/Scripts/Core`，网络模块在 `Assets/Scripts/Networking`，AI 与循 Clang 8.0 代码风格，使用 PascalCase 规范命名。建议使用 Git Flow 工作流。
- **文档**：所有接口均已在 `Docs` 文件夹下生成。请在 PR 时更新对应 Markdown 文档。

> 你可以在项目的 Issues 或 Discussions 区域提出功能请求或报告 BUG。我们十分欢迎贡献者参与开发。

