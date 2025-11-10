---
title: feline.nvim
---

# Feline.nvim 项目

**项目地址：** [https://github.com/feline-nvim/feline.nvim](https://github.com/feline-nvim/feline.nvim)

## 主要特性
Feline.nvim 是一个高度可自定义的 Neovim 状态栏插件，灵感来源于 Vim 的 Airline 和 Lightline。它采用模块化设计，支持 Lua 配置，提供丰富的组件和主题选项。主要特性包括：
- **模块化组件**：内置多种预定义组件，如文件信息、Git 状态、LSP 诊断、模式指示器等，用户可以轻松组合和自定义。
- **高性能**：使用 Lua 实现，渲染效率高，支持异步更新，避免卡顿。
- **主题支持**：兼容多种颜色方案（如 Tokyo Night、Gruvbox），并允许用户自定义颜色和样式。
- **灵活配置**：支持左右侧栏独立配置、条件显示组件，以及与 vi-mode 和 nvim-bufferline 等插件集成。
- **扩展性**：易于添加自定义组件，支持 Lua 函数作为组件内容。

## 功能
- **状态栏显示**：实时显示当前文件路径、行号、列号、文件大小、编码格式等基本信息。
- **Git 集成**：显示分支、变更统计（添加/删除行数）、文件状态。
- **LSP 支持**：集成 LSP 客户端，显示诊断信息（错误、警告、提示）、代码动作。
- **模式指示**：视觉化显示 Normal、Insert、Visual 等模式，支持颜色高亮。
- **进度条和分隔符**：自定义分隔符和进度条，用于美化界面。
- **多缓冲区支持**：与缓冲区管理插件协作，显示缓冲区标签或索引。

## 用法
1. **安装**：使用插件管理器安装，例如 Packer：
   ```
   use { 'feline-nvim/feline.nvim', requires = { 'nvim-tree/nvim-web-devicons', 'luukvbaal/statuscol.nvim' } }
   ```
   或 Lazy.nvim：
   ```
   { 'feline-nvim/feline.nvim', dependencies = { 'nvim-tree/nvim-web-devicons' } }
   ```

2. **基本配置**：在 `init.lua` 中设置：
   ```lua
   require('feline').setup {
     theme = 'auto',  -- 或指定主题如 'morning'
     default_bg = nil,  -- 默认背景
     properties = {
       force_inactive = {
         filetypes = { 'NvimTree' },
         buftypes = { 'terminal' },
       },
     },
   }
   ```
   这将启用默认配置。运行 `:checkhealth feline` 检查状态。

3. **自定义组件**：创建自定义提供者函数：
   ```lua
   local vi_mode_utils = require('feline.providers.vi_mode')
   local components = {
     active = {
       left = {
         { provider = 'vi_mode', hl = function() return { name = vi_mode_utils.get_mode_highlight_name(), fg = vi_mode_utils.get_mode_color() } end },
         { provider = 'file_info', hl = { fg = 'white', bg = 'bright_bg' } },
       },
       -- 更多配置...
     },
   }
   require('feline').setup { components = components }
   ```

4. **高级用法**：
   - **条件显示**：使用 `opts` 中的 `cond` 函数控制组件显示，例如仅在非空缓冲区显示。
   - **事件处理**：通过 `properties` 配置事件钩子，如文件保存后更新 Git 状态。
   - **主题自定义**：编辑 `colors` 表调整颜色，例如 `colors.fg = '#ffffff'`。
   - **禁用默认**：设置 `properties.presets = 'no_statusline'` 完全自定义。

详细文档见项目 README 和 `:help feline`。