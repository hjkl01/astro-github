---
title: dots-hyprland
---

# dots-hyprland

## 项目概述

这是一个为 Hyprland 窗口管理器设计的 dotfiles 配置项目，提供了一个现代化的桌面环境。项目名为 "dots-hyprland"，由用户 end-4 维护。

## 主要功能

- **概述界面**：显示打开的应用及其实时预览，支持输入搜索、计算或运行命令
- **AI 集成**：支持 Gemini API 和 Ollama 模型
- **自动颜色生成**：基于壁纸自动生成符合 Material Design 3 的美观且易访问的颜色方案
- **透明安装**：安装过程中每个命令都会在执行前显示，确保用户了解操作

## 安装方法

### 推荐安装（illogical-impulse Quickshell）

1. 运行以下命令进行自动安装：

   ```bash
   bash <(curl -s https://ii.clsty.link/get)
   ```

2. 或者手动克隆仓库并安装：
   ```bash
   git clone https://github.com/end-4/dots-hyprland.git
   cd dots-hyprland
   ./setup install
   ```

**注意**：如果您是 Linux 新手，使用 Hyprland 可能会遇到一些挑战。建议先熟悉 Linux 基础知识。

## 默认键绑定

- `Super + /`：显示键绑定列表
- `Super + Enter`：打开终端

其他键绑定类似于 Windows 或 GNOME 用户的习惯。

## 软件依赖

- **Hyprland**：Wayland 合成器，负责管理和渲染窗口
- **Quickshell**：基于 QtQuick 的小部件系统，用于状态栏、侧边栏等
- 完整依赖列表请查看项目中的 `sdata/dist-arch` 文件夹

## 社区支持

- Discord 服务器：[https://discord.gg/GtdRBXgMwq](https://discord.gg/GtdRBXgMwq)
- GitHub Issues：用于报告问题和功能请求

## 许可证

本项目采用 GPL-3.0 许可证。
