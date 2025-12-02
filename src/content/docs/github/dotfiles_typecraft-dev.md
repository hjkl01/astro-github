---
title: dotfiles
---

## 功能介绍

这个仓库包含了typecraft-dev的dotfiles配置，旨在为Linux用户提供一套完整的桌面环境配置。主要包括以下工具的配置：

- **Neovim**：现代化的文本编辑器配置，使用Lua脚本定制插件和界面。
- **Hyprland**：Wayland窗口管理器配置，提供平铺和浮动窗口管理。
- **Alacritty**：GPU加速的终端模拟器配置，支持自定义主题和字体。
- **Ghostty**：另一个终端模拟器配置。
- **其他工具**：包括i3、Polybar、Rofi、Waybar、Picom、Starship等，用于构建完整的桌面体验。

这些配置旨在提高开发效率和用户体验，支持多种主题和自定义选项。

## 用法

1. **克隆仓库**：

   ```bash
   git clone https://github.com/typecraft-dev/dotfiles.git
   cd dotfiles
   ```

2. **安装配置**：
   使用GNU Stow或其他dotfiles管理工具来链接配置文件到用户目录。例如：

   ```bash
   stow nvim  # 安装Neovim配置
   stow hyprland  # 安装Hyprland配置
   ```

3. **自定义**：
   根据个人需求修改配置文件中的设置，如主题、快捷键等。

4. **依赖安装**：
   确保系统已安装相应工具，如Neovim、Hyprland等。参考各配置文件中的注释了解具体依赖。

这些dotfiles适用于Arch Linux或其他兼容的Linux发行版，提供了一个现代化的开发环境。
