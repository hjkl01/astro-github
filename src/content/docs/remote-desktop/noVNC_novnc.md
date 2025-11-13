---
title: noVNC
---

# noVNC 项目

## 项目地址
[https://github.com/novnc/noVNC](https://github.com/novnc/noVNC)

## 主要特性
noVNC 是一个开源的 HTML5 VNC 客户端，使用 WebSocket 协议实现浏览器端远程桌面访问。主要特性包括：
- **浏览器原生支持**：无需安装插件，直接在现代浏览器（如 Chrome、Firefox）中运行，支持桌面和移动设备。
- **WebSocket 集成**：通过 WebSocket 连接 VNC 服务器，提供低延迟的远程控制体验。
- **跨平台兼容**：支持多种 VNC 协议变体（如 TightVNC、RealVNC），并兼容 WebRTC 用于更高效的传输。
- **安全性**：支持加密连接（wss://），可与代理服务器如 websockify 结合使用。
- **自定义界面**：基于 JavaScript 和 Canvas，提供可自定义的 UI，包括键盘映射、剪贴板共享和分辨率调整。
- **轻量级**：纯前端实现，无需服务器端依赖，便于嵌入 Web 应用。

## 主要功能
- **远程桌面访问**：允许用户通过浏览器连接到远程 VNC 服务器，实时查看和控制远程桌面。
- **输入处理**：支持键盘、鼠标和触摸输入的映射，确保跨设备兼容性。
- **视图控制**：提供缩放、平移、全屏模式和自动调整窗口大小的功能。
- **文件传输**：基本支持剪贴板复制粘贴，实现文本和简单文件共享。
- **错误处理**：内置连接诊断、断线重连和日志记录，便于调试。
- **扩展性**：可作为库集成到其他 Web 项目中，支持自定义主题和插件。

## 用法
1. **安装和部署**：
   - 克隆仓库：`git clone https://github.com/novnc/noVNC.git`
   - 安装依赖（可选，使用 npm）：`npm install`
   - 构建：运行 `make release` 生成发布版本。

2. **运行示例**：
   - 使用内置的 websockify 代理：启动 VNC 服务器（如 `vncserver :1`），然后运行 `utils/novnc_proxy --vnc localhost:5901 --listen 6080`。
   - 在浏览器中访问 `http://localhost:6080/vnc.html`，输入 VNC 服务器地址（ws://localhost:6080）和密码连接。

3. **集成到项目**：
   - 包含 `core/` 和 `app/` 目录的文件到你的 Web 服务器。
   - 在 HTML 中加载 `vnc.html` 或使用 RFB.js 库直接嵌入：`<script src="core/rfb.js"></script>`，然后初始化 `var rfb = new RFB(document.getElementById('screen'), 'ws://your-vnc-server:port');`。
   - 配置参数：支持 URL 参数如 `?host=example.com&port=5900&password=pass`。

更多细节请参考仓库的 README 和文档。