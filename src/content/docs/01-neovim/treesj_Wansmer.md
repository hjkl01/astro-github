---
title: treesj
---

# treesj

Neovim plugin for splitting/joining blocks of code like arrays, hashes, statements, objects, dictionaries, etc. Written in Lua, using Tree-Sitter.

## Features

- Can be called from anywhere in the block
- Cursor follows the text on which it was called
- Toggle-mode present
- Recursive processing
- Recognizes nested languages
- Supports dot repeat

## Requirements

- Neovim 0.9+
- nvim-treesitter (optional)

## Installation

With lazy.nvim:

```lua
{
  'Wansmer/treesj',
  keys = { '<space>m', '<space>j', '<space>s' },
  dependencies = { 'nvim-treesitter/nvim-treesitter' },
  config = function()
    require('treesj').setup({})
  end,
}
```

## Usage

Commands:

- `:TSJToggle` - toggle node under cursor
- `:TSJSplit` - split node under cursor
- `:TSJJoin` - join node under cursor

Default keymaps:

- `<space>m` - toggle
- `<space>j` - join
- `<space>s` - split

## Supported Languages

Javascript, Typescript, Lua, CSS, SCSS, HTML, Pug, Vue, Svelte, JSON, JSONC, JSON5, Toml, Yaml, Perl, PHP, Ruby, Python, Go, Java, Rust, R, C/C++, Nix, Kotlin, Bash, SQL, Dart, Elixir, Haskell, Zig, Julia, Terraform, Typst, etc.
