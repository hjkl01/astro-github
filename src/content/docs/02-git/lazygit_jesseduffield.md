---
title: lazygit
---

# LazyGit 项目

## 项目地址
[https://github.com/jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

## 主要特性
LazyGit 是一个终端（TUI）Git 客户端，使用 Go 语言开发，旨在提供直观的图形界面来简化 Git 操作。它支持大多数 Git 命令，通过键盘快捷键实现高效交互。主要特性包括：
- **可视化 Git 工作流**：显示分支、提交历史、暂存区和未暂存文件的状态，支持实时更新。
- **键盘驱动**：所有操作通过快捷键完成，无需鼠标，支持自定义键绑定。
- **集成 Git 功能**：包括分支管理、提交编辑、变基（rebase）、合并（merge）、拉取（fetch/pull）和推送（push）等。
- **过滤与搜索**：快速搜索提交、文件或分支，支持自定义过滤视图。
- **子模块支持**：处理 Git 子模块的导航和操作。
- **无依赖安装**：跨平台（Linux、macOS、Windows），通过单一二进制文件运行。
- **自定义配置**：支持 YAML 配置文件调整 UI 主题、行为和集成（如 diff 工具）。

## 主要功能
- **文件管理**：查看和操作工作目录文件，支持暂存/取消暂存、解决冲突。
- **提交历史**：浏览日志，支持挑选（cherry-pick）、交互式变基、回滚提交。
- **分支操作**：创建、切换、删除分支；查看分支图（类似 git log --graph）。
- **远程仓库**：管理远程仓库、标签（tags）和 stash 操作。
- **Diff 查看**：内置差异比较，支持外部 diff 工具集成。
- **插件扩展**：可与外部工具如 GitHub CLI 或自定义脚本集成。

## 用法
1. **安装**：
   - 通过 Homebrew（macOS/Linux）：`brew install lazygit`
   - 通过 Scoop（Windows）：`scoop install lazygit`
   - 从 GitHub Releases 下载二进制文件，或使用包管理器如 apt/yum。
   - 验证：运行 `lazygit --version`。

2. **基本使用**：
   - 在 Git 仓库目录中运行 `lazygit` 启动界面。
   - 使用箭头键导航面板（文件、暂存、提交、分支等）。
   - 常见快捷键：
     - `Space`：暂存/取消暂存文件。
     - `c`：开始新提交（进入编辑模式）。
     - `e`：编辑最后一个提交。
     - `b`：切换分支。
     - `p`：推送当前分支。
     - `g`：拉取更新。
     - `q`：退出。
   - 按 `?` 查看帮助菜单，了解所有快捷键。
   - 配置：编辑 `~/.config/lazygit/config.yml` 文件自定义设置。

LazyGit 适合命令行爱好者，提升 Git 效率，而非替换图形化工具如 GitKraken。