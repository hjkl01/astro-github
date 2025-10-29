
---
title: atuin
---


# AtuIN: 终端历史同步与检索工具

**项目地址**: https://github.com/atuinsh/atuin

## 1. 项目概述

AtuIN（Atuin Shell History Sync）是一款用 Rust 开发的、跨平台的终端历史同步与检索工具。它能够轻松地在多台机器之间同步 shell 历史记录、增强搜索功能，并提供 Web UI 用于浏览、管理和批量删除历史。

## 2. 主要特性 | 说明 |
|------|------|
| **跨设备同步** | 通过内置客户端和自托管服务器，自动将历史记录同步到所有已安装的机器。 |
| **加密存储** | 本地历史记录使用 AES-256 加密，服务器端存储同样加密，保证隐私安全。 |
| **全文搜索** | 支持基于 SQLite 的全文检索，支持正则与布尔搜索。 |
| **Web UI** | 访问 http://localhost:4899 以图形化方式查看和管理历史记录。 |
| **命令建议** | 在终端中通过 `atuin rec` 获得历史命令的补全建议。 |
| **插件兼容** | 支持 Bash, Zsh, Fish, PowerShell 等主流 shell 作为插件使用。 |
| **轻量高效** | 采用 Rust 语言，二进制体积小，启动速度快，几乎不占资源。 |
| **自托与托管两种部署** | 可以使用官方托管服务器（免费/付费）或自行部署实例。 |
| **多平台支持** | 包含 Windows、macOS、Linux、FreeBSD 等平台的预编译二进制。 |

## 3. 功能说明

| 功能 | 说明 | 典型命令 |
|------|------|------|
| **初始化** | 配置与创建数据库，下载或启动服务器 | `atuin init` |
| **同步** | 本地历史同步至远程服务器 | `atuin sync` |
| **搜索** | 在本地历史中查询 | `atuin search <关键词>` |
| **历史补全** | 自动补全最近使用的命令 | `atuin rec` |
| **删除** | 删除历史记录或迁移 | `atuin delete` |
| **服务器监控** | 查看同步状态 | `atuin monitor` |
| **插件化** | 在 shell 中自动加载插件 | `atuin attach --shell {bash,zsh,fish}` |

## 4. 安装与使用

### 4.1 安装

```bash
# 通过 Homebrew (macOS)
brew install atuin

# 通过 apt (Debian/Ubuntu)
curl -Ls https://github.com/atuinsh/atuin/releases/latest/download/atuin-1.24.0-amd64.deb | sudo dpkg -i -

# 通过 Scoop (Windows)
scoop bucket add main
scoop install atuin
```

### 4.2 初始化

```bash
atuin init
# 按提示填写服务器地址、邮箱、密码或 API Key
```

### 4.3 同步

```bash
atuin sync
```

### 4.4 配置插件

```bash
atuin attach --shell zsh   # 对于 Zsh
atuin attach --shell bash  # 对于 Bash
atuin attach --shell fish  # 对于 Fish
```

> 插件后续会在终端自动执行 `atuin rec`，提供命令补全与搜索。

### 4.5 Web 界面

```bash
atuin serve
# 访问 http://localhost:4899
```

## 5. 主要文件结构

```
├─ src/
│  ├─ client/      # 客户端 CLI 代码
│  ├─ server/      # 服务器端代码（Self-host）
│  └─ common/      # 共享类型与工具
├─ web/
│  ├─ src/         # React/Vue 前端代码
│  └─ dist/        # 打包产物
└─ LICENSE
```

## 6. 配置

配置文件默认位于 `~/.config/atuin/config.toml`，示例:

```toml
[server]
url = "https://cloud.atuin.sh"
username = "you@example.com"
password = "CLICKS"

[history]
path = "$HOME/.atuin_history"
sync = true
```

## 7. 贡献

本项目欢迎任何形式的贡献：

1. Fork 项目
2. 创建 Feature 分支
3. 提交 Pull Request
4. 在 issue 中提问 / 反馈

查看 `CONTRIBUTING.md` 获取更详细的步骤。

## 8. 许可证

本项目采用 BSD-3-Clause 许可证，详见 `LICENSE`。

---

**官方文档与示例**: https://docs.atuin.sh/
