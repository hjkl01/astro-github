
---
title: ebiten
---


# GitHub项目地址

- [https://github.com/hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten)

## 主要特性

- **跨平台**：支持 Windows、macOS、Linux、iOS、Android、Web (WebAssembly) 等多种平台。
- **高性能**：基于 SDL2 或自研图形库，可在 CPU/GPU 之间高效切换。
- **直接受 2D 像素游戏风格**：提供像素级的图像绘制、混合模式、像素抗锯齿/插值控制。
- **实时游戏循环**：固定 60 FPS 调用 `Update`/`Draw`，已实现标准主循环框架。
- **输入设备支持**：键盘、鼠标、游戏手柄、触摸屏等统一事件系统。
- **音频播放**：支持 Wave、OGG、其他 PCM 格式，低延迟锁定。
- **全部核心 API 用 Go 编写**，无需 C/C++ 交叉编译。  
- **测试友好**：提供主机端 Canvas 及自动 UI 测试工具。

## 核心功能

| 模块 | 说明 |
|------|------|
| **游戏循环** | `ebiten.RunGame(game)` 调用，内部会循环调用 `Update`、`Draw` 并自动处理帧率。 |
| **图像 & 演算** | `ebiten.Image` 是核心图像类型，支持复制、旋转、缩放、切片、像素化、混合等常用操作。 |
| **输入** | `ebiten.IsKeyPressed`, `HasGamepadConnection`, `Keyboard` / `Mouse` 事件 API。 |
| **音频** | `audio.NewPlayer`, 支持流式加载、循环、暂停、淡入淡出。 |
| **UI 交互** | 可通过 `ebiten.DrawImageOptions` 设置旋转、缩放、裁剪、颜色修饰，支持层叠绘制。 |
| **网络** | 提供 `net.Conn`、`http.Client` 示例，`ebiten` 本身不内置网络，但可与标准库无缝集成。 |
| **可扩展性** | 中间件模式支持自定义更新/绘制管线、插件系统。 |

## 使用方式

```go
package main

import (
	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
	"image/color"
)

type Game struct{}

func (g *Game) Update(*ebiten.Game) error {
	// 处理输入、游戏逻辑
	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	// 画面绘制
	screen.Fill(color.RGBA{0, 0, 30, 255})
	ebitenutil.DebugPrint(screen, "Hello, ebiten!")
}

func (g *Game) Layout(int, int) (int, int) {
	return 640, 480
}

func main() {
	ebiten.SetWindowSize(640, 480)
	ebiten.SetWindowTitle("ebiten demo")
	if err := ebiten.RunGame(&Game{}); err != nil {
		panic(err)
	}
}
```

**构建与运行**

```bash
go mod init example.com/ebiten-demo
go get github.com/hajimehoshi/ebiten/v2
go run .
```

**针对 WebAssembly**

```bash
go build -o main.wasm -target wasm
```

在 `static/` 目录下生成相应的 `.js`, 通过 `http-server` 或 `serve` 访问。

**测试**

```bash
go test ./...
```

> 详细 API 文档请参阅官方 Wiki 与源码注释。

---

> 以上内容已办理 Markdown 格式，您可将其保存至 `src/content/docs/00/ebiten_hajimehoshi.md`。
