---
title: neogen
---

# Neogen 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/danymat/neogen)

## 主要特性
Neogen 是一个基于 Neovim 的 Lua 插件，主要用于自动生成注释文档。它支持多种编程语言（如 Lua、Python、C/C++ 等），并提供灵活的配置选项。核心特性包括：
- **多语言支持**：兼容多种文件类型，自动识别并生成相应格式的文档注释。
- **上下文感知**：根据代码结构（如函数、类、变量）智能生成注释模板。
- **自定义模板**：允许用户通过配置自定义注释格式和内容。
- **集成 Treesitter**：利用 Treesitter 解析器提升注释生成的准确性。
- **非侵入式**：无缝集成到 Neovim 编辑器中，支持命令行和快捷键触发。

## 主要功能
- **自动生成函数注释**：在函数定义处生成参数、返回值和描述的文档字符串。
- **类和模块注释**：为类、模块或全局变量添加结构化注释。
- **批量处理**：支持在文件中批量生成或更新注释。
- **语言特定适配**：针对不同语言（如 JSDoc、Python docstring、Lua 注释）提供专属模板。
- **错误处理**：自动跳过无效代码块，避免生成不准确的注释。

## 用法
1. **安装**：
   - 使用插件管理器如 packer.nvim 或 lazy.nvim 安装：
     ```
     use { 'danymat/neogen' }
     ```
   - 确保安装 Treesitter 解析器：`:TSInstall <language>`（例如 `:TSInstall lua`）。

2. **配置**：
   - 在 Neovim 配置中添加：
     ```lua
     require('neogen').setup {
       enabled = true,
       languages = {
         lua = { template = { annotation_convention = "nerd" } },
         python = { template = { annotation_convention = "sphinx" } },
       },
     }
     ```

3. **使用**：
   - 在代码中定位到函数或类定义。
   - 执行命令：`:Neogen`（生成当前节点注释）或 `:Neogen current_function`（指定生成函数注释）。
   - 快捷键示例：映射到 `<leader>gf` 以快速生成函数注释。
   - 生成后，可手动编辑注释内容。

更多细节请参考项目 README。