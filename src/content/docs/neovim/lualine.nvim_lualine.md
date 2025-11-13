---
title: lualine.nvim
---

## 功能介绍

lualine.nvim 是一个快速且易于配置的 Neovim 状态栏插件，完全用 Lua 编写。它提供了高度可定制的状态栏，支持多种主题、组件和扩展。

### 主要特性

- **高性能**：相比其他状态栏插件，启动时间更快，只加载指定的组件。
- **易于配置**：支持 Lua 配置，灵活的组件系统。
- **主题支持**：内置多种主题，并支持自定义主题。
- **组件丰富**：提供分支、诊断、文件信息、模式等多种组件。
- **扩展支持**：支持为特定文件类型定制状态栏外观。
- **图标支持**：可与 nvim-web-devicons 配合显示图标。

### 性能对比

与其他状态栏插件相比，lualine 的启动时间更短：

- 控制组：17.2 ms
- lualine：24.8 ms
- lightline：25.5 ms
- airline：79.9 ms

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
-- Lua 函数作为组件
local function hello()
  return [[hello world]]
end

require('lualine').setup {
  sections = { lualine_a = { hello } }
}
```

### 可用组件

- `branch`：Git 分支
- `buffers`：当前缓冲区
- `diagnostics`：诊断信息
- `diff`：Git 差异状态
- `encoding`：文件编码
- `fileformat`：文件格式
- `filename`：文件名
- `filesize`：文件大小
- `filetype`：文件类型
- `hostname`：主机名
- `location`：位置（行:列）
- `mode`：Vim 模式
- `progress`：进度百分比
- `searchcount`：搜索匹配数
- `selectioncount`：选中文本数
- `tabs`：标签页
- `windows`：窗口
- `lsp_status`：LSP 状态

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

### 扩展

```lua
require('lualine').setup {
  extensions = {'quickfix'}
}
```

支持的扩展包括：aerial, assistant, avante, chadtree, ctrlspace, fern, fugitive, fzf, lazy, man, mason, mundo, neo-tree, nerdtree, nvim-dap-ui, nvim-tree, oil, overseer, quickfix, symbols-outline, toggleterm, trouble 等。

## 自定义主题

```lua
local custom_gruvbox = require'lualine.themes.gruvbox'

-- 修改 normal 模式下 lualine_c 部分的背景色
custom_gruvbox.normal.c.bg = '#112233'

require('lualine').setup {
  options = { theme = custom_gruvbox },
  ...
}
```

## 高级配置

### 组件选项

每个组件都可以配置颜色、图标、格式等选项。

```lua
require('lualine').setup {
  sections = {
    lualine_a = {
      {
        'mode',
        icons_enabled = true,
        icon = nil,
        separator = nil,
        cond = nil,
        draw_empty = false,
        color = nil,
        type = nil,
        padding = 1,
        fmt = nil,
        on_click = nil,
      }
    }
  }
}
```

### 条件显示

```lua
require('lualine').setup {
  sections = {
    lualine_a = {
      {
        'branch',
        cond = function()
          return vim.fn.isdirectory('.git') == 1
        end
      }
    }
  }
}
```

## 故障排除

- 确保使用 Neovim >= 0.7
- 如果图标不显示，确保安装了支持的字体和 nvim-web-devicons
- 使用 `:LualineBuffersJump` 命令跳转缓冲区
- 使用 `:LualineRenameTab` 重命名标签页

更多详细信息请参考 [GitHub 仓库](https://github.com/nvim-lualine/lualine.nvim) 和 [Wiki](https://github.com/nvim-lualine/lualine.nvim/wiki)。
