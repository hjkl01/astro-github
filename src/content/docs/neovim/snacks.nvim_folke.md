---
title: snacks.nvim
---

# snacks.nvim

snacks.nvim 是一个为 Neovim 提供高质量生活 (QoL) 插件的集合，由 folke 创建。它包含多个小型插件，用于增强 Neovim 的功能和用户体验。

## 功能特性

snacks.nvim 提供了以下插件模块：

- **animate**: 高效动画库，支持超过 45 种缓动函数
- **bigfile**: 处理大文件
- **bufdelete**: 删除缓冲区而不破坏窗口布局
- **dashboard**: 美观的声明式仪表板
- **debug**: 调试用的漂亮检查和回溯
- **dim**: 通过调暗其余部分来聚焦活动范围
- **explorer**: 文件浏览器 (伪装成选择器)
- **gh**: GitHub CLI 集成
- **git**: Git 工具
- **gitbrowse**: 在浏览器中打开当前文件、分支、提交或仓库
- **image**: 使用 Kitty 图形协议的图像查看器
- **indent**: 缩进指南和范围
- **input**: 更好的 `vim.ui.input`
- **keymap**: 支持文件类型和 LSP 客户端的更好 `vim.keymap`
- **layout**: 窗口布局
- **lazygit**: 在浮动窗口中打开 LazyGit，自动配置配色方案和 Neovim 集成
- **notifier**: 漂亮的 `vim.notify`
- **notify**: 处理 Neovim `vim.notify` 的工具函数
- **picker**: 选择项目的选择器
- **profiler**: Neovim Lua 性能分析器
- **quickfile**: 快速渲染文件，在加载插件之前
- **rename**: LSP 集成的文件重命名，支持 neo-tree.nvim 和 mini.files 等插件
- **scope**: 基于 treesitter 或缩进的范围检测、文本对象和跳转
- **scratch**: 带有持久文件的草稿缓冲区
- **scroll**: 平滑滚动
- **statuscolumn**: 漂亮的状态列
- **terminal**: 创建和切换浮动/分割终端
- **toggle**: 与 which-key 图标/颜色集成的切换键映射
- **util**: Snacks 的工具函数库
- **win**: 创建和管理浮动窗口或分割
- **words**: 自动显示 LSP 引用并快速导航
- **zen**: 禅模式 • 无干扰编码

## 要求

- Neovim >= 0.9.4
- 可选：mini.icons、nvim-web-devicons 和 Nerd Font 以获得更好的图标支持

## 安装

使用 lazy.nvim 安装：

```lua
{
  "folke/snacks.nvim",
  priority = 1000,
  lazy = false,
  ---@type snacks.Config
  opts = {
    -- 启用所需的插件
    bigfile = { enabled = true },
    dashboard = { enabled = true },
    explorer = { enabled = true },
    indent = { enabled = true },
    input = { enabled = true },
    picker = { enabled = true },
    notifier = { enabled = true },
    quickfile = { enabled = true },
    scope = { enabled = true },
    scroll = { enabled = true },
    statuscolumn = { enabled = true },
    words = { enabled = true },
  },
}
```

## 用法

snacks.nvim 提供了丰富的键映射和功能。例如：

- `<leader><space>`: 智能查找文件
- `<leader>/`: 全局搜索
- `<leader>e`: 文件浏览器
- `<leader>z`: 切换禅模式
- `<leader>.`: 切换草稿缓冲区
- `<leader>gg`: 打开 LazyGit
- `gd`: 跳转到定义
- `gr`: 查找引用

更多用法请参考项目的 README 和各个插件的文档。
