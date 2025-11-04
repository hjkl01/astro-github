
---
title: rustaceanvim
---


# Rustaceanvim (mrcjkb)

> GitHub 地址: <https://github.com/mrcjkb/rustaceanvim>

---

## 简介

`rustaceanvim` 是一个专为 Neovim 设计的 Rust 开发环境插件，提供了完备的 **语言服务器**、**格式化**、**Cargo** 命令、**调试** 等功能，让你无需切换到 IDE 即可获得接近 IDE 的编程体验。

---

## 主要特性

| 功能 | 说明 |
|------|------|
| **LSP 支持** | 通过 `nvim-lspconfig` 自动配置 `rust-analyzer`，实现语法检查、自动补全、跳转、查看文档等。 |
| **Cargo 集成** | 快捷运行 `cargo build / test / run / doc` 等命令；在命令行内查看依赖树、输出结果。 |
| **代码格式化** | 绑定 `:RustFmt`，支持 `rustfmt` 并可在保存时自动格式化。 |
| **调试集成** | 与 `nvim-dap` / `nvim-dap-ui` 集成，支持 LLDB 与 `rust-analyzer` 的调试配置，支持断点、单步执行、变量查看。 |
| **状态栏诊断** | 通过 `diesel`/`lsp_status` 显示错误/警告/提示数目。 |
| **键位绑定** | 提供默认键位 (`<leader>r` 系列) 用于快速访问 LSP、Cargo、调试功能。 |
| **AutoCmd** | 监听文件改动，自动重载 LSP 及生成文件，如 `build.rs` 等。 |
| **多项目支持** | 可为每个 Rust 项目持久化特定的 LSP/调试配置。 |

---

## 快速上手

### 1. 安装

> 使用插件管理器（例如 `lazy.nvim`、`packer.nvim`）：

```lua
{
  "mrcjkb/rustaceanvim",
  version = "^3.0.0",  -- 推荐使用正式版
  ft = { "rust" },
  config = function()
    require("rustaceanvim").setup({})
  end
}
```

### 2. 基本使用

| 操作 | 快捷键 | 说明 |
|------|--------|------|
| 代码格式化 | `:RustFmt` | 也可在 `bufwritepre` 钩子中自动触发 |
| 运行 Cargo | `:RustRun` / `:RustTest` | 快速执行 `cargo run / test` |
| 重新加载 LSP | `:RustReload` | 当 `rust-analyzer` 配置修改后使用 |
| 打开调试 UI | `:RustDebugLaunch` | 启动调试会话，切换窗口查看状态 |
| 跳转至定义 | `gd` | 通过 LSP 跳转 |
| 代码修复 | `:lsp_rename` / `:lsp_codeAction` | LSP 的相关命令 |

> **提示**：默认 `<leader>r` 是 Rust 相关操作的前缀，例如 `<leader>rc` 触发 Cargo 命令。

### 3. 调试配置

在 `init.lua` 或 `init.vim` 中补充：

```lua
require('dap').configurations.rust = {
  {
    type = 'lldb',
    request = 'launch',
    name = 'Launch',
    program = function()
      return vim.fn.input('Path to executable: ', vim.fn.getcwd() .. '/target/debug/', 'file')
    end,
    cwd = '${workspaceFolder}',
    stopOnEntry = false,
  },
}
```

然后使用 `:RustDebugLaunch` 即可。

---

## 配置自定义

插件本身使用 `require('rustaceanvim').setup()` 接收一个配置表。可自定义：

```lua
require('rustaceanvim').setup({
  tools = {
    executor = require('rustaceanvim.executors').from('neotest'),
    reload_workspace_from_cargo_toml = true,
  },
  server = {
    settings = {
      ["rust-analyzer"] = {
        cargo = { loadOutDirsFromCheck = true },
        procMacro = { enable = true },
      }
    }
  }
})
```

---

## 贡献

- Issues: 反馈 bug、功能需求
- PR: 修复、改进

欢迎提交 🚀

--- 

> **GitHub 地址**: [https://github.com/mrcjkb/rustaceanvim](https://github.com/mrcjkb/rustaceanvim)

