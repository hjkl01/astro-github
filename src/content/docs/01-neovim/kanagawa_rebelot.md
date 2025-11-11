---
title: kanagawa.nvim
---

## 功能介绍

kanagawa.nvim 是一个为 Neovim 设计的暗色主题，灵感来源于葛饰北斋（Katsushika Hokusai）的著名画作。该主题提供了三种变体：wave（默认的温暖主题）、dragon（适合深夜编程）和 lotus（适合户外环境）。

### 主要特性

- **广泛的语法高亮支持**：支持 TreeSitter 语法高亮，以及许多流行插件
- **快速启动**：支持编译为 Lua 字节码，实现超快的启动时间
- **可定制性**：允许自定义调色板和主题颜色
- **无障碍设计**：颜色对比度符合 WCAG 2.1 Level AA 标准
- **终端集成**：支持多种终端的颜色配置

## 用法

### 安装

使用你喜欢的包管理器安装：

```lua
-- lazy.nvim
{
  "rebelot/kanagawa.nvim",
  lazy = false,
  priority = 1000,
  opts = {},
}
```

### 基本配置

在你的 Neovim 配置中添加：

```lua
-- 默认配置
require('kanagawa').setup({
    compile = false,             -- 启用编译以加快启动速度
    undercurl = true,            -- 启用下划线
    commentStyle = { italic = true },
    functionStyle = {},
    keywordStyle = { italic = true },
    statementStyle = { bold = true },
    typeStyle = {},
    transparent = false,         -- 不设置背景色
    dimInactive = false,         -- 淡化非活动窗口
    terminalColors = true,       -- 定义终端颜色
    colors = {                   -- 添加/修改主题和调色板颜色
        palette = {},
        theme = { wave = {}, lotus = {}, dragon = {}, all = {} },
    },
    overrides = function(colors) -- 添加/修改高亮组
        return {}
    end,
    theme = "wave",              -- 加载 "wave" 主题
    background = {               -- 将 'background' 选项映射到主题
        dark = "wave",
        light = "lotus"
    },
})

-- 设置主题
vim.cmd("colorscheme kanagawa")
```

### 主题切换

可以通过以下方式切换主题：

- 设置 `config.theme` 为所需主题
- 更改 `vim.o.background` 的值
- 直接加载特定主题：

```lua
vim.cmd("colorscheme kanagawa-wave")
vim.cmd("colorscheme kanagawa-dragon")
vim.cmd("colorscheme kanagawa-lotus")
```

### 自定义

可以通过 `colors` 和 `overrides` 选项进行自定义：

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
            NormalFloat = { bg = "none" },
            FloatBorder = { bg = "none" },
        }
    end,
})
```

### 编译优化

启用编译以加快启动速度：

```lua
require('kanagawa').setup({
    compile = true,
})
```

修改配置后，运行 `:KanagawaCompile` 命令。

## 要求

- Neovim 最新版本
- 支持真彩色的终端
- 可选：支持下划线的终端
