
---
title: nvim-lsp-setup
---

# nvim-lsp-setup 项目描述

## 项目地址
[https://github.com/Junnplus/nvim-lsp-setup](https://github.com/Junnplus/nvim-lsp-setup)

## 主要特性
- **简洁的 LSP 配置框架**：基于 Neovim 的内置 LSP（Language Server Protocol）支持，提供模块化的配置方式，便于扩展和维护。
- **多语言支持**：集成多种编程语言的 LSP 服务器，例如 Lua、Python、JavaScript 等，支持自动安装和配置。
- **插件集成**：兼容 nvim-cmp（自动补全）、lsp-zero 等流行插件，实现智能补全、悬浮提示和诊断功能。
- **零配置优先**：采用 lsp-zero 的理念，减少手动配置，提供开箱即用的体验，同时允许高级自定义。
- **性能优化**：轻量级设计，避免不必要的依赖，确保 Neovim 的启动速度和运行效率。

## 主要功能
- **代码补全与提示**：实时提供代码自动补全、函数签名提示和文档悬浮窗。
- **错误诊断与修复**：高亮显示语法错误、警告，并支持快速修复（code actions）。
- **导航与重构**：跳转到定义、引用查找、符号搜索等 IDE-like 功能。
- **格式化与 linting**：集成 null-ls 或 conform.nvim 等工具，实现代码格式化和 linting。
- **自定义事件处理**：支持 LSP 事件钩子，如 on_attach 用于自定义按键绑定。

## 用法
1. **安装**：使用插件管理器（如 lazy.nvim 或 packer.nvim）克隆仓库：
   ```
   use { 'Junnplus/nvim-lsp-setup' }
   ```
   或在 lazy.nvim 中：
   ```lua
   { 'Junnplus/nvim-lsp-setup' }
   ```

2. **基本配置**：在 Neovim 的 init.lua 中引入并设置：
   ```lua
   require('lsp-setup').setup({
       servers = { 'lua_ls', 'pyright', 'tsserver' },  -- 指定 LSP 服务器
       on_attach = function(client, bufnr)
           -- 自定义按键绑定，例如 <leader>ca 为 code action
           vim.keymap.set('n', '<leader>ca', vim.lsp.buf.code_action, { buffer = bufnr })
       end,
   })
   ```

3. **扩展使用**：
   - 添加更多服务器：通过 `servers` 列表扩展支持的语言。
   - 集成补全：在配置中添加 `require('lsp-setup').setup_nvim_cmp()` 以启用自动补全。
   - 自定义：修改 `on_init` 或 `capabilities` 来调整 LSP 行为，例如设置工作区文件夹。

4. **启动 Neovim**：重启 Neovim 后，LSP 服务器会自动下载并启动。使用 `:LspInfo` 检查状态，按键如 `gd`（go to definition）即可使用功能。

更多细节请参考仓库的 README.md 文件。