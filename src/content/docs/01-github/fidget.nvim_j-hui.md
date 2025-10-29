
---
title: fidget.nvim
---


# fidget.nvim

> **项目地址**: https://github.com/j-hui/fidget.nvim

## 简介

fidget.nvim 是一个为 Neovim 设计的轻量级进度条插件，专门用来展示异步任务（如 LSP、补全、编译等）的执行状态。它以可视化、非侵入式的方式，让你在后台任务执行时获得即时反馈，提升开发效率。

## 主要特性

| 特性 | 说明 |
|------|------|
| **异步任务监控** | 自动捕捉 Neovim 的异步事件（如 LSP 请求、编译、补全等）并显示进度。 |
| **可配置 UI** | 支持多种样式与主题，提供自定义动画、字体、颜色等选项。 |
| **轻量高效** | 仅依赖 Neovim 内置 API，无需额外依赖，最小化资源占用。 |
| **可定制化** | 通过 Lua 配置文件灵活调整行为，例如隐藏特定事件、设置延迟、调整显示位置等。 |
| **多语言 & LSP 支持** | 与 Neovim LSP 集成，自动显示 LSP 进度、诊断、格式化等信息。 |
| **可扩展** | 允许插件作者通过 `fidget:register` 注册自定义事件与动画。 |

## 用法

### 安装

使用插件管理器（示例为 `lazy.nvim`）：

```lua
{
  "j-hui/fidget.nvim",
  opts = {}  -- 直接使用默认配置
}
```

或使用 `vim-plug`：

```vim
Plug 'j-hui/fidget.nvim'
```

### 基本配置

```lua
require('fidget').setup {
  -- 是否显示进度条
  progress = {
    display = true,
    -- 进度条显示的最小长度
    min_width = 40
  },

  -- 动画设置
  animation = {
    -- 进度条动画，支持 'none', 'dots', 'bars', 'spinner', 'progress' 等
    progress = "dots"
  },

  -- 主题样式
  theme = {
    -- 可以直接指定颜色或使用内置主题
    background = "#282c34",
    foreground = "#98c379"
  },

  -- 事件过滤
  filter = {
    -- 仅显示 LSP 相关事件
    lsp = true,
    -- 关闭诊断进度显示
    diagnostics = false
  },

  -- 自定义显示位置
  position = {
    -- 0 = top, 1 = bottom
    row = 0,
    -- 0 = left, 1 = right
    col = 1
  }
}
```

### 高级用法

#### 自定义事件

你可以通过 `fidget:register` 注册自己的异步事件：

```lua
require('fidget').register({
  name = "my_custom_task",
  start = { title = "开始自定义任务" },
  done = { title = "完成自定义任务" }
})
```

#### 修改动画

```lua
require('fidget').setup({
  animation = {
    progress = "bars"  -- 更换为进度条动画
  }
})
```

#### 隐藏特定任务

```lua
require('fidget').setup({
  filter = {
    format = false  -- 隐藏格式化进度
  }
})
```

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 进度条不显示 | 检查是否安装了 LSP 并且有异步请求；确保 `fidget` 已正确加载。 |
| 颜色不匹配 | 调整 `theme` 配置，或使用 `vim.api.nvim_set_hl` 手动设置。 |
| 速度慢 | 关闭或减少 `animation` 选项；将 `min_width` 设置为更小值。 |

---

**提示**：查看插件仓库中的 `README.md` 和 `docs` 目录获取更详细的配置示例和更新日志。祝你使用愉快！
