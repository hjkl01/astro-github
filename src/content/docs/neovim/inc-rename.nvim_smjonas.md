---
title: inc-rename.nvim
---

# inc-rename.nvim

## 项目简介

> Description from GitHub: Incremental LSP renaming based on Neovim's command-preview feature.

## 功能

- **增量重命名**：使用 `:IncRename <new_name>` 命令在 LSP 标识符上进行重命名，并实时预览更改。
- **视觉反馈**：利用 Neovim 的命令预览功能，提供即时视觉反馈。
- **多文件重命名**：支持跨多个文件的重命名操作。
- **插件集成**：支持与 `noice.nvim`、`dressing.nvim` 和 `snacks.nvim` 等插件集成，提供更好的用户界面。
- **自定义选项**：允许用户自定义命令名称、高亮组、消息显示等。

## 安装

该插件需要 Neovim 0.8 或更高版本。

### 使用 lazy.nvim

```lua
{
  "smjonas/inc-rename.nvim",
  opts = {}
}
```

### 使用 packer.nvim

```lua
use {
  "smjonas/inc-rename.nvim",
  config = function()
    require("inc_rename").setup()
  end,
}
```

### 使用 vim-plug

```vim
Plug 'smjonas/inc-rename.nvim'
```

在 `init.lua` 中调用 setup 函数：

```lua
require("inc_rename").setup()
```

## 用法

1. 将光标放在 LSP 标识符上。
2. 输入 `:IncRename <new_name>` 命令。
3. 插件将实时预览重命名的更改。
4. 确认后，LSP 将执行重命名操作。

### 快捷键映射

可以创建快捷键来简化操作：

```lua
vim.keymap.set("n", "<leader>rn", ":IncRename ")
```

或者自动填充当前单词：

```lua
vim.keymap.set("n", "<leader>rn", function()
  return ":IncRename " .. vim.fn.expand("<cword>")
end, { expr = true })
```

### 与其他插件集成

#### noice.nvim

启用 `inc_rename` 预设：

```lua
require("noice").setup {
  presets = { inc_rename = true }
}
```

#### dressing.nvim

设置输入缓冲区类型：

```lua
require("inc_rename").setup {
  input_buffer_type = "dressing",
}
```

#### snacks.nvim

设置输入缓冲区类型：

```lua
require("inc_rename").setup {
  input_buffer_type = "snacks",
}
```

## 自定义选项

可以通过传递 Lua 表到 `setup` 函数来覆盖默认设置：

```lua
require("inc_rename").setup {
  -- 命令名称
  cmd_name = "IncRename",
  -- 高亮组
  hl_group = "Substitute",
  -- 是否预览空名称
  preview_empty_name = false,
  -- 是否显示重命名消息
  show_message = true,
  -- 是否保存命令历史
  save_in_cmdline_history = true,
  -- 输入缓冲区类型
  input_buffer_type = nil,
  -- 重命名后的回调
  post_hook = nil,
}
```

## 注意事项

- 确保在使用多文件重命名时保存所有受影响的缓冲区（`:wa`）。
- 如果 `inccommand` 设置为 `split`，将显示包含所有要重命名标识符信息的缓冲区。
- 已知与某些插件和语言服务器不兼容，如 `traces.vim` 和 `custom-elements-languageserver`。
