
---
title: kanagawa.nvim
---

# kanagawa.nvim (Rebelot)

> GitHub 地址: <https://github.com/rebelot/kanagawa.nvim>

## 项目概述  
`kanagawa.nvim` 是一款为 Neovim 设计的高质量主题，灵感来源于日本传统的水墨画。它提供了多种配色方案，兼具视觉舒适度与可读性，是 Vim 调色板中最受欢迎的主题之一。

## 主要特性 & 功能  
- **多种配色等级**  
  - `wave` – 明亮、暖色系  
  - `lotus` – 暗色、柔和  
  - `dragon` – 高对比、深色  
- **丰富的语法高亮**  
  提供对主流语言（如 JavaScript/TypeScript、Rust、Python、Go 等）的精准高亮。  
- **高可定制性**  
  - 支持自定义 `colorscheme`、`transparent`、`dim-inactive` 等选项。  
  - 可以通过 `link` 将特定语法元素链接到已有的高亮组。  
- **兼容多插件**  
  支持 `treesitter`、`lualine`、`nvim-cmp`、`telescope`、`fzf` 等常见插件的高亮兼容。  
- **精细的光标与侧边栏亮度处理**  
  优化的光标样式和侧边栏缩放，使编辑体验更舒适。  
- **对 VSCode 风格的配色支持**  
  通过 `kanagawa.sublime` 主题兼容 Sypmate 等编辑器。  

## 安装与配置  

使用插件管理器（以 `lazy.nvim` 为例）：

```lua
{
  'rebelot/kanagawa.nvim',
  priority = 1000,
  config = function()
    vim.cmd('colorscheme kanagawa')
    -- 可选：自定义主题选项
    vim.g.kanagawa_override = {
      theme = {
        wave = {
          ui = {
            bg = { normal = '#1f1f28', visual = '#444957' }
          }
        }
      }
    }
 end
}
```

常见安装方式（Vim-Plug）：

```vim
Plug 'rebelot/kanagawa.nvim'
```

然后在 `init.vim` 或 `init.lua` 中：

```vim
colorscheme kanagawa
```

## 简单使用场景  
- **日常编程**：可以直接使用 `kanagawa`，无需额外配置。  
- **分屏/多窗口**: `dim-inactive` 开启后，未聚焦窗口会自动变暗。  
- **夜间阅读**：切换到 `dragon` 配色，获得更深沉、对比度更大的视觉体验。  
- **透明背景**：在支持透明的终端中，`transparent = true` 可以让窗口内容透过终端背景显示。  

## 关键配置示例

```lua
vim.g.kanagawa = {
  theme = 'dragon',          -- 主题选择: wave | lotus | dragon
  background = {             -- 背景设置
    light = 'wave',
    dark = 'lotus',
  },
  dim_inactive = true,      -- 未聚焦窗口变暗
  style = {                 -- 样式定制
    transparent = true,     -- 透明背景
    background = 'none',    -- 对 `lt` 主题透明处理
  },
  colors = {                -- 自定义颜色
    ui = {
      bg          = { normal = '#11101b', visual = '#302f34' },
      bg_gutter   = { normal = nil, visual = '#302f34' },
    },
  },
}
vim.cmd('colorscheme kanagawa')
```

## 兼容插件举例

```lua
-- lualine
require('lualine').setup{
  options = { theme = 'kanagawa' }
}
-- nvim-cmp
require('cmp').setup{
  formatting = {
    format = function(entry, vim_item)
      vim_item.kind = '●'
      return vim_item
    end
  }
}
```

## 维护与支持  
- 开发者: `RebelOt`  
- 许可证: MIT  
- 文档: 请参阅项目 README 以及 `lua/kanagawa` 目录下的配置文件。  

---

> **保存方式**  
> 将上述 Markdown 内容保存为文件路径：  
> ```
> src/content/docs/00/kanagawa.nvim_rebelot.md
> 