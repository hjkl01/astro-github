---
title: Neorg
---

# Neorg

> Description from GitHub: Modernity meets insane extensibility. The future of organizing your life in Neovim.

## 功能

- **结构化笔记**：使用 `.norg` 格式进行高效的笔记记录。
- **项目和任务管理**：内置 GTD（Getting Things Done）系统，支持任务跟踪和项目组织。
- **时间跟踪**：记录和分析时间使用情况。
- **幻灯片**：创建和展示幻灯片。
- **写作和排版**：支持类型化文档的写作。
- **可扩展性**：高度可扩展，允许自定义模块和功能。

## 用法

1. **安装**：
   - 确保 Neovim 版本为 0.10 或以上。
   - 使用插件管理器如 `lazy.nvim` 或 `rocks.nvim` 安装 Neorg。
   - 示例配置：
     ```lua
     {
       "nvim-neorg/neorg",
       lazy = false,
       version = "*",
       config = true,
     }
     ```

2. **基本使用**：
   - 创建 `.norg` 文件开始笔记。
   - 使用 Neorg 命令进行任务管理、时间跟踪等。
   - 参考 [官方教程](https://www.youtube.com/watch?v=NnmRVY22Lq8) 或 [Wiki](https://github.com/nvim-neorg/neorg/wiki) 学习更多用法。

3. **检查健康**：安装后运行 `:checkhealth neorg` 确保配置正确。

注意：Neorg 仍在快速发展中，可能有破坏性更改，建议固定版本使用。
