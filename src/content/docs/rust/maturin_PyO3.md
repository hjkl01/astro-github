---
title: maturin
---


# maturin

> GitHub 项目地址: [https://github.com/PyO3/maturin](https://github.com/PyO3/maturin)

## 概述

maturin 是一个用于将 Rust 代码作为 Python 扩展模块构建、打包、发布的工具。

## 主要特性

- **一站式构建**：直接使用 Cargo 构建 Rust 代码并生成 Python 可导入的 `.so` / `.pyd` 文件。
- **打包支持**：可生成 `.whl`（wheel）和 `.tar.gz` 两种 Python 包形式。
- **PyPI 发布**：内置命令 `maturin upload`，可直接上传到 PyPI。
- **`maturin develop`**：在本地开发时自动生成、安装并即时更新 Rust 代码，适用于持续集成/开发。
- **透明的依赖管理**：使用 Cargo 的 `Cargo.toml` 来声明 Rust 依赖，同时支持互操作。

## 功能

- `maturin develop`：在本地安装开发版本，支持热更新。
- `maturin build`：构建 wheel 或 tar.gz。
- `maturin upload`：上传到 PyPI 或 TestPyPI。
- `maturin init`：创建新项目模板。
- 兼容 `setuptools-rust`、`poetry-dynamic-versioning` 等 Python 包管理工具。

## 用法

```bash
# 初始化新项目
maturin init --name my_crate

# 开发模式（在 Python 环境中自动安装并随文件变更更新）
maturin develop

# 生成 wheel 包
maturin build --release

# 发布到 PyPI
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pk-xxxx
maturin upload target/wheels/*.whl
```

> 进一步的命令与参数请参考官方文档：<https://www.maturin.rs/docs/>。
