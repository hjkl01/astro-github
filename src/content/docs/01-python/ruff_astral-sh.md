
---
title: ruff
---


# Ruff

- **项目地址**: https://github.com/astral-sh/ruff  
- **简介**: Ruff 是一个极快的 Python 静态分析器（linter）和代码格式化工具，兼具 SQA、PEP8、代码质量检查、错误检测以及格式化功能。它借助 Rust 编写，性能远超传统工具，内置大量规则，可通过配置文件进行高度自定义。

## 主要特性

| 序号 | 功能 | 说明 |
|------|------|------|
| 1 | **高速** | 通过 Rust 开发，单文件分析平均耗时 < 10 ms，CLI 速度较 Flake8 提升 10–50 倍。 |
| 2 | **多功能** | 兼具 `flake8` + `black` + `isort` 等多工具功能。 |
| 3 | **自带检查规则** |> 200 条内置规则（PEP8、PEP257、Python Typing 等）。支持按需开启/禁用。 |
| 4 | **格式化** | 自带强大代码格式化器，可与 `black` 对齐或使用默认模式。 |
| 5 | **快速修复** | 自动修复大部分错误（即 `ruff --fix`）。 |
| 6 | **可扩展** | 支持自定义插件、规则以及配置文件（`pyproject.toml`）。 |
| 7 | **兼容性** | 与 VS Code、PyCharm、CLI 以及 CI/CD 流程无缝集成。 |
| 8 | **多语言支持** | 除 Python 外，还可分析 JavaScript/TypeScript（experimental）。 |

## 安装

```bash
# 通过 pip
pip install ruff

# 或使用其他打包工具
pipx install ruff
```

## 基本用法

```bash
# 检查
ruff check path/to/file.py

# 检查整个项目
ruff check .

# 自动修复
ruff check . --fix

# 仅运行格式化
ruff format .

# 查看可用命令
ruff --help
```

## 配置

在项目根目录添加 `pyproject.toml`，示例：

```toml
[tool.ruff]
line-length = 88
select = ["E", "F", "W"]
ignore = ["E203", "W503"]
```

## 集成示例

### VS Code

```json
// settings.json
{
    "python.linting.flake8Enabled": false,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "ruff"
}
```

### GitHub Actions

```yaml
name: Lint
on: [push, pull_request]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install ruff
      - run: ruff check .
```

## 相关链接

- 官方文档: https://docs.astral.sh/ruff/
- GitHub 代码仓库: https://github.com/astral-sh/ruff

