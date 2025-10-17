
---
title: enaml
---

# Enaml 项目

## 项目地址
[https://github.com/nucleic/enaml](https://github.com/nucleic/enaml)

## 主要特性
Enaml 是一个基于 Python 的声明式用户界面（UI）语言和库，灵感来源于 Enthought 的 TraitsUI 和 QML。它允许开发者使用 Python 语法定义 UI 组件，实现声明式编程范式。主要特性包括：
- **声明式语法**：使用 Python-like 的语法描述 UI 结构和行为，而非命令式代码，提高代码可读性和维护性。
- **Python 集成**：Enaml 代码完全嵌入 Python，支持 Traits 模型系统，用于数据绑定和事件处理。
- **跨平台支持**：基于 Qt 后端，支持 Windows、macOS 和 Linux 等平台。
- **组件化设计**：提供丰富的内置组件，如按钮、布局、容器等，并支持自定义组件。
- **响应式绑定**：支持数据模型与 UI 的双向绑定，实现实时更新。
- **模板和继承**：支持 UI 模板复用和继承机制，便于构建复杂界面。

## 主要功能
Enaml 的核心功能聚焦于构建动态、交互式的 GUI 应用：
- **UI 布局管理**：支持各种布局容器（如水平、垂直、网格布局），自动处理组件定位和响应式调整。
- **事件处理**：通过 Traits 事件系统处理用户交互，如点击、拖拽等。
- **数据驱动 UI**：与 Python 对象模型无缝集成，实现视图-模型分离（MVC 模式）。
- **样式和主题**：支持 CSS-like 样式定义，允许自定义外观。
- **扩展性**：可与 NumPy、Pandas 等科学计算库结合，用于数据可视化应用。
- **编译与运行**：Enaml 文件编译为 Python 代码，支持热重载开发。

## 用法
### 安装
使用 pip 安装 Enaml 及其依赖：
```
pip install enaml
pip install PyQt5  # 或其他 Qt 后端
```

### 基本用法示例
1. **创建 Enaml 文件**（例如 `my_app.enaml`）：
   ```
   from enaml.core.api import Looper
   from enaml.widgets.api import Window, Button, HBox, Label

   enamldef MyWindow(Window):
       title = "Enaml 示例"
       HBox:
           Label:
               text = "Hello, Enaml!"
           Button:
               text = "点击我"
               clicked :: print("按钮被点击！")
   ```

2. **在 Python 脚本中加载和运行**（例如 `run_app.py`）：
   ```python
   from enaml.core.api import parse_and_set_source
   from enaml.qt.qt_application import QtApplication

   if __name__ == "__main__":
       app = QtApplication()
       with open("my_app.enaml") as f:
           window = parse_and_set_source(f.read())
       window.show()
       app.start()
   ```

3. **运行应用**：
   ```
   python run_app.py
   ```
   这将启动一个简单的窗口应用，支持交互。

### 高级用法
- **数据绑定**：使用 `@observe` 装饰器在 Traits 中定义属性变化监听，实现 UI 自动更新。
- **自定义组件**：继承 `d_Proxy...` 类创建新组件，并注册到 Enaml 环境中。
- **集成 Traits**：结合 `traits.api` 构建模型，例如：
  ```python
  from traits.api import HasTraits, Str, observe

  class MyModel(HasTraits):
      name = Str("默认值")

      @observe('name')
      def update_ui(self, event):
          # 更新 UI 逻辑
          pass
  ```
更多细节请参考项目文档和示例代码。