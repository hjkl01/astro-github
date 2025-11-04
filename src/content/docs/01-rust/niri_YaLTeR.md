
---
title: niri
---


# Niri: 一个简约高效的 Wayland 窗口管理器

> 项目地址: [https://github.com/YaLTeR/niri](https://github.com/YaLTeR/niri)

---

## 1. 项目简介

Niri 是用 Rust 编写的 **Wayland** 窗口合成器，灵感来源于传统的 tiling compositor（如 Sway、i3），但在设计上采用了更精简、模块化的方案。它以 **无配置** 或 **极简配置** 为目标，提供了一套适用于日常工作流的默认键位与功能。项目通过 `wlroots` 框架实现，兼容多数 Wayland 生态工具（swaymsg、wayland-clipboard、wl-clipboard 等）。

---

## 2. 主要特性

| 特性 | 说明 |
|------|------|
| **完整的动态 tiling** | 自动平铺、划分、切换、最大化，支持多屏与多工作区 |
| **手动划分与自动布局** | 支持矩形切分（horizontal/vertical），和多列/多行布局 |
| **Scratchpad** | 以内存划分方式隐藏/显示窗口（类似 i3 的 scratchpad） |
| **Gap 与 border** | 通过配置文件可设置窗口间隙、边框宽度与颜色 |
| **Wayland 与 X11 双重支持** | 通过 `xwayland` 运行 X11、Wayland 应用 |
| **系统集成** | 与 `swaymsg`、`waybar`、`wlogout`、`swaylock`、`grim` 等工具保持兼容 |
| **模块化配置** | 使用 TOML 配置文件，支持多屏布局、键位表自定义 |
| **日志与调试** | `niri-hyprland` (类似 hyprctl) 用于实时调试与状态查询 |
| **Live Reload** | 修改配置后可即时热重载，提升开发体验 |
| **安全优先** | Rust 语言 + `wlroots` 缓冲区沙盒，最小化权限泄露风险 |

---

## 3. 功能概览

1. **窗口管理**  
   - `Mod + j/k/h/l`：聚焦上下/左右窗口  
   - `Mod + m`：最大化窗口  
   - `Mod + o`：平铺窗口  
   - `Mod + Shift + q`：关闭窗口  

2. **工作区切换**  
   - `Mod + 1…9`：切换工作区  
   - `Mod + Shift + 1…9`：将当前窗口移动到指定工作区  

3. **拔升与分割**  
   - `Mod + ctrl + h/l`：水平拆分窗口  
   - `Mod + ctrl + j/k`：垂直拆分窗口  

4. **Scratchpad 操作**  
   - `Mod + ~`：切换 Scratchpad  
   - `Mod + Shift + Backspace`：清空 Scratchpad  

5. **多屏与多窗口布局**  
   - 通过 `niri-config.toml` 指定每个屏幕的布局（gap、border、分屏比例）  

6. **状态栏 & 监视**  
   - 集成 `swaybar` 或自定义 `waybar` 样式  
   - 可通过 `niri-hyprctl` 查询窗口信息、策略参数  

---

## 4. 安装 & 运行

```bash
# 克隆仓库
git clone https://github.com/YaLTeR/niri.git
cd niri

# 安装依赖 (Ubuntu 示例)
sudo apt-get install -y libwayland-dev libxkbcommon-dev libwlroots-dev libudev-dev libsqlite3-dev pkg-config libsystemd-dev

# 构建
cargo build --release

# 运行
./target/release/niri
```

> **提示**：在 Wayland 会话启动前请使用 `Exec=/path/to/niri` 配置，若使用 `sway` 兼容模式，请在 `sway` 配置中注释 `exec swaybg` 以避免冲突。

---

## 5. 配置示例 (`$HOME/.config/niri/config.toml`)

```toml
# mod键，默认是 Super
mod_key = "Super"

# 所有键盘快捷键
[bindings]
"Mod+j" = "focus_down"
"Mod+k" = "focus_up"
"Mod+l" = "focus_right"
"Mod+h" = "focus_left"
"Mod+m" = "maximise"
"Mod+o" = "tile"

# Scratchpad
"Mod+~" = "scratchpad_show"
"Mod+Shift+Backspace" = "scratchpad_hide_all"

# Gap 与边框
gap = 8
border_width = 2
border_color = "#555555"
```

---

## 6. 常用命令

| 命令 | 用途 |
|------|------|
| `niri-hyprctl get` | 获取当前窗口状态 |
| `niri-hyprctl reload` | 热重载配置 |
| `niri-hyprctl move_to_desktop 2` | 将窗口移动至工作区 2 |
| `niri-hyprctl kill_window` | 终止当前窗口 |

---

> Niri 仍在积极开发中，建议关注官方 issue 以获取最新的功能与修复信息。

--- 

**© 2025 YaLTeR, release under MIT License**