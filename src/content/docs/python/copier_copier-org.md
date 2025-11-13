---
title: copier
---

# Copier 项目

## 项目地址
[GitHub 项目地址](https://github.com/copier-org/copier)

## 主要特性
Copier 是一个基于 Python 的文件复制和模板生成工具，主要用于项目脚手架（scaffolding）和模板管理。它具有以下核心特性：
- **模板驱动**：支持使用 Jinja2 模板引擎生成文件，支持变量注入、条件逻辑和循环等高级功能。
- **交互式生成**：允许用户在生成项目时通过命令行交互输入参数，支持默认值和验证。
- **版本控制集成**：可以从 Git 仓库拉取模板，并支持模板的更新和子模板嵌套。
- **灵活的配置**：通过 YAML 或 JSON 文件定义模板结构，支持自定义钩子（hooks）来执行预/后处理脚本。
- **跨平台兼容**：纯 Python 实现，支持 Windows、macOS 和 Linux。
- **轻量高效**：专注于文件复制和渲染，避免不必要的依赖。

## 主要功能
- **项目生成**：从模板快速创建新项目，支持自定义变量替换。
- **模板更新**：使用 `copier update` 命令拉取模板的最新版本，并智能合并变化。
- **子模板支持**：模板可以引用其他模板，实现模块化复用。
- **钩子执行**：在生成前后运行自定义 Python 脚本，例如安装依赖或初始化 Git 仓库。
- **CLI 界面**：提供简单的命令行工具，支持 `--vcs` 选项自动初始化版本控制系统。
- **扩展性**：可作为库集成到其他 Python 项目中。

## 用法
### 安装
使用 pip 安装：
```
pip install copier
```

### 基本用法
1. **生成项目**：
   ```
   copier copy <template-source> <output-destination> [options]
   ```
   - `<template-source>`：模板来源，可以是本地路径、Git URL 或 copier 模板仓库。
   - `<output-destination>`：输出目录。
   - 示例：`copier copy https://github.com/example/project-template.git my-project`

2. **交互输入**：运行时会提示输入模板中定义的变量。

3. **更新模板**：
   ```
   copier update <output-destination>
   ```
   这会检查模板变化并应用更新。

4. **创建模板**：
   - 在项目目录中创建 `copier.yml` 文件定义模板变量和结构。
   - 示例 `copier.yml`：
     ```
     _templates:
       - README.md.j2
     project_name:
       type: str
       default: "My Project"
     ```
   - 然后使用 `copier` 命令分享或生成。

更多细节请参考官方文档：https://copier.readthedocs.io/