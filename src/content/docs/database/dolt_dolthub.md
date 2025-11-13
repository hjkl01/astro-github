---
title: dolt
---

# Dolt 项目概述

**GitHub 项目地址：** [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)

## 主要特性
Dolt 是一个独特的版本控制数据库系统，它将 Git 的版本控制功能与 MySQL 的数据库特性相结合。主要特性包括：
- **版本化数据存储**：像 Git 管理代码一样管理数据库数据，支持分支、合并和回滚操作。
- **SQL 支持**：兼容 MySQL 协议，使用标准 SQL 语言进行查询和操作。
- **分布式协作**：支持多人协作开发数据库，支持拉取（pull）和推送（push）操作，类似于 Git 的工作流。
- **数据差异追踪**：自动记录数据变更历史，便于审计和调试。
- **可移植性**：数据以文本格式存储，便于移植和备份。
- **性能优化**：针对版本控制场景优化，支持高效的查询和变更管理。

## 主要功能
- **分支管理**：创建、切换和删除分支，允许多个开发路径并行进行。
- **合并与冲突解决**：自动合并变更，支持手动解决冲突。
- **历史查询**：通过 SQL 查询任意历史版本的数据，例如 `SELECT * FROM table AS OF COMMIT 'commit_hash'`。
- **数据导入/导出**：支持 CSV、Parquet 等格式的导入和导出。
- **Git-like 命令**：提供 `dolt commit`、`dolt branch`、`dolt diff` 等命令，与 Git 命令类似。
- **远程仓库支持**：集成 GitHub 等平台，实现远程协作。

## 用法
### 安装
1. 从 GitHub Releases 下载预编译二进制文件，或使用包管理器安装（如 Homebrew：`brew install dolthub/tap/dolt`）。
2. 验证安装：运行 `dolt version`。

### 基本用法
1. **初始化数据库**：
   ```
   dolt init mydb
   cd mydb
   ```

2. **创建表和插入数据**（使用 SQL）：
   ```
   dolt sql -q "CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(50));"
   dolt sql -q "INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob');"
   ```

3. **提交变更**：
   ```
   dolt add .
   dolt commit -m "Initial commit"
   ```

4. **创建分支**：
   ```
   dolt branch feature-branch
   dolt checkout feature-branch
   ```

5. **查询历史数据**：
   ```
   dolt sql -q "SELECT * FROM users AS OF 'HEAD~1';"
   ```

6. **合并分支**：
   ```
   dolt checkout main
   dolt merge feature-branch
   ```

7. **克隆远程仓库**：
   ```
   dolt clone https://doltremote.com/repo-name
   ```

更多高级用法请参考官方文档：https://docs.dolthub.com/。Dolt 适用于数据工程师、开发者和需要版本控制的数据库场景。