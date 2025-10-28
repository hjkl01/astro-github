
---
title: hammerspoon
---

# Hammerspoon 项目概述

## 项目地址
[https://github.com/Hammerspoon/hammerspoon](https://github.com/Hammerspoon/hammerspoon)

## 主要特性
Hammerspoon 是一个 macOS 桌面自动化工具，使用 Lua 脚本语言编写。它允许用户通过编写简单的脚本来自动化和扩展 macOS 的功能。主要特性包括：
- **高效的自动化脚本**：利用 macOS 的原生 API，实现窗口管理、热键自定义和系统事件监听。
- **Lua 脚本支持**：Lua 是一种轻量级脚本语言，易学易用，适合快速开发自动化任务。
- **模块化设计**：提供丰富的内置模块，如窗口控制、键盘/鼠标事件、通知系统和多媒体控制。
- **开源免费**：基于 MIT 许可，完全开源，用户可以自由修改和贡献代码。
- **低资源占用**：运行高效，不会显著影响系统性能。
- **社区支持**：活跃的社区，提供大量预设脚本和配置示例。

## 主要功能
Hammerspoon 的核心功能聚焦于 macOS 桌面环境的增强和自动化，包括：
- **窗口管理**：自动调整窗口大小、位置，支持分屏、多显示器布局。例如，快速将窗口移动到屏幕左侧或最大化。
- **热键和快捷方式**：自定义全局热键，绑定脚本执行特定操作，如切换应用、控制音量或模拟键盘输入。
- **事件监听**：监控系统事件，如应用启动/关闭、鼠标移动或网络变化，并触发相应脚本。
- **系统集成**：与 macOS 的通知中心、剪贴板、Wi-Fi 和蓝牙等系统组件交互。
- **扩展功能**：支持第三方模块扩展，如集成 Spotify 控制、时间跟踪或自定义菜单栏图标。
- **调试和重载**：内置控制台和热重载功能，便于实时测试和修改脚本。

## 用法指南
1. **安装**：
   - 从 GitHub Releases 下载最新版本的 Hammerspoon.app。
   - 将应用拖入 Applications 文件夹，并授予必要的权限（如辅助功能和输入监控）。

2. **配置**：
   - 首次运行后，Hammerspoon 会创建 `~/.hammerspoon/` 目录。
   - 在该目录下编辑 `init.lua` 文件，这是主配置文件。示例：
     ```lua
     -- 示例：创建热键 Ctrl+Alt+H 显示帮助
     hs.hotkey.bind({"ctrl", "alt"}, "H", function()
         hs.alert.show("Hammerspoon 运行中！")
     end)
     ```

3. **编写脚本**：
   - 使用 Lua 语法编写功能模块。参考官方文档中的 API，如 `hs.window` 用于窗口操作。
   - 示例：窗口最大化脚本
     ```lua
     hs.hotkey.bind({"cmd", "alt"}, "M", function()
         local win = hs.window.focusedWindow()
         win:maximize()
     end)
     ```
   - 保存后，按 Cmd+Ctrl+R 热重载配置。

4. **运行和调试**：
   - 通过菜单栏图标访问 Hammerspoon Console，进行脚本测试和错误调试。
   - 探索 Spoons（社区插件）来快速添加功能，如 Reload 配置或窗口提示。

5. **学习资源**：
   - 阅读官方文档：https://www.hammerspoon.org/docs/
   - 加入社区讨论：GitHub Issues 或 Hammerspoon 邮件列表。
   - 示例配置可在 GitHub 的 examples 目录找到。

Hammerspoon 适合开发者、设计师和重度 macOS 用户，用于提升生产力和自定义体验。通过简单脚本，即可实现复杂的自动化任务。