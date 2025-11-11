---
title: kanagawa.nvim
---

## 功能介绍

kanagawa.nvim 是一个为 NeoVim 设计的暗色主题，灵感来源于葛饰北斋的著名画作《神奈川冲浪里》。该主题提供丰富的颜色调色板和语义化色彩设计，支持 TreeSitter 语法高亮，并兼容众多流行插件。主题支持编译为 Lua 字节码，以实现超快的启动时间。

### 主要特性

- **广泛支持**：全面支持 TreeSitter 语法高亮和许多流行插件。
- **高性能**：可编译为 Lua 字节码，显著提升启动速度。
- **多主题变体**：提供三种主题：`wave`（默认，温暖主题）、`dragon`（适合深夜使用）和 `lotus`（适合户外使用）。
- **高度可定制**：允许修改调色板颜色、主题颜色和覆盖高亮组。
- **无障碍友好**：颜色对比度符合 WCAG 2.1 AA 标准。
- **终端集成**：支持多种终端的主题配置。

## 用法

### 安装

使用你喜欢的包管理器安装：

```lua
use "rebelot/kanagawa.nvim"
```

### 要求

- 最新版本的 NeoVim
- 支持真彩色的终端
- 可选：支持 undercurl 的终端

### 基本使用

在你的 `init.lua` 或 `init.vim` 中设置主题：

```lua
vim.cmd("colorscheme kanagawa")
```

或在 Lua 中：

```lua
require('kanagawa').setup()
vim.cmd("colorscheme kanagawa")
```

### 配置

你可以自定义主题设置：

```lua
require('kanagawa').setup({
    compile = false,             -- 启用编译以提升性能
    undercurl = true,            -- 启用 undercurl
    commentStyle = { italic = true },
    functionStyle = {},
    keywordStyle = { italic = true },
    statementStyle = { bold = true },
    typeStyle = {},
    transparent = false,         -- 不设置背景色
    dimInactive = false,         -- 淡化非活动窗口
    terminalColors = true,       -- 定义终端颜色
    colors = {                   -- 修改主题和调色板颜色
        palette = {},
        theme = { wave = {}, lotus = {}, dragon = {}, all = {} },
    },
    overrides = function(colors) -- 添加/修改高亮
        return {}
    end,
    theme = "wave",              -- 加载 "wave" 主题
    background = {               -- 根据 'background' 选项映射主题
        dark = "wave",
        light = "lotus"
    },
})
```

### 切换主题

- 设置 `config.theme` 为所需主题。
- 更改 `vim.o.background` 值以选择映射的主题。
- 直接加载特定主题：

```lua
vim.cmd("colorscheme kanagawa-wave")
vim.cmd("colorscheme kanagawa-dragon")
vim.cmd("colorscheme kanagawa-lotus")
```

或使用 Lua：

```lua
require("kanagawa").load("wave")
```

### 自定义

修改调色板和主题颜色：

```lua
require('kanagawa').setup({
    colors = {
        palette = {
            sumiInk0 = "#000000",
            fujiWhite = "#FFFFFF",
        },
        theme = {
            wave = {
                ui = {
                    float = {
                        bg = "none",
                    },
                },
            },
            all = {
                ui = {
                    bg_gutter = "none"
                }
            }
        }
    },
    overrides = function(colors)
        return {
            String = { fg = colors.palette.carpYellow, italic = true },
            SomePluginHl = { fg = colors.theme.syn.type, bold = true },
        }
    end,
})
```

### 集成

获取当前主题的颜色：

```lua
local colors = require("kanagawa.colors").setup()
local palette_colors = colors.palette
local theme_colors = colors.theme
```

终端集成示例（Kitty）：

```lua
vim.api.nvim_create_autocmd("ColorScheme", {
    pattern = "kanagawa",
    callback = function()
        if vim.o.background == "light" then
            vim.fn.system("kitty +kitten themes Kanagawa_light")
        elseif vim.o.background == "dark" then
            vim.fn.system("kitty +kitten themes Kanagawa_dragon")
        else
            vim.fn.system("kitty +kitten themes Kanagawa")
        end
    end,
})
```

### 额外资源

该项目还提供为其他工具（如 Alacritty、Kitty、WezTerm 等）的主题配置，以及一个 Python 脚本用于从图像提取颜色调色板。
