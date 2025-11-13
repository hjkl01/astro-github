---
title: redis-tui
---

# Redis TUI 项目

**GitHub 项目地址**: [https://github.com/mylxsw/redis-tui](https://github.com/mylxsw/redis-tui)

## 主要特性

Redis TUI 是一个基于终端的用户界面（Terminal User Interface）工具，用于管理和操作 Redis 数据库。它采用 Rust 语言开发，提供了一个直观、交互式的命令行界面，帮助用户可视化地浏览和编辑 Redis 数据。核心特性包括：

- **交互式界面**：使用 ratatui 库构建的终端 UI，支持键盘导航、鼠标操作（如果终端支持），无需图形界面即可管理 Redis。
- **支持多种 Redis 数据类型**：完整支持字符串（String）、哈希（Hash）、列表（List）、集合（Set）、有序集合（Sorted Set）、位图（Bitmap）等常见数据结构。
- **键值浏览与编辑**：实时显示键列表，支持搜索、过滤键，支持直接编辑值、删除键或批量操作。
- **连接管理**：支持连接多个 Redis 实例，包括单机、哨兵（Sentinel）和集群（Cluster）模式。
- **高性能**：基于 Rust 的高效实现，适合处理大规模数据，减少内存占用。
- **跨平台**：支持 Linux、macOS 和 Windows 等操作系统。
- **自定义配置**：通过配置文件或命令行参数自定义主题、快捷键和连接设置。

## 主要功能

- **数据库导航**：切换 Redis 数据库（DB），查看键的统计信息，如键数量、内存使用等。
- **数据操作**：CRUD 操作（创建、读取、更新、删除），包括 TTL 设置、过期键管理。
- **搜索与过滤**：支持模式匹配（如 glob 模式）搜索键，支持按类型过滤。
- **监控与诊断**：查看 Redis 服务器信息、慢查询日志、客户端连接等（依赖 Redis 命令）。
- **导出/导入**：支持将键值数据导出为 JSON 或其他格式，便于备份和迁移。
- **脚本执行**：集成简单的脚本运行功能，允许执行 Redis 命令序列。

## 用法

### 安装

1. **从源代码构建**（推荐）：
   - 确保安装 Rust（通过 [rustup](https://rustup.rs/)）。
   - 克隆仓库：`git clone https://github.com/mylxsw/redis-tui.git`
   - 进入目录：`cd redis-tui`
   - 构建并安装：`cargo install --path .`

2. **预构建二进制**：
   - 从 GitHub Releases 下载适用于你的平台的二进制文件，并添加到 PATH。

### 基本用法

1. **启动工具**：
   ```
   redis-tui [选项]
   ```
   - 默认连接本地 Redis（127.0.0.1:6379），无密码。
   - 示例：`redis-tui --host 192.168.1.100 --port 6379 --auth yourpassword`

2. **命令行选项**：
   - `--host <HOST>`: Redis 主机地址（默认: 127.0.0.1）。
   - `--port <PORT>`: Redis 端口（默认: 6379）。
   - `--auth <PASSWORD>`: 认证密码。
   - `--db <DB>`: 默认数据库索引（默认: 0）。
   - `--tls`: 启用 TLS 连接。
   - `--config <PATH>`: 加载配置文件（TOML 格式，支持多个连接）。

3. **界面操作**：
   - 使用箭头键或 Vim 风格快捷键（h/j/k/l）导航。
   - 按 `?` 查看帮助，显示所有快捷键。
   - 选择键后，按 `e` 编辑值，`d` 删除，`t` 设置 TTL。
   - 搜索：按 `/` 输入搜索模式。
   - 退出：按 `q` 或 `Ctrl+C`。

### 示例

- 连接远程 Redis 并启动：`redis-tui --host example.com --port 6380 --auth secret`
- 在配置文件 `redis-tui.toml` 中定义连接：
  ```
  [[connections]]
  name = "local"
  host = "127.0.0.1"
  port = 6379
  ```
  然后运行：`redis-tui --config redis-tui.toml`

更多细节请参考项目 README 和示例配置文件。