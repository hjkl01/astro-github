
---
title: cli
---


# GitHub CLI (gh)

**项目地址**: https://github.com/cli/cli

GitHub CLI（简称 `gh`）是一个原生命令行工具，允许开发者在终端直接与 GitHub、GitHub Actions、Pull Requests、Issues 等功能交互。它旨在简化工作流程，让常见的 GitHub 操作不再需要切换到浏览器。

## 主要特性

- **原生命令行界面**：无需打开网页，所有 GitHub 相关操作均可在终端完成。  
- **集成 Git**：与 Git 本身无缝配合，使用 `gh` 命令可在现有仓库内直接执行。  
- **支持 Pull Request、Issues、Wiki、Actions**：包括创建、评论、合并、审批等常见操作。  
- **自定义脚本**：支持在 `gh` 中运行自己的脚本或 GitHub Action。  
- **插件扩展**：可以通过插件来扩展功能，社区已提供多种插件。  
- **跨平台**：支持 macOS、Linux、Windows (WSL) 等多平台。  

## 基本用法

### 1. 安装

- **macOS / Linux**  
  ```bash
  brew install gh          # macOS 通过 Homebrew
  sudo apt install gh      # Debian/Ubuntu
  ```

- **Windows**  
  ```powershell
  winget install -e --id=GitHub.cli
  ```

或者直接下载二进制包并解压到 PATH。

### 2. 登录 GitHub

```bash
gh auth login
# 选择 https 还是 ssh；若为 https 会打开浏览器进行授权
```

### 3. 快速创建 Pull Request

```bash
gh pr create --base main --head feature-branch --title "Add new feature" --body "Detailed description"
```

### 4. 查看 Pull Request

```bash
gh pr view 123           # 根据 PR 号码查看
```

### 5. 合并 Pull Request

```bash
gh pr merge 123 --merge   # 直接合并
```

### 6. 处理 Issues

```bash
gh issue create --title "Bug in module" --body "Steps"
gh issue list --state open
gh issue close 456
```

### 7. 调用 GitHub Actions

```bash
gh run list              # 查看最近的工作流运行
gh run watch 123          # 监听特定工作流
```

### 8. 其它有用命令

- 查看仓库信息：`gh repo view`
- 克隆仓库：`gh repo clone user/repo`
- 创建项目：`gh project create`

## 进阶使用

- **组织化工作流程**：利用 CLI 与 `Makefile`、CI 脚本组合，实现自动化任务。  
- **脚本化交互**：在 Bash 脚本中嵌入 `gh`，大幅提升日常运维效率。  
- **多平台脚本**：结合 `gh` 与 `Taskfile`，在不同系统间保持一致行为。  

> **提示**：`gh help` 可查看所有子命令及详细使用说明；`gh <command> --help` 查看具体命令帮助。  

> 访问官方文档了解更多高级功能及插件支持。  

---

> **文件路径**：`src/content/docs/00/cli_cli.md`
