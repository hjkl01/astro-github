
---
title: markview.nvim
---

# markview.nvim

**GitHub 地址**  
<https://github.com/OXY2DEV/markview.nvim>

---

## 简介  
`markview.nvim` 是一款为 Neovim 提供 Markdown 视觉化显示的插件。它使用 Tree‑Sitter 解析 Markdown 文档，并为各种 Markdown 语法元素（标题、列表、代码块、表格、引用、TODO列表等）渲染专业的视觉样式。插件几乎不需要任何配置即可使用，使用者只需在 Neovim 中打开 Markdown 文件即可直接看到经过美化的内容。

---

## 主要特性  

| 特性 | 说明 |
|------|------|
| **自动高亮** | 根据 Tree‑Sitter 语法节点为 Markdown 语法元素（标题、列表、代码块、表格、引用、锚点等）自动渲染颜色和样式。 |
| **视觉化列表** | 层级列表采用左对齐点或符号；任务列表（`- [ ]` / `- [x]`）自动显示勾选与未勾选图标。 |
| **表格支持** | 自动根据表格对齐方式渲染边框与空格，对齐方式（左/中/右）均能正确显示。 |
| **代码块高亮** | 支持文件类型语法高亮（如 ` ```js `）并可使用 `vim.ff` 等决定是否显示页眉/页脚。 |
| **关键词高亮** | `TODO`、`FIXME`、`NOTE` 等关键字在文档中会突出显示。 |
| **块引用与链接** | 块引用使用竖线并添加背景色，外链与内部链接不同颜色区分，并支持悬浮预览（插件已内置）。 |
| **自动折叠** | 可自动折叠子标题或列表节，提升阅读体验。 |
| **可配置** | 支持通过 `require('markview').setup{}` 进行细粒度配置，例如：关闭 Markdown 高亮、定制符号、开启/关闭表格渲染等。 |

---

## 安装与使用  

### 1. 安装

#### 使用 packer.nvim

```lua
use {'OXY2DEV/markview.nvim', requires = {'nvim-treesitter/nvim-treesitter'}}
```

#### 使用 lazy.nvim

```lua
{
  'OXY2DEV/markview.nvim',
  dependencies = {'nvim-treesitter/nvim-treesitter'}
}
```

> **注意**：插件需要 Neovim 0.8+ 以及 `nvim-treesitter`，请确保已正确安装并配置好 Treesitter。

### 2. 自动开启（默认）

打开任意 Markdown 文件（扩展名 `.md`）即可自动加载 `markview.nvim`，无需手动开启。

```vim
:hi link MarkviewHeading    Title
:hi link MarkviewTaskChecked NvimLightBlue
```

> 如果想关闭某些特性（例如折叠），可通过设置 `g:markview_disable` 或通过 `setup` 进行更细致配置。

### 3. 手动/全局开启

```vim
" Vimscript
let g:markview_enable = 1

" Lua
vim.g.markview_enable = true
```

### 4. Lua 配置（可选）

```lua
require('markview').setup {
  use_tree_sitter = true,          -- 允许 Tree‑Sitter 高亮
  fold = true,                     -- 自动折叠
  task = {
    enable = true,                 -- 任务列表图标
    icons = {'✖', '✔'},           -- 未完成/已完成图标
  },
  table = {
    enable = true,                 -- 表格渲染
    use_color_border = true,
  },
  link = {
    enable = true,
    color = 'Orange',
  },
}
```

---

## 示例效果

打开 Markdown 文件后你将看到类似下图的视觉效果（仅做示意）：

```
# 这是标题1
## 这是标题2

- [ ] 任务未完成
- [x] 任务已完成

> 这是块引用

```
```bash
print('Hello, world!')
```
```

表格、列表、代码块等元素都会按照上述配置自动渲染，整体阅读体验明显提升。

---

## 贡献

欢迎贡献代码或提交 Issue，详情请参考项目根目录的 `CONTRIBUTING.md`。

---

## 许可证  

MIT © 2024 OXY2DEV

---