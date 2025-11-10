---
title: pyautogui
---

# PyAutoGUI 项目

## 项目地址
[https://github.com/asweigart/pyautogui](https://github.com/asweigart/pyautogui)

## 主要特性
PyAutoGUI 是一个跨平台的 Python 库，用于自动化 GUI（图形用户界面）交互。它支持 Windows、macOS 和 Linux 系统，主要通过模拟鼠标和键盘操作来控制计算机。主要特性包括：
- **鼠标控制**：移动鼠标、点击、拖拽等，支持像素级精确控制。
- **键盘控制**：模拟按键、组合键（如 Ctrl+C）和输入文本。
- **屏幕截图与图像识别**：捕获屏幕截图，查找屏幕上的图像位置，支持容错匹配。
- **跨平台兼容**：无需额外依赖，即可在多操作系统上运行。
- **简单易用**：API 设计直观，适合初学者和自动化脚本开发者。
- **安全机制**：内置 PAUSE 和 FAILSAFE 功能，防止无限循环（如将鼠标移到屏幕左上角停止脚本）。

## 主要功能
- **鼠标操作**：`pyautogui.moveTo(x, y)` 移动到指定坐标；`pyautogui.click()` 执行点击；`pyautogui.dragTo(x, y)` 拖拽。
- **键盘操作**：`pyautogui.typewrite('text')` 输入文本；`pyautogui.press('enter')` 按下键；`pyautogui.hotkey('ctrl', 'c')` 组合键。
- **图像定位**：`pyautogui.locateOnScreen('image.png')` 在屏幕上查找图像，返回位置；支持置信度参数以处理轻微变化。
- **屏幕信息**：`pyautogui.size()` 获取屏幕分辨率；`pyautogui.screenshot()` 截取屏幕。
- **位置计算**：`pyautogui.center(image_location)` 获取图像中心点。

## 用法
1. **安装**：使用 pip 安装 `pip install pyautogui`。
2. **基本示例**：
   ```python
   import pyautogui
   import time

   # 移动鼠标并点击
   pyautogui.moveTo(100, 150)
   pyautogui.click()

   # 输入文本
   pyautogui.typewrite('Hello, World!', interval=0.1)

   # 查找并点击图像
   location = pyautogui.locateOnScreen('button.png')
   if location:
       pyautogui.click(pyautogui.center(location))
   ```
3. **注意事项**：
   - 导入前确保系统允许自动化（如禁用安全软件）。
   - 使用 `pyautogui.PAUSE = 1` 添加操作间延迟。
   - 对于图像识别，图像文件需与屏幕内容匹配，建议使用小尺寸 PNG 文件。
   - 适用于自动化测试、游戏脚本或日常任务，但需遵守使用规范，避免滥用。