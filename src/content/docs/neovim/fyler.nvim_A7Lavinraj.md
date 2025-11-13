---
title: repository
---

# Fyler.nvim

**一个现代化的 Neovim 文件管理器，具有 Git 集成、LSP 支持和直观的导航功能**

Fyler.nvim 是一个功能强大的 Neovim 文件管理器插件，它允许你像编辑缓冲区一样编辑文件系统，并提供树形视图。该插件具有现代化的界面设计、Git 状态集成、多种窗口布局选项等丰富功能。

## 主要特性

- **树形文件浏览** - 直观的目录结构显示
- **Git 集成** - 显示文件 Git 状态（已修改、已添加、未跟踪等）
- **多种窗口布局** - 支持分割、浮动、替换等多种显示方式
- **文件操作** - 创建、删除、重命名、移动文件和目录
- **LSP 支持** - 与语言服务器协议集成
- **图标支持** - 支持 mini.icons 和 nvim-web-devicons
- **Telescope 扩展** - 提供 Telescope 集成
- **自定义键位映射** - 灵活的键盘快捷键配置
- **回收站支持** - 可选择将删除的文件移至系统回收站

## 安装

### 稳定版本（推荐）

使用 Lazy.nvim：

```lua
{
  "A7Lavinraj/fyler.nvim",
  dependencies = { "nvim-mini/mini.icons" },
  branch = "stable",
  opts = {}
}
```

使用 Mini.deps：

```lua
add({
  source = "A7Lavinraj/fyler.nvim",
  depends = { "nvim-mini/mini.icons" },
  checkout = "stable",
})
```

### 最新版本

使用 Lazy.nvim（配合 mini.icons）：

```lua
{
  "A7Lavinraj/fyler.nvim",
  dependencies = { "nvim-mini/mini.icons" },
  opts = {}
}
```

使用 Lazy.nvim（配合 nvim-web-devicons）：

```lua
{
  "A7Lavinraj/fyler.nvim",
  dependencies = { "nvim-tree/nvim-web-devicons" },
  opts = { icon_provider = "nvim_web_devicons" }
}
```

## 快速开始

### 使用命令

```vim
:Fyler                    " 使用默认选项打开
:Fyler kind=split_left    " 在特定的窗口布局中打开
:Fyler dir=~/projects     " 打开特定目录
```

### 使用 Lua API

```lua
local fyler = require("fyler")

-- 使用可选设置打开 Fyler
fyler.open({
  dir = "~/",              -- (可选) 在特定目录中启动
  kind = "split_left_most" -- (可选) 使用自定义窗口布局
})

-- 使用可选设置切换 Fyler
fyler.toggle({
  dir = "~/",              -- (可选) 在特定目录中启动
  kind = "split_left_most" -- (可选) 使用自定义窗口布局
})
```

## 配置选项

Fyler.nvim 开箱即用，具有合理的默认设置。以下是完整的配置参考：

