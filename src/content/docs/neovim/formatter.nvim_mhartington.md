---
title: formatter.nvim
---

# formatter.nvim

[![GitHub](https://img.shields.io/github/stars/mhartington/formatter.nvim)](https://github.com/mhartington/formatter.nvim/stargazers)
[![LuaRocks](https://img.shields.io/luarocks/v/mhartington/formatter.nvim?logo=lua&color=purple)](https://luarocks.org/modules/mhartington/formatter.nvim)

A format runner for Neovim, written in Lua.

## ✨ Features

- **Asynchronous**: Formatting is done asynchronously, so it doesn't block the editor.
- **Configurable**: Highly configurable, with support for multiple formatters per filetype.
- **Extensible**: Easy to add new formatters.
- **Fast**: Written in Lua, with minimal overhead.
- **Simple**: Simple API, easy to use.

## 📦 Installation

### Using [lazy.nvim](https://github.com/folke/lazy.nvim)

```lua
{
    'mhartington/formatter.nvim',
    config = function()
        require('formatter').setup({
            -- Enable or disable logging
            logging = true,
            -- Set the log level
            log_level = vim.log.levels.WARN,
            -- All formatter configurations are opt-in
            filetype = {
                -- Formatter configurations for filetype "lua" go here
                -- and will be executed in order
                lua = {
                    -- "formatter.filetypes.lua" defines default configurations for the
                    -- "lua" filetype
                    require("formatter.filetypes.lua").stylua,

                    -- You can also define your own configuration
                    function()
                        -- Supports conditional formatting
                        if util.get_current_buffer_file_name() == "special.lua" then
                            return nil
                        end

                        -- Full specification of a formatter
                        return {
                            exe = "stylua",
                            args = {
                                "--search-parent-directories",
                                "--stdin-filepath",
                                util.escape_path(util.get_current_buffer_file_path()),
                                "--",
                                "-",
                            },
                            stdin = true,
                        }
                    end
                },

                -- Use the special "*" filetype for defining formatter configurations on
                -- any filetype
                ["*"] = {
                    -- "formatter.filetypes.any" defines default configurations for any
                    -- filetype
                    require("formatter.filetypes.any").remove_trailing_whitespace
                }
            }
        })
    end
}
```

### Using [packer.nvim](https://github.com/wbthomason/packer.nvim)

```lua
use {
    'mhartington/formatter.nvim',
    config = function()
        require('formatter').setup({
            filetype = {
                lua = {
                    require("formatter.filetypes.lua").stylua,
                },
            }
        })
    end
}
```

### Using [vim-plug](https://github.com/junegunn/vim-plug)

```vim
Plug 'mhartington/formatter.nvim'
```

Then in your `init.lua`:

```lua
require('formatter').setup({
    filetype = {
        lua = {
            require("formatter.filetypes.lua").stylua,
        },
    }
})
```

## 🚀 Usage

### Commands

- `:Format` - Format the current buffer
- `:FormatWrite` - Format the current buffer and write it to disk
- `:FormatLock` - Lock the current buffer from formatting
- `:FormatUnlock` - Unlock the current buffer from formatting

### Keybindings

You can set up keybindings to format the current buffer:

```lua
vim.api.nvim_set_keymap('n', '<leader>f', '<cmd>Format<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>F', '<cmd>FormatWrite<CR>', { noremap = true, silent = true })
```

### Autoformat on save

You can set up autoformatting on save using autocmds:

```lua
vim.api.nvim_exec([[
augroup FormatAutogroup
  autocmd!
  autocmd BufWritePost *.lua,*.py,*.js,*.ts FormatWrite
augroup END
]], true)
```

Or using the `vim.api.nvim_create_autocmd` API:

```lua
vim.api.nvim_create_autocmd({ "BufWritePost" }, {
    pattern = { "*.lua", "*.py", "*.js", "*.ts" },
    command = "FormatWrite",
})
```

### LSP Integration

Formatter can be used as a fallback formatter for LSP. You can configure it to run when LSP formatting is not available:

```lua
require('formatter').setup({
    filetype = {
        lua = {
            require("formatter.filetypes.lua").stylua,
        },
        -- Add other filetypes here
    }
})

-- Use formatter as LSP fallback
vim.api.nvim_create_autocmd({ "LspAttach" }, {
    callback = function(args)
        local client = vim.lsp.get_client_by_id(args.data.client_id)
        if client and client.server_capabilities.documentFormattingProvider then
            vim.api.nvim_create_autocmd({ "BufWritePre" }, {
                buffer = args.buf,
                callback = function()
                    vim.lsp.buf.format({ async = false })
                end,
            })
        else
            vim.api.nvim_create_autocmd({ "BufWritePre" }, {
                buffer = args.buf,
                callback = function()
                    vim.cmd("FormatWrite")
                end,
            })
        end
    end,
})
```

## ⚙️ Configuration

### Basic Configuration

```lua
require('formatter').setup({
    -- Enable or disable logging
    logging = true,
    -- Set the log level
    log_level = vim.log.levels.WARN,
    -- All formatter configurations are opt-in
    filetype = {
        lua = {
            require("formatter.filetypes.lua").stylua,
        },
        python = {
            require("formatter.filetypes.python").black,
        },
    }
})
```

### Advanced Configuration

```lua
require('formatter').setup({
    logging = true,
    log_level = vim.log.levels.WARN,
    filetype = {
        lua = {
            function()
                return {
                    exe = "stylua",
                    args = {
                        "--search-parent-directories",
                        "--stdin-filepath",
                        util.escape_path(util.get_current_buffer_file_path()),
                        "--",
                        "-",
                    },
                    stdin = true,
                }
            end
        },
        python = {
            function()
                return {
                    exe = "black",
                    args = {
                        "--quiet",
                        "-",
                    },
                    stdin = true,
                }
            end
        },
    }
})
```

### Formatter Specification

A formatter is a function that returns a table with the following keys:

- `exe` (string): The executable to run
- `args` (table): Arguments to pass to the executable
- `stdin` (boolean): Whether to pass the buffer content via stdin
- `cwd` (string): The working directory to run the executable in
- `env` (table): Environment variables to set
- `ignore_exitcode` (boolean): Whether to ignore the exit code of the executable
- `no_append` (boolean): Whether to append the buffer content to the args

### Built-in Formatters

Formatter comes with built-in formatters for many filetypes. You can find them in the `formatter.filetypes` module.

#### Lua

- `require("formatter.filetypes.lua").stylua`
- `require("formatter.filetypes.lua").luaformatter`

#### Python

- `require("formatter.filetypes.python").black`
- `require("formatter.filetypes.python").yapf`
- `require("formatter.filetypes.python").autopep8`

#### JavaScript/TypeScript

- `require("formatter.filetypes.javascript").prettier`
- `require("formatter.filetypes.javascript").eslint_d`
- `require("formatter.filetypes.javascript").standard`

#### Go

- `require("formatter.filetypes.go").gofmt`
- `require("formatter.filetypes.go").goimports`

#### Rust

- `require("formatter.filetypes.rust").rustfmt`

#### C/C++

- `require("formatter.filetypes.c").clangformat`

#### Any

- `require("formatter.filetypes.any").remove_trailing_whitespace`

### Custom Formatters

You can define your own formatters:

```lua
require('formatter').setup({
    filetype = {
        lua = {
            function()
                return {
                    exe = "stylua",
                    args = {
                        "--search-parent-directories",
                        "--stdin-filepath",
                        util.escape_path(util.get_current_buffer_file_path()),
                        "--",
                        "-",
                    },
                    stdin = true,
                }
            end
        },
    }
})
```

### Conditional Formatting

You can conditionally format based on the current buffer:

```lua
require('formatter').setup({
    filetype = {
        lua = {
            function()
                if util.get_current_buffer_file_name() == "special.lua" then
                    return nil
                end

                return {
                    exe = "stylua",
                    args = {
                        "--search-parent-directories",
                        "--stdin-filepath",
                        util.escape_path(util.get_current_buffer_file_path()),
                        "--",
                        "-",
                    },
                    stdin = true,
                }
            end
        },
    }
})
```

### Multiple Formatters

You can run multiple formatters for a single filetype:

```lua
require('formatter').setup({
    filetype = {
        lua = {
            require("formatter.filetypes.lua").stylua,
            require("formatter.filetypes.any").remove_trailing_whitespace,
        },
    }
})
```

## 📚 API

### `require('formatter').setup(config)`

Setup formatter with the given configuration.

### `require('formatter').format()`

Format the current buffer.

### `require('formatter').format_write()`

Format the current buffer and write it to disk.

### `require('formatter').lock()`

Lock the current buffer from formatting.

### `require('formatter').unlock()`

Unlock the current buffer from formatting.

### `require('formatter').is_locked()`

Check if the current buffer is locked from formatting.

## 🤝 Contributing

Contributions are welcome! Please see the [contributing guidelines](CONTRIBUTING.md) for more information.

## 📄 License

Formatter is licensed under the MIT license. See [LICENSE](LICENSE) for more information.
