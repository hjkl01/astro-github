
---
title: sqlite-web
---

# sqlite-web 项目

**GitHub 项目地址:** [https://github.com/coleifer/sqlite-web](https://github.com/coleifer/sqlite-web)

## 主要特性
sqlite-web 是一个简单易用的 Web 界面工具，用于管理和操作 SQLite 数据库。它基于 Python 开发，提供了一个零配置的 Web 应用，允许用户通过浏览器直接访问和编辑 SQLite 文件。主要特性包括：
- **零配置启动**：无需复杂设置，直接运行即可访问 Web 界面。
- **数据库浏览**：可视化显示数据库表、视图和索引，支持排序、过滤和分页。
- **SQL 查询执行**：内置 SQL 编辑器，支持执行任意 SQL 语句，并显示结果。
- **数据编辑**：支持直接在 Web 界面中插入、更新和删除数据库记录。
- **导出功能**：可以将查询结果导出为 CSV 或 JSON 格式。
- **安全性**：可选的密码保护和只读模式，支持多用户访问控制。
- **轻量级**：体积小巧，适合开发、测试和小型生产环境。

## 主要功能
- **数据库管理**：上传或指定 SQLite 文件路径，实时浏览 schema 和数据。
- **查询与分析**：执行 SELECT、INSERT、UPDATE、DELETE 等 SQL 操作，支持语法高亮和错误提示。
- **文件操作**：创建新数据库、备份现有文件，或从文件加载数据库。
- **自定义配置**：通过命令行参数或配置文件调整端口、主题和访问权限。
- **集成友好**：可作为独立应用运行，或嵌入 Flask 项目中扩展功能。

## 用法
1. **安装**：
   - 确保安装 Python 3.x 和 pip。
   - 运行 `pip install sqlite-web` 安装包。

2. **运行应用**：
   - 基本启动：`sqlite-web /path/to/your/database.db`（替换为你的 SQLite 文件路径）。
   - 指定端口：`sqlite-web -p 8080 /path/to/database.db`（默认端口为 5000）。
   - 只读模式：`sqlite-web --readonly /path/to/database.db`。
   - 带密码保护：`sqlite-web --password yourpassword /path/to/database.db`。

3. **访问界面**：
   - 在浏览器中打开 `http://localhost:5000`（或指定的端口）。
   - 如果未指定数据库文件，可在界面中上传或创建新文件。

4. **高级用法**：
   - 作为模块导入：在 Python 脚本中使用 `from sqlite_web import main; main()` 启动。
   - 配置选项：运行 `sqlite-web --help` 查看所有命令行参数，如主题（--theme dark）和最大行数限制（--maxrows 1000）。
   - 示例：处理多个数据库时，可通过 Web 界面切换文件。

此工具特别适合开发者快速原型设计、数据调试或教学演示，无需安装完整的数据库管理软件如 SQLite Browser。