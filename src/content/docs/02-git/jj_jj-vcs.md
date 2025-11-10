---
title: jj
---

# jj - next‑generation 分布式版本控制系统

**项目地址**  
[https://github.com/jj-vcs/jj](https://github.com/jj-vcs/jj)

## 概述
jj 是一个用 Rust 编写的分布式版本控制系统，旨在提供比 Git 更简洁、更安全、更高效的体验。它采用“Change”而非“Commit”来描述版本历史，以无冲突的方式实现分支与合并，并兼容 Git 生态。

## 主要特性
- **纯 Rust**：高性能、内存安全、易维护。
- **简化数据模型**：使用“Change”而非“Commit”，操作更直观。
- **安全无冲突**：所有更改都是原子性的，天然避免“merge conflicts”。
- **高效快速**：大文件、海量提交情况下仍保持低延迟。
- **Git 兼容**：可以使用 `jj` 与 Git 仓库交互，或直接使用 Git 工具链。
- **可扩展的插件系统**：支持自定义子命令与行为。

## 核心命令
| 命令 | 说明 |
|------|------|
| `jj init` | 初始化本地仓库 |
| `jj clone <url>` | 克隆远程仓库 |
| `jj commit -m "msg"` | 提交更改 |
| `jj push <remote>` | 推送更改到远程 |
| `jj pull <remote>` | 拉取远程更改 |
| `jj log` | 查看提交历史 |
| `jj diff` | 查看差异 |
| `jj status` | 查看工作树状态 |
| `jj branch` | 管理分支 |
| `jj tag` | 管理标签 |
| `jj checkout <ref>` | 切换到指定 Change 或分支 |

## 示例用法
```bash
# 初始化仓库
jj init

# 克隆项目
jj clone https://github.com/jj-vcs/jj.git

# 查看更改
jj status

# 提交更改
jj commit -m "添加新功能"

# 查看日志
jj log --graph

# 推送到远程
jj push origin main

# 拉取远程更新
jj pull origin main
```

## 其他资源
- 官方文档: [https://jj.build/](https://jj.build/)
- 社区讨论: [https://github.com/jj-vcs/jj/discussions](https://github.com/jj-vcs/jj/discussions)
- 贡献指南: [CONTRIBUTING.md](https://github.com/jj-vcs/jj/blob/main/CONTRIBUTING.md)

---