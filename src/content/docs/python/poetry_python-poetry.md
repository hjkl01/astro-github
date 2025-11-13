---
title: poetry
---

# Poetry 项目

**GitHub 项目地址**: [https://github.com/python-poetry/poetry](https://github.com/python-poetry/poetry)

## 主要特性

Poetry 是一个现代化的 Python 依赖管理和打包工具，旨在简化 Python 项目的工作流程。它采用声明式配置方式，类似于 Cargo（Rust）或 npm（Node.js），提供以下核心特性：

- **依赖管理**：使用单一的 `pyproject.toml` 文件声明项目依赖和元数据，支持版本约束和锁定文件（`poetry.lock`）确保环境可重现。
- **虚拟环境管理**：自动创建和管理项目隔离的虚拟环境，支持多种 Python 版本。
- **打包与发布**：内置支持生成 wheel 或 sdist 包，并直接发布到 PyPI 等仓库。
- **脚本执行**：允许定义和管理项目脚本，便于运行自定义命令。
- **插件系统**：支持扩展功能，如自定义发布插件。
- **跨平台兼容**：在 Windows、macOS 和 Linux 上运行良好，支持 Python 3.7+。

Poetry 强调简洁性和可靠性，避免了传统工具如 pip 和 setuptools 的复杂性。

## 主要功能

- **项目初始化**：快速创建新项目骨架，包括 `pyproject.toml` 配置。
- **依赖添加/移除**：智能解析依赖关系，支持开发依赖（dev-dependencies）和可选依赖组。
- **环境安装**：安装项目依赖到隔离环境中，确保一致性。
- **包发布**：验证、构建和上传包到仓库，支持动态元数据。
- **版本管理**：自动 bump 版本号，支持语义化版本（SemVer）。
- **Shell 集成**：提供 `poetry shell` 激活虚拟环境，以及 `poetry run` 执行命令。

## 用法

### 安装 Poetry
通过官方安装脚本：
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
或使用 pip：
```bash
pip install poetry
```
添加 Poetry 到 PATH（参考官方文档）。

### 基本命令

1. **初始化项目**：
   ```bash
   poetry init
   ```
   交互式创建 `pyproject.toml`。

2. **添加依赖**：
   ```bash
   poetry add requests  # 添加运行时依赖
   poetry add pytest --group dev  # 添加开发依赖
   ```

3. **安装依赖**：
   ```bash
   poetry install  # 安装所有依赖，包括开发依赖
   poetry install --no-dev  # 仅安装运行时依赖
   ```

4. **激活环境**：
   ```bash
   poetry shell  # 进入虚拟环境 shell
   # 或
   poetry run python your_script.py  # 在环境中运行命令
   ```

5. **构建和发布**：
   ```bash
   poetry build  # 生成 dist/ 目录下的包
   poetry publish  # 发布到 PyPI（需配置凭证）
   ```

6. **更新和锁定**：
   ```bash
   poetry update  # 更新依赖到最新兼容版本
   poetry lock  # 生成/更新 poetry.lock
   ```

更多高级用法，请参考官方文档：https://python-poetry.org/docs/。