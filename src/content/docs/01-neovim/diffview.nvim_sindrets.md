---
title: diffview.nvim
---

# diffview.nvim

## 功能介绍

diffview.nvim 是一个 Neovim 插件，提供了一个统一的单标签页界面，用于轻松浏览任何 Git 修订版中所有修改文件的差异。它增强了 Vim 的 diff 模式，允许用户快速查看和比较文件更改。

主要功能包括：

- **差异查看**：打开一个 diff 视图，比较当前索引或指定 Git 修订版中的文件更改。
- **合并工具**：在合并或变基期间，提供 3-way 或 4-way diff 布局，帮助解决冲突。
- **文件历史**：查看指定路径的文件历史记录，包括提交信息和更改追踪。
- **暂存支持**：允许暂存单个 hunk 或文件。
- **自定义布局**：支持多种 diff 布局，如水平、垂直和混合视图。

## 用法

### 安装

使用你的包管理器安装插件，例如：

```vim
" Plug
Plug 'sindrets/diffview.nvim'
```

```lua
-- Packer
use "sindrets/diffview.nvim"
```

### 基本命令

- `:DiffviewOpen [git rev] [options] [ -- {paths...}]`：打开 diff 视图。无参数时比较当前索引。
  - 示例：`:DiffviewOpen HEAD~2` 查看相对于 HEAD~2 的更改。
- `:DiffviewClose`：关闭当前 diff 视图。
- `:DiffviewFileHistory [paths] [options]`：打开文件历史视图。
  - 示例：`:DiffviewFileHistory %` 查看当前文件的历史。
- `:DiffviewToggleFiles`：切换文件面板。
- `:DiffviewFocusFiles`：聚焦文件面板。

### 导航和操作

在 diff 视图中：

- 使用 `<tab>` 和 `<s-tab>` 在文件间切换。
- 使用 `[c` 和 `]c` 在 hunk 间跳转。
- 在文件面板中，使用 `j`/`k` 移动，`<cr>` 打开文件。
- 暂存：编辑索引缓冲区并保存，或在文件面板中使用 `-` 键。

### 配置

插件支持高度自定义，包括布局、键映射和钩子。参考插件文档以获取完整配置选项。

更多详细信息，请查看 [GitHub 仓库](https://github.com/sindrets/diffview.nvim)。
