---
title: bufferline.nvim
---

# bufferline.nvim

**GitHub 地址**: <https://github.com/akinsho/bufferline.nvim>

## 项目简介
`bufferline.nvim` 是 Neovim 的一个插件，用于在顶部提供类似选择栏的缓冲区条（Bufferline）。它让你可以直观地查看、切换和管理打开的缓冲区，支持丰富的图标、状态指示、标签、自定义样式等功能。

## 主要特性
- **缓冲区标签显示**：在窗口顶部以标签形式展示所有打开的缓冲区名称，支持多列滚动。
- **图标支持**：集成 NERDTree、Lualine、catppuccin 等主题的图标，可显示文件图标、状态图标等。
- **缓冲区排序**：按访问顺序、加载顺序、或手动拖拽重新排序。
- **切换快捷键**：默认采用 `<Ctrl-s>` 组合键快速切换缓冲区，也可以设置自定义映射。
- **可关闭缓冲区**：使用 `x` 或 `X` 关闭标签栏中的缓冲区，支持多选关闭。
- **标签高亮**：根据缓冲区状态（未保存、含错误、正被使用等）自动高亮显示。
- **支持 Neovim 0.10+**，但也兼容旧版本（需禁止图标）。
- **主题兼容**：内置多种主题样式（`default`, `palenight`, `tokyonight`, `catppuccin` 等），可完全自定义颜色和字体。
- **插件依赖**：需要 `nvim-web-devicons` (用于文件图标) 与 `nvim-lspconfig` 或 `nvim-treesitter`（同名进行协同工作）。

## 基本使用

### 安装（推荐使用插件管理器）

```lua
-- packer.nvim
use {
  'akinsho/bufferline.nvim',
  requires = 'kyazdani42/nvim-web-devicons',  -- 可选，用于显示图标
  tag = "v3.*",
  config = function()
    require('bufferline').setup {}
  end
}
```

### 配置示例（Lua）

```lua
require('bufferline').setup {
  options = {
    -- 关闭缓冲区的快捷键
    close_command = "bd",  -- 关闭缓冲区命令
    right_mouse_command = "buffer <c-r>",  -- 右键切换
    left_mouse_command = "buffer <c-l>",   -- 左键切换

    -- 显示文件图标
    show_icons = true,
    icon_separator_active = '',
    icon_separator_inactive = '',

    -- 高亮设置
    buffer_close_icon = '',
    modified_icon = '●',
    close_icon = '',
    diagnostics = "nvim_lsp",

    -- 缓冲区列表长度
    max_name_length = 30,
    max_prefix_length = 30,

    separator_style = "thin",
    color_icons = true,
    show_buffer_icons = true,
    show_buffer_close_icons = true,
    show_close_icon = false,
    show_tab_indicators = true,

    enforce_regular_tabs = false,
    always_show_bufferline = true,
    hover = {
      enabled = true,
      delay = 200,
      reveal = {"close"}
    }
  }
}
```

### 快捷键（默认）

| 键位 | 操作 |
|------|------|
| `<C-s>` | 下一缓冲区 |
| `<C-S>` | 上一缓冲区 |
| `x`    | 关闭当前检视栏缓冲区 |
| `X`    | 关闭其他缓冲区 |
| `<Tab>` | 右侧缓冲区 |
| `<S-Tab>` | 左侧缓冲区 |

> 你可以在 `init.lua` 或 `init.vim` 中自定义上述映射。

## 进阶功能

| 功能 | 说明 |
|------|------|
| **自动关闭未保存缓冲区** | 通过 `auto_save` 选项实现 |
| **可展示 LSP 错误/警告** | `diagnostics` 官方集成 |
| **多标签页支持** | 通过 `tabpages` 选项与 Tabline 集成 |
| **缓存可视化** | 通过 `separator_style` 设置不同分隔线样式 |
| **多标签窗格** | `both` & `separator_style` 兼容多窗口 |

## 参考文档

- [官方 Wiki](https://github.com/akinsho/bufferline.nvim/wiki)
- [插件配置范例](https://github.com/akinsho/bufferline.nvim)

---
> 以上描述基于最新 `v3.*` 版本，使用时请根据自己的 Neovim 版本或插件管理器进行相应调整。祝用得愉快！