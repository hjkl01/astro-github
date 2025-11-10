---
title: supermaven-nvim
---


# Supermaven Nvim

**仓库地址**: https://github.com/supermaven-inc/supermaven-nvim

Supermaven Nvim 是一款为 Neovim 设计的 AI 辅助编码插件，旨在通过实时代码补全和建议提升开发效率。插件基于 Supermaven 的 AI 模型，在本地进行推理，保持高性能与低延迟。

## 主要特性

- **即时代码补全**  
  在编辑过程中实时提供候选代码片段，支持多种语言（JavaScript/TypeScript, Python, Go, Rust, PHP, 等）。

- **无缝集成**  
  通过 Lua 配置，轻松集成到任何 Neovim 配置中（vim-plug、packer.nvim、dein.nvim 等）。

- **自定义提示**  
  支持自定义提示文本与优先级，帮助你快速定位最适合的补全。

- **多窗口支持**  
  适配多窗口与标签页，确保每个编辑窗口都有独立的补全上下文。

- **键位与快捷键**  
  支持 Tab/Shift‑Tab 选择补全，Enter 直接插入，Esc 取消，并可自定义快捷键。

- **语言服务器兼容**  
  与已有的 LSP 插件兼容，能够互补使用。

## 安装与配置

### 1. 插件管理器示例

#### vim-plug
```vim
Plug 'supermaven-inc/supermaven-nvim'
```

#### packer.nvim
```lua
use 'supermaven-inc/supermaven-nvim'
```

#### dein.nvim
```vim
call dein#add('supermaven-inc/supermaven-nvim')
```

### 2. 基本配置

```lua
-- load the plugin
require("supermaven-nvim").setup({
  -- 可选配置项
  keymaps = {
    accept = "<Tab>",
    prev = "<S-Tab>",
    next = "<Tab>",
    close = "<Esc>"
  },
  theme = "night", -- 可选主题
  minimum_trigger_len = 2, -- 触发补全部分字符数
})
```

### 3. 启用/禁用

```vim
:SupermavenEnable   -- 开启
:SupermavenDisable  -- 关闭
```

## 使用方式

1. 在编辑器中开始键入代码，AI 会自动弹出补全列表。  
2. 使用配置的快捷键 (默认 `<Tab>/<S-Tab>`) 选取建议。  
3. 按 `<Enter>` 直接插入代码。  
4. 若想忽略实时补全，可按 `<Esc>` 关闭建议列表。  

## 文档与支持

- 官方帮助文档: https://github.com/supermaven-inc/supermaven-nvim/wiki
- GitHub Issue: https://github.com/supermaven-inc/supermaven-nvim/issues
- 贡献指南: https://github.com/supermaven-inc/supermaven-nvim/blob/main/CONTRIBUTING.md

> 只需要将此文件保存在 `src/content/docs/00/supermaven-nvim_supermaven-inc.md`，即可正常使用，文件内容已包含项目地址及全部必要信息。
