---
title: copilot.lua
---

# copilot.lua_zbirenbaum

## 项目描述

copilot.lua 是 GitHub Copilot 的纯 Lua 替代插件，专为 Neovim 设计。它提供了与 GitHub Copilot 交互的完整 API，支持代码自动补全和建议功能。

## 主要功能

- **面板建议**：在分割窗口中预览建议，支持跳转和接受。
- **自动触发建议**：进入插入模式时自动显示建议。
- **NES (Next Edit Suggestion)**：基于下一编辑的实验性建议功能。
- **文件类型支持**：可配置特定文件类型的支持。
- **API 集成**：提供模块用于与其他插件集成，如 nvim-cmp。

## 安装

使用插件管理器安装，例如 packer.nvim：

```lua
use {
  "zbirenbaum/copilot.lua",
  requires = {
    "copilotlsp-nvim/copilot-lsp", -- 可选，用于 NES 功能
  },
}
```

## 配置

在配置中调用 setup 函数：

```lua
require("copilot").setup({
  panel = {
    enabled = true,
    auto_refresh = false,
    keymap = {
      accept = "<CR>",
      jump_next = "]]",
      jump_prev = "[[",
    },
  },
  suggestion = {
    enabled = true,
    auto_trigger = false,
    keymap = {
      accept = "<M-l>",
      next = "<M-]>",
      prev = "<M-[>",
    },
  },
  -- 其他选项...
})
```

## 用法

- **认证**：运行 `:Copilot auth` 进行认证。
- **面板**：`:Copilot panel` 打开建议面板。
- **建议**：在插入模式中使用配置的键映射接受或导航建议。
- **命令**：使用 `:Copilot` 命令执行各种操作，如 `:Copilot suggestion accept`。

更多详情请参考 [GitHub 仓库](https://github.com/zbirenbaum/copilot.lua)。
