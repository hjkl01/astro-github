---
title: Smear Cursor.Nvim
---

# smear-cursor.nvim

## 功能介绍

smear-cursor.nvim 是一个 Neovim 插件，为光标添加涂抹效果动画，在所有终端中工作。该插件受 Neovide 的动画光标启发，旨在为仅能显示文本的终端/GUI 提供光标动画效果（不像 Neovide 或 Kitty 终端那样具有图形能力）。

主要特性：

- 在所有终端中提供光标涂抹动画
- 支持缓冲区切换和窗口切换时的涂抹效果
- 支持插入模式下的光标涂抹
- 可配置的动画参数，如刚度、阻尼、颜色等
- 支持透明背景和无 GUI 颜色模式

## 用法

### 安装

#### 使用 lazy.nvim

在 `~/.config/nvim/lua/plugins/smear_cursor.lua` 中添加：

```lua
return {
  "sphamba/smear-cursor.nvim",
  opts = {},
}
```

#### 使用 vim-plug

在 `init.vim` 中添加：

```vim
call plug#begin()
Plug 'sphamba/smear-cursor.nvim'
call plug#end()

lua require('smear_cursor').enabled = true
```

### 配置

插件支持多种配置选项。以下是默认配置：

```lua
opts = {
  -- 在切换缓冲区或窗口时涂抹光标
  smear_between_buffers = true,
  -- 在行内移动或到相邻行时涂抹光标
  smear_between_neighbor_lines = true,
  -- 在滚动时在缓冲区空间而不是屏幕空间绘制涂抹
  scroll_buffer_space = true,
  -- 如果字体支持旧式计算符号（块 unicode 符号），设置为 true
  legacy_computing_symbols_support = false,
  -- 在插入模式下涂抹光标
  smear_insert_mode = true,
}
```

### 命令

- `:SmearCursorToggle` - 切换涂抹光标开关
- `:lua require("smear_cursor").toggle()` - 切换涂抹光标开关

### 示例配置

#### 更快的涂抹效果

```lua
opts = {
  stiffness = 0.8,
  trailing_stiffness = 0.6,
  damping = 0.95,
}
```

#### 平滑光标（无涂抹）

```lua
opts = {
  stiffness = 0.5,
  trailing_stiffness = 0.5,
  matrix_pixel_threshold = 0.5,
}
```

#### 透明背景

```lua
opts = {
  legacy_computing_symbols_support = true,
}
```

### 最低要求

- Neovim 0.10.2
