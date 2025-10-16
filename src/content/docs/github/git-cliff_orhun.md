
---
title: git-cliff
---

# Git-Cliff 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/orhun/git-cliff)

## 主要特性
Git-Cliff 是一个高度可定制的 changelog 生成工具，用于从 Git 历史中自动生成变更日志。它支持多种配置选项和模板自定义，旨在帮助开发者快速创建清晰、结构化的项目发布笔记。主要特性包括：
- **高度可定制**：通过 TOML 或 JSON 配置文件自定义生成规则，支持过滤提交、分类标签和模板渲染。
- **Git 集成**：直接从 Git 仓库中解析提交消息，支持 conventional commits 规范。
- **多格式输出**：生成 Markdown、JSON 或纯文本格式的 changelog，支持嵌入 GitHub Actions 等 CI/CD 流程。
- **性能优化**：高效处理大型仓库，支持并行处理和缓存机制。
- **跨平台支持**：适用于 Linux、macOS 和 Windows，支持 Rust 生态的工具链。

## 主要功能
- **自动生成 Changelog**：基于 Git 标签或日期范围，从提交历史中提取并组织变更信息。
- **提交分类**：自动或手动分类提交（如 feat、fix、docs），并生成结构化输出。
- **模板支持**：使用 Handlebars 模板自定义输出格式，支持变量替换和条件渲染。
- **过滤与排除**：排除特定提交、作者或路径，支持正则表达式过滤。
- **集成与扩展**：可作为命令行工具或库使用，支持与其他 Git 工具（如 git-chglog）互操作。

## 用法
### 安装
通过 Cargo（Rust 包管理器）安装：
```
cargo install git-cliff
```
或从 GitHub Releases 下载预编译二进制文件。

### 基本用法
1. **初始化配置文件**：在项目根目录运行 `git cliff --init` 生成默认的 `cliff.toml` 配置文件。
2. **生成 Changelog**：
   - 从最新标签生成：`git cliff --output CHANGELOG.md`
   - 指定标签范围：`git cliff v1.0.0..v2.0.0 --output CHANGELOG.md`
   - 使用配置文件：`git cliff -c cliff.toml`
3. **自定义配置**（在 `cliff.toml` 中）：
   ```
   [changelog]
   header = "## Changelog"
   body = "{{#each commit_groups}}{{#if this.header}}### {{this.header}}\n{{/if}}{{#each this.commits}}- {{this.body}}\n{{/each}}\n{{/each}}"
   tag = "{{version}}"
   ```
4. **高级选项**：
   - 预览模式：`git cliff --unreleased --print`
   - 集成 GitHub：`git cliff --output CHANGELOG.md && git add CHANGELOG.md && git commit -m "docs: update changelog"`
   - 帮助：`git cliff --help` 查看完整选项。

更多细节请参考项目 README。