
---
title: uv
---

# uv — Astral-sh

项目地址: https://github.com/astral-sh/uv

## 简介

uv 是一个用 Rust 编写的高速、跨平台 Python 包管理器和构建工具，兼容 pip 的命令行接口，旨在提供更快、更可靠、更可预测的 Python 包安装与解析体验。

## 主要特性

- **极速安装**：使用 Rust 的依赖解析与多线程下载，安装速度比 pip 快数倍。
- **可锁定依赖**：`uv lock` 生成精确的 lockfile，确保团队环境一致。
- **全功能包管理**：`uv sync`、`uv pip install`、`uv pip uninstall` 等命令覆盖 pip 常用功能。
- **虚拟环境管理**：`uv venv` 创建、激活、删除虚拟环境，支持多版本 Python。
- **构建与发布**：`uv build` 构建 wheel，`uv publish` 发布到 PyPI 或私服。
- **运行脚本**：`uv run` 直接执行项目脚本，自动激活虚拟环境与依赖。
- **缓存与离线**：本地缓存已下载的 wheel，支持离线安装。
- **多平台兼容**：支持 Windows、macOS、Linux，且在 32/64 位平台均可运行。
- **与 pip 兼容**：大多数 pip 命令行参数均被 uv 支持，迁移成本低。

## 基本用法

```bash
# 安装 uv
curl -Ls https://astral.sh/uv/install.sh | sh

# 生成 lockfile
uv lock

# 同步依赖到虚拟环境
uv sync

# 安装单个包
uv pip install requests

# 升级包
uv pip install --upgrade requests

# 创建虚拟环境
uv venv .venv

# 激活虚拟环境（bash/zsh）
source .venv/bin/activate

# 运行脚本
uv run python script.py

# 构建 wheel
uv build

# 发布到 PyPI
uv publish

# 查看已安装包
uv list
```

## 进阶功能

- **多项目依赖锁**：`uv lock --workspace` 生成工作区锁文件，支持 monorepo 风格项目。
- **镜像源配置**：`uv config` 可以添加自定义镜像，加速国内访问。
- **离线模式**：`uv sync --offline` 仅使用本地缓存安装。

## 参考文档

- 官方文档: https://docs.astral.sh/uv/
- GitHub 仓库: https://github.com/astral-sh/uv