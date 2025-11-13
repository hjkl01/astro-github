---
title: neo-tree.nvim
---

# neo-tree.nvim

## 项目描述

Neo-tree 是一个 Neovim 插件，用于管理文件系统和其他树状结构。它提供了多种显示方式，包括侧边栏、浮动窗口、netrw 风格等，同时支持文件浏览、缓冲区管理、Git 状态查看等功能。

## 主要功能

- **文件系统浏览**：以树状结构显示文件和文件夹，支持添加、复制、删除、移动、重命名等操作。
- **缓冲区管理**：显示当前打开的缓冲区列表。
- **Git 状态集成**：显示 Git 状态，支持添加、提交、推送等操作。
- **文档符号**：显示当前文档的符号结构（实验性功能）。
- **预览模式**：支持文件预览，包括图像预览。
- **自定义配置**：高度可定制，支持多种布局和映射。
- **事件系统**：支持钩子事件，用于扩展功能。
- **稳定性保证**：遵循语义化版本控制，避免破坏性更改。

## 用法

### 基本命令

- `:Neotree`：打开 Neo-tree 文件系统浏览器（默认左侧侧边栏）。
- `:Neotree buffers`：显示缓冲区列表。
- `:Neotree git_status`：显示 Git 状态。
- `:Neotree document_symbols`：显示文档符号（实验性）。

### 命令参数

- `position`：指定位置，如 `left`、`right`、`top`、`bottom`、`float`、`current`。
- `reveal`：自动聚焦当前文件。
- `toggle`：切换窗口显示/隐藏。
- `dir`：指定根目录。

示例：

```
:Neotree filesystem reveal right  # 在右侧打开并聚焦当前文件
:Neotree buffers position=float   # 以浮动窗口显示缓冲区
```

### 键盘映射

在 Neo-tree 窗口中：

- `<CR>` 或 `o`：打开文件/文件夹。
- `a`：添加文件/文件夹。
- `d`：删除。
- `r`：重命名。
- `y`：复制到剪贴板。
- `p`：从剪贴板粘贴。
- `?`：显示帮助。

### 预览模式

- `P`：切换预览模式，支持浮动窗口或现有分割窗口预览文件。

## 安装

使用 lazy.nvim：

```lua
{
  "nvim-neo-tree/neo-tree.nvim",
  branch = "v3.x",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "MunifTanjim/nui.nvim",
    "nvim-tree/nvim-web-devicons", -- 可选，用于文件图标
  },
}
```

## 配置示例

```lua
require("neo-tree").setup({
  close_if_last_window = false,
  enable_git_status = true,
  enable_diagnostics = true,
  window = {
    position = "left",
    width = 40,
    mappings = {
      ["<space>"] = "toggle_node",
      ["<cr>"] = "open",
      ["a"] = "add",
      ["d"] = "delete",
      ["r"] = "rename",
    },
  },
  filesystem = {
    filtered_items = {
      hide_dotfiles = true,
      hide_gitignored = true,
    },
    follow_current_file = {
      enabled = true,
    },
  },
})
```

更多配置选项请参考 `:h neo-tree` 或项目文档。
