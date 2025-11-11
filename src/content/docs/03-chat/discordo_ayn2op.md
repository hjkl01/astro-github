---
title: discordo
---

## 功能

Discordo 是一个轻量级、安全且功能丰富的 Discord 终端 (TUI) 客户端。它提供了以下主要功能：

- **轻量级**：占用资源少，适合在终端环境中使用。
- **可配置**：支持自定义配置，包括主题、键绑定等。
- **鼠标和剪贴板支持**：提供直观的交互体验。
- **附件支持**：可以处理和显示附件。
- **通知**：支持系统通知。
- **双因素认证和二维码认证**：安全的登录方式。
- **Discord 风格的 Markdown**：支持富文本格式。

## 用法

### 安装

#### 预构建二进制文件

从 [nightly.link](https://nightly.link/ayn2op/discordo/workflows/ci/main) 下载适用于 Windows、macOS 或 Linux 的预构建二进制文件。

#### 包管理器

- Arch Linux: `yay -S discordo-git`
- Gentoo: `emerge net-im/discordo`
- FreeBSD: `pkg install discordo`
- Nix: 添加 `pkgs.discordo` 到 `environment.systemPackages` 或 `home.packages`。
- Windows (Scoop):
  ```
  scoop bucket add vvxrtues https://github.com/vvirtues/bucket
  scoop install discordo
  ```

#### 从源码构建

```bash
git clone https://github.com/ayn2op/discordo
cd discordo
go build .
```

#### Wayland 剪贴板支持

对于 X11 剪贴板兼容性，需要安装 `x11-dev`：

- Ubuntu: `apt install xwayland`
- Arch Linux: `pacman -S xorg-xwayland`

### 使用

1. 运行 `discordo` 可执行文件，无需参数。
   - 如果使用认证令牌，提供 `--token` 命令行标志，或设置 `DISCORDO_TOKEN` 环境变量。令牌会安全存储在操作系统特定的钥匙环中。
2. 输入邮箱和密码，点击 "Login" 按钮继续。

### 配置

配置文件位于：

- Unix: `$XDG_CONFIG_HOME/discordo/config.toml` 或 `$HOME/.config/discordo/config.toml`
- Darwin: `$HOME/Library/Application Support/discordo/config.toml`
- Windows: `%AppData%/discordo/config.toml`

如果未找到配置文件，将使用默认配置。默认配置文件可在 [此处](https://github.com/ayn2op/discordo/blob/main/internal/config/config.toml) 查看。

### FAQ

#### 手动添加令牌到钥匙环

如果遇到错误 "failed to get token from keyring: secret not found in keyring"，请手动添加令牌。

- **Windows**:

  ```
  cmdkey /add:discordo /user:token /pass:YOUR_DISCORD_TOKEN
  ```

- **macOS**:

  ```
  security add-generic-password -s discordo -a token -w "YOUR_DISCORD_TOKEN"
  ```

- **Linux**:
  1. 启动钥匙环守护进程：
     ```
     eval $(gnome-keyring-daemon --start)
     export $(gnome-keyring-daemon --start)
     ```
  2. 创建 `login` 钥匙环（如果不存在）。
  3. 添加令牌：
     ```
     secret-tool store --label="Discord Token" service discordo username token
     ```
     提示输入密码时，粘贴令牌并确认。

**注意**：自动化用户账户或 "self-bots" 违反 Discord 的服务条款。使用此类功能造成的任何损失，本项目不承担责任。
