
---
title: git-quick-stats
---

# Git Quick Stats 项目描述

**项目地址：** [https://github.com/arzzen/git-quick-stats](https://github.com/arzzen/git-quick-stats)

## 主要特性
Git Quick Stats 是一个命令行工具，用于快速生成 Git 仓库的统计报告。它支持多种可视化输出格式（如 ASCII 艺术图表），并专注于仓库活动分析，包括提交历史、作者贡献和文件变更等。工具轻量级、无需额外依赖，主要依赖 Git 命令，适用于开发者快速洞察项目健康度。

## 主要功能
- **提交统计**：统计指定时间段内的提交数量、作者贡献和变更分布。
- **作者分析**：显示各作者的提交数、插入/删除行数和活跃度排名。
- **文件变更**：追踪文件修改频率、增长趋势和热力图。
- **时间线图表**：生成提交活动的日、周或月时间线，支持 ASCII 或 JSON 输出。
- **自定义过滤**：支持按日期范围、作者或分支过滤数据。
- **导出支持**：可输出为 JSON、CSV 或纯文本，便于进一步处理。

## 用法
1. **安装**：
   - 通过 Homebrew（macOS/Linux）：`brew install git-quick-stats`
   - 手动安装：克隆仓库后运行 `make install`（需 Go 环境）。

2. **基本命令**：
   - 生成整体统计：`git-quick-stats`（在 Git 仓库根目录运行）。
   - 指定时间范围：`git-quick-stats --since "2023-01-01" --until "2023-12-31"`。
   - 作者统计：`git-quick-stats --author` 或 `git-quick-stats --top-authors 5`（显示前 5 名作者）。
   - 文件统计：`git-quick-stats --files`（显示最活跃文件）。
   - 输出格式：`git-quick-stats --json`（JSON 输出）或 `--csv`（CSV 输出）。
   - 帮助：`git-quick-stats --help` 查看所有选项。

工具需要在 Git 仓库中运行，确保已初始化 Git 项目。更多细节请参考项目 README。