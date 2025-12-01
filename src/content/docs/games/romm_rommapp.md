---
title: romm
---

# Romm

Romm 是一个开源的、自托管的 ROM 管理器，专为复古游戏爱好者设计。它提供了一个现代化的 Web 界面，帮助用户组织、浏览和播放 ROM 文件，同时支持元数据下载、截图管理和多平台游戏库管理。该项目基于 Python 和 FastAPI 构建，前端使用 Vue.js。

## 主要功能

- **ROM 库组织**：自动扫描和分类 ROM 文件，支持多种文件格式（如 ZIP、7Z）。
- **元数据集成**：从 IGDB、MobyGames 等数据库下载游戏信息，包括描述、发布日期和评分。
- **媒体管理**：自动下载游戏截图、封面和视频预览。
- **多平台支持**：支持 NES、SNES、PS1 等数百个游戏平台。
- **用户管理**：支持多用户访问和权限控制。
- **集成仿真**：可与模拟器集成，直接在浏览器中播放游戏。
- **搜索和过滤**：强大的搜索功能，按平台、类型或收藏夹过滤。
- **备份和恢复**：支持 ROM 库的备份和导入。

## 安装说明

Romm 支持 Docker 安装（推荐）和源码安装。以下是 Docker 方式的步骤：

1. **前提条件**：确保安装了 Docker 和 Docker Compose。
2. **克隆仓库**：
   ```
   git clone https://github.com/rommapp/romm.git
   cd romm
   ```
3. **配置环境**：复制 `.env.example` 为 `.env`，并编辑数据库和 Redis 设置。
4. **启动服务**：
   ```
   docker-compose up -d
   ```
   这将启动 Romm 应用、PostgreSQL 数据库和 Redis 缓存。
5. **访问应用**：打开浏览器访问 `http://localhost:8080`，使用默认凭据登录（admin/admin）。

对于源码安装：

- 安装 Python 3.10+ 和依赖：`pip install -r requirements.txt`
- 运行：`python main.py`

## 使用方法

1. **添加 ROM**：在 Web 界面中上传或扫描 ROM 文件夹。Romm 会自动识别平台和游戏。
2. **下载元数据**：选择游戏，点击"下载元数据"以获取详细信息和媒体。
3. **浏览库**：使用侧边栏按平台浏览，或使用搜索栏查找游戏。
4. **播放游戏**：点击游戏图标，选择模拟器启动（需配置模拟器路径）。
5. **管理收藏**：创建收藏夹，标记收藏游戏，或导出库为 JSON。

Romm 强调隐私和自托管，不依赖外部服务。更多详情请查看 GitHub 仓库：https://github.com/rommapp/romm。
