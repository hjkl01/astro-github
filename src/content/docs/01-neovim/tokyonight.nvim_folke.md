
---
title: tokyonight.nvim
---

# tokyonight.nvim（作者：Folke）

> 项目地址：<https://github.com/folke/tokyonight.nvim>

## 项目概述

- **类型**：Neovim 颜色方案  
- **特色**：浅色与深色双主题，支持 true‑color，兼容 TMUX 与终端。  
- **目标**：提供高度可配置、无缝配合插件的现代色彩方案，易于阅读、可自定义。

---

## 主要特性

| 特性 | 说明 |
|---|---|
| **三种配色变体** | *day*（浅色）、*night*（深色）与 *storm*（暗紫) 可随意切换。 |
| **高色深彩支持** | 兼容 24‑bit 真彩色，以及 256 色终端。 |
| **插件集成** | 自动为 `nvim-treesitter`、`lualine`、`telescope`、`cmp`、`gitsigns`、`lspconfig` 等插件提供匹配 Highlight 组。 |
| **编辑器端 UI 调整** | 支持隐藏非活跃 statusline、winbar，侧边栏（sidebar）主题同步。 |
| **对 LSP/Hover/Snippet 等提示** | 内置 Inlay Hint 与 Diagnostic Highlight 预设。 |
| **高效的默认设置** | 彻底优化 `bold`、`italic`、`underline` 的视觉体验。 |

---

## 支持插件与默认高亮配置

| 插件 | 兼容项 |
|---|---|
| **Treesitter** | 语法高亮、注释、字符串、关键字等。 |
| **Lualine** | 状态栏组件高亮，默认 `lualine_bold = true`。 |
| **Telescope** | 结果列表、预览窗口与浮层。 |
| **cmp** | 自动补全菜单与提示。 |
| **gitsigns** | 撤销/提交、图形化 diff、高亮添加/删除。 |
| **lspkind-nvim** | LSP 类型提示。 |
| **barbecue.nvim** | 文件路径栏高亮。 |
| **mini.nvim** | 各模块（文件树、注释工具等）配色。 |

> *所有插件均可在 `colors.tokyonight` 的 config table 通过 `plugins` 关键字单独细调。*

---

## 安装 & 配置

> 推荐使用 packer/nvim‑lspl 等插件管理器。

```lua
-- packer.nvim 示例
use {
  'folke/tokyonight.nvim',
  config = function()
    require('tokyonight').setup({
      style               = "night",          -- "day" / "night" / "storm"
      transparent         = false,            -- 透明背景
      terminal_colors     = true,             -- 终端配色
      hide_inactive_statusline = true,        -- 隐藏非活跃 statusline
      hide_inactive_winbar = true,            -- 隐藏非活跃 winbar
      sidebars            = { "qf", "vista", "terminal", "packer" },
      dim_nc_background   = false,            -- 非活动窗口 dim
      lualine_bold        = true,             -- Lualine bold
      -- 进一步定制化
      on_colors = function(colors)
        colors.fg_dim = "#777777"
      end,
      on_highlights = function(hl, c)
        hl.TokyonightNormal = { bg = c.bg0 }
        -- 在此添加自定义 highlight
      end
    })
    vim.cmd('colorscheme tokyonight')
  end
}
```

> **切换主题**  
> ```vim
> :colorscheme tokyonight
> :let g:tokyonight_style = "storm" | colorscheme tokyonight
> ```

> **更改配色后重载**  
> ```vim
> :lua require('tokyonight').reload()
> ```

---

## 常用配置项

| 选项 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `style` | string | `"night"` | "day"、"night" 或 "storm" |
| `transparent` | bool | `false` | 让 Neovim 透明背景 |
| `terminal_colors` | bool | `true` | 设置终端 color 方案 |
| `dim_nc_background` | bool | `false` | 非活动窗口 dim |
| `hide_inactive_statusline` | bool | `true` | 隐藏非活跃 statusline |
| `hide_inactive_winbar` | bool | `true` | 隐藏非活跃 winbar |
| `sidebars` | table | `{}` | 侧边栏窗口统一配色 |
| `lualine_bold` | bool | `true` | Lualine 文字加粗 |
| `on_colors` | function | - | 自定义颜色表 |
| `on_highlights` | function | - | 自定义 Highlight 组 |
| `plugins` | table | - | 对各插件的单独设置 |

---

## 主题变体与切换

- **day**: 明亮背景，适合日间使用。  
- **night**: 深色背景，减少光污染。  
- **storm**: 暗紫色背景，中间色带柔和。

> 切换方法示例：  
> ```vim
> :let g:tokyonight_style = "day"
> :colorscheme tokyonight
> ```

---

## 常见问题

- **不显示亮度变化** → 检查 `transparent` 与 TMUX `set-option -g default-terminal`。  
- **插件不匹配** → 在 `setup` 时添加对应插件配置 (`plugins`).  
- **光标颜色不正常** → 通过 `on_colors` 或 `on_highlights` 调整 `CursorLine`、`Cursor`.

---

## 结语

`tokyonight.nvim` 以其多变的配色、兼容广泛的插件生态以及高度可定制的设置，为 Neovim 用户提供了一种现代、舒适且易于扩展的视觉体验。适合日常编码、调试和远程终端工作。