---
title: cli
---

# GitHub CLI（GitHub CLI）

**项目地址:** <https://github.com/cli/cli>

## 项目简介
GitHub CLI 是一个官方提供的命令行工具，允许开发者直接在终端中与 GitHub 进行交互。它支持常见的 Git 操作、仓库管理、issue 与 PR 处理、gists、GitHub Actions、企业 GitHub 等多种功能。

## 主要特性

- **仓库管理**  
  - 克隆、创建、删除仓库  
  - 切换分支、合并分支、查看分支状态  
- **Issue 与 Pull Request**  
  - 创建、编辑、关闭 Issue/PR  
  - 评论、分配、标记标签  
  - 查看 PR 状态、比较差异、合并 PR  
- **Gists**  
  - 创建、编辑、删除 Gist  
- **GitHub Actions**  
  - 查看工作流状态  
  - 触发工作流  
- **组织与团队**  
  - 查看组织、团队成员信息  
- **GitHub Pages**  
  - 创建、管理 GitHub Pages  
- **自定义命令**  
  - 通过插件扩展功能  
- **自动化脚本**  
  - 支持 Bash、PowerShell 等脚本集成  
- **多平台支持**  
  - Windows、macOS、Linux

## 安装方式

```bash
# macOS
brew install gh

# Ubuntu
sudo apt install gh

# Windows
winget install --id=GitHub.cli
```

## 基本用法示例

| 命令 | 说明 |
|------|------|
| `gh repo clone <owner/repo>` | 克隆仓库 |
| `gh issue create` | 创建 Issue |
| `gh issue list` | 列出 Issue |
| `gh pr create` | 创建 Pull Request |
| `gh pr merge <pr-number>` | 合并 PR |
| `gh gist create` | 创建 Gist |
| `gh workflow run <workflow>` | 触发工作流 |
| `gh help` | 查看帮助文档 |

## 常用命令

- **仓库操作**  
  - `gh repo clone <repo>`  
  - `gh repo create [<name>]`  
  - `gh repo delete`

- **Issue 操作**  
  - `gh issue create -t <title> -b <body>`  
  - `gh issue close <number>`

- **PR 操作**  
  - `gh pr create -B <base> -H <head>`  
  - `gh pr merge <number>`

- **Gist 操作**  
  - `gh gist create <file>`

- **工作流**  
  - `gh workflow view <name>`  
  - `gh workflow run <name>`

- **插件**  
  - `gh extension install <user/repo>`  
  - `gh extension list`

## 进一步阅读

- 官方文档: <https://cli.github.com/manual/>  
- 插件市场: <https://github.com/cli/cli/blob/trunk/docs/plugins.md>  
- 示例脚本: <https://github.com/cli/cli/tree/trunk/examples>

---