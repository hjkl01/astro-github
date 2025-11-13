---
title: ubuntu-in-termux
---

# Ubuntu in Termux 项目

**GitHub 项目地址:** [https://github.com/MFDGaming/ubuntu-in-termux](https://github.com/MFDGaming/ubuntu-in-termux)

## 主要特性
- **在 Termux 中运行 Ubuntu 环境**：允许用户在 Android 设备上通过 Termux 终端模拟器安装并运行完整的 Ubuntu Linux 系统，而无需 root 权限。
- **轻量级部署**：使用 proot 技术实现无根模拟，支持 Ubuntu 的核心组件如 apt 包管理器、bash shell 等。
- **兼容性强**：适用于大多数 Android 设备，支持 ARM 和 x86 架构，资源占用较低，便于移动设备使用。
- **自定义扩展**：支持安装桌面环境（如 XFCE 或 VNC 远程桌面）、开发工具和服务器软件，实现类似 PC 的 Linux 体验。
- **开源免费**：基于 GNU/Linux 开源许可，用户可自由修改和贡献代码。

## 主要功能
- **系统安装与管理**：通过脚本快速下载并设置 Ubuntu rootfs（文件系统），支持更新、升级和包管理。
- **终端集成**：在 Termux 内直接启动 Ubuntu shell，支持文件共享、命令执行和脚本运行。
- **图形界面支持**：可选安装 X11 或 VNC 服务器，实现图形化 Ubuntu 界面，通过 Termux 的 XSDL 或 VNC Viewer 访问。
- **开发与测试环境**：提供完整的 Linux 工具链，用于编程、编译、运行服务器（如 Node.js、Python 等），适合开发者在手机上测试代码。
- **备份与迁移**：内置工具支持 Ubuntu 环境的备份、恢复和跨设备迁移。

## 用法
1. **安装 Termux**：在 Android 设备上从 F-Droid 或 GitHub 下载并安装 Termux 应用。
2. **更新 Termux**：打开 Termux，运行 `pkg update && pkg upgrade` 更新包源。
3. **安装依赖**：执行 `pkg install wget proot` 安装所需工具。
4. **下载并运行脚本**：在 Termux 中运行以下命令下载安装脚本：
   ```
   wget https://raw.githubusercontent.com/MFDGaming/ubuntu-in-termux/master/ubuntu.sh
   chmod +x ubuntu.sh
   ./ubuntu.sh
   ```
   这将自动下载 Ubuntu rootfs 并设置环境。
5. **启动 Ubuntu**：安装后，运行 `startubuntu` 命令进入 Ubuntu shell。退出时输入 `exit`。
6. **图形化使用（可选）**：安装 VNC 服务器后，运行 `vncserver`，然后使用 VNC Viewer 连接 localhost:1。
7. **更新与维护**：在 Ubuntu 中使用 `apt update && apt upgrade` 保持系统最新；如需卸载，删除相关目录并运行清理脚本。

注意：项目依赖网络连接，首次安装需下载约 500MB 数据。确保 Termux 有存储权限。更多细节请参考 GitHub 仓库的 README 文件。