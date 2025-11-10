---
title: pg
---

# pg_activity 项目

## 项目地址
https://github.com/dalibo/pg_activity

## 主要特性
pg_activity 是一个开源的 PostgreSQL 监控工具，灵感来源于 Linux 的 top 命令。它提供了一个交互式界面，用于实时监控 PostgreSQL 数据库的活动，包括进程、查询、连接和系统资源。核心特性包括：
- **实时监控**：动态显示数据库进程、查询执行时间和资源使用情况。
- **交互式界面**：类似于 top 的文本界面，支持排序、过滤和导航。
- **多视图支持**：包括进程视图（Processes）、后台进程视图（Backend Processes）和查询视图（Queries）。
- **资源指标**：监控 CPU、内存、I/O 和锁等待等数据库指标。
- **跨平台兼容**：支持 Linux、macOS 和 Windows（通过 WSL 或类似环境）。
- **无外部依赖**：纯 Python 实现，仅需 PostgreSQL 连接库。

## 主要功能
- **进程监控**：列出所有数据库连接和活动查询，支持按 CPU、内存或执行时间排序。
- **查询分析**：显示慢查询、锁冲突和等待事件，帮助诊断性能问题。
- **系统集成**：集成 PostgreSQL 的系统视图（如 pg_stat_activity），无需额外插件。
- **警报与过滤**：允许用户过滤特定用户、数据库或状态的进程。
- **导出与日志**：支持将监控数据导出为 CSV 或日志文件，用于进一步分析。
- **自定义配置**：通过配置文件调整刷新间隔、颜色主题和显示字段。

## 用法
1. **安装**：
   - 通过 pip 安装：`pip install pg_activity`。
   - 或从 GitHub 克隆仓库后运行 `python setup.py install`。

2. **基本运行**：
   - 连接到 PostgreSQL：`pg_activity -d <数据库名> -U <用户名> -h <主机> -p <端口>`。
   - 示例：`pg_activity -d mydb -U postgres`（默认使用本地连接）。

3. **交互操作**：
   - 使用箭头键导航，按 `q` 退出。
   - 按 `1` 切换到进程视图，按 `2` 切换到查询视图。
   - 按 `s` 排序当前列，按 `f` 过滤进程。
   - 按 `?` 显示帮助菜单。

4. **高级选项**：
   - 指定刷新间隔：`pg_activity --refresh 2`（每 2 秒刷新）。
   - 监控远程服务器：`pg_activity -h remote-host -p 5432`。
   - 配置密码：使用环境变量 `PGPASSWORD` 或 `.pgpass` 文件。

更多详情请参考项目 README。