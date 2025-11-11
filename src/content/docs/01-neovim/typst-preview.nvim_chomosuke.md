---
title: typst-preview.nvim
---

# typst-preview.nvim

typst-preview.nvim 是一个为 Neovim 设计的低延迟 Typst 预览插件。它基于 [Myriad-Dreamin/tinymist](https://github.com/Myriad-Dreamin/tinymist)，提供实时预览功能。

## 功能特性

- **低延迟预览**：通过增量渲染技术，实现输入时的即时预览。
- **交叉跳转**：支持在代码和预览之间跳转，可以点击预览跳转到对应代码位置，并跟随光标滚动。

## 安装

### 依赖

- curl

### 使用 Lazy.nvim

```lua
{
  'chomosuke/typst-preview.nvim',
  lazy = false, -- 或 ft = 'typst'
  version = '1.*',
  opts = {}, -- lazy.nvim 会隐式调用 setup {}
}
```

### 使用 Packer.nvim

```lua
use {
  'chomosuke/typst-preview.nvim',
  tag = 'v1.*',
  config = function()
    require 'typst-preview'.setup {}
  end,
}
```

### 使用 vim-plug

```vim
Plug 'chomosuke/typst-preview.nvim', {'tag': 'v1.*'}
```

## 用法

### 命令

- `:TypstPreviewUpdate`：下载必要的二进制文件到数据目录。
- `:TypstPreview`：启动预览，可选指定模式 `:TypstPreview document`（默认）或 `:TypstPreview slide`（幻灯片模式）。
- `:TypstPreviewStop`：停止预览。
- `:TypstPreviewToggle`：切换预览。
- `:TypstPreviewFollowCursor`：跟随光标滚动预览。
- `:TypstPreviewNoFollowCursor`：不跟随光标滚动。
- `:TypstPreviewFollowCursorToggle`：切换跟随光标模式。
- `:TypstPreviewSyncCursor`：将预览滚动到当前光标位置。

### 配置

插件开箱即用，但需要调用 `setup()` 来确保二进制文件已下载。

默认配置：

```lua
require 'typst-preview'.setup {
  debug = false,
  open_cmd = nil,
  port = 0,
  invert_colors = 'never',
  follow_cursor = true,
  dependencies_bin = {
    ['tinymist'] = nil,
    ['websocat'] = nil
  },
  extra_args = nil,
  get_root = function(path_of_main_file)
    local root = os.getenv 'TYPST_ROOT'
    if root then
      return root
    end
    return vim.fn.fnamemodify(path_of_main_file, ':p:h')
  end,
  get_main_file = function(path_of_buffer)
    return path_of_buffer
  end,
}
```
