---
title: guietta
---

# Guietta 项目

## 项目地址
[GitHub 项目地址](https://github.com/alfiopuglisi/guietta)

## 主要特性
Guietta 是一个轻量级的 Python GUI 框架，专为简单快速构建图形用户界面而设计。它基于 Tkinter 库，强调简洁性和易用性。主要特性包括：
- **声明式语法**：使用 Python 字典和列表来定义 GUI 布局，无需复杂的类继承或事件处理代码。
- **自动布局**：支持网格（grid）和打包（pack）布局，自动处理组件对齐和间距。
- **内置组件支持**：提供按钮、标签、输入框、文本框、下拉菜单、复选框等常见 Tkinter 组件的简化封装。
- **事件处理简化**：通过函数绑定轻松处理用户交互，如点击按钮或输入变化。
- **跨平台兼容**：基于 Tkinter，支持 Windows、macOS 和 Linux。
- **轻量无依赖**：无需额外安装包，直接使用标准库，适合快速原型开发。
- **主题支持**：内置简单主题自定义选项。

## 主要功能
Guietta 的核心功能是快速创建交互式 GUI 应用，适用于小型工具、数据可视化界面或简单表单。主要功能包括：
- **界面构建**：通过 Python 代码定义窗口、面板和组件，实现拖拽式布局效果。
- **数据绑定**：支持变量绑定，实现实时更新，如输入框与标签的联动。
- **文件和对话框集成**：内置文件打开/保存对话框、消息框等标准功能。
- **多窗口支持**：轻松创建模态对话框或多标签页界面。
- **自定义扩展**：允许嵌入自定义 Tkinter 组件或第三方库，扩展功能。

## 用法
Guietta 的用法简单，只需导入库并使用其 API 构建界面。以下是基本步骤和示例：

### 安装
Guietta 无需安装，直接使用 Python 标准库（Tkinter）。如果需要，可通过 pip 安装（但通常无需）：
```
pip install guietta
```

### 基本用法
1. **导入库**：
   ```python
   from guietta import Gui, Button, Label, Entry
   ```

2. **定义布局**：使用 Gui 类和组件创建界面。
   ```python
   gui = Gui()
   gui.widthheight(300, 200)  # 设置窗口大小
   gui.title('简单计算器')     # 设置标题

   # 添加组件：位置 (row, col) = 组件
   gui[(0, 0)] = Label('输入数字:')
   gui[(0, 1)] = Entry()  # 输入框
   gui[(1, 0)] = Button('计算', call=calculate)  # 按钮绑定函数
   gui[(1, 1)] = Label('结果:')  # 输出标签
   gui[(2, 1)] = Label('')      # 结果显示

   def calculate():
       num = gui[1]  # 获取输入框值
       result = num * 2  # 示例计算
       gui[3] = str(result)  # 更新标签

   gui.run()  # 启动 GUI
   ```

3. **运行**：执行脚本后，GUI 窗口将弹出。组件位置使用元组 (row, col) 指定，支持高级布局选项如 `gui.add_line()` 添加分隔线。

### 高级用法
- **事件绑定**：使用 `call` 参数绑定函数，或 `on_change` 处理输入变化。
- **布局管理**：通过 `gui.line_layout()` 或 `gui.grid_layout()` 自定义网格。
- **示例应用**：适合构建文件浏览器、简单游戏界面或数据编辑器。参考 GitHub 仓库中的 `examples/` 目录获取更多样例。

更多细节请查看项目 README 和源代码。