---
title: Beyond-All-Reason
---

**src/content/docs/00/Beyond-All-Reason_beyond-all-reason.md**

# Beyond All Reason

> GitHub项目地址: [https://github.com/beyond-all-reason/Beyond-All-Reason](https://github.com/beyond-all-reason/Beyond-All-Reason)

## 主要特性

- **开源 RTS 游戏**：基于 Recoil RTS Engine 构建的免费实时战略游戏。
- **跨平台支持**：支持 Windows、Linux、macOS 等平台。
- **社区驱动**：活跃的开源社区，提供持续更新和 mod 支持。
- **免费下载**：从官方网站免费下载和游玩。

## 功能说明

| 功能           | 说明                                              |
| -------------- | ------------------------------------------------- |
| **单位建造**   | 建造各种地面和空中单位，进行战略部署。            |
| **资源管理**   | 采集资源，建造经济单位，维持军队供应。            |
| **战斗系统**   | 实时战斗，支持多种武器和战术。                    |
| **多人对战**   | 支持多人在线对战，通过 lobby 连接。               |
| **地图多样性** | 多种地图类型，支持自定义地图。                    |
| **Mod 支持**   | 开放式 mod 系统，允许自定义单位、地图和游戏模式。 |

## 安装与使用

1. **下载**：从官方网站 [https://www.beyondallreason.info/download](https://www.beyondallreason.info/download) 下载游戏。

2. **安装**：运行安装程序，按照提示安装。

3. **运行**：启动游戏，通过 lobby 进入单人或多人模式。

4. **玩法**：参考指南 [https://www.beyondallreason.info/guides](https://www.beyondallreason.info/guides) 学习游戏规则。

## 开发者指南

- **代码结构**：游戏代码主要使用 Lua 脚本，引擎基于 C++ 的 Recoil RTS Engine。游戏逻辑在 `luarules` 和 `luaui` 目录。
- **开发环境**：需要安装 lobby (Chobby)，然后克隆代码到 `data/games` 目录，创建 `devmode.txt` 文件启用开发模式。
- **贡献**：Fork 仓库，提交 PR。参考 [https://github.com/beyond-all-reason/Beyond-All-Reason](https://github.com/beyond-all-reason/Beyond-All-Reason) 的 README 获取详细开发指南。

> 你可以在项目的 Issues 或 Discussions 区域提出功能请求或报告 BUG。我们十分欢迎贡献者参与开发。
