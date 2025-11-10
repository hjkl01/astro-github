---
title: KeymouseGo
---

# KeymouseGo 项目

## 项目地址
[https://github.com/taojy123/KeymouseGo](https://github.com/taojy123/KeymouseGo)

## 主要特性
KeymouseGo 是一个用 Go 语言编写的跨平台自动化工具，主要用于模拟键盘和鼠标操作。它支持 Windows、macOS 和 Linux 系统，具有以下核心特性：
- **跨平台支持**：无需额外依赖，即可在多个操作系统上运行。
- **简单易用**：通过脚本或命令行方式定义自动化序列，适合初学者和开发者。
- **高效模拟**：精确控制键盘按键、鼠标点击、移动和拖拽等操作。
- **脚本化自动化**：支持编写脚本实现复杂任务，如游戏辅助、测试自动化或日常工作流程优化。
- **轻量级**：体积小、启动快，不占用过多系统资源。

## 主要功能
- **键盘模拟**：发送单个键、组合键（如 Ctrl+C）或连续输入文本。
- **鼠标控制**：实现鼠标移动到指定坐标、左键/右键点击、滚轮滚动和拖拽操作。
- **屏幕交互**：支持截屏、像素颜色检测和图像识别，用于条件判断。
- **定时与循环**：内置延时、循环和条件分支，实现定时任务或重复操作。
- **事件监听**：监控键盘和鼠标事件，触发自定义响应。
- **扩展性**：可通过 Go 语言自定义模块，集成更多功能如 HTTP 请求或文件操作。

## 用法
### 安装
1. 确保安装 Go 环境（版本 1.16+）。
2. 克隆仓库：
   ```
   git clone https://github.com/taojy123/KeymouseGo.git
   cd KeymouseGo
   ```
3. 构建项目：
   ```
   go build -o keymousego main.go
   ```

### 基本用法
- **命令行模式**：运行 `./keymousego` 并传入参数，例如模拟按键：
  ```
  ./keymousego keypress "Ctrl+C"
  ```
- **脚本模式**：创建 `.go` 文件编写脚本，例如：
  ```go
  package main

  import (
      "github.com/taojy123/KeymouseGo"
      "time"
  )

  func main() {
      kmg.Init()
      kmg.KeyPress("A")  // 按下 A 键
      time.Sleep(1 * time.Second)
      kmg.MouseClick(100, 200)  // 点击坐标 (100, 200)
      kmg.Destroy()
  }
  ```
  编译运行：`go run script.go`。
- **高级用法**：参考仓库中的 `examples` 目录，结合图像识别实现如游戏自动化或 UI 测试。确保在合法场景下使用，避免违反平台政策。