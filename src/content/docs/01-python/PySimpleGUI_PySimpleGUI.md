---
title: PySimpleGUI
---

# PySimpleGUI 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/PySimpleGUI/PySimpleGUI)

## 主要特性
PySimpleGUI 是一个用于创建图形用户界面（GUI）的 Python 库，它基于 tkinter、Qt、WxPython 和 Remi 等后端框架，旨在简化 GUI 开发过程。主要特性包括：
- **简单易用**：使用简洁的语法创建复杂的 GUI，无需深入了解底层框架。
- **跨平台支持**：支持 Windows、macOS 和 Linux 等操作系统。
- **多后端兼容**：可以无缝切换不同 GUI 后端，如 tkinter（默认）或 Qt。
- **轻量级**：无需大量代码即可构建窗口、按钮、输入框等元素。
- **事件驱动**：基于事件循环处理用户交互，支持实时响应。
- **主题支持**：内置多种预设主题，便于自定义界面外观。
- **开源免费**：MIT 许可，社区活跃，提供丰富的示例和文档。

## 主要功能
PySimpleGUI 提供了一系列核心功能，用于快速构建交互式应用程序：
- **布局设计**：使用列表和字典定义窗口布局，支持行、列和嵌套元素。
- **控件支持**：包括按钮、文本输入、图像显示、进度条、表格、菜单等常见控件。
- **事件处理**：通过 `window.read()` 或事件循环捕获用户操作，如点击按钮或关闭窗口。
- **文件和图像处理**：内置文件浏览器、多媒体显示功能。
- **多窗口管理**：支持弹出窗口、模态对话框和多线程操作。
- **数据可视化**：集成 Matplotlib 等库，用于图表显示。
- **国际化**：易于添加多语言支持。

## 用法示例
安装 PySimpleGUI 非常简单，使用 pip 命令：
```
pip install PySimpleGUI
```

### 基本用法
以下是一个简单示例，创建一个带有按钮和输入框的窗口：

```python
import PySimpleGUI as sg

# 定义布局：使用列表表示行
layout = [
    [sg.Text("请输入您的姓名：")],
    [sg.Input(key='-NAME-')],
    [sg.Button("提交"), sg.Button("退出")]
]

# 创建窗口
window = sg.Window("简单 GUI 示例", layout)

# 事件循环
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "退出":
        break
    elif event == "提交":
        name = values['-NAME-']
        sg.popup(f"您好，{name}！")

window.close()
```

### 高级用法
- **主题应用**：`sg.theme('DarkBlue3')` 更改窗口主题。
- **文件选择**：使用 `sg.file_browse()` 添加文件选择按钮。
- **图像显示**：`sg.Image(data=image_data)` 加载并显示图像。
- **表格控件**：`sg.Table(values=data, headings=headers)` 创建数据表格。

更多用法请参考官方文档和 GitHub 仓库中的示例代码。该库适合初学者和快速原型开发，学习曲线平缓。