---
title: dotfiles-public
---

# craftzdog/dotfiles-public 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/craftzdog/dotfiles-public)

## 主要特性
- **跨平台支持**：主要针对 macOS 系统优化，但部分配置可适配其他 Unix-like 系统，如 Linux。
- **现代化工具集成**：使用最新的终端工具栈，包括 Nushell（nu shell）作为默认 shell、Starship 提示符、Zellij 会话管理器，以及 eza（ls 的现代替代品）和 bat（cat 的增强版）等，提升命令行体验。
- **编辑器配置**：内置 Neovim 配置，支持 Lazy.nvim 插件管理器，提供高效的代码编辑环境；同时包括 Helix 编辑器的设置。
- **桌面环境**：针对 Hyprland（Wayland 合成器）提供配置，适用于 Linux 桌面用户，实现流畅的窗口管理。
- **自动化脚本**：包含安装脚本（如 install.sh），自动设置环境变量、字体和工具链，简化配置过程。
- **模块化设计**：配置文件采用模块化结构，便于自定义和扩展，支持 Git 子模块管理外部依赖。

## 主要功能
- **Shell 和终端增强**：替换传统 Bash/Zsh 为 Nushell，提供更强大的数据处理和脚本能力；集成 Atuin（命令历史同步）和 Zoxide（智能 cd 工具）。
- **开发工具链**：预配置 Node.js、Rust、Go 等语言环境，支持 tmux 和 zellij 用于多会话管理。
- **美化与生产力**：使用 Catppuccin 主题方案，美化终端和编辑器；包含 broot（文件浏览器）和 ripgrep（搜索工具）等实用 CLI 工具。
- **系统级优化**：macOS 特定设置包括 Homebrew 包管理、字体安装（如 JetBrains Mono Nerd Font）和 Dock 自定义；Linux 配置聚焦 Hyprland 的方式和键盘绑定。
- **备份与同步**：作为 dotfiles 仓库，便于通过 Git 版本控制和跨设备同步个人配置。

## 用法
1. **克隆仓库**：在终端运行 `git clone --recursive https://github.com/craftzdog/dotfiles-public.git ~/dotfiles-public`，确保子模块完整下载。
2. **运行安装脚本**：进入目录 `cd ~/dotfiles-public`，然后执行 `bash install.sh`（macOS）或相应 Linux 脚本。该脚本会备份现有配置、安装依赖（如 Homebrew 或包管理器）和链接 dotfiles 到 `~` 目录。
3. **自定义配置**：编辑仓库中的文件，如 `~/.config/nvim/init.lua` 用于 Neovim，或 `hypr/hyprland.conf` 用于 Hyprland。修改后重新运行安装脚本应用变更。
4. **针对 macOS**：确保已安装 Xcode Command Line Tools，然后运行脚本会自动处理 Brewfile（包列表）和 macOS 默认设置。
5. **针对 Linux**：安装 Hyprland 和依赖后，运行脚本配置 Wayland 环境；使用 `just` 命令行工具（若安装）执行特定任务，如 `just install-fonts`。
6. **更新与维护**：定期拉取更新 `git pull --recurse-submodules`，并运行 `install.sh` 重新应用。遇到问题可参考仓库的 README.md 或 issues 页面。