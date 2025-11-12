---
title: xonsh
---

# Xonsh (xonsh/xonsh)

> 项目地址: <https://github.com/xonsh/xonsh>

## 概述

Xonsh 是一个 Python 驱动的 shell。全功能且跨平台。该语言是 Python 3.6+ 的超集，具有额外的 shell 原语。名称 "Xonsh" 读作 "conch"（🐚），代表它属于命令 shell 的世界。

## 主要特性

- **Python 超集**：在 shell 中直接嵌入 Python 代码，实现脚本化和交互式命令。
- **跨平台**：原生支持 Windows、macOS 和 Linux。
- **混合编程**：结合了 Unix shell 的命令执行能力和 Python 的编程功能。
- **扩展系统**：通过 xontribs（扩展）系统提供额外功能。
- **配置灵活**：通过 xonshrc 文件自定义 shell 行为。
- **钩子机制**：提供生命周期钩子，用于注入自定义逻辑。
- **智能提示**：内置命令补全、语法高亮和历史记录。

## 核心功能

- **环境变量管理**：动态设置和修改 $PATH、$HOME 等。
- **别名系统**：定义命令别名，支持 Python 函数作为命令。
- **模块导入**：直接在 shell 中导入和使用 Python 模块。
- **管道和重定向**：支持 Unix 风格的管道和 I/O 重定向。
- **子进程执行**：无缝执行外部命令和脚本。
- **数据结构**：原生支持列表、字典等 Python 数据结构。

## 安装

### 通过 pip 安装

```bash
python -m pip install 'xonsh[full]'
```

### 通过包管理器

Xonsh 在多个包管理器中可用：

- **Linux/macOS**: `brew install xonsh`
- **更多选项**: 见 [安装文档](https://xon.sh/contents.html#installation)

## 用法

### 基本使用

```bash
# 启动交互式 shell
xonsh

# 执行脚本
xonsh script.xsh

# 内联执行
xonsh -c "echo 'Hello from xonsh'"
```

### Python 集成示例

```python
# 环境变量
$PATH.append('/usr/local/bin')

# 别名
aliases['ll'] = 'ls -l'
aliases['gs'] = 'git status'

# Python 代码
def greet(name):
    return f"Hello, {name}!"

# 使用 Python 特性
files = $(ls).split()
for f in files:
    if f.endswith('.py'):
        echo @(f)
```

### 配置文件 (xonshrc)

在 `~/.xonshrc` 中自定义配置：

```python
# 环境设置
$PATH = ["/usr/local/bin"] + $PATH
$PROMPT = '{user}@{hostname} {cwd} $ '

# 别名
aliases['ll'] = 'ls -la'
aliases['..'] = 'cd ..'

# 钩子函数
def on_pre_init():
    print("Welcome to xonsh!")

# 导入模块
import sys
```

## 扩展 (Xontribs)

Xonsh 支持扩展系统，称为 xontribs：

- [xontrib 列表](https://github.com/topics/xontrib)
- [Awesome xontribs](https://github.com/xonsh/awesome-xontribs)

### 常用 xontribs

```bash
# 安装 xontrib
xpip install xontrib-powerline

# 加载 xontrib
xontrib load powerline
```

## 集成项目

Xonsh 被以下项目使用或兼容：

- **Conda/Mamba**: 现代包管理器
- **Starship**: 跨 shell 提示符
- **Zoxide**: 智能 cd 命令
- **Jupyter**: 通过 xontrib-jupyter
- **更多**: 见 [项目列表](https://xon.sh/projects.html)

## 文档和支持

- 官方文档: <https://xon.sh>
- 教程: <https://xon.sh/tutorial.html>
- 社区: [Zulip Chat](https://xonsh.zulipchat.com/)
- 问题反馈: <https://github.com/xonsh/xonsh/issues>

## 贡献

欢迎贡献！见 [贡献指南](https://xon.sh/devguide.html)。

- 解决 [热门问题](https://github.com/xonsh/xonsh/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc)
- 创建新的 xontrib
- 改进文档或核心功能
