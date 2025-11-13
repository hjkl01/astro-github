---
title: Feline
---

<!-- panvimdoc-ignore-start -->

# Feline

[![GitHub](https://img.shields.io/github/stars/feline-nvim/feline.nvim)](https://github.com/feline-nvim/feline.nvim/stargazers)
[![LuaRocks](https://img.shields.io/luarocks/v/feline-nvim/feline.nvim?logo=lua&color=purple)](https://luarocks.org/modules/feline-nvim/feline.nvim)

> Description from GitHub: A minimal, stylish and customizable statusline for Neovim written in Lua

![feline demo](https://user-images.githubusercontent.com/50679139/147858982-8b8b8b8b-8b8b-8b8b-8b8b-8b8b8b8b8b8b.png)

<!-- panvimdoc-ignore-end -->

## ✨ Features

- **Fast**: Written in Lua with no external dependencies
- **Minimal**: Simple and minimal out of the box
- **Modular**: Create your own components with custom providers and hl functions
- **Extensible**: Easy to extend and customize
- **Separators**: Customizable separators and icons
- **Click support**: Supports clickable components (when Neovim version >= 0.10)
- **Git integration**: Built-in Git status support
- **LSP integration**: Built-in LSP diagnostics and code actions support
- **Themes**: Comes with multiple built-in themes and supports custom themes
- **Conditional components**: Show/hide components based on conditions
- **Async updates**: Supports async updates for components

## 📦 Installation

### Using [lazy.nvim](https://github.com/folke/lazy.nvim)

```lua
{
    'feline-nvim/feline.nvim',
    config = function()
        require('feline').setup()
    end
}
```

### Using [packer.nvim](https://github.com/wbthomason/packer.nvim)

```lua
use {
    'feline-nvim/feline.nvim',
    config = function()
        require('feline').setup()
    end
}
```

### Using [vim-plug](https://github.com/junegunn/vim-plug)

```vim
Plug 'feline-nvim/feline.nvim'
```

Then in your `init.lua`:

```lua
require('feline').setup()
```

## 🚀 Quickstart

After installing, Feline should work out of the box with the default configuration. If you want to customize it, you can pass a table to the `setup` function.

```lua
require('feline').setup({
    -- components = require('feline.presets').default,
    -- theme = 'default',
    -- vi_mode_colors = {
    --     NORMAL = 'green',
    --     INSERT = 'blue',
    --     VISUAL = 'purple',
    --     OP = 'green',
    --     BLOCK = 'purple',
    --     REPLACE = 'red',
    --     ['V-REPLACE'] = 'purple',
    --     ENTER = 'cyan',
    --     MORE = 'cyan',
    --     SELECT = 'orange',
    --     COMMAND = 'green',
    --     SHELL = 'green',
    --     TERM = 'green',
    --     NONE = 'yellow'
    -- }
})
```

## 📚 Documentation

For detailed documentation, see `:help feline` or the [online documentation](https://feline-nvim.github.io/feline.nvim/).

## 🎨 Themes

Feline comes with several built-in themes. You can see them in the [themes directory](lua/feline/themes/).

To use a theme, set the `theme` option in the setup function:

```lua
require('feline').setup({
    theme = 'onedark'
})
```

You can also create your own themes. See the [documentation](https://feline-nvim.github.io/feline.nvim/configuration/themes.html) for more information.

## 🧩 Components

Feline uses a component-based system. Components are the building blocks of the statusline. You can create your own components or use the built-in ones.

### Built-in components

Feline comes with several built-in components that you can use:

- `vi_mode`: Shows the current Vim mode
- `file_info`: Shows file information (name, size, type, etc.)
- `git_branch`: Shows the current Git branch
- `git_diff`: Shows Git diff statistics
- `diagnostics`: Shows LSP diagnostics
- `lsp_client_names`: Shows active LSP client names

### Custom components

You can create your own components using providers and highlight functions. Here's an example:

```lua
local c = require('feline.components')

c.new('my_component', {
    provider = function()
        return 'Hello, World!'
    end,
    hl = {
        fg = 'white',
        bg = 'black',
        style = 'bold'
    }
})
```

For more information on creating components, see the [documentation](https://feline-nvim.github.io/feline.nvim/configuration/components.html).

## 🔧 Configuration

Feline is highly configurable. You can customize almost every aspect of the statusline.

### Basic configuration

```lua
require('feline').setup({
    components = {
        active = {
            {
                { provider = 'vi_mode', hl = { style = 'bold' } },
                { provider = 'file_info' },
                { provider = 'git_branch' },
                { provider = 'git_diff' },
                { provider = 'diagnostics' },
                { provider = 'lsp_client_names' }
            },
            {
                { provider = 'position' },
                { provider = 'line_percentage' },
                { provider = 'scroll_bar' }
            }
        },
        inactive = {
            {
                { provider = 'file_info' }
            }
        }
    },
    theme = 'default',
    vi_mode_colors = {
        NORMAL = 'green',
        INSERT = 'blue',
        VISUAL = 'purple'
    }
})
```

### Advanced configuration

For more advanced configuration options, see the [documentation](https://feline-nvim.github.io/feline.nvim/configuration/).

## 🤝 Contributing

Contributions are welcome! Please see the [contributing guidelines](CONTRIBUTING.md) for more information.

## 📄 License

Feline is licensed under the MIT license. See [LICENSE](LICENSE) for more information.

## 🙏 Acknowledgments

- [lualine.nvim](https://github.com/nvim-lualine/lualine.nvim) for inspiration
- [galaxyline.nvim](https://github.com/glepnir/galaxyline.nvim) for inspiration
- [vim-airline](https://github.com/vim-airline/vim-airline) for inspiration
