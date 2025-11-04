
---
title: typescript-tools.nvim
---


# TypeScript-Tools.nvim

> **项目地址**: https://github.com/pmizio/typescript-tools.nvim

---

## 简介
`typescript-tools.nvim` 是一款为 Neovim 打造的 TypeScript 开发工具集合，集成了 LSP 与多种实用指令，实现了以下核心功能：

- **LSP 集成**：自动加载 TSServer（tsserver）并与 neovim 内置 LSP 进行无缝关联。  
- **代码导航**：支持跳转到定义、引用、实现等。  
- **代码操作**：自动修复、重构、格式化、导入等。  
- **调试集成**：支持 `nvim-dap` 调试 TypeScript 代码。  
- **代码生成**：自动生成 Jest 单元测试、React 组件、TS 类型定义等。  
- **高亮与提示**：利用 Tree-sitter 与 LSP 共同提供更精准的语法高亮和代码提示。  

> 兼容 **Neovim 0.10+** 及 **NVim API**，无外部依赖，直接通过 `:TSInstall` 命令安装。

---

## 主要功能

|功能|描述|
|---|---|
|**自动安装 TSServer**|检测项目 `node_modules/.bin/tsserver`，若不存在会提示安装。|
|**智能补全**|结合 LSP + nvim-cmp 自动完成 TypeScript 语法、接口、类、常量等。|
|**代码导航**|```<leader>gd```: 定义，```<leader>gr```：引用，```<leader>gi```：实现，```<leader>go```：符号搜索。|
|**代码操作**|```<leader>rc```：快速修复，```<leader>rn```：重命名，```<leader>rf```：格式化，```<leader>ri```：导入所需依赖。|
|**调试**|```<leader>dt```：启动调试，```<leader>dS```：暂停/继续，```<leader>do```：单步执行等（需配合 `nvim-dap`）。|
|**单元测试**|```<leader>tt```：生成测试框架，支持 Jest。|
|**文件生成**|```<leader>tf```：生成 React 组件、TS 模块、接口文件等。|
|**代码片段**|通过 `:TSInstall snippets` 注入常用代码片段。|

---

## 安装与配置

### 1. 通过 packer.nvim 安装

```lua
use {
  'pmizio/typescript-tools.nvim',
  config = function()
    require('typescript-tools').setup {
      -- 你的自定义配置
    }
  end
}
```

### 2. 基本配置示例

```lua
require('typescript-tools').setup {
  disabled_commands = {
    -- 禁用默认命令，例如：'OrganizeImports'，使用你喜欢的重写命令
  },
  on_attach = function(client, bufnr)
    -- 可以在这里添加 buffer 级别的 keybind
  end,
  settings = {
    completions = {
      completeFunctionCalls = true
    },
    server = {
      -- 通过传入 node_args 配置启动参数
      node_args = {"--nolazy", "--trace-uncaught"}
      -- server_path = "/absolute/path/to/tsserver"
    }
  }
}
```

> **提示**：对于大型项目，可使用 `--disableAutomaticTypeAcquisition`，减少 tsserver 计算量---

## 用法

### 基础快捷键

| 快捷键 | 功能 |
| --- | --- |
| `<leader>gd` | 跳转到定义 |
| `<leader>gr` | 跳转到引用 |
| `<leader>gi` | 跳转到实现 |
| `<leader>go` | 通过符号搜索 |
| `<leader>rc` | 快速修复 |
| `<leader>rn` | 重命名符号 |
| `<leader>rf` | 自动格式化 |
| `<leader>ri` | 自动导入 |
| `<leader>dt` | 启动调试 |
| `<leader>tt` | 生成 Jest 单元测试 |
| `<leader>tf` | 生成文件 / 代码片段 |

> 你可以在 `on_attach` 钩子里自定义键位。

### 使用命令行

```vim
:TSFixAll            " 彻底修复所有错误
:TSOrganizeImports   " 自动组织 import 语句
:TSRefactor          " 打开重构菜单
:TSInstall <module>  " 安装插件的 additional 模块（如 snippets）
```

### 调试集成

1. 安装 `nvim-dap` 与 `nvim-dap-ui` 。  
2. 设置 TypeScript 调试配置：

```lua
require("dap-config").tsconfig {
  config = {
    typescript = {
      autocomplete = true
    }
  }
}
```

3. 使用 `<leader>dt` 开始调试，使用 `<leader>dS` 暂停/继续，`<leader>do` 单步等。

---

## 贡献与报告问题

- 任何功能建议或 bug 报告都可以提交到 GitHub 的 Issues 页面。  
- 如需贡献代码，请 fork 本仓库，编辑后提交 PR。

---

## 结语

`typescript-tools.nvim` 为 Neovim 爱好者提供了类 VSCode 思路的 TypeScript 开发体验，强大且轻量。无论是日常写代码、调试还是单元测试，均可通过此插件快速完成。  
祝编码愉快 🚀

