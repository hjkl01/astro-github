
---
title: tauri
---

# Tauri 项目

**GitHub 项目地址:** [https://github.com/tauri-apps/tauri](https://github.com/tauri-apps/tauri)

## 主要特性

Tauri 是一个用于构建轻量级、快速且安全的跨平台桌面应用程序的框架。它使用 Web 技术（如 HTML、CSS 和 JavaScript）作为前端，同时利用 Rust 作为后端核心，具有以下主要特性：

- **轻量级和高效**：Tauri 应用程序的二进制文件通常小于 600KB，与 Electron 等框架相比，体积小得多，启动速度更快，内存占用低。
- **跨平台支持**：支持 Windows、macOS 和 Linux 等主流操作系统，无需为每个平台重新构建前端代码。
- **安全性优先**：基于 Rust 的内存安全特性，内置权限系统和隔离机制，防止常见的安全漏洞，如注入攻击。
- **WebView 渲染**：使用系统的 WebView（如 WebKit 或 Edge）渲染前端，避免捆绑完整的浏览器引擎，减少资源消耗。
- **原生集成**：轻松访问系统 API，如文件系统、通知、窗口管理和硬件访问（例如摄像头、麦克风）。
- **热重载开发**：支持前端热重载，便于开发和调试。
- **移动端扩展**：通过 Tauri Mobile 支持 iOS 和 Android 开发（实验性）。

## 主要功能

Tauri 的核心功能围绕构建现代桌面应用展开：

- **前端-后端桥接**：通过命令系统（Invoke）和事件系统（Emit）实现前端与 Rust 后端的通信，支持异步操作和类型安全。
- **窗口管理**：创建和管理多个窗口，支持透明窗口、边框自定义、最大化/最小化等原生功能。
- **插件系统**：内置插件如文件系统、HTTP 客户端、SQL 数据库等，可扩展第三方插件以添加功能（如通知、剪贴板访问）。
- **打包和分发**：自动生成安装程序，支持签名和自动更新。输出格式包括 .exe（Windows）、.dmg/.app（macOS）和 .deb/.AppImage（Linux）。
- **状态管理和持久化**：内置应用状态管理，支持 JSON 或数据库持久化。
- **CLI 工具**：Tauri CLI 提供项目初始化、开发服务器、构建和测试等命令。

## 用法

### 安装和初始化
1. **前提条件**：安装 Rust（通过 rustup.rs）、Node.js 和系统依赖（如 WebView 库）。
2. **安装 Tauri CLI**：
   ```
   cargo install tauri-cli
   ```
3. **创建新项目**：
   ```
   cargo tauri init
   ```
   这会生成一个包含 Rust 后端和前端模板的项目结构（例如，使用 Vue、React 或 Svelte）。

### 开发流程
1. **前端开发**：在 `src-tauri` 外的目录中编写前端代码，使用任意 Web 框架。
2. **后端开发**：在 `src-tauri/src/main.rs` 中定义 Rust 命令，例如：
   ```rust
   #[tauri::command]
   fn greet(name: &str) -> String {
       format!("Hello, {}!", name)
   }

   fn main() {
       tauri::Builder::default()
           .invoke_handler(tauri::generate_handler![greet])
           .run(tauri::generate_context!())
           .expect("error while running tauri application");
   }
   ```
3. **运行开发模式**：
   ```
   cargo tauri dev
   ```
   这会启动开发服务器，前端热重载，后端实时编译。

### 构建和发布
1. **构建应用**：
   ```
   cargo tauri build
   ```
   生成平台特定的二进制文件和安装包。
2. **配置**：在 `src-tauri/tauri.conf.json` 中自定义窗口大小、标题、图标、权限等。
3. **高级用法**：使用插件添加功能，例如集成 SQLite：
   - 添加依赖：`cargo add tauri-plugin-sql`
   - 在配置中启用插件。

更多细节请参考官方文档：https://tauri.app/