---
title: fzf-lua
---

## 功能介绍

fzf-lua 是一个用 Lua 编写的改进版 fzf.vim 插件，为 Neovim 提供强大的模糊搜索功能。它基于 fzf（一个通用的命令行模糊查找器），提供了丰富的搜索和导航功能，包括文件搜索、缓冲区管理、代码搜索、Git 操作、LSP 支持等。

主要功能：

- **文件搜索**：快速查找和打开文件，支持 fd、rg、find 等工具
- **缓冲区管理**：列出和切换打开的缓冲区
- **代码搜索**：使用 grep 或 rg 进行实时代码搜索
- **Git 集成**：支持 Git 文件、状态、提交、分支等操作
- **LSP 支持**：提供引用、定义、符号搜索等 LSP 功能
- **标签和标记**：搜索项目标签和缓冲区标签
- **Neovim 集成**：支持命令历史、键映射、选项等
- **自定义预览**：内置预览器，支持语法高亮和图像预览

## 用法

### 安装

使用 lazy.nvim 安装：

```lua
{
  "ibhagwan/fzf-lua",
  -- 可选，用于图标支持
  dependencies = { "nvim-tree/nvim-web-devicons" },
  -- 或使用 mini.icons
  -- dependencies = { "nvim-tree/nvim-web-devicons" },
  opts = {}
}
```

### 依赖

- Neovim >= 0.9
- fzf >= 0.36 或 skim 二进制文件
- 可选：fd、rg、bat、delta 等工具

### 基本用法

运行 fzf-lua 命令：

```lua
-- Lua 调用
require("fzf-lua").files()
-- 或使用全局对象
FzfLua.files()
-- Vim 命令
:FzfLua files
```

### 主要命令

#### 文件和缓冲区

- `:FzfLua files` - 搜索文件
- `:FzfLua buffers` - 打开的缓冲区
- `:FzfLua oldfiles` - 最近打开的文件
- `:FzfLua tabs` - 打开的标签页

#### 搜索

- `:FzfLua grep` - 使用 grep 搜索模式
- `:FzfLua live_grep` - 实时项目搜索
- `:FzfLua grep_cword` - 搜索光标下的单词

#### Git

- `:FzfLua git_files` - Git 跟踪的文件
- `:FzfLua git_status` - Git 状态
- `:FzfLua git_commits` - Git 提交历史
- `:FzfLua git_branches` - Git 分支

#### LSP

- `:FzfLua lsp_references` - LSP 引用
- `:FzfLua lsp_definitions` - LSP 定义
- `:FzfLua lsp_document_symbols` - 文档符号

### 恢复搜索

恢复上次搜索：

```lua
:FzfLua resume
```

### 全局搜索

VS Code 风格的全局搜索，结合文件、缓冲区和 LSP 符号：

```lua
:FzfLua global
```

### 自定义配置

```lua
require("fzf-lua").setup({
  winopts = {
    height = 0.85,
    width = 0.80,
    preview = {
      layout = "flex",
    },
  },
  files = {
    prompt = '文件❯ ',
    file_icons = true,
    color_icons = true,
  },
  grep = {
    prompt = '搜索❯ ',
    rg_opts = "--column --line-number --no-heading --color=always --smart-case -e",
  },
})
```

### 键绑定

默认键绑定：

- `<C-\>` - 缓冲区
- `<C-p>` - 文件
- `<C-g>` - 搜索
- `<C-l>` - 实时搜索

### 插入模式补全

设置路径补全：

```lua
vim.keymap.set({ "n", "v", "i" }, "<C-x><C-f>",
  function() require("fzf-lua").complete_path() end,
  { silent = true, desc = "模糊补全路径" })
```

fzf-lua 提供了丰富的配置选项和扩展功能，可以根据需要进行深度定制。
