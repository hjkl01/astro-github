
---
title: conform.nvim
---

# conform.nvim 项目

## 项目地址
[https://github.com/stevearc/conform.nvim](https://github.com/stevearc/conform.nvim?tab=readme-ov-file)

## 主要特性
conform.nvim 是一个 Neovim 插件，用于格式化缓冲区内容。它支持多种语言的格式化工具，提供异步格式化、自动格式化和手动格式化功能。主要特性包括：
- **异步格式化**：支持非阻塞的格式化操作，避免卡顿编辑器。
- **多格式化器支持**：集成如 Prettier、Black、Ruff 等流行工具，自动检测并应用合适的格式化器。
- **范围格式化**：可以格式化整个缓冲区、选定范围或光标位置。
- **自动格式化**：在保存文件时自动触发格式化。
- **配置灵活**：通过 Lua 配置自定义格式化规则和工具。
- **错误处理**：内置日志和诊断功能，便于调试格式化问题。
- **与 LSP 集成**：可选与 nvim-lspconfig 结合，避免格式化冲突。

## 功能
- **格式化缓冲区**：使用 `:ConformFormat` 命令格式化当前缓冲区。
- **自动保存格式化**：配置后，在 BufWritePre 事件中自动格式化。
- **手动触发**：支持视觉模式下格式化选定文本，或通过键映射自定义快捷键。
- **工具管理**：插件不捆绑格式化工具，需要用户手动安装（如通过 Mason.nvim）。
- **预设配置**：提供 YAML/JSON 等格式的预设，支持快速设置常见语言的格式化器。

## 用法
1. **安装**：使用插件管理器如 lazy.nvim：
   ```lua
   {
     "stevearc/conform.nvim",
     opts = {},
   }
   ```

2. **基本配置**（在 init.lua 中）：
   ```lua
   require("conform").setup({
     formatters_by_ft = {
       lua = { "stylua" },
       python = { "black" },
       javascript = { { "prettierd", "prettier" } },
     },
     format_on_save = {
       timeout_ms = 500,
       lsp_fallback = true,
     },
   })
   ```

3. **命令和键映射**：
   - 运行 `:ConformInfo` 查看当前缓冲区的格式化器信息。
   - 添加键映射，例如：
     ```lua
     vim.keymap.set({ "n", "v" }, "<leader>f", function()
       require("conform").format({ async = true, lsp_fallback = true })
     end, { desc = "Format file or range" })
     ```
   - 保存时自动格式化已在配置中启用。

更多细节请参考项目 README。