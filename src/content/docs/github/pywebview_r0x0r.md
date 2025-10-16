
---
title: pywebview
---

# pywebview 项目

**GitHub 项目地址:** [https://github.com/r0x0r/pywebview](https://github.com/r0x0r/pywebview)

## 主要特性
pywebview 是一个轻量级的跨平台 Python 库，用于创建基于 Web 技术的桌面 GUI 应用程序。它利用系统的原生 Web 视图（如 Windows 的 WebView2、macOS 的 WebKit 和 Linux 的 WebKitGTK）来渲染 HTML/CSS/JavaScript 界面，而无需安装额外的浏览器引擎。主要特性包括：
- **跨平台支持**：兼容 Windows、macOS 和 Linux，无需修改代码即可运行。
- **轻量级**：体积小巧，不依赖 Electron 等大型框架，避免了不必要的开销。
- **原生集成**：使用系统内置的 Web 视图，提供原生外观和性能。
- **JavaScript-Python 桥接**：允许 Web 界面通过 JavaScript 直接调用 Python 函数，实现前后端交互。
- **窗口管理**：支持创建窗口、对话框、全屏模式和多窗口应用。
- **安全性**：隔离 Web 内容与系统资源，减少潜在风险。
- **易于打包**：可与 PyInstaller 等工具结合，生成独立的可执行文件。

## 主要功能
- **Web 视图渲染**：加载本地 HTML 文件或远程 URL，并在原生窗口中显示。
- **API 暴露**：通过 `api` 对象将 Python 函数暴露给 JavaScript，支持同步/异步调用。
- **事件处理**：监听窗口事件如关闭、调整大小、鼠标/键盘输入。
- **文件和资源访问**：允许 Web 应用访问本地文件系统、剪贴板和系统通知。
- **自定义主题**：支持暗黑模式和自定义窗口样式。
- **HTTP 服务器集成**：内置简单 HTTP 服务器，用于开发和测试。
- **扩展支持**：可集成其他库如 Flask 或 Django 来处理后端逻辑。

## 用法
### 安装
使用 pip 安装：
```
pip install pywebview
```
根据平台，可能需要额外依赖（如 Linux 上安装 webkit2gtk）。

### 基本示例
创建一个简单的窗口加载 HTML 文件：

```python
import webview

# 创建 Python API
class Api:
    def say_hello(self, name):
        return f"Hello, {name}!"

# 暴露 API 并启动窗口
api = Api()
webview.create_window('PyWebView 示例', 'index.html', js_api=api, width=800, height=600)
webview.start()
```

对应的 `index.html`：
```html
<!DOCTYPE html>
<html>
<head><title>示例</title></head>
<body>
    <button onclick="pywebview.api.say_hello('World').then(alert)">点击问候</button>
</body>
</html>
```

### 高级用法
- **多窗口**：使用 `webview.windows` 管理多个窗口。
- **异步支持**：Python 函数可返回 Promise 以处理异步操作。
- **调试**：启用开发者工具（`devtools=True`）进行调试。
- **打包应用**：结合 PyInstaller 生成 exe 或 app 文件。

更多细节请参考项目文档和示例代码。