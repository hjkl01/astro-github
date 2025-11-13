---
title: HyDE
---

# HyDE

HyDE (Hyprland Desktop Environment) 是一个高度定制化的 Linux 桌面环境，专为开发者和美学爱好者设计。它基于 Hyprland 窗口管理器，提供了一个现代、动态且美观的桌面体验。

## 功能特性

- **窗口管理**: 基于 Hyprland 的平铺窗口管理器，支持动态平铺、浮动窗口和多显示器
- **主题系统**: 支持多种预设主题，包括 Catppuccin、Gruvbox、Tokyo Night 等
- **壁纸管理**: 内置壁纸选择器，支持动态壁纸和多种显示模式
- **启动器**: 自定义 Rofi 启动器，支持多种样式和游戏启动器
- **通知系统**: 集成通知动作和自定义样式
- **虚拟机支持**: 提供 HyDEVM 用于测试和开发
- **多语言支持**: 支持多种语言文档

## 安装使用

### 系统要求

- Arch Linux 或基于 Arch 的发行版 (如 EndeavourOS, Garuda Linux)
- 支持 NixOS (通过 Hydenix 项目)

### 安装步骤

1. 克隆仓库：

```bash
git clone --depth 1 https://github.com/HyDE-Project/HyDE ~/HyDE
cd ~/HyDE/Scripts
```

2. 运行安装脚本：

```bash
./install.sh
```

3. 重启系统并登录 SDDM

### 更新

```bash
cd ~/HyDE/Scripts
git pull origin master
./install.sh -r
```

### 主题和样式

- 使用主题补丁器安装官方主题
- 支持自定义主题创建
- 提供多种壁纸和启动器样式选择

## 自定义选项

- **主题选择**: 通过界面选择不同颜色主题
- **壁纸选择**: 动态壁纸和静态壁纸切换
- **启动器样式**: 12 种不同的 Rofi 样式
- **登出菜单**: 自定义 wlogout 样式
- **游戏集成**: 内置游戏启动器

更多详细信息请参考 [官方文档](https://github.com/HyDE-Project/HyDE) 和 [Wiki](https://hydeproject.pages.dev/)。
