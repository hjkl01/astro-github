---
title: ebiten
---

# Ebiten

## 项目简介

Ebiten (现称为 Ebitengine) 是一个专为 Go 编程语言设计的开源 2D 游戏引擎。它提供了简单易用的 API，让开发者能够快速开发 2D 游戏，并支持跨多个平台部署。

## 主要功能

- **2D 图形渲染**：
  - 几何和颜色变换（通过矩阵）
  - 多种合成模式
  - 离屏渲染
  - 文本渲染
  - 自动批处理
  - 自动纹理图集
  - 自定义着色器

- **输入处理**：
  - 鼠标
  - 键盘
  - 游戏手柄
  - 触摸

- **音频支持**：
  - Ogg/Vorbis
  - MP3
  - WAV
  - PCM

## 支持平台

- Windows (无需 Cgo!)
- macOS
- Linux
- FreeBSD
- Android
- iOS
- WebAssembly
- Nintendo Switch
- Xbox (支持有限，仅对特定用户开放)

## 使用方法

1. **安装**：
   - 对于桌面平台，请参考 [安装指南](https://ebitengine.org/en/documents/install.html)。
   - 对于移动平台，请参考 [移动开发指南](https://ebitengine.org/en/documents/mobile.html)。

2. **基本用法**：
   - 导入包：`import "github.com/hajimehoshi/ebiten/v2"`
   - 创建游戏结构体，实现 `Update` 和 `Draw` 方法。
   - 使用 `ebiten.RunGame` 启动游戏循环。

3. **示例代码**：

   ```go
   package main

   import (
       "log"
       "github.com/hajimehoshi/ebiten/v2"
   )

   type Game struct{}

   func (g *Game) Update() error {
       return nil
   }

   func (g *Game) Draw(screen *ebiten.Image) {
       // 绘制逻辑
   }

   func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
       return 320, 240
   }

   func main() {
       game := &Game{}
       if err := ebiten.RunGame(game); err != nil {
           log.Fatal(err)
       }
   }
   ```

4. **更多资源**：
   - [官方网站](https://ebitengine.org)
   - [API 参考](https://pkg.go.dev/github.com/hajimehoshi/ebiten/v2)
   - [速查表](https://ebitengine.org/en/documents/cheatsheet.html)
   - [示例](https://github.com/hajimehoshi/ebiten/tree/main/examples)

## 许可证

Ebiten 采用 Apache 许可证版本 2.0。
