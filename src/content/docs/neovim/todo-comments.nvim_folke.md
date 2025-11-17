---
title: todo-comments.nvim
---

## 项目简介

todo-comments.nvim 是一个用于 Neovim >= 0.8.0 的 Lua 插件，用于高亮、列出和搜索项目中的 TODO 注释，如 `TODO`、`HACK`、`BUG` 等。

## 功能特性

- **高亮注释**：以不同样式高亮 TODO 注释
- **可选 TreeSitter 支持**：仅高亮注释中的 TODO
- **可配置标志**：自定义标志图标和颜色
- **快速修复列表**：在 quickfix 列表中打开 TODO
- **Trouble 集成**：在 Trouble 中显示 TODO
- **搜索功能**：使用 Telescope 或 FzfLua 搜索 TODO

## 安装要求

- Neovim >= 0.8.0
- 补丁字体（如 Nerd Fonts）用于图标显示
- 可选依赖：
  - ripgrep 和 plenary.nvim 用于搜索
  - Trouble
  - Telescope
  - FzfLua

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

## 配置选项

插件提供丰富的配置选项，包括关键字定义、颜色设置、高亮样式等。默认支持的关键字包括 FIX、TODO、HACK、WARN、PERF、NOTE、TEST 等。

## 使用方法

### 基本用法

插件会自动匹配以关键字后跟冒号的注释，如：

- `TODO: 做某事`
- `FIX: 修复这个问题`
- `HACK: 奇怪的代码警告`

### 命令

- `:TodoQuickFix` - 在 quickfix 列表中显示所有 TODO
- `:TodoLocList` - 在位置列表中显示所有 TODO
- `:Trouble todo` - 在 Trouble 中显示 TODO
- `:TodoTelescope` - 使用 Telescope 搜索 TODO
- `:TodoFzfLua` - 使用 FzfLua 搜索 TODO

### 跳转

可以使用快捷键跳转到下一个/上一个 TODO：

```lua
vim.keymap.set("n", "]t", function()
  require("todo-comments").jump_next()
end, { desc = "下一个 TODO 注释" })

vim.keymap.set("n", "[t", function()
  require("todo-comments").jump_prev()
end, { desc = "上一个 TODO 注释" })
```

### 过滤

命令支持参数过滤，如 `cwd` 指定目录，`keywords` 指定关键字。
