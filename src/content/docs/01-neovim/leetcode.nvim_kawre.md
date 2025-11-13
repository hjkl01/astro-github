---
title: leetcode.nvim
---

## 功能介绍

`leetcode.nvim` 是一个 Neovim 插件，允许你在 Neovim 编辑器中直接解决 LeetCode 问题。它提供了直观的仪表板、问题描述格式化、LeetCode 个人资料统计、每日和随机问题支持，以及缓存优化性能等功能。

### 主要特性

- 📌 直观的仪表板，便于在插件内导航
- 😍 问题描述格式化，提升可读性
- 📈 在 Neovim 中显示 LeetCode 个人资料统计
- 🔀 支持每日和随机问题
- 💾 缓存机制，优化性能

## 用法

### 安装

使用 lazy.nvim 安装：

```lua
{
    "kawre/leetcode.nvim",
    build = ":TSUpdate html", -- 如果安装了 nvim-treesitter
    dependencies = {
        -- 选择一个 picker，如 telescope 或 fzf-lua
        "nvim-lua/plenary.nvim",
        "MunifTanjim/nui.nvim",
    },
    opts = {
        -- 配置选项
    },
}
```

### 配置

默认配置包括语言设置、存储路径、插件选项等。支持多种 picker 如 telescope、fzf-lua 等。

### 命令

- `:Leet` - 打开菜单仪表板
- `:Leet list` - 打开所有可用问题的选择器
- `:Leet random` - 打开随机问题
- `:Leet daily` - 打开今日问题
- `:Leet run` - 运行当前问题
- `:Leet submit` - 提交当前问题

### 启动方式

可以通过两种方式启动：

1. 作为 Neovim 参数：`nvim leetcode.nvim`
2. 在 Neovim 中使用 `:Leet` 命令（需要非独立模式）

### 登录

需要从浏览器复制 Cookie 来登录 LeetCode。

### 常见问题

- 如果遇到 Cookie 过期错误，可能需要等待或更新 Cookie。
- 支持多种编程语言，如 C++、Java、Python 等。
