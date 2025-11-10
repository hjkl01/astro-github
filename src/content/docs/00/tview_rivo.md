---
title: tview
---

# tview_rivo

## 项目介绍

tview 是一个用 Golang 编写的终端用户界面库，提供丰富的交互式组件。它允许开发者在终端中创建复杂的用户界面，而无需依赖图形界面库。

## 主要功能

tview 提供了以下常用组件：

- **输入表单**：包括文本输入、选择、复选框和按钮
- **导航多色文本视图**
- **可编辑的多行文本区域**
- **复杂的可导航表格视图**
- **灵活的树视图**
- **可选择的列表**
- **图像显示**
- **网格、弹性盒子和页面布局**
- **模态消息窗口**
- **应用程序包装器**

这些组件具有大量的自定义选项，并且可以轻松扩展以满足特定需求。

## 用法

### 安装

要将此包添加到您的项目中：

```bash
go get github.com/rivo/tview@master
```

### Hello World 示例

以下是一个基本的示例，创建一个标题为 "Hello, World!" 的框并在终端中显示：

```go
package main

import (
    "github.com/rivo/tview"
)

func main() {
    box := tview.NewBox().SetBorder(true).SetTitle("Hello, world!")
    if err := tview.NewApplication().SetRoot(box, true).Run(); err != nil {
        panic(err)
    }
}
```

### 更多示例

查看 [GitHub Wiki](https://github.com/rivo/tview/wiki) 获取更多示例和截图。或者尝试 "demos" 子目录中的示例。

## 依赖

此包基于 [github.com/gdamore/tcell](https://github.com/gdamore/tcell)（及其依赖）以及 [github.com/rivo/uniseg](https://github.com/rivo/uniseg)。

## 文档

参考 [https://pkg.go.dev/github.com/rivo/tview](https://pkg.go.dev/github.com/rivo/tview) 获取包的文档。也请查看 [Wiki](https://github.com/rivo/tview/wiki)。
