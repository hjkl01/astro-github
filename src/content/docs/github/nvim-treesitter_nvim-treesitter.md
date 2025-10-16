
---
title: nvim-treesitter
---

# nvim-treesitter 项目

## 项目地址
[GitHub 项目地址](https://github.com/nvim-treesitter/nvim-treesitter)

## 主要特性
nvim-treesitter 是 Neovim 的一个插件，利用 Tree-sitter 解析库为各种编程语言提供高级语法高亮、代码折叠、增量选择等功能。它支持超过 100 种编程语言的解析器，能够生成精确的语法树，从而实现更智能的编辑体验。主要特性包括：
- **精确语法高亮**：基于语法树的高亮，比传统正则表达式高亮更准确和高效。
- **增量选择**：通过 `viw`、`vis` 等命令快速选择代码块、函数或语句。
- **代码折叠**：自动根据语法结构折叠代码，提高可读性。
- **多语言支持**：集成 Tree-sitter 解析器，支持 JavaScript、Python、Rust、C++ 等众多语言。
- **模块化扩展**：可与其他插件集成，如 textobjects、playground 等，用于自定义文本对象或可视化语法树。
- **性能优化**：增量解析减少 CPU 使用，支持 Neovim 的 LSP 和其他生态。

## 主要功能
- **语法解析**：为 Neovim 提供 Tree-sitter 驱动的语法分析，支持查询语法树以实现高级编辑功能。
- **高亮和着色**：使用 `@` 标记的查询规则自定义高亮，支持主题集成。
- **文本对象和运动**：定义如 `@function.inner`、`@parameter` 等文本对象，用于 Surround、Leap 等插件。
- **查询和注入**：允许用户编写 Tree-sitter 查询来捕获特定模式，支持语言注入（如 Markdown 中的代码块）。
- **配置管理**：通过 Lua API 配置确保、更新和忽略特定语言的解析器。

## 用法
### 安装
使用插件管理器如 packer.nvim 或 lazy.nvim 安装：
```lua
-- 使用 lazy.nvim 示例
{
  'nvim-treesitter/nvim-treesitter',
  build = ':TSUpdate',
  config = function()
    require('nvim-treesitter.configs').setup({
      ensure_installed = { "lua", "vim", "vimdoc" },  -- 安装特定语言解析器
      sync_install = false,
      auto_install = true,
      highlight = { enable = true },
      indent = { enable = true },
      incremental_selection = {
        enable = true,
        keymaps = {
          init_selection = '<C-space>',
          node_incremental = '<C-space>',
          scope_incremental = '<C-s>',
          node_decremental = '<M-space>',
        },
      },
    })
  end
}
```
运行 `:TSUpdate` 更新解析器。

### 基本使用
- **语法高亮**：启用后自动高亮当前缓冲区代码。
- **增量选择**：在 normal 模式下按 `<C-space>` 开始选择语法节点，按多次扩展范围。
- **折叠**：使用 `zc`、`zo` 等命令折叠/展开基于语法的代码块。
- **自定义查询**：在 `queries/` 目录下编辑高亮规则，例如为 Lua 添加自定义高亮：
  ```lisp
  ;; queries/lua/highlights.scm
  (function_declaration name: (identifier) @function)
  ```
- **文本对象**：结合 textobjects 插件，使用 `af`（around function）等操作函数体。
- **Playground**：安装 nvim-treesitter/playground 插件，运行 `:TSPlaygroundToggle` 可视化语法树。

更多细节请参考项目 README。