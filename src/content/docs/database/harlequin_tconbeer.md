
---
title: harlequin
---

# Harlequin 项目概述

**GitHub 项目地址**: [https://github.com/tconbeer/harlequin](https://github.com/tconbeer/harlequin)

## 主要特性
Harlequin 是一个开源的 SQL 客户端工具，专为数据工程师和分析师设计。它提供了一个现代化的图形界面，支持多种数据库连接，并强调易用性和可扩展性。主要特性包括：
- **多数据库支持**：兼容 SQLite、DuckDB、PostgreSQL、MySQL 等流行数据库引擎。
- **查询编辑器**：内置语法高亮、自动补全和错误检查的功能，帮助用户高效编写 SQL 查询。
- **结果可视化**：支持表格视图、图表渲染（如柱状图、折线图）和数据导出（CSV、JSON 等格式）。
- **插件系统**：允许用户扩展功能，例如添加自定义数据源或可视化组件。
- **跨平台兼容**：基于 Python 和 Tauri 构建，支持 Windows、macOS 和 Linux 系统。
- **轻量级设计**：无需复杂安装，资源占用低，适合本地开发和快速原型。

## 主要功能
- **数据库连接管理**：轻松配置和切换多个数据源，支持连接字符串或配置文件。
- **SQL 执行与调试**：实时执行查询、查看执行计划，并提供查询历史记录。
- **数据探索**：内置 schema 浏览器，允许用户浏览表结构、列信息和样本数据。
- **协作与分享**：支持查询保存、导出报告，以及通过 Web 界面分享结果。
- **自定义主题**：可调整 UI 主题、字体和布局，以适应个人偏好。
- **集成工具**：与 Jupyter Notebook、VS Code 等开发环境集成，便于数据工作流。

## 用法指南
1. **安装**：
   - 通过 pip 安装：`pip install harlequin`
   - 或从 GitHub Releases 下载预构建二进制文件。

2. **启动**：
   - 命令行运行：`harlequin`
   - 这将打开图形界面。

3. **连接数据库**：
   - 在界面中点击“New Connection”，输入数据库 URI（如 `sqlite:///path/to/db.sqlite`）或选择连接类型并填写凭证。
   - 测试连接后保存。

4. **编写和执行查询**：
   - 在查询编辑器中输入 SQL 语句。
   - 点击“Run”执行，查看结果在下方面板。
   - 使用快捷键（如 Ctrl+Enter）加速操作。

5. **高级用法**：
   - 安装插件：运行 `harlequin --install-plugin <plugin-name>`。
   - 导出数据：执行查询后，选择“Export”选项。
   - 配置：编辑 `~/.harlequin/config.toml` 文件自定义设置。

更多细节请参考项目 README 和文档。