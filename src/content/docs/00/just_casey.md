
---
title: just
---


# just

> **GitHub 项目地址**  
> https://github.com/casey/just

## 项目简介
just 是一个现代化的命令行任务运行器，类似于 Makefile、NPM scripts，但更轻量、易用。它允许你在项目根目录下定义 `justfile`，在其中声明一系列可执行的任务，并通过 `just <task>` 命令快速触发。

## 主要特性
- **语法简洁**：`justfile` 使用 YAML/JSON 类似语法，易于阅读和维护。
- **自动补全**：支持 Bash、Zsh、Fish、PowerShell 等 shell 的命令行补全。
- **变量与参数**：支持全局/局部变量、任务参数、环境变量注入。
- **依赖链**：任务可以依赖其他任务，支持递归调用。
- **跨平台**：兼容 Linux、macOS、Windows。
- **可扩展**：支持自定义函数、插件系统。

## 核心功能

| 功能 | 说明 |
|------|------|
| **任务执行** | `just task_name` 直接执行定义的命令。 |
| **参数传递** | `just task_name --arg1 value1 --arg2 value2` |
| **环境变量** | 在 `justfile` 中使用 `$VAR`，或通过 `just --env VAR=value` 传入。 |
| **任务依赖** | 在任务定义中使用 `depends_on: [task1, task2]`。 |
| **默认任务** | 通过 `default: task_name` 指定默认执行任务。 |
| **命令行补全** | `just --completions` 生成对应 shell 的补全脚本。 |
| **插件** | 通过 `just plugins install <plugin_name>` 安装第三方插件。 |

## 使用示例

1. **安装**  
   ```bash
   cargo install just
   # 或者在 Homebrew 上
   brew install just
   ```

2. **创建 justfile**  
   ```just
   # justfile
   # 定义变量
   hello = "world"

   # 默认任务
   default: greet

   # 任务: greet
   greet:
       echo "Hello, {{hello}}!"

   # 任务: build
   build:
       echo "Building project..."
       # 这里可以放任意 shell 命令
   ```

3. **执行任务**  
   ```bash
   just greet          # 输出: Hello, world!
   just build          # 执行 build 任务
   just greet --hello=ChatGPT   # 传递参数覆盖变量
   ```

4. **补全脚本**  
   ```bash
   just --completions > just-completion.bash
   source just-completion.bash
   ```

5. **查看帮助**  
   ```bash
   just --help
   ```

## 参考文档
- 官方文档: https://just.systems/
- GitHub 仓库: https://github.com/casey/just

