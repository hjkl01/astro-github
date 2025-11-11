---
title: lualine.nvim
---

# Lualine.nvim

## Overview

Lualine.nvim is a fast and configurable statusline plugin for Neovim, written in Lua. It offers customizable sections and components for an enhanced user interface, providing a modern and efficient way to display editor information.

## Key Features

- **Customizable Sections**: Divided into lualine_a through lualine_z for flexible layout.
- **Built-in Components**: Includes mode, branch, diff, diagnostics, filename, encoding, fileformat, filetype, progress, location, searchcount, and more.
- **Extensions Support**: Load extensions for specific filetypes like quickfix.
- **Tabline and Winbar**: Support for displaying tabs and window bars.
- **Themes**: Auto-detection and custom theme support.
- **Icons**: Integration with nvim-web-devicons for filetype icons.
- **Lua Expressions**: Use Lua functions or expressions as components.
- **Options**: Global and per-component configuration for colors, separators, and behavior.
- **Performance**: Event-based refreshing with customizable intervals.

## Installation

Install via your preferred Neovim plugin manager:

**Lazy.nvim**:

```lua
{
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' }
}
```

**Packer.nvim**:

```lua
use {
  'nvim-lualine/lualine.nvim',
  requires = { 'nvim-tree/nvim-web-devicons', opt = true }
}
```

**Vim-Plug**:

```vimscript
Plug 'nvim-lualine/lualine.nvim'
Plug 'nvim-tree/nvim-web-devicons'
```

## Configuration Examples

### Basic Setup

```lua
require('lualine').setup()
```

### Advanced Setup

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

### Custom Component Example

```lua
sections = { lualine_c = { "os.date('%a')", 'data', "require'lsp-status'.status()" } }
```

### Diagnostics Component Configuration

```lua
sections = {
  lualine_a = {
    {
      'diagnostics',
      sources = { 'nvim_diagnostic', 'coc' },
      sections = { 'error', 'warn', 'info', 'hint' },
      diagnostics_color = {
        error = 'DiagnosticError',
        warn  = 'DiagnosticWarn',
        info  = 'DiagnosticInfo',
        hint  = 'DiagnosticHint',
      },
      symbols = {error = 'E', warn = 'W', info = 'I', hint = 'H'},
      colored = true,
      update_in_insert = false,
      always_visible = false,
    }
  }
}
```
