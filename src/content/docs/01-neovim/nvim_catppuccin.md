---
title: nvim
---

# nvim_catppuccin

## 项目简介

[nvim_catppuccin](https://github.com/catppuccin/nvim) 是一个为 (Neo)Vim 设计的舒缓柔和的颜色主题。它是 Catppuccin 主题系列的一部分，提供多种柔和的色彩方案，帮助用户在编程时获得更好的视觉体验。

## 主要功能

- **多种色彩方案**：提供 4 种不同的色彩风格（flavours）：
  - 🌻 Latte：浅色主题
  - 🪴 Frappé：中性主题
  - 🌺 Macchiato：温暖主题
  - 🌿 Mocha：深色主题

- **高度可配置**：支持自定义颜色、样式、透明背景等
- **插件集成**：支持众多 Neovim 插件的主题集成，如 LSP、Treesitter、GitSigns 等
- **编译优化**：支持预编译配置以提升启动速度
- **兼容性**：支持 Neovim >= 0.8 和 Vim >= 9（需编译支持 Lua）

## 安装方法

### 使用 lazy.nvim

```lua
{
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000
}
```

### 使用 packer.nvim

```lua
use { "catppuccin/nvim", as = "catppuccin" }
```

### 使用 vim-plug

```vim
Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
```

## 基本用法

1. **设置颜色主题**：

   ```vim
   colorscheme catppuccin
   ```

   或在 Lua 中：

   ```lua
   vim.cmd.colorscheme "catppuccin"
   ```

2. **选择特定风格**：
   ```vim
   colorscheme catppuccin-latte
   colorscheme catppuccin-frappe
   colorscheme catppuccin-macchiato
   colorscheme catppuccin-mocha
   ```

## 配置示例

```lua
require("catppuccin").setup({
    flavour = "auto", -- latte, frappe, macchiato, mocha
    background = {
        light = "latte",
        dark = "mocha",
    },
    transparent_background = false,
    show_end_of_buffer = false,
    term_colors = false,
    dim_inactive = {
        enabled = false,
        shade = "dark",
        percentage = 0.15,
    },
    no_italic = false,
    no_bold = false,
    no_underline = false,
    styles = {
        comments = { "italic" },
        conditionals = { "italic" },
        loops = {},
        functions = {},
        keywords = {},
        strings = {},
        variables = {},
        numbers = {},
        booleans = {},
        properties = {},
        types = {},
        operators = {},
    },
    color_overrides = {},
    custom_highlights = {},
    default_integrations = true,
    integrations = {
        cmp = true,
        gitsigns = true,
        nvimtree = true,
        telescope = true,
        treesitter = true,
        -- 更多插件集成...
    },
})

vim.cmd.colorscheme "catppuccin"
```

## 自定义选项

### 获取颜色调色板

```lua
local colors = require("catppuccin.palettes").get_palette "mocha"
```

### 覆盖颜色

```lua
require("catppuccin").setup {
    color_overrides = {
        all = {
            text = "#ffffff",
        },
        latte = {
            base = "#ff0000",
        },
    }
}
```

### 自定义高亮组

```lua
require("catppuccin").setup {
    custom_highlights = function(colors)
        return {
            Comment = { fg = colors.flamingo },
            TabLineSel = { bg = colors.pink },
        }
    end
}
```

## 支持的插件集成

该主题支持大量 Neovim 插件的集成，包括但不限于：

- aerial.nvim
- alpha-nvim
- barbar.nvim
- bufferline.nvim
- cmp
- dashboard-nvim
- diffview.nvim
- feline.nvim
- gitsigns.nvim
- indent-blankline.nvim
- lualine.nvim
- mason.nvim
- mini.nvim
- neo-tree.nvim
- neogit
- nvim-dap
- nvim-notify
- nvim-tree.lua
- telescope.nvim
- treesitter
- which-key.nvim

## 注意事项

- 需要终端支持真彩色（true color）
- 对于 tmux 用户，需要启用真彩色支持
- 建议禁用 `additional_vim_regex_highlighting` 以获得最佳 Treesitter 高亮效果
