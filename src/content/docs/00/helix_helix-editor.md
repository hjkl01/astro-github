
---
title: helix
---


# Helix 编辑器（helix-editor）

- **项目地址**：<https://github.com/helix-editor/helix>
- **语言**：Rust  
- **主要目标**：轻量、快速的模态编辑器，兼容 Vim 习惯，内置 LSP，支持多语言编程。

## 1. 主要特性

| 特色 | 简介 |
|------|------|
| 模态编辑 | Normal、Insert、Visual、Operator 等多种模式；如 Vim，快捷键直观、可组合 |
| LSP 原生支持 | 内置语言服务器协议（LSP）客户端，支持大多数主流语言 |
| 异步架构 | 事件循环 + 任务队列，编辑器始终保持响应 |
| 可扩展 UI | 通过 `ui/` 目录编写自定义 UI 模块（如 Statusline、Popups） |
| 包含高级功能 | 多文档、分块、代码折叠、搜索/替换、宏、插件等 |
| 跨平台 | 支持 Linux、macOS、Windows（如官方发行版或自行编译） |

## 2. 快速起步

### 2.1 安装

| 平台 | 方式 | 命令 |
|------|------|------|
| **发行版（官方预编译）** | 直接下载 | `curl -L -o helix.tar.gz https://github.com/helix-editor/helix/releases/latest/download/helix-linux-amd64.tar.gz` <br> `tar xzf helix.tar.gz` <br> `sudo mv helix /usr/local/bin/` |
| **Debian/Ubuntu** | `apt` | `sudo apt install helix`（官方 PPA） |
| **Arch Linux** | AUR | `yay -S helix` |
| **macOS** | Homebrew | `brew install helix` |
| **Windows** | 官方发行版或 winget | `winget install Helix` |
| **源代码编译** | Rust Toolchain | `cargo build --release` <br> `sudo cp target/release/helix /usr/local/bin/` |

> **提示**：安装后可执行 `helix --version` 查看版本。

2.2 启动

```bash
# 打开单文件
helix main.rs

# 或打开多个文件
helix main.rs utils.rs
```

在 Normal 模式下：

- `i` 进入 Insert 模式
- `:wq` 写入并退出
- `:h` 调用帮助
- `Ctrl+Space` 搜索命令

在 Normal 模式下使用 LSP：

- `gd` 跳转到定义
- `gr` 跳转到引用
- `K` 查看文档（悬浮）
- `:lsp` 列出可用命令

## 3. 配置

Helix 的配置文件使用 YAML，默认路径：

- Windows：`%APPDATA%\helix\config.toml`
- macOS/Linux：`~/.config/helix/config.toml`

### 3.1 基本配置示例

```toml
theme = "poison"

[editor]
font = "Fira Code"
line_numbers = true
auto_save = true

[bindings.normal]
"gd" = "goto-definition"
"gr" = "goto-references"
"qq" = "quit"
```

### 3.2 自定义键绑定

```toml
[bindings.insert]
"kj" = "esc"
```

### 3.3 LSP 配置

在 `languages.toml`（同样位于 `~/.config/helix`）：

```toml
[language.rust]
server.path = "rust-analyzer"
server.args = ["-v"]
```

Helix 将根据此自动启动语言服务器。

## 4. 插件（可选）

Helix 通过 `plugins.toml` 支持插件，主要是 Rust crate：

```toml
[plugin]
"formatter" = { package = "helix-formatter", version = "0.3" }
```

> 详细插件开发文档请参见官方仓库的 `plugins/` 目录。

## 5. 常用命令与快捷键

| 快捷键 | 说明 |
|--------|------|
| `:q` | 退出 |
| `:w` | 保存 |
| `:wq` | 保存并退出 |
| `:h` | 帮助 |
| `Ctrl+O` | 弹出文件树 |
| `Ctrl+T` | 打开新标签页 |
| `gd` | 跳转到定义 |
| `gr` | 跳转到引用 |
| `K` | 查看悬浮文档 |
| `:repl` | 打开 REPL（如支持） |

---

> **更多信息**：请查看官方 GitHub 仓库的 README、wiki 以及社区 Wiki。  
> 链接：<https://github.com/helix-editor/helix>
