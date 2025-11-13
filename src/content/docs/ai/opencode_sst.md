---
title: opencode
---

# opencode

## 功能

opencode 是一个专为终端构建的 AI 编程代理。它帮助用户处理软件工程任务，包括解决 bug、添加新功能、重构代码、解释代码等。opencode 100% 开源，支持多种 AI 提供商（如 Anthropic、OpenAI、Google 或本地模型），并提供 LSP 支持、TUI 界面和客户端/服务器架构。

## 用法

### 安装

#### 一键安装

```bash
curl -fsSL https://opencode.ai/install | bash
```

#### 包管理器

```bash
npm i -g opencode-ai@latest        # 或 bun/pnpm/yarn
scoop bucket add extras; scoop install extras/opencode  # Windows
choco install opencode             # Windows
brew install opencode      # macOS 和 Linux
paru -S opencode-bin               # Arch Linux
```

**提示：** 在安装前，请移除 0.1.x 之前的版本。

#### 自定义安装目录

opencode 遵循以下优先级安装路径：

1. `$OPENCODE_INSTALL_DIR` - 自定义安装目录
2. `$XDG_BIN_DIR` - XDG Base Directory Specification 兼容路径
3. `$HOME/bin` - 标准用户二进制目录（如果存在或可创建）
4. `$HOME/.opencode/bin` - 默认后备

示例：

```bash
OPENCODE_INSTALL_DIR=/usr/local/bin curl -fsSL https://opencode.ai/install | bash
XDG_BIN_DIR=$HOME/.local/bin curl -fsSL https://opencode.ai/install | bash
```

### 配置和使用

安装后，在终端中运行 opencode 以开始使用。更多配置信息请参考 [官方文档](https://opencode.ai/docs)。

### 社区

- [Discord](https://opencode.ai/discord)
- [X.com](https://x.com/opencode)
