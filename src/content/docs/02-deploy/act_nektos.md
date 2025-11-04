
---
title: act
---

# act (nektos/act)

**项目地址**: <https://github.com/nektos/act>

## 主要特性

- **本地运行 GitHub Actions**：在本地机器上执行 GitHub Actions 工作流，方便调试与测试。
- **支持多种 Docker 镜像**：使用官方或自定义 Docker 镜像模拟 GitHub Actions 运行环境。
- **与 GitHub API 集成**：可通过 `--secret`、`--env` 等参数传递环境变量和密钥。
- **多语言与多平台**：支持 Linux、macOS、Windows 等平台。
- **插件式配置**：通过 YAML 文件配置工作流，完全兼容 GitHub Actions 的语法。
- **缓存与依赖管理**：支持缓存策略与依赖安装，提升执行效率。

## 功能概览

| 功能 | 描述 |
|------|------|
| 触发器 | `push`、`pull_request`、`workflow_dispatch` 等 |
| 事件模拟 | `act -e event.json` 以自定义事件触发 |
| 环境变量 | `--env` / `--secret` 传递 |
| 工作流缓存 | `--cache` 开启或关闭缓存 |
| 并发执行 | 支持多工作流并行 |
| 日志 | 详细日志输出，支持 `--log-format` |

## 用法示例

```bash
# 安装
brew install act

# 运行默认工作流
act

# 指定分支
act -b main

# 传递密钥和环境变量
act -s GITHUB_TOKEN=xxxx -e my_event.json

# 使用自定义 Docker 镜像
act -P ubuntu-latest=nektos/act-base:ubuntu-20.04
```

> **提示**：首次运行时，`act` 会自动拉取所需的 Docker 镜像，后续执行速度更快。

--- 

此文档概述了 **nektos/act** 的核心功能与使用方法，帮助开发者在本地快速模拟 GitHub Actions 环境。