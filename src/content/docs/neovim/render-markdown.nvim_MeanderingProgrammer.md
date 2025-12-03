
---
title: render-markdown.nvim
---

# [MeanderingProgrammer render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim)



### 中文翻译
该项目是一个基于 Neovim 的 Markdown 渲染插件，使用 Treesitter 解析 Markdown 文件，提供语法高亮、代码块、表格、列表、数学公式等渲染功能，支持自定义处理程序扩展。主要特性包括：
- 通过 Lua 配置支持多种 Markdown 变体（如 Vimwiki、Obsidian）
- 支持代码块语言高亮、表格渲染、数学公式显示
- 提供颜色主题配置（如标题背景色、代码块样式）
- 与 Obsidian.nvim 和 Vimwiki 插件的兼容性设置
- 支持通过 `file_types` 配置扩展解析文件类型
- 提供符号标记、缩进、链接图标等可视化增强功能

---

### 核心内容总结
**功能**  
基于 Treesitter 的 Markdown 渲染插件，支持语法高亮、代码块、表格、数学公式等渲染，提供自定义处理程序扩展。

**使用方法**  
1. 安装依赖（Treesitter、Mini.nvim 等）
2. 通过 Lua 配置插件，设置文件类型（如 `markdown`、`vimwiki`）
3. 配置颜色主题、缩进规则、符号标记等
4. 处理与其他插件（如 Obsidian.nvim）的兼容性（需禁用其 UI）

**主要特性**  
- 支持 Vimwiki、Obsidian 等 Markdown 变体
- 代码块语言高亮、表格渲染、数学公式显示
- 可自定义渲染规则和颜色主题
- 提供符号标记、缩进、链接图标等增强功能
- 支持通过 `file_types` 扩展解析文件类型