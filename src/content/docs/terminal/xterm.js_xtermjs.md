
---
title: xterm.js
---

# xterm.js 项目

## 项目地址
[https://github.com/xtermjs/xterm.js](https://github.com/xtermjs/xterm.js)

## 主要特性
xterm.js 是一个用于浏览器和 Node.js 环境的终端仿真器库，主要用于构建前端终端界面。它基于 HTML5 Canvas 实现，支持高性能渲染和现代 Web 标准。核心特性包括：
- **高性能渲染**：使用 Canvas 2D 上下文绘制终端，支持快速更新和滚动。
- **模块化设计**：可扩展的架构，支持插件系统，如图像支持、序列化等。
- **跨平台兼容**：在现代浏览器（如 Chrome、Firefox）和 Node.js 中运行良好。
- **无依赖**：纯 JavaScript 实现，不依赖外部框架。
- **可访问性**：支持屏幕阅读器和键盘导航，提高无障碍性。
- **主题和样式自定义**：内置多种主题，支持 CSS 自定义颜色和字体。

## 主要功能
- **终端仿真**：模拟 ANSI 转义序列，支持颜色、粗体、斜体、下划线等文本样式。
- **输入输出处理**：处理键盘输入、鼠标事件，并提供 API 读取/写入数据。
- **搜索和选择**：内置文本搜索、复制粘贴功能，支持多行选择。
- **滚动和缓冲区**：管理终端缓冲区，支持无限滚动和历史记录。
- **插件扩展**：集成 addon 如 FitAddon（自动调整大小）、WebLinksAddon（链接检测）、ImageAddon（图像显示）。
- **序列化支持**：可保存和恢复终端状态，用于持久化会话。

## 用法
### 安装
通过 npm 安装：
```
npm install xterm
npm install xterm-addon-fit  # 示例：安装 FitAddon
```

### 基本用法
1. **导入和初始化**：
   ```javascript
   import { Terminal } from 'xterm';
   import { FitAddon } from 'xterm-addon-fit';
   import 'xterm/css/xterm.css';

   const term = new Terminal({
     cursorBlink: true,
     theme: { background: '#1e1e1e' }
   });

   const fitAddon = new FitAddon();
   term.loadAddon(fitAddon);
   term.open(document.getElementById('terminal'));
   fitAddon.fit();
   ```

2. **写入数据**：
   ```javascript
   term.write('Hello, World!\r\n');
   ```

3. **读取输入**：
   ```javascript
   term.onData(data => {
     // 处理输入数据
     process.stdin.write(data);
   });
   ```

4. **连接后端**（如 WebSocket）：
   ```javascript
   const socket = new WebSocket('ws://localhost:8080');
   socket.onopen = () => term.attachToProcess(socket);
   ```

更多细节请参考官方文档：https://xtermjs.org/docs/。