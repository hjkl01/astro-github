---
title: todo-comments.nvim
---

## 简介

todo-comments.nvim 是一个用于 Neovim >= 0.8.0 的 Lua 插件，用于高亮、列出和搜索代码库中的 TODO 注释，如 `TODO`、`HACK`、`BUG` 等。

## 功能特性

- **高亮注释**：以不同样式高亮 TODO 注释
- **可选 TreeSitter**：仅高亮注释中的 TODO，使用 TreeSitter
- **可配置符号**：自定义符号列中的图标
- **快速修复列表**：在 quickfix 列表中打开 TODO
- **集成工具**：支持 Trouble、Telescope 和 FzfLua 进行搜索

## 要求

- Neovim >= 0.8.0（旧版本使用 `neovim-pre-0.8.0` 分支）
- 支持图标的 patched font，或更改为 ASCII 字符
- 可选依赖：
  - ripgrep 和 plenary.nvim 用于搜索
  - Trouble
  - Telescope
  - FzfLua

## 安装

使用 lazy.nvim 安装：

```lua
{
  "folke/todo-comments.nvim",
  dependencies = { "nvim-lua/plenary.nvim" },
  opts = {
    -- 配置选项
  }
}
```

## 配置

插件提供默认配置，包括关键字如 FIX、TODO、HACK 等。可以自定义颜色、图标和搜索模式。

## 用法

插件匹配以关键字后跟冒号的文本，例如：

- `TODO: 做某事`
- `FIX: 这应该被修复`
- `HACK: 奇怪的代码警告`

### 命令

- `:TodoQuickFix`：在 quickfix 列表中显示所有 TODO
- `:TodoLocList`：在位置列表中显示所有 TODO
- `:Trouble todo`：在 Trouble 中列出所有 TODO
- `:TodoTelescope`：使用 Telescope 搜索 TODO

### 跳转

绑定键位跳转到下一个/上一个 TODO：

```lua
vim.keymap.set("n", "]t", function()
  require("todo-comments").jump_next()
end, { desc = "下一个 TODO 注释" })

vim.keymap.set("n", "[t", function()
  require("todo-comments").jump_prev()
end, { desc = "上一个 TODO 注释" })
```
