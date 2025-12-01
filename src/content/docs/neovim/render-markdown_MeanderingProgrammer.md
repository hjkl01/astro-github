---
title: render-markdown.nvim
---

# render-markdown.nvim 介绍

## 项目概述

`render-markdown.nvim` 是一个 Neovim 插件，用于改善 Markdown 文件的查看体验。它通过渲染 Markdown 组件（如标题、代码块、列表、表格等）来提供更直观的视觉效果，完全在 Neovim 内部运行，无需外部窗口。

## 主要功能

- **渲染组件**：支持标题、代码块、内联代码、水平分割线、列表项目、复选框、引用块、标注、表格、链接、LaTeX 公式等。
- **模式切换**：根据 Vim 模式（正常、命令、终端）自动切换渲染和原始视图。
- **自定义配置**：所有组件的图标、颜色、填充、边框等均可自定义。
- **文件类型支持**：可渲染注入到任何文件中的 Markdown 内容。
- **性能优化**：仅渲染可见区域，支持大文件禁用。
- **扩展性**：提供自定义渲染扩展点。

## 安装

推荐使用 `lazy.nvim` 进行安装：

```lua
{
    'MeanderingProgrammer/render-markdown.nvim',
    dependencies = { 'nvim-treesitter/nvim-treesitter', 'nvim-mini/mini.nvim' },
    ---@module 'render-markdown'
    ---@type render.md.UserConfig
    opts = {},
}
```

其他插件管理器如 `rocks.nvim`、`packer.nvim` 等也支持，详见项目 README。

## 配置

插件默认启用，可通过 `opts` 自定义配置。例如：

```lua
require('render-markdown').setup({
    enabled = true,  -- 默认启用
    render_modes = { 'n', 'c', 't' },  -- 渲染模式
    heading = {
        enabled = true,
        icons = { '󰲡 ', '󰲣 ', '󰲥 ', '󰲧 ', '󰲩 ', '󰲫 ' },  -- 标题图标
    },
    code = {
        enabled = true,
        style = 'full',  -- 代码块样式
    },
    -- 更多选项见默认配置
})
```

## 用法

- 安装后自动渲染 Markdown 文件。
- 使用命令切换：
  - `:RenderMarkdown toggle` - 切换渲染状态
  - `:RenderMarkdown enable` - 启用渲染
  - `:RenderMarkdown disable` - 禁用渲染
- 支持补全复选框和标注（需启用 LSP 补全）。

更多详情请参考 [GitHub 项目页面](https://github.com/MeanderingProgrammer/render-markdown.nvim)。
