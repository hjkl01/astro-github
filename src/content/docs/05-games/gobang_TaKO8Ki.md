---
title: gobang
---

# Gobang 项目

## 项目地址

[https://github.com/TaKO8Ki/gobang](https://github.com/TaKO8Ki/gobang)

## 主要特性

- **跨平台支持**：支持 macOS、Windows、Linux。
- **多数据库支持**：支持 MySQL、PostgreSQL、SQLite。
- **直观的键盘控制**：仅使用键盘进行操作，无需鼠标。
- **TUI 界面**：终端用户界面，提供直观的数据库浏览和管理。

## 主要功能

- **数据库连接**：配置并连接到多种数据库。
- **数据浏览**：查看表、记录、列、约束、外键等。
- **查询执行**：支持 SQL 查询（计划中）。
- **键盘导航**：高效的键盘快捷键进行导航和操作。

## 用法

1. **安装**：
   - 使用 Homebrew（Linux、macOS）：`brew install tako8ki/tap/gobang`
   - 使用 Scoop（Windows）：`scoop install gobang`
   - 使用 Cargo：`cargo install gobang`
   - 或从 Releases 下载二进制文件。

2. **运行**：
   - `gobang`

3. **配置**：
   - 编辑配置文件添加数据库连接（位置取决于 OS，如 `~/.config/gobang/config.toml`）。
   - 示例配置：
     ```
     [[conn]]
     type = "mysql"
     host = "localhost"
     user = "root"
     ```

4. **按键映射**：
   - h/j/k/l：滚动
   - Ctrl+u/Ctrl+d：多行滚动
   - g/G：滚动到顶/底
   - 1-5：切换到记录/列/约束/外键/索引标签
   - /：过滤
   - ?：帮助
