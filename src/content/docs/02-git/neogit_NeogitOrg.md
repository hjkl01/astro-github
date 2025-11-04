
---
title: neogit
---


# Neogit

**项目地址**: [https://github.com/NeogitOrg/neogit](https://github.com/NeogitOrg/neogit)

---

## 简介  
Neogit 是一个为 Neovim 设计的完整 Git 图形交互插件，采用 Neovim 的浮窗和 Telescope 提供直观的界面。它让在 Vim 中完成 Git 操作变得像使用图形化 IDE 一样高效。

---

## 主要特性  
- **Git 状态面板**：一次性可视化工作区、暂存区与 HEAD 的差异。  
- **暂存/取消暂存**：按键即可单个/批量操作文件。  
- **提交**：支持提交信息编写、带签名提交、分组提交。  
- **分支管理**：创建、切换、删除、合并、重命名分支。  
- **变基(Rebase)与合并(Merge)**：可视化冲突解决、交互式变基。  
- **标签(Tag)**：创建、删除、签署标签。  
- **Pull / Push**：一键拉取、推送、设定上层仓库。  
- **远程操作**：镜像管理、拉取/推送协作。  
- **Diff 视图**：一次性查看文件差异，支持对比、合并冲突。  
- **上下文快捷键**：在对应视图内即时完成常用命令。  
- **高度可配置**：支持 Lua 自定义 keymap、外观、功能开关。  

---

## 安装与使用（示以 `packer.nvim` 为例）

```lua
use {
  'NeogitOrg/neogit',
  requires = {
    'nvim-lua/plenary.nvim',
   nvim-telescope/telescope.nvim',  -- 可选，用于渲染窗口
    'sindrets/diffview.nvim'          -- 可选，改进 diff 体验
  },
  config = function()
    require('neogit').setup {
      integrations = {
        diffview = true,   -- 启用 Diffview
        telescope = true   -- 启用 Telescope
      }
    }
  end
}
```

---

## 常用命令

| 调用方式 | 说明 |
| ------- | ---- |
| `:Neogit` / `:NeogitStatus` | 打开 Neogit 状态面板 |
| `:NeogitDiff` | 以单个文件 diff 视图打开 |
| `:NeogitCommit` | 打开提交信息编辑器 |
| **分支** | `:NeogitBranch` 提供分支操作菜单 |
| **标签** | `:NeogitTag` 进行标签管理 |
| **Pull / Push** | `:NeogitPull` / `:NeogitPush` |
| **重置** | `:NeogitReset` 进行重置操作 |

### 在状态面板中的键位示例

- `s`：暂存当前文件  
- `u`：取消暂存当前文件  
- `c`：提交选中文件  
- `b`：分支菜单  
- `t`：标签菜单  
- `p`：Pull  
- `P`：Push（推送）  
- `r`：重置（递归/硬/软）  

（键位可在 `neogit` 的 `config` 部分自定义）

---

## 参考

- 官方仓库 README: https://github.com/NeogitOrg/neogit  
- 插件配置示例: https://github.com/NeogitOrg/neogit/blob/main/docs/configuration.md  
- 常见问题 & FAQ: https://github.com/NeogitOrg/neogit/blob/main/docs/faq.md  

--- 
