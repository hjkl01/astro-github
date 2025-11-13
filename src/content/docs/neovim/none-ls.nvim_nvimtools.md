---
title: none-ls.nvim
---

# none-ls.nvim

## 项目简介

none-ls.nvim（原 null-ls.nvim）是一个 Neovim 插件，它允许使用 Neovim 作为语言服务器，通过 Lua 注入 LSP 诊断、代码操作等功能。该项目由社区维护，是 null-ls.nvim 的重载版本。

## 主要功能

- **代码操作 (Code Actions)**: 提供代码重构和修复建议。
- **诊断 (Diagnostics)**: 支持文件级和项目级诊断，包括语法检查和错误报告。
- **格式化 (Formatting)**: 支持代码格式化，包括范围格式化。
- **悬停 (Hover)**: 提供悬停信息，如文档或类型信息。
- **补全 (Completion)**: 提供代码补全建议。

该插件内置了许多源，并提供辅助工具来创建自定义源，无需外部进程，提高性能。

## 用法

1. 安装插件（依赖 plenary.nvim）。
2. 在配置中设置 null-ls 并注册源：

```lua
local null_ls = require("null-ls")

null_ls.setup({
    sources = {
        null_ls.builtins.formatting.stylua,
        null_ls.builtins.completion.spell,
        -- 添加更多源
    },
})
```

3. 使用 LSP 功能，如 `:lua vim.lsp.buf.format()` 进行格式化。

更多配置和内置源请参考项目文档。
