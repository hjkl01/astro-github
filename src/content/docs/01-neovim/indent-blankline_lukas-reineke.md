---
title: indent-blankline.nvim
---

## 功能介绍

indent-blankline.nvim 是一个 Neovim 插件，用于在代码中添加缩进指南。它使用 Neovim 的虚拟文本功能，不依赖 conceal，提供清晰的缩进可视化。

主要功能：

- 显示缩进空白线，帮助识别代码块结构
- 支持作用域高亮（需要 treesitter）
- 支持混合缩进检测
- 可自定义颜色和字符
- 与其他插件如 rainbow-delimiters.nvim 集成

## 用法

### 安装

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

### 基本设置

在 init.lua 或插件配置文件中添加：

```lua
require("ibl").setup()
```

### 高级配置

#### 多彩缩进

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

#### 作用域高亮

```lua
require("ibl").setup()
```

需要 treesitter 支持，用于显示变量和函数的作用域范围。

更多配置选项请参考 `:help ibl.config`。
