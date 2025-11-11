---
title: lualine.nvim
---

## 功能介绍

lualine.nvim 是一个快速且易于配置的 Neovim 状态栏插件，完全用 Lua 编写。它提供了高度可定制的状态栏，支持多种主题、组件和扩展。

### 主要特性

- **高性能**：仅加载指定的组件，避免不必要的开销
- **易于配置**：支持 Lua 配置，灵活的组件系统
- **主题支持**：内置多种主题，可自定义颜色和样式
- **组件丰富**：提供分支、诊断、文件信息等多种组件
- **扩展支持**：针对特定文件类型或插件的扩展配置
- **图标支持**：可与 nvim-web-devicons 配合显示图标

## 安装

### 使用 vim-plug

```vim
Plug 'nvim-lualine/lualine.nvim'
" 如果想要状态栏中显示图标，请选择以下之一
Plug 'nvim-tree/nvim-web-devicons'
```

### 使用 packer.nvim

```lua
use {
  'nvim-lualine/lualine.nvim',
  requires = { 'nvim-tree/nvim-web-devicons', opt = true }
}
```

### 使用 lazy.nvim

```lua
{
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' }
}
```

## 基本用法

### 启动 lualine

```lua
require('lualine').setup()
```

### 默认配置

```lua
require('lualine').setup {
  options = {
    icons_enabled = true,
    theme = 'auto',
    component_separators = { left = '', right = ''},
    section_separators = { left = '', right = ''},
    disabled_filetypes = {
      statusline = {},
      winbar = {},
    },
    ignore_focus = {},
    always_divide_middle = true,
    always_show_tabline = true,
    globalstatus = false,
    refresh = {
      statusline = 1000,
      tabline = 1000,
      winbar = 1000,
      refresh_time = 16,
      events = {
        'WinEnter',
        'BufEnter',
        'BufWritePost',
        'SessionLoadPost',
        'FileChangedShellPost',
        'VimResized',
        'Filetype',
        'CursorMoved',
        'CursorMovedI',
        'ModeChanged',
      },
    }
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {},
  winbar = {},
  inactive_winbar = {},
  extensions = {}
}
```

### 设置主题

```lua
require('lualine').setup {
  options = { theme = 'gruvbox' },
  ...
}
```

### 自定义组件

```lua
local function hello()
  return [[hello world]]
end

require('lualine').setup {
  sections = { lualine_a = { hello } }
}
```

### 可用组件

- `branch` (git 分支)
- `buffers` (当前缓冲区)
- `diagnostics` (诊断计数)
- `diff` (git diff 状态)
- `encoding` (文件编码)
- `fileformat` (文件格式)
- `filename`
- `filesize`
- `filetype`
- `hostname`
- `location` (行:列格式的位置)
- `mode` (vim 模式)
- `progress` (文件进度百分比)
- `searchcount` (搜索匹配数)
- `selectioncount` (选中文本数)
- `tabs` (当前标签页)
- `windows` (当前窗口)
- `lsp_status` (LSP 状态)

### 扩展

```lua
require('lualine').setup {
  extensions = {'quickfix'}
}
```

支持的扩展包括：aerial, chadtree, fugitive, nvim-tree 等。

## 高级配置

### 自定义主题

```lua
local custom_gruvbox = require'lualine.themes.gruvbox'
custom_gruvbox.normal.c.bg = '#112233'

require('lualine').setup {
  options = { theme = custom_gruvbox },
  ...
}
```

### Tabline 配置

```lua
require('lualine').setup {
  tabline = {
    lualine_a = {'buffers'},
    lualine_b = {'branch'},
    lualine_c = {'filename'},
    lualine_x = {},
    lualine_y = {},
    lualine_z = {'tabs'}
  }
}
```

### Winbar 配置

```lua
require('lualine').setup {
  winbar = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {},
    lualine_y = {},
    lualine_z = {}
  },
  inactive_winbar = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {},
    lualine_y = {},
    lualine_z = {}
  }
}
```

## 注意事项

- 需要 Neovim >= 0.7
- 如果要显示图标，需要安装支持的字体和 nvim-web-devicons 插件
- 性能优于其他状态栏插件，因为只加载使用的组件
