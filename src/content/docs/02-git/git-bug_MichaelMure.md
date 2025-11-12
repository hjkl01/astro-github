---
title: git-bug
---

# git-bug 项目

## 项目地址

[https://github.com/MichaelMure/git-bug](https://github.com/MichaelMure/git-bug)

## 主要特性

git-bug 是一个分布式问题跟踪器，构建在 Git 之上。它将问题作为 Git 的对象处理，利用 Git 的版本控制和分布式特性来管理问题跟踪。核心特性包括：

- **分布式存储**：问题数据存储在 Git 仓库中，支持离线工作和多设备同步。
- **版本化历史**：所有问题更新（如评论、状态变化）都记录为 Git 提交，形成不可变的历史记录。
- **隐私与安全**：支持加密问题数据，适合私有或敏感项目。
- **轻量级集成**：无需额外服务器，直接在现有 Git 仓库中使用。
- **可扩展性**：通过插件或脚本扩展功能，支持自定义操作符和集成。

## 主要功能

- **问题创建与管理**：创建、编辑、关闭问题，支持标签、分配和优先级。
- **评论与协作**：添加评论、提及用户、附件，支持 Markdown 格式。
- **查询与搜索**：使用操作符（如 `status:open author:me`）快速搜索问题。
- **同步与克隆**：像 Git 仓库一样推送/拉取问题数据，支持多仓库协作。
- **报告生成**：生成问题统计报告和可视化视图。
- **身份管理**：使用 Git 身份或自定义身份系统，支持多用户环境。

## 用法

1. **安装**：
   - 通过包管理器安装（如 Homebrew: `brew install git-bug`）或从源代码构建。
   - 确保 Git 已安装。

2. **初始化**：
   - 在现有 Git 仓库中运行 `git bug init` 初始化问题跟踪器。
   - 或在空目录：`git init && git bug init`。

3. **基本命令**：
   - 创建问题：`git bug add --title "问题标题" --message "描述"`。
   - 查看问题：`git bug show <bug-id>`。
   - 列出问题：`git bug log` 或 `git bug log status:open`。
   - 添加评论：`git bug change <bug-id> --message "新评论"`。
   - 关闭问题：`git bug close <bug-id>`。
   - 同步：`git bug push` 和 `git bug fetch`。

4. **高级用法**：
   - 配置身份：`git bug config user.name "Your Name"`。
   - 集成到 CI/CD：使用 API 或钩子自动化 bug 更新。
   - 更多细节参考官方文档：仓库中的 README 和 `git bug help` 命令。

该项目适合 Git 用户寻求简单、分布式的问题跟踪解决方案。
