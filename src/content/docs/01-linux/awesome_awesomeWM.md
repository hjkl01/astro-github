---
title: awesome
---

---

## title: awesome

## Awesome Window Manager（awesomeWM）

**GitHub 项目地址**：<https://github.com/awesomeWM/awesome>

### 简介

Awesome 是一个极简、可编程的窗口管理器，专为 X Window 系统设计。它以 Lua 语言为核心，通过配置文件实现高度可定制的桌面体验。

### 主要特性

- **高度可定制**：所有功能均可通过 Lua 脚本配置，甚至可以写插件扩展。
- **动态窗口布局**：支持多种布局模式（如平铺、浮动、最大化、旋转等），并能在窗口之间自由切换。
- **多显示器支持**：可在多屏幕环境中独立管理每个屏幕的布局、标签和窗口。
- **主题与视觉定制**：提供丰富的主题系统，用户可自行更改图标、颜色、字体等视觉元素。
- **键盘驱动**：几乎所有操作都可以通过键盘快捷键完成，极大提升效率。
- **扩展生态**：社区提供大量 Lua 脚本插件，涵盖状态栏、桌面小工具、系统监控等。

### 主要功能

| 功能            | 说明                                           |
| --------------- | ---------------------------------------------- |
| **窗口管理**    | 自动平铺、浮动窗口，支持窗口分屏、移动、缩放   |
| **标签（Tag）** | 类似工作区，按需求切换显示特定窗口             |
| **多屏幕**      | 对每个屏幕维护独立的标签和布局                 |
| **键盘快捷键**  | 通过 `rc.lua` 配置全局快捷键                   |
| **主题系统**    | `theme.lua` 控制颜色、图标、字体等             |
| **插件系统**    | `rc.lua` 可加载 Lua 脚本实现额外功能           |
| **状态栏**      | `lain`、`wibox` 等库可创建自定义状态栏与小工具 |

### 用法示例

1. **安装**

   ```bash
   # Debian/Ubuntu
   sudo apt install awesome

   # Arch Linux
   sudo pacman -S awesome
   ```

2. **启动**  
   在登录管理器（LightDM、GDM、SDDM 等）中选择 _Awesome_，或在终端输入

   ```bash
   awesome
   ```

3. **配置**  
   配置文件位于 `~/.config/awesome/rc.lua`。

   ```lua
   -- 例：设置快捷键
   awful.key({ modkey,           }, "Return", function () awful.spawn(terminal) end,
             {description = "打开终端", group = "launcher"})
   ```

4. **主题**  
   主题文件在 `~/.config/awesome/themes/`。可复制官方主题并修改 `theme.lua`。

   ```lua
   theme.bg_normal = "#000000"
   theme.fg_normal = "#FFFFFF"
   ```

5. **加载插件**

   ```lua
   -- 例如加载 lain 模块
   local lain = require("lain")
   ```

6. **重载配置**  
   按 `Mod4` + `Ctrl` + `r`（默认）即可在不重启 Awesome 的情况下重新加载配置。

### 小结

Awesome 通过 Lua 脚本实现极致可定制的窗口管理体验，适合喜欢键盘操作、追求极简与高效的用户。其强大的插件系统和主题支持，让你可以随心所欲地打造专属桌面。