```lua
{
  hooks = {
    -- function(path) end
    on_delete = nil,
    -- function(src_path, dst_path) end
    on_rename = nil,
    -- function(hl_groups, palette) end
    on_highlight = nil,
  },
  integrations = {
    icon = "mini_icons",
  },
  views = {
    finder = {
      -- 选择文件时关闭资源管理器
      close_on_select = true,
      -- 自动确认简单的文件操作
      confirm_simple = false,
      -- 替换 netrw 作为默认资源管理器
      default_explorer = false,
      -- 将删除的文件/目录移动到系统回收站
      delete_to_trash = false,
      -- Git 状态
      git_status = {
        enabled = true,
        symbols = {
          Untracked = "?",
          Added = "+",
          Modified = "*",
          Deleted = "x",
          Renamed = ">",
          Copied = "~",
          Conflict = "!",
          Ignored = "#",
        },
      },
      -- 目录状态图标
      icon = {
        directory_collapsed = nil,
        directory_empty = nil,
        directory_expanded = nil,
      },
      -- 缩进指示器
      indentscope = {
        enabled = true,
        group = "FylerIndentMarker",
        marker = "│",
      },
      -- 键位映射
      mappings = {
        ["q"] = "CloseView",
        ["<CR>"] = "Select",
        ["<C-t>"] = "SelectTab",
        ["|"] = "SelectVSplit",
        ["-"] = "SelectSplit",
        ["^"] = "GotoParent",
        ["="] = "GotoCwd",
        ["."] = "GotoNode",
        ["#"] = "CollapseAll",
        ["<BS>"] = "CollapseNode",
      },
      -- 当前文件跟踪
      follow_current_file = true,
      -- 文件系统监控（包括 Git 状态）
      watcher = {
        enabled = false,
      },
      -- 窗口配置
      win = {
        border = vim.o.winborder == "" and "single" or vim.o.winborder,
        buf_opts = {
          filetype = "fyler",
          syntax = "fyler",
          buflisted = false,
          buftype = "acwrite",
          expandtab = true,
          shiftwidth = 2,
        },
        kind = "replace",
        kinds = {
          float = {
            height = "70%",
            width = "70%",
            top = "10%",
            left = "15%",
          },
          replace = {},
          split_above = {
            height = "70%",
          },
          split_above_all = {
            height = "70%",
          },
          split_below = {
            height = "70%",
          },
          split_below_all = {
            height = "70%",
          },
          split_left = {
            width = "70%",
          },
          split_left_most = {
            width = "30%",
          },
          split_right = {
            width = "30%",
          },
          split_right_most = {
            width = "30%",
          },
        },
        win_opts = {
          concealcursor = "nvic",
          conceallevel = 3,
          cursorline = false,
          number = false,
          relativenumber = false,
          winhighlight = "Normal:FylerNormal",
          wrap = false,
        },
      },
    },
  },
}
```

启用 `delete_to_trash` 可以将删除操作发送到操作系统的回收站（macOS `~/.Trash`、Linux XDG Trash、Windows 回收站），而不是永久删除文件。如果目标文件已经在回收站目录中，Fyler 会自动执行永久删除。

**注意**：当在不同文件系统之间移动文件时（例如，移动到不同驱动器上的回收站目录），操作会自动回退到复制然后删除，这对于大文件或目录可能会比较慢。Windows 操作包含 30 秒超时以防止挂起。

## Telescope 扩展

Fyler.nvim 包含一个 Telescope 扩展，用于增强目录导航：

```lua
local telescope = require("telescope")

telescope.setup({
  extensions = {
    fyler = {
      -- 扩展配置
    }
  }
})

telescope.load_extension("fyler")
```

## 默认键位映射

- `q` - 关闭视图
- `<CR>` - 选择文件/目录
- `<C-t>` - 在新标签页中打开
- `|` - 在垂直分割中打开
- `-` - 在水平分割中打开
- `^` - 转到父目录
- `=` - 转到当前工作目录
- `.` - 转到当前节点
- `#` - 折叠所有目录
- `<BS>` - 折叠当前目录

## 文档和资源

- **Wiki**: 综合文档可在 [Wiki 页面](https://github.com/A7Lavinraj/fyler.nvim/wiki) 获取
- **直播**: 开发直播在 [YouTube](https://youtube.com/playlist?list=PLE5gu3yOYmtiTiC1J3BysrcormCt_eWuq&si=L6yEiJI7rNuCp5cy)
- **稳定版文档**: [稳定分支文档](https://github.com/A7Lavinraj/fyler.nvim/blob/stable/README.md)

## 类似项目

如果 fyler.nvim 不满足你的需求，可以考虑这些替代方案：

- [mini.files](https://github.com/nvim-mini/mini.files)
- [oil.nvim](https://github.com/stevearc/oil.nvim)

## 许可证

本项目采用 Apache-2.0 许可证。详情请查看仓库中的完整许可证文件。
