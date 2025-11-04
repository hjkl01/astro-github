
---
title: todo-comments.nvim
---


# todo-comments.nvim (folke)

- **项目地址**：<https://github.com/folke/todo-comments.nvim>

## 概述
`todo-comments.nvim` 是一个 Neovim 插件，用于在代码中高亮显示、搜索和导航 `TODO`、`FIXME`、`HACK` 等标签。它支持多种关键字、颜色主题以及与 Telescope、LSP、Grep 等工具集成。

## 安装
使用插件管理器安装（以 `lazy.nvim` 为例）：

```lua
{
  "folke/todo-comments.nvim",
  dependencies = { "nvim-lua/plenary.nvim" },
  opts = {},
}
```

## 配置
默认配置已足够使用，若想自定义可在 `opts` 中添加：

```lua
{
  signs = true,          -- 在 gutter 显示符号
  line_custom_colors = {  -- 自定义行高亮颜色
    INFO = "#00b0ff",
  },
  keywords = {          -- 自定义关键词
    TODO = { icon = " ", color = "info", alt = { "TODO" } },
    HACK = { icon = " ", color = "warning", alt = { "HACK" } },
  },
}
```

## 用法

### 高亮
插件会自动在编辑器中高亮所有配置的关键字。可以通过 `:TodoToggle` 切换高亮显示。

### 搜索
- **Telescope 集成**：`<leader>ft` 调出带过滤器的 Todo 列表。
- **Grep**：`<leader>fg` 通过 `:TodoGrep` 在全局搜索。

### 跳转
- `]t` / `[t`：跳转到下一个/上一个 Todo。
- `gd`：跳转到当前行的关键字。

### 显示信息
- `:TodoInfo`：显示关于插件的帮助信息。

## 主要特性

| 功能 | 描述 |
|------|------|
| **多关键字支持** | 默认支持 `TODO`, `FIXME`, `HACK`, `NOTE`, `BUG`，可自定义。 |
| **自定义颜色 & 图标** | 每个关键字可设置独立图标、颜色与自定义高亮。 |
| **Gutter signs** | 在行号侧栏显示符号，方便快速定位。 |
| **Telescope / LSP 集成** | 通过 Telescope 搜索、跳转；可与 LSP 语义高亮配合。 |
| **全局搜索** | 使用 `:TodoGrep` 或 Telescope 进行文件范围搜索。 |
| **跳转快捷键** | `]t` / `[t` 以及 `gd` 快捷跳转。 |
| **可配置高亮开关** | `:TodoToggle` 在需要时关闭高亮，保持干净编辑环境。 |
| **多语言支持** | 通过正则匹配，支持多种语言的注释格式。 |

## 常用命令

| 命令 | 作用 |
|------|------|
| `:TodoToggle` | 开/关 Todo 高亮 |
| `:TodoInfo` | 查看插件信息 |
| `:TodoGrep` | 全局搜索 Todo |
| `:TodoQuickFix` | 打开 QuickFix 列表 |
| `:TodoTelescope` | 通过 Telescope 打开列表 |
| `:TodoLocList` | 打开 LocList 列表 |

## 贡献
如需提交流程请访问项目主页的 **Issues** 或 **Pull Requests**。

---

**文件路径**：`src/content/docs/00/todo-comments.nvim_folke.md`
