---
title: bottom
---

# bottom

**作者**: ClementTsang  
**项目地址**: https://github.com/ClementTsang/bottom  
**许可证**: MIT

## 项目简介

bottom (btm) 是一个跨平台的图形化进程/系统监控器，灵感来源于 gtop、gotop 和 htop。它提供了一个现代化的终端界面，用于监控系统资源和进程。

## 主要功能

- **图形化可视化小部件**:
  - CPU 使用率（平均和每核）
  - RAM 和 swap 使用率
  - 网络 I/O 使用率
  - 磁盘容量/使用率
  - 温度传感器
  - 电池使用率

- **进程管理**:
  - 显示、排序和搜索进程
  - 支持杀死信号
  - 树模式查看进程关系

- **跨平台支持**: Linux、macOS、Windows
- **可定制性**: 内置和自定义颜色主题、布局调整、过滤选项等
- **基本模式**: htop 风格的简单界面
- **扩展模式**: 聚焦单个小部件

## 用法

### 安装

#### 使用 Cargo

```bash
cargo install bottom --locked
```

#### 使用包管理器

- Arch Linux: `pacman -S bottom`
- Ubuntu/Debian: 下载 .deb 文件并安装
- Homebrew: `brew install bottom`
- 更多安装方式请参考项目文档

### 运行

```bash
btm
```

### 命令行选项

- `btm -h`: 快速帮助
- `btm --help`: 详细帮助

### 键绑定

在应用内按 `?` 查看所有键绑定和鼠标操作。

### 配置

bottom 支持配置文件，可通过命令行参数或编辑配置文件自定义行为。首次运行时会自动生成配置文件。

## 文档

详细文档: https://bottom.pages.dev
