
---
title: gitbatch
---

# GitBatch 项目

## 项目地址
[GitHub 项目地址](https://github.com/isacikgoz/gitbatch)

## 主要特性
GitBatch 是一个命令行工具，用于批量处理 Git 仓库。它支持在多个 Git 仓库中同时执行常见的 Git 操作，如拉取、推送、状态检查等。主要特性包括：
- **批量操作**：在指定目录下的所有 Git 仓库中并行执行 Git 命令，提高效率。
- **简单易用**：基于命令行，支持交互式和非交互式模式。
- **跨平台支持**：适用于 Linux、macOS 和 Windows 系统。
- **自定义配置**：允许用户通过配置文件或命令行参数自定义行为。
- **错误处理**：提供详细的日志和错误报告，便于调试。

## 主要功能
- **批量 Git 操作**：支持 `git pull`、`git push`、`git status`、`git fetch` 等命令的批量执行。
- **仓库发现**：自动扫描当前目录及其子目录中的 Git 仓库（.git 文件夹）。
- **并行执行**：使用 goroutine（Go 语言实现）并行处理多个仓库，加速操作。
- **过滤与排除**：可以根据仓库名称或路径过滤仓库，支持排除特定目录。
- **状态汇总**：显示所有仓库的状态摘要，包括未提交的更改或远程差异。

## 用法
### 安装
1. 通过 Go 安装：`go install github.com/isacikgoz/gitbatch@latest`
2. 或从 GitHub Releases 下载预编译二进制文件。

### 基本用法
- **扫描并显示状态**：在包含多个 Git 仓库的目录中运行 `gitbatch status`，它会列出所有仓库的状态。
- **批量拉取**：`gitbatch pull` – 在所有仓库中执行 `git pull`。
- **指定命令**：`gitbatch -c "git fetch origin"` – 执行自定义 Git 命令。
- **选项示例**：
  - `-d /path/to/repos`：指定仓库目录。
  - `-e "*.tmp"`：排除匹配的仓库。
  - `-j 4`：设置并行作业数（默认使用 CPU 核心数）。
  - `-v`：启用详细输出。

更多详细信息，请参考项目 README 文件。