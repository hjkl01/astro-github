---
title: todo-comments.nvim
---

## 项目简介

todo-comments.nvim 是一个用于 Neovim >= 0.8.0 的 Lua 插件，用于高亮、列出和搜索代码库中的 todo 注释，如 `TODO`、`HACK`、`BUG` 等。

## 主要功能

- **高亮注释**：以不同样式高亮 todo 注释。
- **TreeSitter 支持**：可选地仅在注释中使用 TreeSitter 高亮。
- **可配置标志**：自定义标志图标和颜色。
- **快速修复列表**：在 quickfix 列表中打开 todos。
- **Trouble 集成**：在 Trouble 中显示 todos。
- **搜索功能**：使用 Telescope 或 FzfLua 搜索 todos。

## 安装要求

- Neovim >= 0.8.0（旧版本使用 `neovim-pre-0.8.0` 分支）。
- 支持图标的补丁字体，或更改为简单 ASCII 字符。
- 可选依赖：
  - ripgrep 和 plenary.nvim 用于搜索。
  - Trouble、Telescope 或 FzfLua。

## 安装方法

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

## 配置示例

插件提供默认配置，包括关键字如 FIX、TODO、HACK 等。可以自定义图标、颜色和高亮样式。

## 使用方法

- **匹配注释**：插件匹配以关键字后跟冒号的文本，如 `TODO: 做某事`。
- **命令**：
  - `:TodoQuickFix`：在 quickfix 列表中显示所有 todos。
  - `:TodoLocList`：在位置列表中显示 todos。
  - `:Trouble todo`：在 Trouble 中列出 todos。
  - `:TodoTelescope`：使用 Telescope 搜索 todos。
- **跳转**：使用 `]t` 和 `[t` 键映射跳转到下一个/上一个 todo 注释。

## 许可证

Apache-2.0
