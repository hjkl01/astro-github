
---
title: nvim
---

# catppuccin.nvim

[GitHub 项目](https://github.com/catppuccin/nvim)

## 项目简介
catppuccin.nvim 是一款为 Neovim 开源的多主题色彩方案，基于 Catppuccin 主题提供柔和、统一的配色。该插件支持多种 Neovim 插件（譬如 Lualine、Telescope、Treesitter、NvimTree、Bufferline、Which-Key、Comment.nvim 等）的无缝配色兼容。

## 主要特性

- **多主题支持**  
  提供 `latte`、`frappe`、`macchiato` 与 `mocha` 四种不同的配色方案，支持主题切换。

- **全栈兼容**  
  与绝大部分流行插件无缝配合：Neovim API、Telescope、Lualine、Treesitter、Rust Analyzer、Gitsigns、NvimTree、Bufferline、Which-Key、Comment.nvim 等。

- **透明背景**  
  可轻松开启透明背景：`vim.g.catppuccin_transparent_background = true`。

- **插件自动提取配色**  
  通过 `catppuccin.setup` 可自动识别插件并应用相应主题颜色。

- **高亮专案**  
  对 LSP、Diagnostics、Search(`Ctrl+F`)、Git 状态等进行细致高亮配置。

- **可定制**  
  可通过 `catppuccin.init_vars` 进行自定义颜色、透明度、插件高亮等。

## 安装方式

```lua
-- packer.nvim
use {
  "catppuccin/nvim",
  as = "catppuccin",
  config = function()
    vim.cmd [[colorscheme catppuccin]]
  end
}
```

## 基础配置

```lua
require("catppuccin").setup {
  flavour = "mocha", -- latte | frappe | macchiato | mocha
  background = {
    light = "latte",
    dark = "mocha",
  },
  transparent_background = true,
  term_colors = true,
  dim_inactive = false,
  styles = {
    comments = {italic = true},
    conditionals = {italic = true},
    loops = {},
    functions = {italic = true},
    keywords = {},
    strings = {},
    variables = {},
    numbers = {},
    booleans = {},
    properties = {},
    types = {italic = true},
    operators = {},
  },
  custom_highlights = {},
  plugins = {
    treesitter = true,
    cmp = true,
    lsp_trouble = true,
    which_key = true,
    notify = true,
    telescope = true,
    mini = true,
    asea = true,
    native_lsp = true,
    native_lsp_cmp = true,
    cmp_lspkind = true,
    lualine = false,
  },
}
```

## 自动化插件配色

```lua
local catppuccin = require("catppuccin")
catppuccin.init_variables()
```

## 切换主题

```vim
:Cats
```

或在 Lua 中：

```lua
vim.cmd [[colorscheme catppuccin]]
```

## 常见插件集成示例

- **Lualine**

```lua
require('lualine').setup {
  options = { theme = 'catppuccin' }
}
```

- **Telescope**

```lua
require('telescope').setup {
  defaults = { mappings = { n = { ['q'] = require('telescope.actions').close } } }
}
```

- **Treesitter**

```vim
set ts=17
# 安装树状解析器
nvim-tree.lua
```

## 文档与源码

- 官方文档：https://github.com/catppuccin/nvim  
- 源码：https://github.com/catppuccin/nvim

---  
请将以上内容保存至 `src/docs/00/nvim_catppuccin.md`。