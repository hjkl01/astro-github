
---
title: DearPyGui
---

# DearPyGui 项目

**GitHub 项目地址:** [https://github.com/hoffstadt/DearPyGui](https://github.com/hoffstadt/DearPyGui)

## 主要特性
DearPyGui 是一个基于 Dear ImGui 的 Python 图形用户界面 (GUI) 库，设计用于快速构建高性能、可交互的应用程序。它具有以下核心特性：
- **高性能渲染**：利用 GPU 加速和即时模式渲染，支持实时 UI 更新，适合数据可视化、游戏开发和科学计算等场景。
- **跨平台支持**：兼容 Windows、macOS 和 Linux 系统，无需额外依赖即可运行。
- **轻量级设计**：体积小巧，安装简单，仅需 Python 环境，支持 Python 3.6+。
- **内置控件丰富**：提供按钮、滑块、文本框、绘图窗口、表格、菜单等多样化 UI 组件。
- **多线程友好**：支持异步回调和多线程操作，便于集成复杂逻辑。
- **主题与样式自定义**：允许用户自定义颜色、字体和布局，支持暗黑模式等主题。
- **扩展性强**：集成 NumPy、Matplotlib 等科学库，便于数据处理和可视化。

## 主要功能
- **GUI 构建**：通过 Python 脚本快速创建窗口、对话框和布局，支持嵌套容器和动态调整。
- **绘图与可视化**：内置绘图 API，支持 2D/3D 图表、热力图、散点图等，适用于实时数据展示。
- **输入输出处理**：处理鼠标、键盘事件，以及文件拖拽、剪贴板操作。
- **动画与特效**：支持简单动画、渐变和粒子效果，提升用户体验。
- **插件系统**：可扩展自定义控件和后端集成，如 OpenGL 或 Vulkan 渲染。
- **调试工具**：内置性能监控和日志系统，便于开发调试。

## 用法
1. **安装**：使用 pip 安装库：
   ```
   pip install dearpygui
   ```

2. **基本用法**：
   - 导入库：`import dearpygui.dearpygui as dpg`
   - 创建上下文：`dpg.create_context()`
   - 设置主窗口：`with dpg.window(label="主窗口"):`
   - 添加控件，例如按钮：`dpg.add_button(label="点击我", callback=回调函数)`
   - 渲染循环：`dpg.create_viewport(title='应用标题', width=800, height=600)`、`dpg.setup_dearpygui()`、`dpg.show_viewport()`、`dpg.start_dearpygui()`、`dpg.destroy_context()`

3. **示例代码**（简单窗口）：
   ```python
   import dearpygui.dearpygui as dpg

   def button_callback():
       print("按钮被点击！")

   dpg.create_context()
   dpg.create_viewport(title='DearPyGui 示例', width=600, height=400)

   with dpg.window(label="示例窗口"):
       dpg.add_text("Hello, DearPyGui!")
       dpg.add_button(label="点击", callback=button_callback)
       dpg.add_slider_float(label="滑块", default_value=0.5, min_value=0, max_value=1)

   dpg.setup_dearpygui()
   dpg.show_viewport()
   dpg.start_dearpygui()
   dpg.destroy_context()
   ```

4. **高级用法**：
   - 使用 `dpg.add_plot()` 创建图表：传入数据数组进行绘图。
   - 主题应用：`with dpg.theme() as theme: dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 0, 0, 255))`，然后 `dpg.bind_theme(theme)`。
   - 文档参考：项目 README 和示例文件夹提供详细教程，建议从基础示例开始学习。

该项目适合 Python 开发者快速原型开发，社区活跃，更新频繁。