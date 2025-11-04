
---
title: rainbow-delimiters.nvim
---


# Rainbow Delimiters.nvim

**项目地址**  
https://github.com/HiPhish/rainbow-delimiters.nvim

---

## 简介

`Rainbow Delimiters.nvim` 是一款为 Neovim 编写的插件，能够为代码中的各种分隔符（如括号、花括号、方括号、尖括号等）动态分配多种颜色。通过可视化分层，帮助你快速识别对应关系，提升代码可读性与调试效率。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **自定义颜色分级** | 支持多达 15 层不同颜色（`RainbowDelimiter1` ~ `RainbowDelimiter15`） |
| **自动检测文件行数** | `max_file_lines` 选项可限制插件只在文件行数不超过阈值时生效，提高大型文件性能 |
| **可选跳过注释** | `highlight_nondistinct` 与 `disable` 选项可控制是否跳过或禁用某些环境（如注释、文本块） |
| **与各种插件兼容** | 兼容 `nvim-treesitter`、`vim-rainbow` 等语法高亮工具 |
| **轻量级** | 纯 Lua 编写，依赖最小，仅占用几 KB 内存 |

---

## 用法

### 1. 安装

#### 使用 `packer.nvim`

```lua
use {
  'HiPhish/rainbow-delimiters.nvim',
  config = function()
    require('rainbow-delimiters').configure()
  end
}
```

#### 使用 `vim-plug`

```vim
Plug 'HiPhish/rainbow-delimiters.nvim', { 'do': ':lua require("rainbow-delimiters").configure()' }
```

### 2. 配置

```lua
require('rainbow-delimiters').configure({
  -- 颜色分级（默认 5）
  highlight = { 'RainbowDelimiterRed', 'RainbowDelimiterYellow',
                'RainbowDelimiterBlue', 'RainbowDelimiterOrange',
                'RainbowDelimiterGreen' },

  -- 只在文件行数小于等于 3000 时启用
  max_file_lines = 3000,

  -- 跳过注释块（不为单行注释）
  identifier_scope = "local",
})
```

> 注意：确保对应的 `cterm` / `gui` 颜色组在 `init.vim` 或 `init.lua` 已定义，否则会使用默认颜色。

### 3. 快速使用体验

- 打开包含多层括号的文件，光标位于任何括号时，单击 `Ctrl-V`（或指定按键）即可通过光标所在位置快速跳转到对应的另一侧括号。
- 在树莓派等资源受限环境下，只加载前几层颜色即可保持高性能。

---

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 插件无法识别分隔符 | 确认 `cterm` / `gui` 颜色组已定义，且文件类型已正确配置 (`filetype plugin on`) |
| 性能下降 | 调整 `max_file_lines` 或减少 `highlight` 数量 |
| 与 `nvim-treesitter` 冲突 | 在 `treesitter` 配置中禁用高亮或将 `Rainbow` 合并为 `treesitter` 语法文件中的高亮 |

---

## 贡献

欢迎 issue 与 PR！项目采用 MIT 许可证，任何改进和 bug 修复都受到欢迎。

---
