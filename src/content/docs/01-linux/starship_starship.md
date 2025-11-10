---
title: starship
---


# Starship

**GitHub 项目地址**: https://github.com/starship/starship

## 主要特性

- **跨平台**：支持 Linux、macOS、Windows、FreeBSD、NetBSD、OpenBSD、Solaris、Android、WSL 等系统。
- **模块化**：通过配置文件 `starship.toml` 启用/禁用各个模块（如 `git_status`、`python`、`nodejs` 等），可按需自定义提示符。
- **极速渲染**：使用 Rust 编写，渲染速度极快，几乎无延迟。
- **高度可定制**：支持颜色、图标、格式、前缀后缀等多种自定义选项。
- **插件生态**：社区维护大量插件，支持多种语言、工具链（Docker、Kubernetes、Rust、Go、Python 等）。
- **多语言支持**：内置多种语言的提示符，支持中文、俄语等。

## 功能概览

| 功能 | 描述 |
|------|------|
| **Git 状态** | 显示当前分支、提交数、未提交更改、冲突等信息。 |
| **版本控制** | 自动识别并显示当前使用的语言版本（Python, Node.js, Rust, Go 等）。 |
| **时间/日期** | 可选显示当前时间或日期。 |
| **进程信息** | 显示当前进程/终端会话信息。 |
| **目录路径** | 显示当前工作目录，支持自定义显示长度。 |
| **命令执行状态** | 通过 `❯` 或 `❯❯` 等符号显示命令执行成功/失败。 |
| **自定义模块** | 通过插件或自定义脚本添加新功能。 |

## 用法

### 安装

```bash
# macOS (Homebrew)
brew install starship

# Windows (scoop)
scoop install starship

# Linux (curl)
curl -fsSL https://starship.rs/install.sh | sh
```

### 初始化

```bash
# 生成默认配置文件
starship init bash > ~/.bashrc
# 或者 zsh
starship init zsh >> ~/.zshrc
```

### 自定义配置

编辑 `~/.config/starship.toml`（或 `C:\Users\<User>\AppData\Roaming\starship.toml`）：

```toml
# starship.toml

# 设置提示符分隔符
separator = " | "

# 启用 git 状态模块
[git_status]
disabled = false

# 自定义颜色
[username]
style = "bold green"

# 只显示前 3 个目录层级
[directory]
truncation_length = 3

# 禁用 Docker 模块
[docker_context]
disabled = true
```

### 示例

```bash
❯ cd ~/projects/starship
❯ python3 main.py
```

提示符会根据配置显示：

```
❯  main |  python3.11 | ~/proj/starship ❯
```

### 高级用法

- **多终端会话**：在 tmux、screen 等中使用 `starship init` 并启用 `module`。
- **插件**：通过 `starship.toml` 添加第三方插件，例如 `golang`, `kubectl`, `docker`, `terraform` 等。
- **主题切换**：通过更改 `style` 或 `palette` 实现多主题。

---
> **提示**：每次修改 `starship.toml` 后，重启终端或执行 `source ~/.bashrc` / `source ~/.zshrc` 使配置生效。
