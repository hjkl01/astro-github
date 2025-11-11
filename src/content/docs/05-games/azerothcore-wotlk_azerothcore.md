---
title: AzerothCore WotLK
---

# AzerothCore WotLK

AzerothCore WotLK 是一个开源的游戏服务器应用程序和框架，专为托管大型多人在线角色扮演游戏（MMORPG）而设计。它基于流行的MMORPG《魔兽世界》（World of Warcraft），旨在重现原始游戏从补丁3.3.5a的游戏体验。

## 功能

- **开源和模块化**：基于MaNGOS、TrinityCore和SunwellCore，提供完整的开源解决方案，支持高度模块化扩展。
- **Blizzlike内容**：致力于使所有游戏内容与官方Blizzlike一致，确保高标准的修复和稳定性。
- **定制化**：通过模块系统轻松定制游戏体验，添加自定义功能、内容和修改。
- **社区驱动**：活跃的开发者、贡献者和用户社区，通过论坛、Discord等平台协作和支持。
- **稳定性**：所有更改在合并到主分支前通过CI测试，确保服务器稳定运行。
- **多平台支持**：支持Linux、Windows、macOS等平台构建和运行。

## 用法

### 安装

详细的安装指南请参考[官方Wiki](http://www.azerothcore.org/wiki/installation)。基本步骤包括：

1. 克隆仓库：`git clone https://github.com/azerothcore/azerothcore-wotlk.git`
2. 安装依赖：根据平台安装必要的构建工具和库（如CMake、MySQL等）。
3. 构建项目：使用提供的脚本或CMake进行编译。
4. 配置数据库：设置MySQL数据库并导入SQL文件。
5. 运行服务器：启动世界服务器和认证服务器。

### 使用模块

AzerothCore支持模块化扩展，可从[模块目录](https://www.azerothcore.org/catalogue.html#/)获取社区开发的模块。安装模块通常涉及：

1. 下载模块代码。
2. 将模块放置在`modules/`目录中。
3. 重新构建项目以包含模块。
4. 根据模块文档配置和启用功能。

### 贡献

如果您想贡献代码，请查看[贡献指南](https://www.azerothcore.org/wiki/contribute)。加入[Discord服务器](https://discord.gg/gkt4y2x)与社区交流。

## 许可证

- 新组件基于GNU AGPL v3。
- 旧组件基于GNU GPL v2。

注意：AzerothCore不是暴雪娱乐的官方产品，不支持非法公共服务器。
