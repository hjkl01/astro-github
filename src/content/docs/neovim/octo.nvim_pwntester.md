---
title: octo.nvim
---


# octo.nvim
> GitHub 项目地址：<https://github.com/pwntester/octo.nvim>

## 项目概述
octo.nvim 是一款为 Neovim 设计的 GitHub 交互插件，整合了 GitHub 相关的核心功能，旨在让开发者能够在 Neovim 内部完成 Issue/PR 的创建、查看、评论、审核以及仓库状态查看等操作。

## 主要特性
- **Issue/PR 管理**：搜索、打开、创建、关闭、重新打开、讨论、合并 PR。
- **可定制化视图**：支持多种布局（分割、垂直分割、列表、网格）以适配不同工作流程。
- **自动触发快捷键**：一键完成常见操作，如快速打开 PR、在 Markdown 文件中跳转到对应的 Issue。
- **与 Git 集成**：可通过 git 命令检索相关 PR，并进行进一步操作，支持自定义 `git` 命令的映射。

## 功能细节
| 功能 | 说明 |
|------|------|
| 创建 PR/Issue | 通过提示窗口输入标题、内容、标签等信息。 |
| 浏览 PR/Issue 列表 | 支持分页、筛选（状态、标签、作者）以及排序。 |
| 评论与讨论 | 在 PR 或 Issue 页面中直接输入评论，支持 Markdown。 |
| 合并 PR | 一键执行合并操作，提供分支、冲突检查提示。 |
| 标签管理 | 添加/删除标签，快速筛选。 |
| 访问仓库健康状态 | 查看拉取请求、分支保护规则，快速定位问题。 |

## 使用方法
1. **安装**  
   ```bash
   # 以 packer 为例
   use {
     'pwntester/octo.nvim',
     requires = 'nvim-lua/plenary.nvim'
   }
   ```

2. **配置**可选，按需覆盖默认键位）  
   ```lua
   require('octo').setup({
     -- 例如自定义快捷键
     keymaps = {
       switch_to_panel = '<cr>',  -- 跳转到面板
       close = 'q',               -- 关闭面板
     },
     -- 其他可选设置
   })
   ```

3. **使用快捷键**  
   - `:Octo` 打开面板或执行全局命令  
   - `:Octo pr create` 创建 Pull Request  
   - `:Octo issue create` 创建 Issue  

4. **自定义 GitHub OAuth**  
   通过环境变量 `GH_TOKEN` 或 `GH_PAT` 设置访问令牌，或者在 Neovim 内部使用 `:Octo auth` 登录。

## 快速命令参考
| 命令 | 作用 |
|------|------|
| `:Octo` | 打开默认面板 |
| `:Octo pr list` | 列出 PR |
| `:Octo issue list` | 列出 Issue |
| `:Octo pr review <id>` | 打开 PR 评审 |
| `:Octo pr merge <id>` | 合并 PR |
| `:Octo issue comment <id> <comment>` | 评论 Issue |

## 示例
```lua
-- 在 init.lua
require('octo').setup({
  colorscheme = 'onedark',
  floating = {
    border = 'rounded',
  },
  commands = {
    -- 自定义命令
    pr = 'Octo pr list',
  },
})
```

## 贡献
欢迎提交 Issue 或 Pull Request，共同完善插件。

---
> 文件路径：`src/content/docs/00/octo.nvim_pwntester.md`  
> 内容已包含上述 Markdown 文档。