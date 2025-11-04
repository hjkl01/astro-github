
---
title: egui
---


# egui

**GitHub 项目地址**  
<https://github.com/emilk/egui>

---

## 简介

egui（`egui`：Easy GUI）是一个用 Rust 编写的即时模式 GUI（Immediate Mode GUI）框架。它专注于提供高性能、易用、可组合的 UI 组件，适合游戏、工具、图形编辑器等实时渲染场景。

---

## 主要特性

- **即时模式（Immediate Mode）**：每帧重绘 UI，逻辑与状态分离，代码结构直观。
- **无额外依赖**：仅依赖 `winit`, `pixels`, `egui_wgpu_backend` 等，易于集成。
- **高性能**：使用 GPU 加速，更新和渲染极低延迟。
- **可组合与可扩展**：内置多种组件（按钮、滑条、下拉框、树形视图、聊天框等），支持自定义组件与插件。
- **跨平台**：支持 Windows、macOS、Linux、WebAssembly 和多种后端（OpenGL, Vulkan, WebGL, wgpu, etc.）。
- **主题和样式**：内置主题（Light, Dark, etc.），支持自定义 `Style`。
- **输入系统**：完整的键盘、鼠标、触控事件处理。
- **无痛的布局**：`Layout`, `Align`, `Column`, `Row`, `Grid` 等布局方式。
- **拖拽 & 重排**：支持窗口拖拽、树形节点拖拽。
- **可组合**：通过 `egui::Containers`、`Debug`, `Plot`, `Visuals` 等，快速构建复杂 UI。
- **自带工具**：例如 `egui_demo_lib` 示例演示了大量官方组件与用法。

---

## 核心概念

| 术语 | 说明 |
|------|------|
| `egui::Ctx` | UI 上下文，维护状态与布局。 |
| `egui::Ui` | 代表一个可绘制区域，所有 UI 调用中都通过它完成。 |
| `Response` | 交互结果（如点击、改变），常用于判断交互。 |
| `Style` | 全局与局部 UI 风格配置。 |
| `Frame` | 自定义窗口、弹窗等容器。 |

---

## 快速开始

```rust
use eframe::{egui, epi};

struct MyApp;

impl Default for MyApp {
    fn default() -> Self { Self }
}

impl epi::App for MyApp {
    fn name(&self) -> &str { "egui 示例" }

    fn update(&mut self, ctx: &egui::Context, _frame: &mut epi::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Hello, egui!");
            if ui.button("点击").clicked() {
                println!("按钮被点击");
            }
        });
    }
}

fn main() {
    let app = MyApp::default();
    let options = eframe::NativeOptions::default();
    eframe::run_native(Box::new(app), options);
}
```

- **创建应用**：实现 `epi::App` 或 `eframe::App`，在 `update` 中构造 UI。
- **运行**：使用 `eframe::run_native`（桌面）或 `eframe::run_native_web`（WebAssembly）。

---

## 用法与插件

- **`egui-winit-vulkano`**：结合 `winit`，`vulkano` 后端实现高度自定义渲染。
- **`egui-winit-pixels`**：基于 `pixels` 的窗口渲染方案，适合快速原型。
- **`egui_plot`**：绘制实时图表与统计信息。
- **`egui_demo_lib`**：示例项目，覆盖基本组件、主题、插件。使用 `cargo run --example demo`.

---

## 文档与资源

- 官方文档：<https://emilk.github.io/egui/>  
- 代码仓库：<https://github.com/emilk/egui>  
- 示例项目：<https://github.com/emilk/egui/tree/master/examples>  
- 社区讨论：Discord、Rust 用户论坛

---

## 结语

egui 通过即时模式简化 UI 开发，保持高性能且易于集成。无论是游戏 UI、图形工具，还是调试面板，都能在 **Rust** 生态中快速实现。