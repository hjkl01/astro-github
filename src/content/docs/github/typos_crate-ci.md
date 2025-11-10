---
title: Typos
---

# typos

## 功能介绍

typos 是一个源代码拼写检查器，用于查找和纠正源代码中的拼写错误。它具有以下特点：

- **高效性能**：足够快，可以在大型代码库（monorepos）上运行
- **低误报率**：可以安全地在拉取请求（PR）上运行
- **灵活配置**：支持自定义字典、忽略规则和文件类型配置
- **多种集成**：支持 GitHub Actions、pre-commit 等工具集成

## 用法

### 安装

可以通过多种方式安装 typos：

- **Cargo**：`cargo install typos-cli --locked`
- **Homebrew**：`brew install typos-cli`
- **Conda**：`conda install typos`
- **Pacman**：`sudo pacman -S typos`
- **预构建二进制**：从 [GitHub Releases](https://github.com/crate-ci/typos/releases) 下载

### 基本使用

- **检查拼写错误**：`typos`
- **自动修复错误**：`typos --write-changes` 或 `typos -w`

### 配置

typos 使用 `_typos.toml` 文件进行配置，可以：

- 忽略特定单词或标识符
- 扩展字典
- 配置不同文件类型的检查规则
- 排除特定文件或目录

示例配置：

```toml
[default.extend-words]
# 不要纠正姓氏 "Teh"
teh = "teh"

[files]
extend-exclude = ["localized/*.po"]
```

### 集成

- **GitHub Actions**：使用 typos-action
- **pre-commit**：配置 pre-commit hooks
- **其他工具**：支持 VS Code 扩展、LSP 服务器等

### 调试

- 查看有效配置：`typos --dump-config -`
- 查看处理的文件：`typos --files`
- 查看标识符：`typos --identifiers`
- 查看单词：`typos --words`
- 启用调试日志：`typos -v`
