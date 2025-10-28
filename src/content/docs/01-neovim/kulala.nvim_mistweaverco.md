
---
title: kulala.nvim
---


# kulala.nvim (mistweaverco)

**项目地址**: https://github.com/mistweaverco/kulala.nvim

## 主要特性

- **自定义快捷键**：支持多种自定义快捷键配置，提升工作效率。
- **多语言支持**：内置对多种编程语言的语法和提示支持。
- **插件互操作**：可与其他 Neovim 插件无缝协作，扩展功能。
- **可视化界面**：提供直观的可视化界面，方便快速定位问题。
- **插件化设计**：模块化插件结构，易于维护和扩展。

## 功能概览

| 功能 | 描述 |
|------|------|
| 快捷键映射 | `:KulalaMap` 命令可自定义快捷键 |
| 代码补全 | 支持 LSP 和自定义补全源 |
| 语法高亮 | 自动识别并高亮多种语言 |
| 代码片段 | 提供常用代码片段管理 |
| 视图切换 | `:KulalaToggleView` 轻松切换视图模式 |

## 用法

1. **安装**  
   ```vim
   Plug 'mistweaverco/kulala.nvim'
   ```
2. **配置**  
   ```lua
   require('kulala').setup({
     keymap = {
       toggle = "<leader>k",
       next   = "<leader>k>",
       prev   = "<leader>k<",
     },
     languages = { "lua", "python", "javascript" },
   })
   ```
3. **使用**  
   - `:KulalaToggleView`：切换视图  
   - `:KulalaNext`、`:KulalaPrev`：切换到下一个/上一个项目  
   - `:KulalaMap <key> <action>`：自定义快捷键

> 详细信息请参阅官方文档或使用 `:help kulala.nvim` 获取帮助。