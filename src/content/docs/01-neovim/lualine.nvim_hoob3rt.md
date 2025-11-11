---
title: lualine.nvim
---

## 功能介绍

lualine.nvim 是一个快速且易于配置的 Neovim 状态栏插件，完全用纯 Lua 编写。它提供了高度可定制的状态栏，支持多种内置组件、主题和扩展，能够根据不同的文件类型和窗口状态动态调整外观。

### 主要特性

- **高性能**：相比其他状态栏插件，lualine 只加载指定的组件，避免不必要的开销。
- **易于配置**：支持 Lua 配置，提供丰富的选项和组件。
- **主题支持**：内置多种主题，并支持自定义主题。
- **组件丰富**：提供分支、诊断、文件信息、模式等内置组件，支持自定义组件。
- **扩展支持**：针对特定文件类型（如 quickfix、fzf 等）提供专用扩展。
- **图标支持**：可与 nvim-web-devicons 集成显示图标。

## 安装

### 使用 vim-plug

```vim
Plug 'nvim-lualine/lualine.nvim'
" 如果想要图标支持
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

在 `init.lua` 中添加：

```lua
require('lualine').setup()
```

### 默认配置

lualine 将状态栏分为 A、B、C、X、Y、Z 六个部分，默认配置如下：

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
  options = { theme = 'gruvbox' }
}
```

可用主题列表请参考 [THEMES.md](https://github.com/nvim-lualine/lualine.nvim/blob/master/THEMES.md)。

### 自定义组件

#### 使用 Lua 函数作为组件

```lua
local function hello()
  return [[hello world]]
end

require('lualine').setup {
  sections = { lualine_a = { hello } }
}
```

#### 使用 Vim 函数

```lua
require('lualine').setup {
  sections = { lualine_a = {'FugitiveHead'} }
}
```

### 常用组件

- `branch`: Git 分支
- `diagnostics`: 诊断信息
- `diff`: Git 差异状态
- `filename`: 文件名
- `filetype`: 文件类型
- `mode`: Vim 模式
- `progress`: 文件进度百分比
- `location`: 行:列位置

### 扩展

lualine 支持为特定文件类型定制状态栏：

```lua
require('lualine').setup {
  extensions = {'quickfix', 'fzf'}
}
```

可用扩展包括：aerial, chadtree, fugitive, nvim-tree 等。

## 高级配置

### 自定义主题

```lua
local custom_gruvbox = require'lualine.themes.gruvbox'
custom_gruvbox.normal.c.bg = '#112233'

require('lualine').setup {
  options = { theme = custom_gruvbox }
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

### Winbar 配置 (Neovim 0.8+)

```lua
require('lualine').setup {
  winbar = {
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
- 对于图标显示，建议安装 nvim-web-devicons
- 性能优化：lualine 只加载指定的组件，避免加载所有组件
- 兼容性：对于旧版本 Neovim，可使用兼容性标签，如 compat-nvim-0.5
