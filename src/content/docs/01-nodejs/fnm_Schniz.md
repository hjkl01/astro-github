---
title: fnm
---

## 功能介绍

fnm 是一个快速且简单的 Node.js 版本管理器，使用 Rust 构建。它提供了跨平台支持（macOS、Windows、Linux），单文件安装，瞬间启动，并支持 `.node-version` 和 `.nvmrc` 文件。

主要特性：

- 🌎 跨平台支持
- ✨ 单文件安装，易于使用
- 🚀 速度快
- 📂 支持 `.node-version` 和 `.nvmrc` 文件

## 安装方法

### 使用脚本（macOS/Linux）

确保系统已安装 `curl` 和 `unzip`，然后运行：

```bash
curl -fsSL https://fnm.vercel.app/install | bash
```

### 使用 Homebrew（macOS/Linux）

```bash
brew install fnm
```

### 使用 Winget（Windows）

```bash
winget install Schniz.fnm
```

### 使用 Scoop（Windows）

```bash
scoop install fnm
```

### 使用 Chocolatey（Windows）

```bash
choco install fnm
```

### 使用 Cargo（Linux/macOS/Windows）

```bash
cargo install fnm
```

### 使用二进制文件

从 [GitHub Releases](https://github.com/Schniz/fnm/releases) 下载最新二进制文件，并将其添加到 PATH 环境变量中。

## Shell 设置

在使用 fnm 之前，需要设置环境变量。通过评估 `fnm env` 的输出来完成。

### Bash

在 `.bashrc` 中添加：

```bash
eval "$(fnm env --use-on-cd --shell bash)"
```

### Zsh

在 `.zshrc` 中添加：

```bash
eval "$(fnm env --use-on-cd --shell zsh)"
```

### Fish

创建 `~/.config/fish/conf.d/fnm.fish` 并添加：

```fish
fnm env --use-on-cd --shell fish | source
```

### PowerShell

在配置文件中添加：

```powershell
fnm env --use-on-cd --shell powershell | Out-String | Invoke-Expression
```

## 基本用法

- 安装 Node.js 版本：`fnm install <version>`
- 使用特定版本：`fnm use <version>`
- 列出已安装版本：`fnm list`
- 查看当前版本：`fnm current`

更多命令请参考 [官方文档](https://github.com/Schniz/fnm/blob/master/docs/commands.md)。
