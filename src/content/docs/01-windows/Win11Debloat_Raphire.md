---
title: Win11Debloat
---

# Win11Debloat 项目描述

## 项目地址

[GitHub 项目地址](https://github.com/Raphire/Win11Debloat)

## 主要特性

Win11Debloat 是一个简单、易用且轻量的 PowerShell 脚本，用于快速清理和改善 Windows 体验。它可以移除预装的 bloatware 应用、禁用遥测、移除侵入性界面元素等，无需手动逐一设置。主要特性包括：

- **应用移除**：移除各种预装应用，包括 Microsoft 和第三方应用。
- **遥测和跟踪禁用**：禁用遥测、诊断数据、活动历史、应用启动跟踪和定向广告。
- **AI 功能禁用**：禁用 Bing 搜索、Copilot、Windows Recall 等。
- **个性化**：启用暗模式、禁用透明度和动画、恢复旧上下文菜单等。
- **文件资源管理器和任务栏自定义**：更改默认设置、隐藏元素等。
- **其他优化**：禁用 Xbox 录制、快速启动等。

## 主要功能

- **应用移除**：移除默认或自定义选择的预装应用，包括 Cortana、Xbox、Candy Crush 等。
- **隐私和跟踪**：禁用广告、建议、MSN 新闻馈送、Edge 中的广告。
- **Bing 和 AI**：禁用 Bing 搜索、Copilot、AI 功能。
- **个性化**：暗模式、禁用动画、鼠标加速等。
- **文件资源管理器**：显示文件扩展名、隐藏文件夹等。
- **任务栏和开始菜单**：对齐图标、隐藏搜索、禁用推荐等。
- **其他**：禁用游戏覆盖、快速启动、网络连接等。
- **高级功能**：支持审计模式、应用于其他用户、Sysprep 模式。

## 用法

1. **快速方法**：打开 PowerShell（管理员），运行：

   ```
   & ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
   ```

   跟随提示。

2. **传统方法**：下载最新版本 ZIP，从 Releases 解压，双击 `Run.bat`。

3. **高级方法**：下载 ZIP，解压，以管理员打开 PowerShell，设置执行策略：

   ```
   Set-ExecutionPolicy Unrestricted -Scope Process -Force
   ```

   导航到目录，运行 `.\Win11Debloat.ps1`。

4. **默认设置**：选择默认模式移除默认应用，或使用 `-RunDefaults` 参数。

5. **注意事项**：使用风险自负；更改可通过 Microsoft Store 恢复；支持命令行参数自定义。

更多细节请参考项目 Wiki。
