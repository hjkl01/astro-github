
---
title: lualine.nvim
---

# lualine.nvim

> GitHub 项目地址: <https://github.com/nvim-lualine/lualine.nvim>

## 简介

`lualine.nvim` 是一款基于 Lua 的 Neovim 状态栏插件，旨在提供高性能、可定制化且易于使用的状态栏。它利用 Neovim 的 `statusline` API，支持多种主题、模式、插件扩展以及完整的 Lua 配置。

## 主要特性

| 特性 | 说明 |
|------|------|
| **高性能** | 纯 Lua 实现，渲染速度快，几乎无卡顿。 |
| **可定制化** | 通过 `sections`、`inactive_sections`、`component_separators`、`section_separators` 等选项自由配置状态栏布局。 |
| **主题支持** | 内置多款主题（如 `gruvbox`, `tokyonight`, `dracula` 等），也可自定义主题。 |
| **插件集成** | 自动识别并展示常用插件状态（如 `git`, `filetype`, `diagnostics`, `lsp` 等）。 |
| **多模式** | 支持普通模式、插入模式、可视模式、命令模式等不同显示方式。 |
| **扩展点** | 通过 `lualine.setup` 注册自定义组件，支持动态信息（如进度、时间、电量）。 |
| **跨平台** | 兼容 Windows、Linux、macOS。 |
| **Responsive** | 自动根据窗口宽度调整显示内容，避免溢出。 |

## 基本用法

1. **安装**（使用 `packer.nvim` 为例）  

   ```lua
   use {
     'nvim-lualine/lualine.nvim',
     requires = { 'kyazdani42/nvim-web-devicons', opt = true } -- 可选的图标插件
   }
   ```

2. **配置**（简称 `setup`）  

   ```lua
   require('lualine').setup {
     options = {
       icons_enabled = true,
       theme = 'gruvbox',          -- 主题
       component_separators = '|',
       section_separators = '',
       disabled_filetypes = {}
     },
     sections = {
       lualine_a = {'mode'},
       lualine_b = {'branch', 'diff', 'diagnostics'},
       lualine_c = {'filename'},
       lualine_x = {'encoding', 'fileformat', 'filetype'},
       lualine_y = {'progress'},
       lualine_z = {'location'}
     },
     inactive_sections = {
       lualine_a = {},
       lualine_b = {},
       lualine_c = {'filename'},
       lualine_x = {'location'},
       lualine_y = {},
       lualine_z = {}
     },
     tabline = {},
     extensions = {}
   }
   ```

3. **自定义主题**（示例）  

   ```lua
   local custom_theme = {
     normal = { c = '#1c1f26' },  -- 背景色
     insert = { c = '#5c6370' },
     visual = { c = '#e06c75' },
     command = { c = '#98c379' },
     replace = { c = '#c678dd' },
     inactive = { c = '#3e4452' }
   }

   require('lualine').setup {
     options = { theme = custom_theme, ... }
   }
   ```

4. **添加自定义组件**（示例：显示当前时间）  

   ```lua
   local function clock()
     return os.date('%H:%M:%S')
   end

   require('lualine').setup {
     sections = {
       lualine_a = {'mode'},
       lualine_b = {'branch'},
       lualine_c = {'filename'},
       lualine_x = {'encoding', 'fileformat', 'filetype', clock},
       lualine_y = {'progress'},
       lualine_z = {'location'}
     }
   }
   ```

## 常用命令

| 命令 | 作用 |
|------|------|
| `:LualineRefresh` | 刷新状态栏，手动触发更新 |
| `:LualineEnable` | 启用状态栏（在 `lualine.nvim` 被禁用后） |
| `:LualineDisable` | 禁用状态栏 |

## 参考文档

- 官方 GitHub 仓库: <https://github.com/nvim-lualine/lualine.nvim>
- 详细配置示例: `lua/user/lualine.lua`（可根据项目自行创建）

---