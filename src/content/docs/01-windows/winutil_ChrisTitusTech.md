
---
title: winutil
---

# 项目地址

https://github.com/ChrisTitusTech/winutil

# 主要特性

Chris Titus Tech's Windows Utility 是一个用于Windows系统的实用工具集合，由Chris Titus Tech开发。它旨在简化Windows系统的安装、优化、故障排除和更新过程。该工具编译了作者在每个Windows系统上执行的常见任务，包括安装程序、系统优化调整、故障修复和更新管理。项目注重保持代码的清洁和高效，对贡献有严格的要求。

# 功能

- **安装程序**：提供一键安装常用软件和工具的功能。
- **系统优化（Tweaks）**：包括去膨胀（debloat）功能，帮助移除不必要的预装软件和组件，以提升系统性能。
- **故障排除（Config）**：提供配置和诊断工具，帮助解决常见的Windows问题。
- **修复和更新**：自动化处理Windows更新和修复常见系统错误。
- **构建和开发**：支持源码编译，用户可以克隆仓库并使用自定义编译脚本生成可执行文件。
- **社区支持**：提供Discord社区、文档和YouTube教程，帮助用户使用和贡献项目。

# 用法

Winutil必须以管理员模式运行，因为它执行系统级别的调整。可以通过以下方式启动PowerShell管理员模式：

1. **开始菜单方法**：
   - 右键点击开始菜单。
   - 选择“Windows PowerShell (Admin)”（Windows 10）或“Terminal (Admin)”（Windows 11）。

2. **搜索启动方法**：
   - 按Windows键。
   - 输入“PowerShell”或“Terminal”（Windows 11）。
   - 按Ctrl + Shift + Enter或右键选择“以管理员身份运行”。

### 启动命令

#### 稳定分支（推荐）

```
irm "https://christitus.com/win" | iex
```

#### 开发分支

```
irm "https://christitus.com/windev" | iex
```

如果遇到问题，请参考[已知问题](https://winutil.christitus.com/knownissues/)。

### 构建和开发

Winutil是一个大型脚本，分为多个文件，使用自定义编译器合并为单个.ps1文件。克隆仓库后，运行PowerShell（无需管理员权限）：

```
git clone --depth 1 "https://github.com/ChrisTitusTech/winutil.git"
cd winutil
.\Compile.ps1
```

这将生成`winutil.ps1`文件，可以以管理员身份运行。

更多信息请参考[贡献指南](https://winutil.christitus.com/contributing/)和[Discord社区](https://discord.gg/RUbZUZyByQ)。
