---
title: noice.nvim
---


# noice.nvim (folke)

> 项目地址: <https://github.com/folke/noice.nvim>

## 主要特性

| 功能 | 描述 |
|------|------|
| **消息过滤** | 自动隐藏不必要的 Neovim 消息，保持终端整洁。 |
| **通知系统** | 统一的弹窗式通知，支持图标、超时、可点击操作。 |
| **命令行 UI** | 对 `:` 命令行进行美化，支持提示、补全、历史记录。 |
| **浮动窗口** | 将 LSP、诊断、搜索结果等信息显示在弹窗中，避免干扰编辑区。 |
| **自定义格式** | 通过 Lua API 可自定义消息、通知、命令行的渲染方式。 |
| **键位映射** | 内置易用的快捷键，快速访问通知、命令行等。 |

## 快速使用

```lua
-- init.lua
require('lazy').setup({
  {
    "folke/noice.nvim",
    event = "VeryLazy",
    dependencies = {
      "MunifTanjim/nui.nvim",
      "rcarriga/nvim-notify",
    },
    opts = {
      -- 默认配置，按需覆盖
      lsp = { override = { ["vim.lsp.util.convert_input_to_markdown_lines"] = true } },
      notify = { level = "INFO" },
    },
  },
})
```

```vim
" 可选的 Vimscript 快捷键
nnoremap <leader>n :Noice<CR>      " 查看通知列表
```

## 配置示例

```lua
require('noice').setup({
  presets = {
    bottom_search = true,   -- 让搜索命令行显示在底部
    command_palette = true, -- 让命令行像调色板一样
    long_message_to_split = true, -- 长消息打开分割窗口
  },
  routes = {
    { view = "notify", filter = { event = "msg_show" } }, -- 将普通消息转为通知
  },
})
```

> 以上即为 `noice.nvim` 的核心功能与基本使用方式。详细配置请参见官方仓库文档。