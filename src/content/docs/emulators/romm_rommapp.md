
---
title: romm
---

# ROMM 项目

## 项目地址
[https://github.com/rommapp/romm](https://github.com/rommapp/romm)

## 主要特性
ROMM（ROM Management）是一个开源的游戏ROM管理工具，主要用于管理、组织和分享游戏ROM文件。它支持多种平台（如Nintendo、Sony、Sega等）的ROM文件，提供用户友好的界面和强大的搜索功能。核心特性包括：
- **ROM 库管理**：自动扫描和导入ROM文件，支持元数据提取和封面艺术下载。
- **多平台支持**：兼容NES、SNES、Game Boy、PlayStation等多种游戏系统。
- **搜索与过滤**：高级搜索功能，可按平台、名称、评分等过滤ROM。
- **用户界面**：响应式Web界面，支持移动设备访问。
- **备份与同步**：内置备份机制，便于数据迁移和云同步。
- **插件扩展**：支持自定义插件，扩展功能如刮削器或主题自定义。
- **开源免费**：基于MIT许可，社区驱动开发。

## 主要功能
- **ROM 导入与组织**：从本地文件夹或外部源导入ROM，支持批量处理和去重。
- **元数据管理**：自动从在线数据库（如TheGamesDB）获取游戏信息、截图和描述。
- **播放集成**：与模拟器（如RetroArch）集成，可直接从ROMM启动游戏。
- **用户权限**：多用户支持，管理员可管理访问权限。
- **统计与报告**：生成ROM库统计，如游戏数量、平台分布。
- **API 接口**：提供RESTful API，便于与其他工具集成。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/rommapp/romm.git`
   - 进入目录：`cd romm`
   - 安装依赖：使用Docker（推荐）或Node.js环境。Docker命令：`docker-compose up -d`。
   - 配置数据库（SQLite或PostgreSQL）和ROM路径。

2. **配置**：
   - 编辑`config.json`文件，设置ROM扫描目录、数据库连接和API密钥。
   - 启动服务：`npm start` 或通过Docker运行。

3. **使用**：
   - 访问Web界面（默认http://localhost:3000）。
   - 登录后，点击“扫描ROM”导入文件。
   - 浏览库、搜索游戏、下载封面或启动模拟器。
   - 高级用法：通过API调用管理ROM，例如`GET /api/roms?platform=nes`查询NES游戏。

更多细节请参考项目README。