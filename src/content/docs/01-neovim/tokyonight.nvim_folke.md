
---
title: tokyonight.nvim
---


# tokyonight.nvim (by folke)

GitHub 地址：<https://github.com/folke/tokyonight.nvim>

---

## 🎨 主要特性

- **多种配色风格**  
  - `night`（默认）: 适合深色背景，强调可读性。  
  - `storm`: 暗色系但更柔和，适合长时间使用。  
  - `day`: 明亮的浅色背景，适合日间使用。  
-可定制性**  
  - 通过 `style`, `terminal_colors`, `sidebars`, `hide_inactive_statusline` 等选项轻松调整。  
- **与 Neovim 原生终端兼容**  
  - 可在 Neovim 内置终端中使用同一配色。  
- **插件兼容**  
  - 自动补全（nvim-cmp）、文件树（nvim-tree）、Git 指示、LSP、插件状态栏等均可无缝使用。  
- **高亮主题**  
  - 支持 `lualine`, `nvim-web-devicons`, `bufferline.nvim`, `gitsigns.nvim` 等插件的高亮设定。  
- **色彩平滑的视觉体验**  
  - 采用 `tokyonight` 主题色彩，保证在高对比度模式下也能保持舒适的阅读体验。  

---

## 🚀 使用方法

### 1. 安装

#### 使用 `packer.nvim`

```lua
use {
  'folke/tokyonight.nvim',
  opt = true
}
```

```lua
-- 完整示例
require('packer').startup(function()
  use {
    'folke/tokyonight.nvim',
    opt = true
  }
  -- 安装完毕后
  vim.cmd('colorscheme tokyonight')
end)
```

#### 使用 `vim-plug`

```vim
Plug 'folke/tokyonight.nvim'
```

然后执行 `:PlugInstall` 并重启 Neovim。

---

### 2. 基本设置

```lua
vim.g.tokyonight_style = 'storm'          -- 位置: night / storm / day
vim.g.tokyonight_italic_comments = true   -- 备注文本斜体
vim.g.tokyonight_dark_sidebar = true      -- 侧边栏深色化
vim.g.tokyonight_terminal_colors = true   -- 终端颜色同步
```

---

### 3. 主题配置示例

```lua
require('tokyonight').setup({
  style = "night",
  transparent = false,
  terminal_colors = true,
  dim_inactive = false,
  styles = {
    comments = {italic = true},
    keywords = {italic = true},
    functions = {},
    variables = {},
    strings = {},
    numerals = {},
    booleans = {},
    properties = {}
  },
  sidebars = { "qf", "vista_kind", "terminal", "packer" },
  hide_inactive_statusline = false,
  fold_style = "default",
})
```

---

### 4. 兼容插件 (按需开启)

```lua
-- nvim-web-devicons
vim.g.tokyonight_devicons = true

-- lualine
require('lualine').setup({
  options = {
    theme = "tokyonight",
  }
})

-- nvim-tree
require('nvim-tree').setup({
  renderer = {
    icons = {show = {file = true, folder = true, git = true}},
    highlight_git = true,
    highlight_opened_files = "all",
  }
})
```

---

### 5. 在终端中调整配色

```lua
vim.g.tokyonight_terminal_colors = true
-- 重新加载后，保证终端内的 ANSI 颜色与主题保持一致
```

---

## 📄 关键键绑定

| 键位 | 功能 |
|------|------|
| `:colorscheme tonynight` | 切换主题 |
| `:TL` (或者自快捷键) | 切换 `light/dark` 样式 |

---

## 👋 结束语

`tokyonight.nvim` 是一款高度定制、配色优雅、与 Neovim 生态深度兼容的主题，适合各种工作时间与环境。通过简单配置即可在编辑、终端、插件等多层面保持视觉一致。祝你愉快使用！