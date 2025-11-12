---
title: indent-blankline.nvim
---

## 功能介绍

indent-blankline.nvim 是一个为 Neovim 添加缩进指南的插件。它利用 Neovim 的虚拟文本功能来显示缩进线，而不使用 conceal 特性。该插件可以帮助开发者更好地可视化代码的缩进结构，提高代码可读性。

主要功能包括：

- 显示缩进指南线
- 支持作用域高亮（需要 treesitter）
- 支持混合缩进检测
- 支持多种颜色高亮
- 支持背景色缩进指南
- 与 rainbow-delimiters.nvim 等插件集成

## 用法

### 安装

使用你喜欢的插件管理器安装。

对于 lazy.nvim：

```lua
{
    "lukas-reineke/indent-blankline.nvim",
    main = "ibl",
    ---@module "ibl"
    ---@type ibl.config
    opts = {},
}
```

对于 pckr.nvim：

```lua
use "lukas-reineke/indent-blankline.nvim"
```

### 设置

在你的 Neovim 配置中调用 setup 函数：

```lua
require("ibl").setup()
```

你可以传递配置表来自定义行为。所有可用选项请参考 `:help ibl.config`。

### 示例配置

#### 简单配置

```lua
require("ibl").setup()
```

#### 彩虹缩进

```lua
local highlight = {
    "RainbowRed",
    "RainbowYellow",
    "RainbowBlue",
    "RainbowOrange",
    "RainbowGreen",
    "RainbowViolet",
    "RainbowCyan",
}

local hooks = require "ibl.hooks"
-- 在高亮设置钩子中创建高亮组，以便每次颜色方案改变时重置
hooks.register(hooks.type.HIGHLIGHT_SETUP, function()
    vim.api.nvim_set_hl(0, "RainbowRed", { fg = "#E06C75" })
    vim.api.nvim_set_hl(0, "RainbowYellow", { fg = "#E5C07B" })
    vim.api.nvim_set_hl(0, "RainbowBlue", { fg = "#61AFEF" })
    vim.api.nvim_set_hl(0, "RainbowOrange", { fg = "#D19A66" })
    vim.api.nvim_set_hl(0, "RainbowGreen", { fg = "#98C379" })
    vim.api.nvim_set_hl(0, "RainbowViolet", { fg = "#C678DD" })
    vim.api.nvim_set_hl(0, "RainbowCyan", { fg = "#56B6C2" })
end)

require("ibl").setup { indent = { highlight = highlight } }
```

#### 作用域高亮

```lua
require("ibl").setup()
```

作用域需要 treesitter 设置。作用域不是当前缩进级别，而是变量或函数可访问的缩进级别，取决于编程语言。

#### 背景色缩进指南

```lua
local highlight = {
    "CursorColumn",
    "Whitespace",
}
require("ibl").setup {
    indent = { highlight = highlight, char = "" },
    whitespace = {
        highlight = highlight,
        remove_blankline_trail = false,
    },
    scope = { enabled = false },
}
```

该插件需要 Neovim 的最新稳定版本。
