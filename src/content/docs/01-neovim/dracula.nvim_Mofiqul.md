---
title: dracula.nvim
---

# dracula.nvim

## 功能介绍

dracula.nvim 是为 Neovim 编写的 Dracula 颜色方案，使用 Lua 实现。它提供了经典的 Dracula 主题，支持多种 Neovim 插件和组件，包括 LSP、Treesitter、Telescope、NvimTree、BufferLine、Git Signs、Lualine 等。

主要特性：

- 支持 Neovim >= 0.9.2
- 可选 Treesitter 支持
- 透明背景选项
- 自定义颜色调色板
- 支持多种插件的高亮

## 用法

### 安装

使用包管理器安装：

```lua
-- Packer
use 'Mofiqul/dracula.nvim'

-- Vim-Plug
Plug 'Mofiqul/dracula.nvim'
```

### 基本使用

```lua
-- 设置颜色方案
vim.cmd[[colorscheme dracula]]
-- 或软色版本
vim.cmd[[colorscheme dracula-soft]]
```

### Lualine 集成

```lua
require('lualine').setup {
  options = {
    theme = 'dracula-nvim'
  }
}
```

### LazyVim 配置

```lua
return {
  { "Mofiqul/dracula.nvim" },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "dracula",
    },
  },
}
```

### 高级配置

```lua
local dracula = require("dracula")
dracula.setup({
  colors = {
    bg = "#282A36",
    fg = "#F8F8F2",
    -- 其他颜色自定义
  },
  transparent_bg = true,
  italic_comment = true,
  -- 更多选项...
})
```

### 导入颜色

```lua
local colors = require('dracula').colors()
-- 使用颜色表进行自定义高亮
```
