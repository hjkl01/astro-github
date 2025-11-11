---
title: ExplorerPatcher
---

# ExplorerPatcher (valinet)

GitHub地址: https://github.com/valinet/ExplorerPatcher

## 主要特性

- **支持 Windows 10 和 11**：旨在增强 Windows 工作环境。
- **任务栏自定义**：恢复 Windows 10 风格的任务栏，或使用其他样式。
- **开始菜单选项**：选择 Windows 10 开始菜单样式。
- **窗口切换器**：使用 Windows 10 Alt+Tab 样式。
- **内置更新**：支持自动检查和安装更新。
- **兼容性**：适用于 Intel/AMD 和 ARM64 处理器。

## 功能概览

| 功能           | 说明                             |
| -------------- | -------------------------------- |
| 任务栏样式     | 选择 Windows 10 或其他任务栏外观 |
| 开始菜单样式   | 切换到 Windows 10 开始菜单       |
| Alt+Tab 切换器 | 使用 Windows 10 窗口切换器       |
| 配置选项       | 右键任务栏访问属性进行自定义     |
| 更新管理       | 内置更新检查和安装               |
| 卸载支持       | 多种卸载方式，包括控制面板       |

## 安装与使用

1. 从 [GitHub Releases](https://github.com/valinet/ExplorerPatcher/releases/latest) 下载最新版本的 `ep_setup.exe`（Intel/AMD）或 `ep_setup_arm64.exe`（Snapdragon）。
2. 运行安装程序，它会自动请求提升权限，关闭 explorer.exe 并安装文件。
3. 安装完成后，看到桌面和 Windows 10 任务栏。
4. 右键任务栏，选择“Properties”进行配置。
5. 在“Taskbar”部分更改任务栏样式。
6. 在“Start menu”部分更改开始菜单样式为 Windows 10。
7. 在“Window switcher”部分更改 Alt+Tab 样式为 Windows 10。
8. 检查其他配置选项。

**卸载**

- 右键任务栏，选择“Properties”，转到“Uninstall”部分，或
- 使用控制面板的“程序和功能”或“应用和功能”，或
- 运行 `ep_setup.exe /uninstall`，或
- 将 `ep_setup.exe` 重命名为 `ep_uninstall.exe` 并运行。

**更新**

- 内置更新：转到“Properties” - “Updates” 配置、检查和安装最新更新。
- 或下载最新 setup 文件并运行。

> 注：某些功能在某些 Windows 版本上可能不可用。

---

如需进一步配置或自定义，可查看项目 README 或直接编辑 `settings.json`（位于 `%LocalAppData%\ExplorerPatcher\`）。
