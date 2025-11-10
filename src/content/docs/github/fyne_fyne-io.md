---
title: fyne
---

# Fyne

## 功能

Fyne是一个用Go编写的易用UI工具包和应用API，设计用于构建在桌面和移动设备上运行的应用程序，使用单一代码库。受Material Design启发。

## 用法

### 安装

使用go get安装：

```bash
go get fyne.io/fyne/v2@latest
go mod tidy
```

### 运行演示

```bash
go install fyne.io/fyne/v2/cmd/fyne_demo@latest
fyne_demo
```

### 基本示例

```go
package main

import (
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	a := app.New()
	w := a.NewWindow("Hello")

	hello := widget.NewLabel("Hello Fyne!")
	w.SetContent(container.NewVBox(
		hello,
		widget.NewButton("Hi!", func() {
			hello.SetText("Welcome :)")
		}),
	))

	w.ShowAndRun()
}
```

运行：

```bash
go run main.go
```

### 移动模拟

```bash
go run -tags mobile main.go
```

### 打包为移动应用

```bash
fyne package -os android -appID my.domain.appname
fyne install -os android
```

### 更多信息

更多文档请访问[Fyne开发者网站](https://developer.fyne.io/)或[pkg.go.dev](https://pkg.go.dev/fyne.io/fyne/v2?tab=doc)。
