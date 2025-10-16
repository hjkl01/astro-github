
---
title: which-key.nvim
---

# which-key.nvim

**GitHub 项目地址:** [https://github.com/folke/which-key.nvim](https://github.com/folke/which-key.nvim)

## 主要特性
which-key.nvim 是一个 Neovim 插件，灵感来源于 Emacs 的 which-key 包。它旨在帮助用户快速发现和学习键绑定，提供一个交互式的前缀键提示界面。主要特性包括：
- **智能键绑定提示**：当用户输入前缀键（如 leader 键）后，自动弹出浮动窗口显示所有可用的后续键绑定。
- **延迟触发**：支持配置延迟时间，避免频繁弹出干扰正常输入。
- **自定义分组**：键绑定可以按组分类显示，支持图标和描述文本，提升视觉体验。
- **集成支持**：兼容 Telescope、LSP 等插件，提供搜索和过滤功能。
- **性能优化**：使用 Lua 实现，轻量高效，不依赖外部依赖。
- **可扩展性**：允许用户注册自定义键绑定和事件钩子。

## 主要功能
- **前缀键可视化**：显示当前前缀下所有子命令，帮助新手快速上手 Neovim 的复杂键绑定。
- **自动注册**：插件会自动检测并注册已安装插件的键绑定，无需手动配置。
- **搜索与过滤**：在弹出窗口中支持实时搜索键绑定，提高导航效率。
- **模式支持**：适用于 normal、visual 等多种 Vim 模式。
- **主题集成**：无缝集成 Neovim 的颜色方案，支持暗黑模式等。
- **事件驱动**：支持在特定事件（如插件加载）时动态更新键绑定提示。

## 用法
### 安装
使用插件管理器安装，例如 packer.nvim：
```lua
use {
  "folke/which-key.nvim",
  config = function()
    require("which-key").setup {}
  end
}
```

### 基本配置
在 Neovim 配置中（init.lua）添加：
```lua
require("which-key").setup {
  -- 延迟时间（毫秒）
  delay = 300,
  -- 自定义图标
  icons = {
    breadcrumb = "»", -- 面包屑分隔符
    separator = "➜", -- 子菜单分隔符
    group = "+", -- 组前缀
  },
  -- 窗口选项
  window = {
    border = "single", -- 窗口边框
    position = "bottom", -- 位置：top, bottom, left, right
  },
}
```

### 手动注册键绑定
```lua
local wk = require("which-key")
wk.register({
  ["<leader>"] = {
    f = { "<cmd>Telescope find_files<cr>", "Find Files" }, -- 键绑定和描述
    b = { "<cmd>Telescope buffers<cr>", "Buffers" },
    g = {
      name = "Git", -- 分组名称
      s = { "<cmd>Git status<cr>", "Status" },
      b = { "<cmd>Git blame<cr>", "Blame" },
    },
  },
}, { prefix = "<leader>" }) -- 指定前缀
```

### 使用示例
1. 启动 Neovim，按下 leader 键（默认 `<Space>`），插件会弹出窗口显示所有 leader 开头的绑定。
2. 输入部分键序列（如 `<leader>f`），窗口会过滤并显示匹配项。
3. 支持缩写和别名，帮助记忆复杂命令。

更多高级用法请参考项目 README。