---
title: serie
---

# serie

**项目地址**: [https://github.com/lusingander/serie](https://github.com/lusingander/serie)

## 功能介绍

Serie (`/zéːriə/`) 是一个 TUI (Terminal User Interface) 应用程序，使用终端仿真器的图像显示协议在终端中渲染丰富的 git commit graph，类似于 `git log --graph --all` 的增强版。

### 主要特性

- **丰富的 commit graph 显示**: 在终端中提供类似 GUI 的 git log graph 体验
- **图像协议支持**: 支持 iTerm2 Inline Images Protocol 和 kitty Terminal Graphics Protocol
- **多种排序算法**: 支持按提交日期 (chrono) 或分支连续性 (topo) 排序
- **可配置的 graph 宽度**: 支持单字符或双字符宽度显示
- **搜索功能**: 支持提交信息的搜索，包括忽略大小写和模糊匹配
- **自定义用户命令**: 可以集成外部工具如 diff 查看器
- **键绑定自定义**: 支持自定义键盘快捷键

### 兼容性

支持以下终端仿真器：

- iTerm2
- WezTerm
- VSCode 集成终端 (需启用图像支持)
- kitty
- Ghostty

不支持终端复用器 (screen, tmux, Zellij 等) 和 Sixel 图形。

## 安装方法

### Cargo (推荐)

```bash
cargo install --locked serie
```

### Arch Linux

```bash
pacman -S serie
```

### Homebrew

```bash
brew install serie
```

或从 tap 安装：

```bash
brew install lusingander/tap/serie
```

### NetBSD

```bash
pkgin install serie
```

### 下载二进制文件

从 [Releases 页面](https://github.com/lusingander/serie/releases) 下载预编译二进制文件。

### 从源码构建

```bash
git clone https://github.com/lusingander/serie.git
cd serie
cargo build --release
```

## 基本用法

在 git 仓库目录中运行：

```bash
cd <your-git-repository>
serie
```

### 命令行选项

- `-p, --protocol <TYPE>`: 图像协议类型 (auto/iterm/kitty，默认 auto)
- `-o, --order <TYPE>`: 提交排序算法 (chrono/topo，默认 chrono)
- `-g, --graph-width <TYPE>`: graph 单元格宽度 (auto/double/single，默认 auto)
- `--preload`: 预加载所有 graph 图像以提高性能

### 主要键绑定

- `j/k` 或 `↓/↑`: 上下移动
- `Enter`: 显示提交详情
- `/`: 开始搜索
- `Tab`: 打开引用列表
- `?`: 显示帮助
- `q` 或 `Ctrl-c`: 退出

### 高级功能

- **搜索**: 支持正则表达式、忽略大小写、模糊匹配
- **用户命令**: 可配置外部命令查看 diff 等 (如 `git diff` 或 `difft`)
- **配置**: 支持 TOML 配置文件自定义颜色、键绑定等

更多详细信息请参考 [官方文档](https://github.com/lusingander/serie)。
