---
title: blink.indent
---

## 功能介绍

blink.indent 是一个为 Neovim 提供高性能缩进引导线的插件。它能够在每次按键时实时显示缩进引导线，包括作用域范围，渲染速度极快（0.1-2ms），即使在大型文件中也能流畅运行。该插件使用约 500 行代码实现，比基于 Treesitter 的解决方案更快（约 10 倍）。

主要特性：

- 实时缩进引导线，每按键更新
- 支持作用域范围显示
- 高性能，适用于大型文件
- 可自定义字符、高亮和优先级
- 支持彩虹风格的缩进引导线
- 可按缓冲区或全局启用/禁用

## 用法

### 安装

使用 lazy.nvim：

```lua
{
  'saghen/blink.indent',
  --- @module 'blink.indent'
  --- @type blink.indent.Config
  -- opts = {},
}
```

使用 vim.pack：

```lua
vim.pack.add({ 'saghen/blink.indent' })
-- require('blink.indent').setup({})
```

### 配置

调用 `setup()` 是可选的，插件会自动使用默认配置初始化。

```lua
require('blink.indent').setup({
  blocked = {
    -- 默认: 'terminal', 'quickfix', 'nofile', 'prompt'
    buftypes = { include_defaults = true },
    -- 默认: 'lspinfo', 'packer', 'checkhealth', 'help', 'man', 'gitcommit', 'dashboard', ''
    filetypes = { include_defaults = true },
  },
  static = {
    enabled = true,
    char = '▎',
    priority = 1,
    -- 指定多个高亮以实现彩虹风格缩进引导线
    -- highlights = { 'BlinkIndentRed', 'BlinkIndentOrange', 'BlinkIndentYellow', 'BlinkIndentGreen', 'BlinkIndentViolet', 'BlinkIndentCyan' },
    highlights = { 'BlinkIndent' },
  },
  scope = {
    enabled = true,
    char = '▎',
    priority = 1000,
    -- 设置为单个高亮如 'BlinkIndent' 以禁用彩虹风格
    -- highlights = { 'BlinkIndentScope' },
    -- 可选添加: 'BlinkIndentRed', 'BlinkIndentCyan', 'BlinkIndentYellow', 'BlinkIndentGreen'
    highlights = { 'BlinkIndentOrange', 'BlinkIndentViolet', 'BlinkIndentBlue' },
    -- 启用以在当前作用域上方行显示下划线
    underline = {
      enabled = false,
      -- 可选添加: 'BlinkIndentRedUnderline', 'BlinkIndentCyanUnderline', 'BlinkIndentYellowUnderline', 'BlinkIndentGreenUnderline'
      highlights = { 'BlinkIndentOrangeUnderline', 'BlinkIndentVioletUnderline', 'BlinkIndentBlueUnderline' },
    },
  },
})
```

### 启用/禁用

全局禁用：`vim.g.indent_guide = false`

按缓冲区禁用：`vim.b[bufnr].indent_guide = false`

切换可见性：

```lua
local indent = require('blink.indent')
vim.keymap.set('n', 'some-key', function() indent.enable(not indent.is_enabled()) end, { desc = 'Toggle indent guides' })
```

按缓冲区切换：`indent.enable(not indent.is_enabled({ bufnr = 0 }), { bufnr = 0 })`
