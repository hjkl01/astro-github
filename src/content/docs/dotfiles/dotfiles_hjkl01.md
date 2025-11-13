---
title: dotfiles
---

# GitHub 项目：hjkl01/dotfiles

## 项目地址
[https://github.com/hjkl01/dotfiles](https://github.com/hjkl01/dotfiles)

## 主要特性
- **配置管理**：这是一个个人 dotfiles 项目，用于管理各种 shell 和工具的配置文件（如 .bashrc、.vimrc 等），便于跨设备同步和版本控制。
- **模块化设计**：配置文件采用模块化结构，支持 Vim、Neovim、Zsh 等编辑器和 shell 的自定义设置。
- **自动化安装**：提供脚本支持一键安装和更新配置，简化环境搭建过程。
- **兼容性强**：针对 Linux 和 macOS 系统优化，包含主题、插件和快捷键自定义。

## 主要功能
- **编辑器配置**：集成 Vim/Neovim 的插件管理（如使用 vim-plug 或 packer.nvim），支持语法高亮、代码补全和主题切换。
- **Shell 增强**：自定义 Zsh 或 Bash 提示符、别名和函数，提高命令行效率。
- **工具集成**：包含 Git、Tmux 和其他开发工具的配置文件，支持工作流优化。
- **备份与同步**：通过 Git 仓库实现配置的备份、版本追踪和多机同步。

## 用法
1. **克隆仓库**：运行 `git clone https://github.com/hjkl01/dotfiles.git ~/dotfiles` 将项目克隆到本地。
2. **安装脚本**：进入目录 `cd ~/dotfiles`，然后执行 `./install.sh`（或类似脚本）来链接配置文件到用户主目录。
3. **自定义**：编辑仓库中的配置文件以匹配个人偏好，然后重新运行安装脚本应用更改。
4. **更新**：使用 `git pull` 更新仓库，并重新运行安装脚本以同步最新配置。
5. **注意**：备份现有配置文件以避免覆盖；适用于 Unix-like 系统，首次使用可能需安装依赖如 Vim 或 Zsh。