
---
title: neotest
---


# Neotest

**GitHub 地址**: https://github.com/nvim-neotest/neotest

## 项目概述

Neotest 是一个基于 Neovim 的轻量级测试框架插件，旨在提供跨语言、易用、快速的单元测试体验。它通过集成多语言测试适配器，在 Neovim 内部统一执行和展示测试结果，极大地提升了测试工作流的效率。

## 主要特性

| 特性 | 说明 |
|------|------|
| **轻量且插件化** | 只需安装核心插件 `neotest`，再根据需要加载相应的测试适配器，例如 `neotest-python`、`neotest-jest` 等。 |
| **快速执行** | 支持异步执行测试，利用 Neovim 的事件循环避免阻塞 UI。 |
| **统一 UI** | 使用浮窗和诊断信息（`signs`, `virtual text`）显示测试结果，支持单行、单文件、单测试等多种查看方式。 |
| **交互式操作** | 提供命令、键映射和 telescope/fzf 光标菜单，便于快速跳转到失败/通过/求 `fail` 的测试位置。 |
| **代码覆盖率支持** | 通过专门的覆盖率适配器（如 `neotest-cmake`、`neotest-open-coverage`）可以直接查看代码覆盖率图。 |
| **可扩展** | 开发者可通过 `require('neotest').setup()` 配置插件行为，也可自定义 `config.default_test_suite()`，或编写新的测试适配器。 |
| **多语言支持** | 现有适配器覆盖 Python、JavaScript/TypeScript、Bash、Go、Rust、PHP、C++、Java 等多种语言。 |
| **集成第三方框架** | 兼容 `unittest`, `pytest`, `mocha`, `jest`, `tape`, `xUnit`, `ginkgo`, `testthat` 等生态。 |
| **命令行接口** | 同时提供 `:Neotest`、`:NeotestPlayground`等命令，方便脚本化或手动执行。 |

## 基本用法

1. **安装**  
   ```bash
   # 以 packer.nvim 为例
   use {
     "nvim-neotest/neotest",
     requires = {
       "nvim-lua/plenary.nvim",
     },
     config = function()
       require("neotest").setup()
     end,
   }
   ```

2. **安装语言适配器**  
   ```bash
   # 例如 Python
   use {
     "nvim-neotest/neotest-python",
     requires = {
       "nvim-neotest/neotest",
     },
   }
   ```

3. **配置（可选）**  
   ```lua
   require("neotest").setup({
     adapters = {
       require("neotest-python")({
         -- 可定制参数
         dap = { justMyCode = false },
         python = "python3",
       }),
     },
     status = {
       virtual_text = false,
     },
     output.open_on_run = "float",
     diagnostic = {
       enabled = true,
       signs = {
         enabled = true,
       },
     },
   })
   ```

4. **常用命令**  
   - `:Neotest run`：运行当前缓冲区文件的所有测试。  
   - `:Neotest run <path>`：运行指定路径的所有测试。  
   - `:Neotest stop`：停止所有测试。  
   - `:Neotest focus`：仅执行被焦点标记的测试。  
   - `:Neotest position`：在当前光标位置执行测试。  
   - `:Neotest summary`：显示测试摘要。  
   - `:Neotest watch`：开启持续测试模式。

5. **快捷键**（示例）  
   ```lua
   local neotest = require("neotest")
   local api = vim.api
   api.nvim_set_keymap('n', '<leader>tt', ':Neotest run<CR>', { noremap=true, silent=true })
   api.nvim_set_keymap('n', '<leader>tf', ':Neotest run<CR>', { noremap=true, silent=true })
   api.nvim_set_keymap('n', '<leader>ts', ':Neotest summary<CR>', { noremap=true, silent=true })
   ```

6. **集成 Telescope**  
   ```lua
   require('telescope').load_extension('neotest')
   -- 例如运行最近失败的测试
   vim.api.nvim_set_keymap('n', '<leader>tL', "<cmd>Telescope neotest last<CR>", { silent = true })
   ```

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| `neotest` 运行时报错无法找到适配器 | 确认已安装对应适配器，并在 `setup` 时正确传入 `adapters` 选项 |
| 测试结果没有显示 | 检查 `diagnostic.enabled`、`status.virtual_text` 配置；确认测试文件路径正确 |
| 想在 Neovim 里看到覆盖率 | 安装特定的覆盖率适配器，如 `neotest-dotnet-test` 并在 `setup` 配置 `coverage` |
| 需要自定义命令行为 | 在 `setup` 中调整 `run`、`stop` 等回调，或覆盖默认命令 `:Neotest` |

## 总结

Neotest 通过统一的 API 与丰富的 UI，提供了来自多语言生态的完整测试体验。无论是 Python 的 `pytest`，还是 JavaScript 的 `jest`，仅需添加对应适配器即可获得顺畅的编写、运行与调试流程。它使得在 Neovim 内完成整个单元测试生命周期成为一种轻松且高效的习惯。

--- 

> **Tip**：查看 [Neotest 官方文档](https://github.com/nvim-neotest/neotest/blob/main/README.md) 获取最新适配器、API 及浏览器的详细信息。