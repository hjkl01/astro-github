
---
title: mergestat
---

# Mergestat 项目

## 项目地址
[GitHub 项目地址](https://github.com/mergestat/mergestat)

## 主要特性
Mergestat 是一个命令行工具，用于查询和分析 Git 仓库中的数据。它将 Git 仓库作为数据库，支持使用 SQL 语言进行查询，允许用户轻松提取和分析代码变更、提交历史、文件统计等信息。主要特性包括：
- **SQL 查询支持**：将 Git 数据（如提交、作者、文件变更）转换为可查询的结构化数据，支持标准 SQL 操作。
- **多仓库支持**：可以同时查询单个仓库或多个仓库的数据。
- **高效性能**：利用 SQLite 作为后端，处理大规模 Git 数据时高效且轻量级。
- **扩展性**：内置多种预定义查询模板，并支持自定义 SQL 查询。
- **开源免费**：基于 Go 语言开发，易于安装和扩展。

## 主要功能
- **数据提取**：从 Git 仓库中提取提交日志、作者信息、文件修改统计、代码行变化等。
- **分析功能**：支持计算代码贡献度、变更频率、作者活跃度等指标。
- **集成查询**：可以结合外部工具或脚本进行数据可视化和报告生成。
- **批量处理**：处理多个 Git 仓库，支持本地或远程仓库。

## 用法
### 安装
1. 通过 Homebrew（macOS/Linux）：  
   ```
   brew install mergestat
   ```
2. 通过 Go 安装：  
   ```
   go install github.com/mergestat/mergestat@latest
   ```
3. 下载预编译二进制文件：从 GitHub Releases 页面下载适合系统的版本。

### 基本用法
1. **查询单个仓库**：  
   导航到仓库目录，运行：  
   ```
   mergestat --repo . "SELECT * FROM commits LIMIT 10"
   ```  
   这将查询当前目录仓库的最近 10 个提交。

2. **查询多个仓库**：  
   ```
   mergestat --repo /path/to/repo1.git --repo /path/to/repo2.git "SELECT repo, author_name, COUNT(*) as commits FROM commits GROUP BY repo, author_name"
   ```  
   这将统计多个仓库中作者的提交数量。

3. **使用预定义查询**：  
   ```
   mergestat --repo . top-authors.sql
   ```  
   其中 `top-authors.sql` 是自定义 SQL 文件，查询顶级贡献者。

4. **帮助命令**：  
   ```
   mergestat --help
   ```  
   查看完整选项和示例。更多用法请参考项目文档中的 SQL 模式和示例查询。