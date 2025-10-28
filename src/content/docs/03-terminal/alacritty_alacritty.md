
---
title: alacritty
---


# Alacritty

## 项目地址
[Alacritty on GitHub](https://github.com/alacritty/alacritty)

## 主要特性
- **GPU 加速渲染**：使用 OpenGL、Metal 或 Vulkan 提升渲染速度，提供极低的延迟和高帧率。  
- **跨平台**：支持 Linux、macOS、Windows。  
- **高度可配置**：全部配置信息存放在一个 `yaml` 文件中，支持颜色、字体、键盘映射、透明度等自定义。  
- **12 种 ANSI/16 种真彩色**：提供高质量的颜色支持。  
- **内嵌 Ligatures**：支持字体合字，提升代码可读性。  
- **透明和模糊效果**：可根据系统支持进行透明处理。  
- **拆分与重排**：通过快捷键可以水平或垂直拆分窗口。  
- **快捷键自定义**：几乎所有功能均可通过键盘映射进行自定义。  
- **语法高亮与自动补全**：不直接提供，但通过插件/终端嵌套可完成。  
- **光标形状与尺寸自定义**：支持块/线/下划线等。  

## 功能概览
| 功能 | 描述 |
|------|------|
| **字体渲染** | 支持 OpenType, TrueType, variable fonts |
| **颜色管理** | 16/256/ANSI/TrueColors，支持主题切换 |
| **鼠标支持** | 文本选择、点击链接，右键复制/粘贴 |
| **窗口缩放** | 通过滚轮或快捷键调节字体大小 |
| **OSC 8 链接** | 支持终端内超链接 |
| **OSC 12 切换背景** | 屏幕捕获/截图前自动禁用透明 |
| **终端内图形** | 通过 kitty integration 等实现容器 |
| **窗口管理** | 单窗口、全屏、最小化、关闭 |

## 快速开始

### 1. 安装

#### Linux  
```bash
# Arch Linux
sudo pacman -S alacritty

# Ubuntu/Debian
sudo add-apt-repository ppa:aslatter/ppa
sudo apt update
sudo apt install alacritty

# 编译
git clone https://github.com/alacritty/alacritty.git
cd alacritty
cargo build --release
cp target/release/alacritty ~/.local/bin/
```

#### macOS  
```bash
brew install alacritty
```

#### Windows  
```powershell
choco install alacritty
```

### 2. 配置文件（`alacritty.yml`）

```yaml
font:
  family: "Fira Code"
  size: 12.0

colors:
  primary:
    background: "0x1e1e2e"
    foreground: "0xFFFFFF"

cursor:
  style: Block

key_bindings:
  - { key: N, mods: Control|Shift, command: SpawnNewInstance }
```

### 3. 打开 Alacritty

```bash
alacritty
```

### 4. 基本快捷键

| 组合 | 功能 |
|------|------|
| `Ctrl+Shift+N` | 新建实例 |
| `Ctrl+Shift+C` | 复制 |
| `Ctrl+Shift+V` | 粘贴 |
| `Ctrl+Shift+T` | 打开标签页 |
| `Ctrl+Shift+W` | 关闭标签页 |
| `Ctrl+Shift+Enter` | 进入全屏 |
| `Ctrl+Plus` | 放大字体 |
| `Ctrl+Minus` | 缩小字体 |
| `Ctrl+0` | 重置字体大小 |

> 更多配置和快捷键请参考 [官方文档](https://github.com/alacritty/alacritty/blob/master/README.md)。

---

> **注**：Alacritty 专注于性能与简洁性，缺少如 tmux 等窗口管理功能，建议与外部终端多路复用器配合使用以获得高级拆分/管理功能。

---  
```
```

将以上内容保存为 `src/content/docs/00/alacritty_alacritty.md`。