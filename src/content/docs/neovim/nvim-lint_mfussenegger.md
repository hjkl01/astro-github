---
title: nvim-lint
---

# nvim-lint

An asynchronous linter plugin for Neovim (>= 0.9.5) complementary to the built-in Language Server Protocol support.

## Features

- Asynchronous linting: Runs linters in the background without blocking the editor.
- Integrates with Neovim's diagnostic system: Reports linting results via `vim.diagnostic`.
- Supports multiple filetypes: Configurable linters per filetype.
- Built-in linters: Includes support for over 100 popular linters like ESLint, Flake8, ShellCheck, etc.
- Custom linters: Allows defining custom linters with flexible parsing options.
- Lightweight: Focused scope compared to full-featured plugins like ALE.

## Usage

1. **Installation**: Install via plugin manager like vim-plug or packer, or clone directly.

2. **Configuration**: Set up linters per filetype in your Neovim config:

   ```lua
   require('lint').linters_by_ft = {
     markdown = {'vale'},
     python = {'flake8'},
   }
   ```

3. **Triggering**: Use autocmds to run linting, e.g., on save:

   ```lua
   vim.api.nvim_create_autocmd({ "BufWritePost" }, {
     callback = function()
       require("lint").try_lint()
     end,
   })
   ```

4. **Custom Linters**: Define custom linters if needed:

   ```lua
   require('lint').linters.my_linter = {
     cmd = 'my_linter_cmd',
     args = {'--arg'},
     parser = require('lint.parser').from_pattern(pattern, groups)
   }
   ```

5. **Display**: Customize diagnostic display with `vim.diagnostic.config()`.

For full documentation, see the [GitHub repository](https://github.com/mfussenegger/nvim-lint).
