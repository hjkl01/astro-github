---
title: ExplorerPatcher
---

# ExplorerPatcher

这个项目旨在增强 Windows 的工作环境。

## 如何操作？

1. 从 [这里](https://github.com/valinet/ExplorerPatcher/releases/latest) 下载最新版本的设置程序。
   - 选择 `ep_setup.exe` 如果你的设备使用 Intel 或 AMD 处理器，或 `ep_setup_arm64.exe` 如果你的设备使用 Snapdragon 处理器。
1. 运行安装程序。它会自动请求提升权限，关闭 `explorer.exe` 并安装必要的文件。完成后，你会看到桌面和 Windows 10 任务栏。
1. 右键任务栏，选择“Properties”。
1. 要更改任务栏样式，转到“Taskbar”部分并查找“Taskbar style”。
1. 要使用 Windows 10 开始菜单，转到“Start menu”部分并将开始菜单样式更改为 Windows 10。
1. 要使用 Windows 10 Alt+Tab，转到“Window switcher”部分并将“Window switcher (Alt+tab) style”更改为 Windows 10。
1. 随意检查其他配置选项。

就是这样！

**注意：** 某些功能在某些 Windows 版本上可能不可用。

## 卸载

- 右键任务栏，然后点击“Properties”或搜索“ExplorerPatcher”，然后转到“Uninstall”部分，或
- 使用控制面板的“Programs and Features”或“Apps & features”，或
- 运行 `ep_setup.exe /uninstall`，或
- 将 `ep_setup.exe` 重命名为 `ep_uninstall.exe` 并运行。

## 更新

- 程序具有内置更新：转到“Properties” - “Updates” 配置、检查和安装最新更新。了解更多 [这里](https://github.com/valinet/ExplorerPatcher/wiki/Configure-updates)。
- 或者下载最新的 [setup 文件 for x64](https://github.com/valinet/ExplorerPatcher/releases/latest/download/ep_setup.exe) 或 [setup 文件 for ARM64](https://github.com/valinet/ExplorerPatcher/releases/latest/download/ep_setup_arm64.exe) 并简单运行它。

## 捐赠

如果你发现这个项目对你的日常生活至关重要，请考虑通过页面顶部的 [Sponsor](https://github.com/valinet/ExplorerPatcher?sponsor) 按钮捐赠以支持开发，这样我们就可以继续支持更新的 Windows 构建。

## Discord 服务器

加入我们的 Discord 服务器，如果你需要支持，想要讨论这个项目，或者只是想和我们闲聊！

[![Join on Discord](https://discordapp.com/api/guilds/1155912047897350204/widget.png?style=shield)](https://discord.gg/gsPcfqHTD2)

[阅读更多](https://github.com/valinet/ExplorerPatcher/wiki)
