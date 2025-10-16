
---
title: sqlectron-gui
---

# Sqlectron GUI 项目

## 项目地址
[https://github.com/sqlectron/sqlectron-gui](https://github.com/sqlectron/sqlectron-gui)

## 主要特性
Sqlectron GUI 是一个开源的桌面图形用户界面（GUI）工具，专为数据库管理设计。它基于 Electron 框架构建，支持多种流行数据库，提供直观的界面来简化数据库操作。主要特性包括：
- **多数据库支持**：兼容 PostgreSQL、MySQL、SQLite、Microsoft SQL Server 和 MariaDB 等数据库。
- **查询编辑器**：内置 SQL 查询编辑器，支持语法高亮、自动补全和实时执行。
- **数据可视化**：以表格、树状或图表形式显示查询结果，便于数据浏览和分析。
- **连接管理**：轻松添加、编辑和保存数据库连接，支持环境变量和加密存储凭据。
- **跨平台兼容**：可在 Windows、macOS 和 Linux 上运行，无需额外配置。
- **扩展性**：支持插件系统，允许用户自定义功能。
- **轻量级设计**：界面简洁，资源占用低，适合开发者和数据库管理员使用。

## 功能
- **数据库连接**：通过图形界面配置连接参数，包括主机、端口、用户名、密码和数据库名称。支持 SSL 和 SSH 隧道。
- **SQL 操作**：编写和执行 SELECT、INSERT、UPDATE、DELETE 等 SQL 语句，支持多标签页管理查询。
- **数据导出/导入**：将查询结果导出为 CSV、JSON 或 SQL 文件；支持从文件导入数据。
- **架构浏览**：查看数据库 schema、表结构、索引和外键关系。
- **查询历史**：记录和重用之前的 SQL 查询。
- **主题与自定义**：支持浅色/深色主题，并允许调整字体和布局。
- **错误处理**：提供详细的错误消息和调试工具，帮助诊断连接或查询问题。

## 用法
1. **安装**：
   - 从 GitHub Releases 页面下载适用于您操作系统的安装包（.exe、.dmg 或 .deb）。
   - 或者，使用包管理器安装：如在 macOS 上通过 Homebrew `brew install --cask sqlectron`；在 Windows 上通过 Chocolatey `choco install sqlectron`。

2. **启动和连接数据库**：
   - 打开 Sqlectron GUI 应用。
   - 点击“Connections”菜单，选择“New Connection”。
   - 选择数据库类型（如 PostgreSQL），输入连接细节（主机、端口等），然后测试连接。
   - 保存连接后，双击列表中的连接项打开。

3. **执行查询**：
   - 在查询编辑器中输入 SQL 语句。
   - 点击“Execute”按钮运行查询，结果将显示在下方面板。
   - 使用工具栏按钮导出结果或保存查询。

4. **高级用法**：
   - 对于 SQLite 文件，直接选择“SQLite”类型并浏览本地文件。
   - 使用“Schema”标签浏览数据库结构。
   - 若需自定义，编辑 `~/.sqlectron/config.json` 文件或安装插件。

项目活跃维护，适合日常数据库开发和测试。更多详情请查看 GitHub 仓库的 README。