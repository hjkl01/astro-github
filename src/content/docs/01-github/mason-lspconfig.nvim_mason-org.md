
---
title: mason-lspconfig.nvim
---

下面的内容可直接粘贴到 `src/content/docs/00/mason-lspconfig.nvim_mason-org.md` 保存为 Markdown 文档。

```markdown
# mason-lspconfig.nvim（mason-org）

**GitHub 地址**  
[https://github.com/mason-org/mason-lspconfig.nvim](https://github.com/mason-org/mason-lspconfig.nvim)

---

## 简介

`mason-lspconfig.nvim` 将 Mason（用于安装、更新和管理 LSP 服务器的插件）与 Neovim 官方的 `lspconfig` 进行无缝集成。  
它会在 Mason 发现、安装或更新服务器后，自动把对应的 LSP 注册到 `lspconfig`，并允许你为每个服务器提供自定义配置。

---

## 主要特性

| 功能 | 说明 |
|------|------|
| **自动注册** | Mason 安装的服务器会立刻 `lspconfig` 注册，无需手动配置 `setup()` 调用。 |
| **自定义服务器配置** | 通过 `setup_handlers` 为任何服务器提供精确的配置（`settings`、`init_options`、`capabilities` 等）。 |
| **自动安装/启用** | `ensure_installed` 与 `automatic_installation` 可以让指定服务器在启动时自动安装并启用。 |
| **与 Mason UI 集成** | 通过 Neovim 的 Mason 交互窗口（`:Mason`）查看已安装/可用服务器，并手动安装/卸载。 |
| **与 `nvim-lspconfig` 兼容** | 支持 Neovim 0.10+ 与 `nvim-lspconfig` 最新版本。 |

---

## 快速使用

```lua
-- 1. 初始化 Mason
require('mason').setup()

-- 2. 初始化 mason-lspconfig
require('mason-lspconfig').setup {
  ensure_installed = { "lua_ls", "pyright", "tsserver" },  -- 强制安装的服务器
  automatic_installation = true,                           -- 已安装服务器自动启用
}

-- 3. 配置服务器（默认全局配置）
require('mason-lspconfig').setup_handlers {
  -- 默认处理：对未覆盖的服务器使用空配置
  function(server_name)
    require('lspconfig')[server_name].setup {}
  end,

  -- 为特定服务器提供自定义配置
  ["lua_ls"] = function()
    require('lspconfig').lua_ls.setup {
      settings = {
        Lua = {
          diagnostics = { globals = { "vim" } },
          runtime = { version = "LuaJIT" },
        },
      },
    }
  end,
}
```

> **Tip**：在 `init.lua` 或 `init.vim` 中一次性引入上述代码即可让 Mason 与 LSP 服务器无缝协作。

---

## Mason 的常用命令

| 命令 | 功能 |
|------|------|
| `:Mason` | 打开 Mason UI；查看已安装/可用服务器 |
| `:MasonInstall <server>` | 手动安装服务器 |
| `:MasonUninstall <server>` | 卸载服务器 |
| `:MasonLog` | 查看 Mason 的安装/更新日志 |

---

## 依赖与兼容性

- Neovim **0.10** 及以上
- `nvim-lspconfig` **0.9.0** 及以上
- Mason **0.5.0** 及以上

---

## 贡献

欢迎提交 PR 或 Issue。详细使用与贡献指南见 README。
```

该 Markdown 已包含了项目地址、核心特性、功能、基本用法示例与必要的依赖信息，适合直接保存为文件 `src/content/docs/00/mason-lspconfig.nvim_mason-org.md`。