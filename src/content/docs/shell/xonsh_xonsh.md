
---
title: xonsh
---

# Xonsh 项目文档：xonshrc.rst

## 项目地址
[https://github.com/xonsh/xonsh/blob/master/docs/xonshrc.rst](https://github.com/xonsh/xonsh/blob/master/docs/xonshrc.rst)

## 主要特性
xonshrc.rst 是 Xonsh 项目文档的一部分，Xonsh 是一个 Python 驱动的命令行 shell，结合了 Unix shell 的命令执行能力和 Python 的编程功能。该文档主要描述 xonshrc 文件的配置特性，包括环境变量设置、别名定义、钩子函数和启动脚本的自定义。核心特性包括：
- **混合编程支持**：允许在 shell 中直接嵌入 Python 代码，实现脚本化和交互式命令。
- **跨平台兼容**：支持 Windows、macOS 和 Linux，支持多种子命令行（如 bash、cmd.exe）。
- **配置灵活性**：通过 xonshrc 文件自定义 shell 行为，如路径搜索、命令历史和环境变量。
- **扩展性强**：提供钩子（hooks）机制，用于在 shell 生命周期中注入自定义逻辑。

## 主要功能
- **环境配置**：设置 $PATH、$HOME 等环境变量，支持动态修改。
- **别名和命令**：定义命令别名（如 alias ls='ls --color=auto'），并支持 Python 函数作为命令。
- **钩子系统**：包括 on_pre_init、on_post_init 等钩子，用于初始化和事件处理。
- **启动脚本**：xonshrc 文件作为用户配置文件，支持模块导入和全局设置。
- **历史和补全**：配置命令历史记录、自动补全和错误处理。

## 用法
1. **创建配置文件**：在用户目录下创建 `~/.xonshrc` 文件（Windows 为 `%USERPROFILE%\xonshrc.xsh`）。
2. **基本语法**：使用 Python 语法编写，例如：
   ```
   $PATH = ["/usr/local/bin"] + $PATH
   aliases['ll'] = 'ls -l'
   ```
3. **钩子示例**：在 xonshrc 中定义钩子函数：
   ```
   def on_pre_init():
       print("Xonsh 初始化中...")
   ```
4. **运行 Xonsh**：启动 shell 时自动加载 xonshrc。使用 `xonsh` 命令进入交互模式，或通过脚本运行 `xonsh script.xsh`。
5. **高级用法**：导入模块扩展功能，如 `import subprocess` 用于自定义命令执行。参考文档中示例配置环境、集成工具链（如 Git、Docker）。

更多细节请查看源文档。