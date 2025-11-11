---
title: astrocommunity
---

# AstroCommunity（AstroNvim 生态社区）

**GitHub 项目地址:** [https://github.com/AstroNvim/astrocommunity](https://github.com/AstroNvim/astrocommunity)

> Description from GitHub: A community repository of common plugin specifications

## 项目简介

AstroCommunity 是 AstroNvim 生态的插件集合与配置仓库，提供了丰富的 Neovim 插件、主题、工具及一键脚本配置，旨在帮助用户快速搭建并维护高效的 Neovim 开发环境。

## 主要特性与功能

| #   | 功能分类       | 关键插件/组件                                                           | 说明                                       |
| --- | -------------- | ----------------------------------------------------------------------- | ------------------------------------------ |
| 1   | **主题 & UI**  | `telescope.nvim`、`nvim-tree.lua`、`bufferline.nvim` 等                 | 统一的配色方案与界面组件，支持多主题切换。 |
| 2   | **编辑器增强** | `nvim-lspconfig`、`lsp-zero.nvim`、`completion-nvim`、`cmp-nvim-lsp` 等 | 内建 LSP、自动补全、诊断，支持多语言。     |
| 3   | **多语言支持** | `rust-tools.nvim`、`gpt.nvim`、`copilot.lua` 等                         | 针对多种编程语言提供专属扩展。             |
| 4   | **工具集**     | `nvim-dap`、`telescope.nvim`、`plenary.nvim`、`auto-session.nvim` 等    | 调试、文件搜索、会话管理等。               |
| 5   | **插件集成**   | `astrocommunity` 自带的插件集合与规范                                   | User-friendly 的插件管理与一次性配置集。   |

## 如何使用

1. **安装 AstroNvim**

   ```bash
   git clone https://github.com/AstroNvim/AstroNvim ~/.config/nvim
   nvim +'MasonInstallAll' +qa
   ```

2. **配置 AstroCommunity**  
   在 `lua/community.lua` 文件中添加以下内容（如果使用 AstroNvim Template）：

   ```lua
   return {
     "AstroNvim/astrocommunity",
     { import = "astrocommunity.colorscheme.catppuccin" },
     -- ... 导入任何社区贡献的插件
   }
   ```

3. **启动 Neovim**  
   第一次启动时，AstroNvim 会自动加载社区插件并完成安装。

   ```bash
   nvim
   ```

4. **可选配置**
   - 自定义插件：在 `lua/plugins/` 目录中进一步配置。
   - 禁用导入：设置 `enabled` 为 `false`。

5. **更新**
   - 更新插件：`:AstroUpdate`

> 通过上述步骤，即可获得一个完整、可定制化、功能丰富的 Neovim 开发环境，涵盖从文件导航、代码补全、调试到主题美化等全部需求。

---

---使用 GitHub 项目地址为参考链接。
