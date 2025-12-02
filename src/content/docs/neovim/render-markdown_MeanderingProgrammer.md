---
title: render-markdown.nvim
---

## 功能介绍

render-markdown.nvim 是一个 Neovim 插件，旨在改善在 Neovim 编辑器中查看 Markdown 文件的体验。它通过渲染 Markdown 元素（如标题、代码块、列表、表格、引用等）来增强可读性，同时保持原始文本的完整性。

### 主要功能

- **标题渲染**：为不同级别的标题添加图标、背景色和边框。
- **代码块渲染**：支持代码块的背景高亮、语言图标显示，并可隐藏分隔符。
- **列表和复选框**：渲染列表项目符号和任务复选框，支持自定义状态。
- **表格渲染**：美化表格显示，包括边框、对齐指示器等。
- **引用和标注**：渲染块引用和 GitHub/Obsidian 风格的标注。
- **链接渲染**：为不同类型的链接添加图标，如图片、邮件、超链接等。
- **LaTeX 渲染**：支持数学公式的渲染（需要额外依赖）。
- **内联高亮**：支持 Obsidian 风格的内联高亮。
- **缩进模式**：模拟 org-indent-mode，根据标题级别缩进内容。

### 特性

- **自包含**：完全在 Neovim 内部运行，无需外部窗口。
- **可配置**：所有组件、填充、图标和颜色均可自定义。
- **文件类型无关**：可渲染注入到任何文件中的 Markdown。
- **模式渲染**：根据 Vim 模式在渲染和原始视图之间切换。
- **反隐藏**：在光标行隐藏添加的虚拟文本。
- **窗口选项**：在渲染和原始视图之间更改选项值。
- **大文件支持**：仅渲染可见范围，可根据大小完全禁用。
- **自定义渲染**：提供扩展点，用户可添加任何内容。

## 用法

### 安装

使用 lazy.nvim：

```lua
{
    'MeanderingProgrammer/render-markdown.nvim',
    dependencies = { 'nvim-treesitter/nvim-treesitter', 'nvim-mini/mini.nvim' },
    ---@module 'render-markdown'
    ---@type render.md.UserConfig
    opts = {},
}
```

### 命令

- `:RenderMarkdown` 或 `:RenderMarkdown enable`：启用渲染
- `:RenderMarkdown disable`：禁用渲染
- `:RenderMarkdown toggle`：切换渲染状态
- `:RenderMarkdown preview`：在侧边显示渲染的缓冲区
- `:RenderMarkdown log`：打开插件日志文件

### 配置示例

```lua
require('render-markdown').setup({
    enabled = true,
    render_modes = { 'n', 'c', 't' },
    heading = {
        enabled = true,
        icons = { '󰲡 ', '󰲣 ', '󰲥 ', '󰲧 ', '󰲩 ', '󰲫 ' },
    },
    code = {
        enabled = true,
        style = 'full',
    },
    checkbox = {
        enabled = true,
        custom = {
            todo = { raw = '\\[-\\]', rendered = '󰥔 ', highlight = 'RenderMarkdownTodo' },
        },
    },
})
```

### 要求

- Neovim >= 0.9.0（推荐 >= 0.10.0）
- Nerd 字体符号
- Treesitter 解析器：markdown、markdown_inline（可选：html、latex、yaml）
- 图标提供者（可选）：mini.icons 或 nvim-web-devicons
- 系统依赖（可选）：libtexprintf 或 pylatexenc 用于 LaTeX 渲染

该插件极大地提升了在 Neovim 中编辑和查看 Markdown 文件的用户体验，通过视觉渲染使文档更加直观易读。
