---
title: indent-blankline.nvim
---

# indent-blankline.nvim

这是一个为 Neovim 添加缩进指南的插件。它使用 Neovim 的虚拟文本功能，不依赖 conceal。

## 功能

- 显示缩进指南，帮助可视化代码结构
- 支持多种样式：简单线条、多彩缩进、背景色高亮
- 集成 scope 高亮（需要 treesitter）
- 支持混合缩进检测
- 可自定义高亮颜色和字符

## 安装

使用插件管理器安装，例如 lazy.nvim：

```lua
{
    "lukas-reineke/indent-blankline.nvim",
    main = "ibl",
    ---@module "ibl"
    ---@type ibl.config
    opts = {},
}
```

或 pckr.nvim：

```lua
use "lukas-reineke/indent-blankline.nvim"
```

## 用法

在 Neovim 配置中调用 setup 函数：

```lua
require("ibl").setup()
```

### 基本配置

```lua
require("ibl").setup({
    indent = { char = "│" },
    scope = { enabled = true }
})
```

### 多彩缩进

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

### 背景色缩进

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

更多配置选项请参考 `:help ibl.config`。
