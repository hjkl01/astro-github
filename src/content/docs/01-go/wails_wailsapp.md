---
title: wailsapp/wails
---

# Wails

Wails 是一个用于使用 Go 和 Web 技术构建桌面应用程序的框架。它允许开发者将 Go 代码和 Web 前端打包成单个二进制文件，提供了一种不同于传统内置 Web 服务器的方法。

## 功能特性

- **后端使用标准 Go**：利用 Go 的强大性能和并发能力。
- **前端灵活性**：支持任何熟悉的前端技术（如 React、Vue、Angular、Svelte 等）构建 UI。
- **快速开发**：提供预建模板，快速创建丰富的用户界面。
- **Go-JS 互操作**：轻松从 JavaScript 调用 Go 方法，并自动生成 TypeScript 定义。
- **原生功能**：支持原生对话框、菜单、暗/亮模式切换，以及现代半透明和“frosted window”效果。
- **事件系统**：统一的 Go 和 JavaScript 事件系统。
- **CLI 工具**：强大的命令行工具，用于项目生成、编译和打包。
- **多平台支持**：支持 Windows、macOS 和 Linux。
- **原生渲染**：使用原生渲染引擎，无需嵌入浏览器。

## 使用方法

1. **安装 Wails**：访问 [官方文档](https://wails.io/docs/gettingstarted/installation) 获取安装指南。

2. **创建新项目**：

   ```bash
   wails init -n myproject
   cd myproject
   ```

3. **运行项目**：

   ```bash
   wails dev
   ```

4. **构建生产版本**：
   ```bash
   wails build
   ```

更多详细信息请参考 [Wails 官方文档](https://wails.io/docs/gettingstarted/installation)。
