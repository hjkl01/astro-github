
---
title: nes
---

# fogleman/nes

**项目地址**  
[https://github.com/fogleman/nes](https://github.com/fogleman/nes)

---

## 项目简介  
`nes` 是用 Go 语言实现的完整 **NES（Nintendo Entertainment System）** 模拟器。它包含了 CPU、PPU、APU、输入、ROM 加载等核心功能，适合作为学习硬件仿真、游戏开发或嵌入式系统的实验平台。

---

## 主要特性  

| 特性 | 说明 |
|------|------|
| **完整硬件仿真** | 兼容 NES 60Hz 时钟，支持所有 CPU 指令、PPU 渲染、APU 声音。 |
| **图形渲染** | 使用 OpenGL（或软件渲染）在窗口中显示 256×240 像素画面。 |
| **输入支持** | 支持键盘、游戏手柄等多种输入设备。 |
| **调试工具** | 可通过命令行参数开启调试模式，查看 CPU/PPU 状态、内存映像。 |
| **ROM 读取** | 支持标准 NES ROM（.nes）文件格式，自动读取加密/加速信息。 |
| **插件化架构** | 代码组织清晰，易于扩展或替换组件。 |

---

## 功能概览  

* **CPU**：6502/6502-2 兼容，完整指令集实现。  
* **PPU**：像素级渲染，支持背景、精灵、颜色表等。  
* **APU**：波形合成，提供四个音频通道。  
* **内存映射**：支持 RAM、ROM、PPU 寄存器、I/O 等。  
* **输入系统**：键盘映射到 NES 控制器，支持多玩家。  
* **调试接口**：命令行选项 `-debug` 打开调试信息，`-trace` 输出指令执行日志。  
* **渲染后端**：默认使用 OpenGL；在无图形环境下可切换为软件渲染。  

---

## 用法示例  

```bash
# 安装 Go 依赖
go mod tidy

# 直接运行 ROM
go run main.go path/to/game.nes

# 开启调试模式
go run main.go -debug path/to/game.nes

# 只渲染（无音频）
go run main.go -audio=false path/to/game.nes

# 查看帮助
go run main.go -h
```

> **提示**：在 Linux/macOS 上需要先安装 `glfw` 库；在 Windows 上可直接使用预编译的可执行文件。

---

## 运行环境  

| 平台 | 依赖 |
|------|------|
| Windows | .NET 6+ 兼容，OpenGL 3.3 |
| macOS | Xcode 12+，GLFW |
| Linux | glx, glfw3-dev |

---

## 贡献指南  

1. Fork 本仓库。  
2. 新建功能分支，编写代码并添加单元测试。  
3. 提交 Pull Request，说明功能与改动。  

---

## 参考资料  

- [NES 官方硬件文档](http://nesdev.com/)  
- [Go 官方文档](https://golang.org/doc/)  

---