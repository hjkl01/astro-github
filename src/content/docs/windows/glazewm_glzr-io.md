---
title: glazewm
---

# GlazeWM

GlazeWM 是一个受 i3wm 启发的 Windows 平铺窗口管理器。它允许用户通过键盘驱动的命令轻松组织窗口并动态调整布局。

## 主要功能

- **简单 YAML 配置**：易于自定义的配置文件。
- **多显示器支持**：支持多个显示器的工作空间管理。
- **自定义窗口规则**：为特定窗口设置规则，如始终全屏或分配到特定工作空间。
- **一键安装**：通过安装程序轻松安装。
- **与 Zebar 集成**：可选的状态栏集成。

## 安装

从 [GitHub Releases](https://github.com/glzr-io/GlazeWM/releases) 下载最新版本。安装时可以选择安装 Zebar。

也可以通过包管理器安装：

- **Winget**：`winget install GlazeWM`
- **Chocolatey**：`choco install glazewm`
- **Scoop**：`scoop bucket add extras && scoop install extras/glazewm`

## 配置

默认配置文件位于 `%userprofile%\.glzr\glazewm\config.yaml`。

### 一般设置

```yaml
general:
  startup_commands: [] # 启动时运行的命令
  shutdown_commands: [] # 关闭前运行的命令
  config_reload_commands: [] # 配置重载后运行的命令
  focus_follows_cursor: false # 光标跟随焦点
  toggle_workspace_on_refocus: false # 切换工作空间时切换
  cursor_jump:
    enabled: true
    trigger: 'monitor_focus' # 或 "window_focus"
```

### 键绑定

自定义键盘快捷键：

```yaml
keybindings:
  - commands: ['focus --workspace 1']
    bindings: ['alt+1']
  - commands: ['move --workspace 1', 'focus --workspace 1']
    bindings: ['alt+shift+1']
```

支持的键包括字母、数字、功能键、修饰键等。

### 间隙

设置窗口间的间隙：

```yaml
gaps:
  inner_gap: '20px'
  outer_gap:
    top: '20px'
    right: '20px'
    bottom: '20px'
    left: '20px'
```

### 工作空间

预定义工作空间：

```yaml
workspaces:
  - name: '1'
    display_name: 'Work'
    bind_to_monitor: 0
    keep_alive: false
```

### 窗口规则

为特定窗口设置规则：

```yaml
window_rules:
  - commands: ['move --workspace 1']
    match:
      - window_process: { regex: 'msedge|brave|chrome' }
  - commands: ['ignore']
    match:
      - window_process: { equals: 'zebar' }
```

### 窗口效果

仅适用于 Windows 11：

```yaml
window_effects:
  focused_window:
    border:
      enabled: true
      color: '#0000ff'
  other_windows:
    border:
      enabled: false
      color: '#d3d3d3'
```

### 窗口行为

```yaml
window_behavior:
  initial_state: 'tiling' # 或 "floating"
  state_defaults:
    floating:
      centered: true
      shown_on_top: false
    fullscreen:
      maximized: false
```

### 绑定模式

```yaml
binding_modes:
  - name: 'resize'
    keybindings:
      - commands: ['resize --width -2%']
        bindings: ['h', 'left']
      # ...
```

## 用法

- 使用键盘快捷键管理窗口布局。
- 默认键绑定包括聚焦工作空间、移动窗口、调整大小等。
- 查看 [默认键绑定图表](https://github.com/glzr-io/glazewm/blob/main/resources/assets/cheatsheet.png) 以获取完整列表。

## 常见问题

- **如何在启动时运行？**：创建快捷方式并放入启动文件夹（`shell:startup`）。
- **如何创建自定义布局？**：使用 `alt+v` 更改平铺方向。
- **如何为应用创建规则？**：使用窗口进程、标题或类名匹配。

更多详情请参考 [GitHub 仓库](https://github.com/glzr-io/glazewm)。
