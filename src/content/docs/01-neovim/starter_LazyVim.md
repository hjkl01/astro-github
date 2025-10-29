
---
title: starter
---

# LazyVim Starter  
项目地址: https://github.com/LazyVim/starter

## 主要特性
- 基于 Neovim 0.10+，完全使用 Lua 配置  
- 轻量级启动脚本，`lazy.nvim` 自动管理插件  
- 默认配置包括 LSP、Treesitter、Telescope、NvimTree、Gitsigns、Luasnip、Catppuccin 主题等  
- 与 LazyVim 官方 starter 兼容，可随时升级  

## 功能
| 功能 | 说明 |
|------|------|
| **插件管理** | `lazy.nvim` 负责并行安装、更新与卸载 |
| **语言服务器** | 自动配置常见 LSP，提供诊断、补全、重构 |
| **代码片段** | `luasnip` 整合，快捷触发代码模板 |
| **文件浏览** | `nvim-tree.lua` 作为文件树浏览器 |
| **语法高亮** | Treesitter 提供多语言高亮 |
| **Git 集成** | `gitsigns.nvim` 显示行级 Git 状态 |
| **Popup 主题** | 默认 Catppuccin，支持自定义配色 |

## 用法
```bash
# 1. 克隆仓库
git clone https://github.com/LazyVim/starter.git ~/.config/nvim

# 2. 安装插件（使用或更新）
nvim +Lazy! sync

# 3. 启动 Neovim
nvim
```

### 常用快捷键
- `Ctrl-p`：Telescope 搜索文件  
- `Ctrl-n`：打开文件树  
- `gd`：跳转到定义  
- `K`：查看光标下的 Hover 信息  
- `<leader>f`：格式化当前文件  

### 自定义配置
编辑 `lua/custom/settings.lua`：
```lua
return {
  colorscheme = "catppuccin",
  icons = true,
}
```

### 插件升级
```vim
:Lazy update
```

## 结语  
LazyVim starter 为 Neovim 提供了即插即用、现代化的配置方案，既适合快速落地，也便于深入自定义。