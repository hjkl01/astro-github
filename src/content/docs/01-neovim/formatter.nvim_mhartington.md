---
title: formatter.nvim
---

# formatter.nvim 项目

## 项目地址
[GitHub 项目地址](https://github.com/mhartington/formatter.nvim)

## 主要特性
- **多语言支持**：支持多种编程语言的代码格式化，包括Lua、Python、JavaScript、TypeScript、C/C++、Go、Rust 等，通过集成外部格式化工具实现。
- **异步格式化**：使用异步方式进行代码格式化，避免阻塞Neovim 编辑器，提高性能。
- **高度可配置**：允许用户自定义格式化工具的配置，支持多个格式化器并行使用，并提供Lua 配置接口。
- **自动和手动格式化**：支持在保存文件时自动格式化、LSP 集成或手动触发格式化。
- **错误处理**：内置错误报告机制，当格式化失败时会显示相关信息，便于调试。

## 主要功能
- **集成外部工具**：兼容如Black、prettier、clang-format、goimports 等流行格式化工具，用户只需安装这些工具即可使用。
- **LSP 集成**：可以与 Neovim 的 LSP 客户端无缝集成，实现代码格式化作为 LSP 功能的一部分。
- **范围格式化**：支持格式化整个文件、选定范围或光标所在行。
- **配置管理**：通过 Lua 表格配置格式化器，支持条件判断（如文件类型）来选择合适的格式化工具。
- **性能优化**：异步执行确保格式化过程不影响编辑体验，尤其适合大型项目。

## 用法
1. **安装**：
   - 使用插件管理器如 packer.nvim 或 lazy.nvim 安装：
     ```lua
     use { 'mhartington/formatter.nvim' }
     ```

2. **基本配置**：
   - 在 Neovim 配置中初始化并设置格式化器：
     ```lua
     require('formatter').setup {
       logging = true,
       log_level = vim.log.levels.WARN,
       filetype = {
         lua = { require('formatter.filetypes.lua').stylua },  -- 示例：使用 stylua 格式化 Lua
         python = { require('formatter.filetypes.python').black },  -- 示例：使用 black 格式化 Python
         -- 添加更多文件类型配置
       },
     }
     ```

3. **命令和自动触发**：
   - **手动格式化**：运行 `:Format` 命令格式化当前缓冲区，或 `:FormatWrite` 保存并格式化。
   - **自动格式化**：在 autocmd 中设置保存时自动格式化：
     ```lua
     vim.api.nvim_exec([[
       augroup FormatAutogroup
         autocmd!
         autocmd BufWritePost *.lua,*.py FormatWrite
       augroup END
     ]], true)
     ```
   - **范围格式化**：在视觉模式下选择代码后运行 `:Format`。

4. **自定义格式化器**：
   - 对于不支持的工具，可以手动定义：
     ```lua
     local util = require 'formatter.util'
     require('formatter.filetypes.any').setup {
       function()
         return {
           exe = 'prettier',  -- 示例工具
           args = { '--stdin-filepath', util.escape_path(util.get_current_buffer_file_path()) },
           stdin = true,
         }
       end,
     }
     ```

更多细节请参考项目 README。