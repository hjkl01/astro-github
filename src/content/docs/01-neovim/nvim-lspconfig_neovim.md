---
title: nvim-lspconfig
---


# nvim-lspconfig

项目地址: [https://github.com/neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)

## 主要特性

1. **多语言 LSP 支持**  
   提供与多种语言服务器（如 `pyright`、`tsserver`、`gopls` 等）的集成。

2. **轻量、易配置**  
   通过 Lua 脚本快速完成 LSP 的安装、配置与启动，几行代码即可完成基础功能。

3. **默认配置管理**  
   内置默认设置，支持按需覆盖。提供 `setup()`、`config()` 等 API。

4. **自动补全、诊断、跳转**  
   与 `nvim-cmp`、`telescope.nvim` 等插件无缝配合，展示诊断信息、代码补全、转到定义、查找引用等功能。

5. **自定义命令与键映射**  
   可以通过 `on_attach` 函数定义与 LSP 交互的快捷键。

## 主要功能

| 功能 | 描述 |
|------|------|
| `setup()` | 初始化插件，加载默认或自定义的语言服务器配置。 |
| `config()` | 根据语言服务器返回的配置自动进行设置。 |
| `servers` | 预定义常用语言服务器列表，可通过 `servers.<name>` 表示单服务器配置。 |
| `ensure_installed` | 与 `mason.nvim` 配合，自动安装缺失的语言服务器。 |
| `filetypes` | 指定语言服务器适用的文件类型。 |
| `root_dir` | 定义项目根目录的查找规则。 |
| `settings` | 通过 `settings = { ... }` 传递给 LSP 的特定配置。 |
| `on_attach` | LSP 建立连接后执行的回调，常用于设置缓冲区本地键映射。 |
| `flags` | 设置超时、重连等全局标志。 |

## 用法示例

```lua
-- ~/.config/nvim/lua/lsp.lua
local lspconfig = require("lspconfig")

lspconfig.pyright.setup{
  on_attach = function(client, bufnr)
    -- 设置快捷键
    local opts = { noremap=true, silent=true }
    vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gd', '<Cmd>lua vim.lsp.buf.definition()<CR>', opts)
  end,
  settings = { python = { analysis = { typeCheckingMode = "basic" } } }
}
```

如果想一次性配置多种服务器，可使用 **mason.nvim** 自动管理安装：

```lua
require("mason").setup()
require("mason-lspconfig").setup {
  ensure_installed = { "pyright", "tsserver", "gopls" },
  automatic_installation = true
}
require("lspconfig").setup {}
```

## 如何开始

1. 安装 Neovim 0.9+。  
2. 安装 `nvim-lspconfig`：  
   ```bash
   git clone https://github.com/neovim/nvim-lspconfig ~/.config/nvim/lua/plugins/nvim-lspconfig
   ```  
   或通过插件管理器（如 `packer.nvim`）安装。  
3. 在 `init.lua` 或对应插件配置文件中调用 `require("lspconfig").setup()` 并按需加入自定义服务器配置。  

---
> 该插件是 Neovim 官方 LSP 配置工具，专为快速、灵活的语言服务集成而生。  
```md
src/content/docs/00/nvim-lspconfig_neovim.md
```
