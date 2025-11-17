---
title: gpui-component
---

## 功能介绍

gpui-component 是一个基于 [GPUI](https://gpui.rs) 的 Rust GUI 组件库，用于构建优秀的跨平台桌面应用程序。它提供了丰富的 UI 组件和功能，帮助开发者快速创建现代化的桌面应用。

### 主要特性

- **丰富组件**：提供 60+ 个跨平台桌面 UI 组件，包括按钮、输入框、表格、列表、图表等。
- **原生设计**：受 macOS 和 Windows 控件启发，结合 shadcn/ui 设计理念，提供现代化的用户体验。
- **易于使用**：采用无状态的 `RenderOnce` 组件设计，简单直观。
- **高度可定制**：内置主题系统和主题颜色，支持多主题配置和基于变量的定制。
- **多尺寸支持**：支持 `xs`、`sm`、`md`、`lg` 等多种尺寸。
- **灵活布局**：支持 Dock 布局用于面板排列、调整大小，以及自由形式的 Tiles 布局。
- **高性能**：虚拟化 Table 和 List 组件，支持大数据集的流畅渲染。
- **内容渲染**：原生支持 Markdown 和简单 HTML 渲染。
- **图表功能**：内置图表组件，用于数据可视化。
- **代码编辑器**：高性能代码编辑器，支持高达 20 万行的代码，支持 LSP（诊断、补全、悬停等）。
- **语法高亮**：使用 Tree Sitter 提供语法高亮，支持编辑器和 Markdown 组件。

### 展示应用

该库已被用于构建如 [Longbridge Pro](https://longbridge.com/desktop) 等实际应用程序，展示了其在生产环境中的实用性。

## 使用方法

GPUI 和 gpui-component 仍在开发中，因此需要通过 Git 添加依赖。

### 添加依赖

在 `Cargo.toml` 中添加：

```toml
gpui = "0.2.2"
gpui-component = "0.4.0-preview2"
```

### 基本示例

以下是一个简单的 Hello World 示例：

```rust
use gpui::*;
use gpui_component::{button::*, *};

pub struct HelloWorld;

impl Render for HelloWorld {
    fn render(&mut self, _: &mut Window, _: &mut Context<Self>) -> impl IntoElement {
        div()
            .v_flex()
            .gap_2()
            .size_full()
            .items_center()
            .justify_center()
            .child("Hello, World!")
            .child(
                Button::new("ok")
                    .primary()
                    .label("Let's Go!")
                    .on_click(|_, _, _| println!("Clicked!")),
            )
    }
}

fn main() {
    let app = Application::new();

    app.run(move |cx| {
        // 使用任何 GPUI Component 功能前必须调用此函数
        gpui_component::init(cx);

        cx.spawn(async move |cx| {
            cx.open_window(WindowOptions::default(), |window, cx| {
                let view = cx.new(|_| HelloWorld);
                // 窗口的第一级应该是 Root
                cx.new(|cx| Root::new(view, window, cx))
            })?;

            Ok::<_, anyhow::Error>(())
        })
        .detach();
    });
}
```

### WebView 支持

gpui-component 提供基于 [Wry](https://github.com/tauri-apps/wry) 的 WebView 组件（实验性功能）。启用方式：

```toml
gpui-component = { version = "0.4.0-preview2", features = ["webview"] }
wry = { version = "0.53.3", package = "lb-wry" }
```

### 图标使用

gpui-component 包含 `Icon` 元素，但默认不包含 SVG 文件。示例使用 [Lucide](https://lucide.dev) 图标，你可以根据 [IconName](https://github.com/longbridge/gpui-component/blob/main/crates/ui/src/icon.rs#L86) 定义添加所需的图标。

## 开发

运行示例应用：

```bash
cargo run
```

更多示例可在 `examples` 目录中找到，使用 `cargo run --example <example_name>` 运行。

## 许可证

Apache-2.0

- UI 设计基于 [shadcn/ui](https://ui.shadcn.com)
- 图标来自 [Lucide](https://lucide.dev)
