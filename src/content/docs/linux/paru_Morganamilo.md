---
title: paru
---

# paru

paru 是一个功能丰富的 AUR 助手工具，专为 Arch Linux 设计。它是 pacman 的包装器，提供简洁的界面来安装来自 Arch User Repository (AUR) 的包。

## 功能

- **AUR 包管理**：轻松搜索、安装和更新 AUR 包。
- **pacman 集成**：作为 pacman 的包装器，支持所有 pacman 命令。
- **最小交互**：设计为减少用户交互，提供高效的包管理体验。
- **高级功能**：支持 PKGBUILD 编辑、文件管理器集成、语法高亮等。
- **开发包跟踪**：自动跟踪 \*-git 包的更新。

## 用法

### 安装

```bash
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

### 基本命令

- `paru <target>`：交互式搜索并安装 `<target>`。
- `paru`：等同于 `paru -Syu`，更新系统和 AUR 包。
- `paru -S <target>`：安装特定包。
- `paru -Sua`：升级 AUR 包。
- `paru -Qua`：显示可用的 AUR 更新。
- `paru -G <target>`：下载 `<target>` 的 PKGBUILD 和相关文件。
- `paru -Gp <target>`：打印 `<target>` 的 PKGBUILD。
- `paru -Gc <target>`：打印 `<target>` 的 AUR 评论。
- `paru --gendb`：生成开发数据库，用于跟踪 \*-git 包。
- `paru -Bi .`：构建并安装当前目录的 PKGBUILD。

### 配置

- 查看 `paru(8)` 和 `paru.conf(5)` 手册页获取详细选项和配置。
- 启用颜色：在 `pacman.conf` 中启用 `color`。
- 文件管理器集成：在 `paru.conf` 中设置 `FileManager`。
- 搜索顺序：在 `paru.conf` 中启用 `BottomUp` 以从底部开始搜索。

### 提示

- 使用 `bat` 工具启用 PKGBUILD 语法高亮。
- 编辑 PKGBUILD 时，可以提交更改以使其永久化。
