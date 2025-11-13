---
title: kanagawa.nvim
---

## 功能介绍

kanagawa.nvim 是一个受葛饰北斋著名画作色彩启发的 NeoVim 深色配色方案。它提供了丰富的 TreeSitter 语法高亮支持，并兼容众多流行插件。该配色方案通过编译为 Lua 字节码，实现超快的启动时间。

主要特性：

- 广泛支持 TreeSitter 语法高亮和流行插件
- 编译为 Lua 字节码以提升启动速度
- 提供三种主题变体：wave（默认）、dragon 和 lotus
- 高度可定制，包括颜色调色板和主题颜色
- 符合 WCAG 2.1 Level AA 对比度标准

## 用法

### 安装

使用你喜欢的包管理器下载：

```lua
use "rebelot/kanagawa.nvim"
```

### 要求

- 最新版本的 Neovim
- 支持真彩色的终端
- 可选：支持下划线终端

### 基本使用

设置配色方案：

```vim
colorscheme kanagawa
```

或在 Lua 中：

```lua
vim.cmd("colorscheme kanagawa")
```

### 配置

无需调用 setup 即可使用默认设置。以下是默认配置选项：

```lua
require('kanagawa').setup({
    compile = false,             -- 启用配色方案编译
    undercurl = true,            -- 启用下划线
    commentStyle = { italic = true },
    functionStyle = {},
    keywordStyle = { italic = true },
    statementStyle = { bold = true },
    typeStyle = {},
    transparent = false,         -- 不设置背景色
    dimInactive = false,         -- 调暗非活动窗口
    terminalColors = true,       -- 定义 vim.g.terminal_color_{0,17}
    colors = {                   -- 添加/修改主题和调色板颜色
        palette = {},
        theme = { wave = {}, lotus = {}, dragon = {}, all = {} },
    },
    overrides = function(colors) -- 添加/修改高亮
        return {}
    end,
    theme = "wave",              -- 加载 "wave" 主题
    background = {               -- 将 'background' 选项的值映射到主题
        dark = "wave",           -- 尝试 "dragon"！
        light = "lotus"
    },
})
```

注意：如果启用编译，确保在更改配置后运行 `:KanagawaCompile` 命令。

### 主题切换

可以通过以下方式更改主题：

- 设置 `config.theme` 为所需主题
- 使用 `background` 选项：更改 `vim.o.background` 的值将选择映射的主题
- 直接加载配色方案：

```lua
vim.cmd("colorscheme kanagawa-wave")
vim.cmd("colorscheme kanagawa-dragon")
vim.cmd("colorscheme kanagawa-lotus")
```

或

```lua
require("kanagawa").load("wave")
```

### 自定义

可以通过 `config.colors` 修改调色板和主题颜色，通过 `config.overrides` 添加/修改高亮组。

### 集成

支持终端集成，如 Kitty 等。还提供获取调色板和主题颜色的 API。
