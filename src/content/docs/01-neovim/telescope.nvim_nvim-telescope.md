
---
title: telescope.nvim
---

# Telescope.nvim

**GitHub 项目地址:** [https://github.com/nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)

## 主要特性

Telescope.nvim 是一个高度可扩展的模糊查找器（fuzzy finder）插件，专为 Neovim 设计。它基于 Neovim 的内置 LSP 支持和内置 UI 组件，提供高效的搜索和导航体验。主要特性包括：

- **模糊搜索**：支持实时模糊匹配，快速过滤结果，提高搜索效率。
- **内置拾取器**：集成多种 Neovim 内置功能，如文件查找、缓冲区切换、历史记录浏览等。
- **可扩展性**：允许用户通过 Lua 配置自定义扩展，支持与第三方插件（如 fzf、ripgrep）集成。
- **美观 UI**：使用浮动窗口显示结果，支持预览、排序和多列布局。
- **性能优化**：利用 Neovim 的异步机制，确保搜索过程不阻塞编辑器。
- **跨平台支持**：兼容 Windows、macOS 和 Linux，无需额外依赖（可选外部工具增强功能）。

## 主要功能

Telescope.nvim 提供丰富的内置拾取器（pickers），覆盖 Neovim 的核心工作流：

- **文件相关**：
  - `find_files`：在当前工作目录或指定路径中查找文件，支持 git 项目过滤。
  - `git_files`：仅搜索 git 仓库中的文件。
  - `live_grep`：使用 ripgrep 等工具实时搜索文件内容。

- **缓冲区和窗口**：
  - `buffers`：列出并切换打开的缓冲区。
  - `windows`：快速切换 Neovim 窗口。

- **历史和命令**：
  - `command_history`：浏览命令历史。
  - `search_history`：搜索历史记录。
  - `commands`：执行 Neovim 命令。

- **LSP 和代码相关**：
  - `lsp_references`：查找 LSP 符号引用。
  - `diagnostics`：显示诊断信息。

- **其他**：
  - `oldfiles`：最近打开的文件列表。
  - `marks`：浏览和跳转书签。
  - 支持自定义拾取器扩展，如颜色方案选择或插件管理。

此外，它支持动作（actions），如预览文件内容、复制路径或直接打开链接。

## 用法

### 安装

使用插件管理器安装，例如 packer.nvim：

```lua
use {
  'nvim-telescope/telescope.nvim',
  requires = { {'nvim-lua/plenary.nvim'} }
}
```

或 lazy.nvim：

```lua
{
  'nvim-telescope/telescope.nvim',
  dependencies = { 'nvim-lua/plenary.nvim' }
}
```

### 配置

在 Neovim 的 `init.lua` 中基本配置：

```lua
require('telescope').setup({
  defaults = {
    -- 主题配置
    theme = 'dropdown',
    -- 布局设置
    layout_strategy = 'horizontal',
    layout_config = { height = 0.95, width = 0.95 },
    -- 映射键位
    mappings = {
      i = { -- 插入模式
        ['<C-j>'] = require('telescope.actions').move_selection_next,
        ['<C-k>'] = require('telescope.actions').move_selection_previous,
      },
      n = { -- 正常模式
        ['<C-d>'] = require('telescope.actions').delete_buffer,
      },
    },
  },
  pickers = {
    find_files = {
      hidden = true, -- 包含隐藏文件
    },
  },
  extensions = {
    fzf = { fuzzy = true, override_generic_sorter = true },
  },
})
```

加载扩展（如果安装）：

```lua
require('telescope').load_extension('fzf')
```

### 使用

- 启动拾取器：使用 `:Telescope <picker_name>` 命令，或通过键映射。
- 示例键映射（在 init.lua 中添加）：

```lua
local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
vim.keymap.set('n', '<leader>fb', builtin.buffers, {})
vim.keymap.set('n', '<leader>fh', builtin.help_tags, {})
```

- 操作：
  - 输入文本进行模糊搜索。
  - 使用 `<C-n>/<C-p>` 或箭头键导航结果。
  - `<C-u>` 清空输入。
  - `<CR>` 选择并执行（例如打开文件）。
  - `<C-q>` 预览/关闭预览。

更多细节请参考项目文档：https://github.com/nvim-telescope/telescope.nvim