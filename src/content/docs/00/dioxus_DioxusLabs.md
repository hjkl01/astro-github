
---
title: dioxus
---


# Dioxus

> GitHub 项目地址: <https://github.com/DioxusLabs/dioxus>

## 主要特性

- **跨平台 UI**：支持 Web（WebAssembly）、桌面（Tauri, tauri‑runtime）与移动（React Native）等多平台渲染。
- **声明式 + 虚拟 DOM**：以类似 React 的 JSX/TSX 语法编写 UI，使用虚拟 DOM 进行高效 diff 和更新。
- **高性能**：使用 Rust 编写核心，具备低内存占用、零拷贝、即时编译的优势。
- **多路由**：集成多路由方案，支持动态路由、懒加载等。
- **状态管理**：自带“信号”（`Signal`）和“存储”（`Store`）两种状态管理模式，方便组件共享状态。
- **插件生态**：通过插件系统（比如 `dioxus-router`、`dioxus-tailwind`）扩展功能。

## 核心功能

| 功能 | 描述 |
|------|------|
| **组件化** | `Component` 接口、`#[component]` 宏，支持模板语法 `html!{}` 或 `rsx!{}` |
| **JSX/TSX 语法** | 轻松使用 JSX/TSX，例如 `fn App() -> Element { rsx! { <div>Hello Dioxus</div> } }` |
| **状态/事件** | `use_signal`, `use_state`, `use_effect`, `on_click!` 等 Hook |
| **路由** | `Router`, `Route`, `Link` 等 API |
| **性能检查** | `devtools` 包，支持 Rust 的 `Conduit Profiler` |
| **移动 + 桌面** | 通过 `dioxus-mobile`、`dioxus-desktop` 运行时构建 apk/ipa 或二进制可执行文件 |
| **集成 Tailwind** | `#[cfg(feature = "tailwind")]` 自动生成 CSS，支持 `dioxus-scss`**

## 快速开始

1. **创建项目**  
   ```bash
   cargo new dioxus_app
   cd dioxus_app
   cargo add dioxus
   ```

2. **编写 `main.rs`**  
   ```rust
   use dioxus::prelude::*;

   fn main() {
       launch(app);
   }

   fn app(cx: Scope) -> Element {
       rsx! {
           <h1>{ "Hello, Dioxus!" }</h1>
           <button
               on_click={|_| println!("clicked")}>
               { "Click me" }
           </button>
       }
   }
   ```

3. **运行 (Web)**  
   ```bash
   cargo web start
   ```

4. **运行 (桌面)**  
   ```bash
   cargo tauri dev
   ```

## 文档与社区

- 官方文档: <https://dioxuslabs.com/docs/0.5/current/>
- Discord 社区: <https://discord.gg/dioxus>
- 示例仓库: <https://github.com/DioxusLabs/examples>

--- 

> 项目地址: <https://github.com/DioxusLabs/dioxus>
