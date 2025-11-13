---
title: gitsigns.nvim
---

# Gitsigns.nvim 项目

## 项目地址
[https://github.com/lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim)

## 主要特性
Gitsigns.nvim 是一个 Neovim 插件，用于在缓冲区中显示 Git 变更信息。它利用 Neovim 的虚拟文本和扩展功能，提供高效的 Git 集成。主要特性包括：
- **Git 变更高亮**：在行号旁显示添加（+）、删除（-）或变更的标记，支持虚拟文本显示。
- **导航功能**：快速跳转到下一个/上一个变更的 hunk（代码块）。
- **预览支持**：悬停或命令预览 hunk 的差异内容。
- **阶段标记**：显示 staged 和 unstaged 变更的指示器。
- **自定义配置**：高度可配置，支持主题集成和性能优化。
- **LSP 集成**：与 Neovim 的 LSP 功能兼容，提供 blame 信息显示。
- **性能优化**：使用 Lua 实现，轻量且快速，仅在 Git 仓库中激活。

## 主要功能
- **Hunk 显示**：自动在侧边或行号处标记 Git diff 中的添加、删除和变更。
- **Hunk 操作**：通过命令或映射执行 stage、reset 或 undo hunk 操作。
- **Blame 注解**：显示当前行的最后提交者信息，支持缓存以提高速度。
- **Diff 预览**：在浮动窗口中查看 hunk 的详细 diff。
- **当前行高亮**：突出显示当前行的 Git 状态。
- **Git 符号自定义**：允许用户自定义符号、颜色和行为。

## 用法
### 安装
使用插件管理器安装，例如 packer.nvim：
```lua
use {
  'lewis6991/gitsigns.nvim',
  config = function()
    require('gitsigns').setup()
  end
}
```

### 基本配置
在 Neovim 配置中添加：
```lua
require('gitsigns').setup({
  signs = {
    add = { text = '+' },
    change = { text = '~' },
    delete = { text = '_' },
    topdelete = { text = '‾' },
    changedelete = { text = '~' },
  },
  signcolumn = true,  -- 始终显示 signcolumn
  numhl = false,      -- 不高亮行号
  linehl = false,     -- 不高亮行
  word_diff = false,  -- 不启用 word diff
})
```

### 常用命令和映射
- `:Gitsigns toggle_current_line_blame` - 切换当前行 blame 显示。
- `:Gitsigns toggle_linehl` - 切换行高亮。
- `:Gitsigns toggle_numhl` - 切换行号高亮。
- `:Gitsigns toggle_signs` - 切换所有符号显示。
- 映射示例（在 setup 中添加）：
  ```lua
  -- 导航 hunk
  vim.keymap.set('n', ']c', ":Gitsigns next_hunk<CR>")
  vim.keymap.set('n', '[c', ":Gitsigns prev_hunk<CR>")
  -- Stage hunk
  vim.keymap.set('n', '<leader>hs', ":Gitsigns stage_hunk<CR>")
  -- Reset hunk
  vim.keymap.set('n', '<leader>hr', ":Gitsigns reset_hunk<CR>")
  -- 预览 hunk
  vim.keymap.set('n', '<leader>hp', ":Gitsigns preview_hunk<CR>")
  ```

插件会自动在 Git 仓库中加载。更多高级用法请参考 GitHub 仓库的文档。