---
title: xdotool
---

# xdotool 项目描述

## 项目地址
[https://github.com/jordansissel/xdotool](https://github.com/jordansissel/xdotool)

## 主要特性
xdotool 是一个命令行工具，用于模拟 X11 窗口系统的键盘输入和鼠标事件。它支持在 Linux/Unix 环境中自动化图形界面操作，具有以下核心特性：
- **键盘模拟**：发送单个键、键组合或字符串输入，支持修饰键（如 Ctrl、Shift）。
- **鼠标控制**：移动鼠标光标、点击按钮、拖拽操作，以及查询鼠标位置。
- **窗口管理**：搜索、激活、调整大小、移动窗口，支持基于标题、类名或 PID 的窗口匹配。
- **跨窗口操作**：在特定窗口中执行输入或动作，而不干扰其他窗口。
- **脚本友好**：设计为命令行工具，便于集成到 shell 脚本或自动化任务中，支持批量操作。
- **轻量级**：无需图形界面依赖，仅需 X11 环境即可运行。

## 主要功能
- **输入模拟**：模拟用户键盘和鼠标交互，用于测试、自动化脚本或无障碍辅助。
- **窗口操作**：查找窗口、设置焦点、获取窗口信息（如几何尺寸、位置）。
- **事件处理**：支持搜索窗口、等待窗口出现/消失，以及执行键序列。
- **高级功能**：如类型字符串、按键序列执行、鼠标滚轮模拟，以及与 XTEST 扩展集成以实现精确控制。

## 用法示例
xdotool 需要安装后通过命令行使用。基本语法：`xdotool [选项] 命令 [参数]`。

- **发送键盘输入**：
  - 发送单个键：`xdotool key space`（按空格键）。
  - 发送键组合：`xdotool key ctrl+c`（复制）。
  - 输入字符串：`xdotool type "Hello World"`（在当前焦点窗口输入文本）。
  - 执行键序列：`xdotool keydown ctrl key a keyup ctrl`（按住 Ctrl 并按 A）。

- **鼠标操作**：
  - 移动鼠标：`xdotool mousemove 100 200`（移动到坐标 (100,200)）。
  - 点击：`xdotool click 1`（左键单击）。
  - 拖拽：`xdotool mousedown 1 mousemove 300 400 mouseup 1`（从当前位置拖到 (300,400)）。

- **窗口管理**：
  - 搜索窗口：`xdotool search --name "Firefox"`（查找标题含 "Firefox" 的窗口，返回窗口 ID）。
  - 激活窗口：`xdotool windowactivate --sync $(xdotool search --name "Terminal")`（激活终端窗口）。
  - 调整窗口：`xdotool windowmove 0x123456 100 100`（移动窗口 ID 0x123456 到 (100,100)）。

更多用法请参考项目 README 或运行 `xdotool --help`。安装方式：通过包管理器如 `apt install xdotool`（Debian/Ubuntu）或从源代码编译。