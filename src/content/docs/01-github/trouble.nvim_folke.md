
---
title: trouble.nvim
---


# Trouble.nvim（folke 版）

> **项目地址**：<https://github.com/folke/trouble.nvim>

## 简介
`trouble.nvim` 是一款为 Neovim 设计的诊断、错误、警告、搜索结果等列表插件。它可以将 `:messages`、`quickfix`、`locationlist`、`diagnostics` 等信息以可交互的列表形式展示，极大提升排查和调试效率。

## 主要特性

| 特性 | 说明 |
|------|------|
| **多来源整合** | 同时支持 `quickfix`、`locationlist`、`diagnostics`、`lsp` 消息、`grep` 结果、`lsp` 搜索等多种来源 |
| **可视化界面** | 列表以侧边栏形式展示，支持分组、折叠、颜色高亮 |
| **交互式操作** | 快捷键跳转、折叠/展开、切换来源、过滤、删除等 |
| **自定义配置** | 支持自定义图标、快捷键、窗口布局、过滤规则 |
| **插件集成** | 与 `nvim-lspconfig`、`telescope.nvim`、`fzf-lua` 等插件无缝协作 |
| **可扩展** | 支持插件化的 `trouble` 视图（如 `trouble.nvim` 的 `trouble` 视图） |

## 安装

使用 `lazy.nvim`（推荐）：

```lua
{
  "folke/trouble.nvim",
  dependencies = { "nvim-tree/nvim-web-devicons" },
  opts = {}, -- 可在此处自定义配置
}
```

或者使用 `vim-plug`：

```vim
Plug 'folke/trouble.nvim', {'do': ':UpdateRemotePlugins'}
```

## 基本用法

### 打开/关闭 Trouble 列表

```vim
:TroubleToggle          " 切换显示
:Trouble                " 打开列表
:TroubleClose           " 关闭列表
```

### 诊断（LSP）视图

```vim
:Trouble diagnostics    " 显示当前缓冲区所有诊断
:Trouble lsp             " 显示 LSP 提供的所有信息
```

### Quickfix / Locationlist

```vim
:Trouble quickfix       " 显示 quickfix 列表
:Trouble loclist        " 显示 locationlist 列表
```

### 过滤 & 搜索

- 在列表窗口中按 `f` 进入过滤模式，输入关键词即可过滤条目。
- 按 `r` 刷新列表。

### 快捷键（默认）  

| 快捷键 | 功能 |
|--------|------|
| `Enter` | 跳转到对应的位置 |
| `o` 或 `Enter` | 跳转并关闭列表 |
| `q` | 关闭列表 |
| `r` | 刷新 |
| `x` | 删除条目 |
| `t` | 在新标签页打开 |
| `c` | 复制路径 |
| `p` | 在系统剪贴板复制信息 |
| `f` | 过滤 |
| `k` | 展开/折叠分组 |
| `a` | 切换到所有来源 |

> 你可以通过 `:h trouble.nvim` 查看完整的快捷键列表和高级配置。

## 配置示例

```lua
require('trouble').setup {
  icons = true,
  position = "bottom",     -- "bottom" | "left" | "right" | "top"
  height = 10,             -- 仅当 position 为 bottom/top 时有效
  width = 40,              -- 仅当 position 为 left/right 时有效
  fold_open = true,
  mode = "workspace_diagnostics",
  auto_open = false,
  auto_close = false,
  auto_preview = false,
  auto_fold = true,
  signs = {
    error = "",
    warning = "",
    hint = "",
    information = "",
    other = "﫠",
  },
}
```

## 小技巧

- **快速定位错误**：在 `diagnostics` 视图中按 `Enter`，Neovim 会跳转到对应行并打开编辑器。
- **批量删除**：多选条目后按 `x` 删除。
- **多分组**：`trouble` 视图可以按 LSP 名称或文件分组，便于快速查看。

## 结语

`trouble.nvim` 通过统一、可交互的列表展示了 Neovim 生态中的各种诊断信息，让调试流程更加直观、高效。适配了大多数插件和 LSP 提供的功能，几乎是所有 Neovim 用户的必备工具。祝你使用愉快 🚀

