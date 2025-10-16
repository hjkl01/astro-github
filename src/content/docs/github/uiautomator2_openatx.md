
---
title: uiautomator2
---

# uiautomator2 项目参考

## 项目地址
[https://github.com/openatx/uiautomator2](https://github.com/openatx/uiautomator2/blob/master/QUICK_REFERENCE.md)

## 主要特性
uiautomator2 是一个 Python 库，用于 Android 设备的 UI 自动化测试。它基于 Android 的 uiautomator 框架，提供简洁的 API 来模拟用户交互、检查 UI 元素和执行自动化任务。主要特性包括：
- **跨设备支持**：兼容多种 Android 版本和设备，无需 root 权限。
- **元素定位**：使用 XPath、ID、类名等选择器快速定位 UI 元素。
- **交互模拟**：支持点击、滑动、输入文本、拖拽等用户操作。
- **截屏与日志**：内置截图捕获、设备日志获取和性能监控。
- **无侵入性**：通过 ADB (Android Debug Bridge) 连接设备，纯 Python 实现，便于集成到测试框架如 pytest 或 unittest。
- **扩展性**：支持图像识别（结合 OpenCV）和多设备并行测试。

## 主要功能
- **设备连接与管理**：通过 ADB 连接设备，启动/停止应用，获取设备信息（如分辨率、进程列表）。
- **UI 元素操作**：查找元素、执行动作（如 click、send_keys）、获取属性（如 text、bounds）。
- **手势与导航**：模拟 swipe、pinch、long_press 等复杂手势；处理页面等待和滚动。
- **测试辅助**：等待元素出现/消失、捕获异常、生成报告。
- **高级功能**：支持按键事件、通知栏交互、安装/卸载 APK，以及与 Appium 的兼容性。

## 用法
### 安装
```bash
pip install uiautomator2
```

### 基本用法示例
1. **连接设备**：
   ```python
   import uiautomator2 as u2
   d = u2.connect()  # 连接当前设备，或指定 IP 如 u2.connect('192.168.1.100')
   ```

2. **启动应用并点击元素**：
   ```python
   d.app_start("com.example.app")  # 启动应用
   d(resourceId="com.example:id/button").click()  # 点击 ID 为 button 的元素
   ```

3. **输入文本和滑动**：
   ```python
   d(resourceId="com.example:id/edit").set_text("Hello World")  # 输入文本
   d.swipe(0.5, 0.8, 0.5, 0.2)  # 从屏幕下方向上滑动
   ```

4. **等待元素并截屏**：
   ```python
   d(resourceId="com.example:id/target").wait(timeout=10.0)  # 等待元素出现，最多 10 秒
   d.screenshot("screenshot.png")  # 截取屏幕
   ```

5. **获取设备信息**：
   ```python
   print(d.info)  # 获取设备字典信息
   print(d.dump_hierarchy())  # 获取当前 UI 层次 XML
   ```

更多细节请参考项目文档。建议在实际使用前确保 ADB 已安装并设备处于调试模式。