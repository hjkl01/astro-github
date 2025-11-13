---
title: lua-language-server
---


# Lua Language Server (LuaLS)

**项目地址**: https://github.com/LuaLS/lua-language-server

## 主要特性

- **语言服务**：提供语法检查、自动补全、类型提示、跳转到定义、查找引用、重命名等 IDE 级功能。  
- **跨平台**：支持 Windows、macOS、Linux，使用 LuaJIT 或标准 Lua 运行。  
- **可扩展插件**：支持通过 `LuaLS` 的插件机制实现自定义功能。  
- **Lua 5.1/5.2/5.3/5.4/5.2+**：兼容多版本 Lua。  
- **内置 LSP**：实现 LSP（Language Server Protocol）协议，易于与 VSCode、Vim、Emacs 等编辑器集成。  
- **自带脚本库**：内置 `lua-language-server` 的配置文件、语法规则、语义分析。  
- **性能优化**：使用 `luacheck` 与 `luacheck` 的缓存机制，快速响应。  

## 功能概览

| 功能 | 说明 |
|------|------|
| **自动补全** | 根据上下文提供变量、函数、字段等补全建议。 |
| **类型推断** | 通过注释（`---@type` 等）或 LuaJIT 的 `---@class` 进行类型推断。 |
| **错误/警告** | 在编辑时实时检测语法错误、未定义变量、类型不匹配等。 |
| **跳转到定义** | 快速定位变量、函数、模块的定义位置。 |
| **查找引用** | 全局搜索某个符号的所有引用。 |
| **重命名** | 统一重命名变量、函数、类等。 |
| **代码格式化** | 使用 `stylua` 进行代码格式化。 |
| **代码片段** | 支持自定义代码片段，提升编码效率。 |
| **文档生成** | 通过注释生成 API 文档。 |

## 安装与使用

1. **克隆仓库**  
   ```bash
   git clone https://github.com/LuaLS/lua-language-server.git
   cd lua-language-server
   ```

2. **编译（可选）**  
   - 直接使用预编译的二进制文件（Windows/Linux/macOS）。  
   - 或者使用 `clang` 编译：  
     ```bash
     make
     ```

3. **配置编辑器**  
   - **VSCode**：安装 `Lua Language Server` 插件，插件会自动下载并使用此代码库。  
   - **Vim/Neovim**：使用 `coc.nvim` 或 `nvim-lspconfig`，配置 `lua-language-server` 的可执行文件路径。  
   - **Emacs**：使用 `lsp-mode`，配置 `lua-language-server` 路径。

4. **运行**  
   ```bash
   ./bin/lua-language-server
   ```

5. **自定义配置**  
   - 在项目根目录下创建 `settings.lua` 或 `lua-language-server/settings.lua`，使用 `Lua` 语法配置项目选项。  
   - 示例：  
     ```lua
     -- settings.lua
     return {
       settings = {
         Lua = {
           runtime = {
             version = 'LuaJIT',
           },
           diagnostics = {
             globals = {'vim'},
           },
           workspace = {
             library = vim.api.nvim_get_runtime_file("", true),
           },
           telemetry = {
             enable = false,
           },
         },
       },
     }
     ```

## 开发与贡献

- **代码结构**：核心逻辑在 `lua` 目录下，使用 `Lua` 语言实现。  
- **测试**：在 `tests` 目录下编写 LSP 交互测试。  
- **提交**：请遵循现有的代码风格，提交 PR 时附上对应功能描述。  

> **提示**：如果想自定义插件，可在 `plugins` 目录下编写 Lua 插件，然后在 `settings.lua` 中启用。  

---  

**项目地址**: https://github.com/LuaLS/lua-language-server
