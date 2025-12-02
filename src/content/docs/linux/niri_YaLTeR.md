---
title: niri
---

## 功能介绍

niri 是一个可滚动的平铺 Wayland 合成器，专为 Linux 桌面环境设计。它采用独特的窗口管理方式，将窗口排列在无限向右延伸的条带上，新窗口的打开不会导致现有窗口重新调整大小。

### 主要特性

- **可滚动平铺布局**：窗口按列排列在无限条带上，支持水平滚动浏览。
- **动态工作区**：工作区垂直排列，每个显示器独立管理，支持动态创建和删除。
- **多显示器支持**：每个显示器有独立的窗口条带和工作区，支持混合 DPI。
- **概览模式**：提供缩放视图，便于快速切换工作区和窗口。
- **截图功能**：内置截图界面，支持区域截图。
- **屏幕录制**：通过 xdg-desktop-portal-gnome 支持窗口和显示器录制，可屏蔽敏感窗口。
- **手势支持**：支持触摸板和鼠标手势。
- **标签分组**：可以将窗口分组为标签页。
- **可配置布局**：支持间隙、边框、支柱、窗口大小等自定义。
- **渐变边框**：支持 Oklab 和 Oklch 颜色空间的渐变边框。
- **动画效果**：内置动画，支持自定义着色器。
- **配置热重载**：修改配置后无需重启即可生效。
- **无障碍支持**：兼容屏幕阅读器。

niri 稳定可靠，适合日常使用，支持 NVIDIA 显卡、分数缩放、浮动窗口等高级功能。

## 用法指南

### 安装

niri 可通过多种方式安装：

- **从源码编译**：克隆仓库后使用 Cargo 构建。
- **包管理器**：在 Arch Linux 上可通过 AUR 安装，在 NixOS 上使用 flakes。
- **二进制发布**：从 GitHub Releases 下载预编译二进制文件。

详细安装步骤请参考[官方文档](https://yalter.github.io/niri/Getting-Started.html)。

### 基本使用

启动 niri 后，它将作为 Wayland 合成器运行。你需要配合状态栏（如 waybar）和启动器（如 fuzzel）使用。

#### 常用快捷键

- `Super + T`：打开终端
- `Super + D`：打开应用启动器
- `Super + Q`：关闭窗口
- `Super + H/J/K/L`：切换窗口焦点
- `Super + Shift + H/J/K/L`：移动窗口
- `Super + 1-9`：切换到指定工作区
- `Super + Shift + 1-9`：将窗口移动到指定工作区
- `Super + A`：打开概览模式
- `Super + S`：截图

#### 配置

niri 的配置文件位于 `~/.config/niri/config.kdl`。配置使用 KDL 格式，支持热重载。

示例配置：

```txt
output "eDP-1" {
    scale 1.0
}

layout {
    gaps 16
    struts {
        left 0
        right 0
        top 0
        bottom 0
    }
}

binds {
    Mod+Shift+Q { close-window; }
    Mod+T { spawn "alacritty"; }
    Mod+D { spawn "fuzzel"; }
}
```

更多配置选项请参考[配置文档](https://yalter.github.io/niri/Configuration%3A-Introduction.html)。

### 社区和支持

- **Matrix 聊天室**：[https://matrix.to/#/#niri:matrix.org](https://matrix.to/#/#niri:matrix.org)
- **Discord 服务器**：[https://discord.gg/vT8Sfjy7sx](https://discord.gg/vT8Sfjy7sx)
- **GitHub 仓库**：[https://github.com/YaLTeR/niri](https://github.com/YaLTeR/niri)

niri 是一个活跃的项目，欢迎贡献代码或报告问题。
