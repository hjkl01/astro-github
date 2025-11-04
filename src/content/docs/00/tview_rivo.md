
---
title: tview
---


# tview

GitHub项目地址: **https://github.com/rivo/tview**

tview 是一套使用 Go 语言实现的终端用户界面 (TUI) 框架，基于 **tcell** 库构建。它提供了丰富的控件、灵活的布局系统以及事件处理机制，帮助开发者快速创建交互式终端应用。

## 主要特性

| Feature | 说明 |
|---------|------|
| **控件丰富** | 包括 `TextView`, `Table`, `TreeView`, `List`, `Form`, `InputField`, `Dropdown`, `Modal`, `Box`, `Flex`, `Pages` 等，覆盖从文本展示到表格、树形结构、表单等常用 UI 需求。 |
| **布局灵活** | 通过 `Flex`（弹性盒布局）和 `Pages`（层叠页面）实现多列/多页布局，支持水平/垂直滚动、自动换行。 |
| **事件与键盘快捷** | 支持全局键盘事件、每个组件的输入事件、切换焦点、回退、切换页面等，方便自定义快捷键。 |
| **主题/颜色** | 内置多套配色方案，支持自定义 `Styles`（如 `Highlight`, `Primary`, `Secondary` 等）。 |
| **可组合、可扩展** | 所有控件均实现 `Primitive` 接口，可自由嵌套、替换；支持自定义实现 `Primitive` 以扩展新控件。 |
| **高性能** | 采用 tcell，直接操作终端不依赖 curses，渲染速度快且兼容多类终端。 |
| **易于集成** | 小巧易装（`go get github.com/rivo/tview`），可在任何 Go 项目中直接使用，无需额外依赖。 |

## 主要功能

 **构建交互式表格**：支持行列选择、单元格编辑、分组、排序。
- **树形视图**：可折叠/展开节点，适合文件系统、组织结构等展示。
- **表单输入**：多种输入框、下拉框、选项卡、提交处理。
- **层叠页面导航**：使用 `Pages` 控件实现多页面切换，例如登陆页 → 主页面。
- **弹出窗口**：使用 `Modal` 或自定义 `ModalBox` 提示信息、确认对话框。
- **文本渲染**：高亮、转义字符、颜色/背景支持，适合日志查看、代码显示。
- **自定义键盘扫描**：通过 `SetInputCapture` 捕获并处理全局或单个组件的按键。
- **主题切换**：快速切换不同视觉风格，适配暗色/亮色终端。
- **布局自适应**：自动重窗口尺寸变化，保证 UI 一致性。

## 基本使用

```go
package main

import (
    "github.com/r/tview"
)

func main() {
    // 创建应用
    app := tview.NewApplication()

    // 创建表格
    table := tview.NewTable().
        SetBorders(true)

    // 填充数据
    for row := 0; row < 10; row++ {
        for col := 0; col < 5; col++ {
            cell := tview.NewTableCell(fmt.Sprintf("R%dC%d", row, col)).
                SetTextColor(tcell.ColorWhite)
            table.SetCell(row, col, cell)
        }
    }

    // 给表格添加键盘事件
    table.SetDoneFunc(func(key tcell.Key) {
        if key == tcell.KeyEnter {
            app.Stop()
        }
    })

    // 运行 UI
    if err := app.SetRoot(table, true).Run(); err != nil {
        panic(err)
    }
}
```

> **提示**：  
> - `SetRoot` 的第二个参数 `fullScreen` 指明视图是否占据全屏。  
> - 所有组件都实现 `Primitive` 接口，可直接放入 `Flex`、`Pages` 等容器中。  
> - `SetInputCapture` 可用来自定义任何按键的响应逻辑。

## 文档与示例

- 官方 GitHub 仓库 README 内已包含完整安装指南与示例。  
- 仓库同目录下的 `examples/` 目录包含丰富演示代码，可以直接 `go run` 运行。  
- 详细 API 文档可以在仓库 `docs/` 或通过 `go doc github.com/rivo/tview/...` 生成。

---

使用 tview，你可以在几分钟内从零开始构建一个功能完整、视效优雅的终端交互应用。祝编码愉快！