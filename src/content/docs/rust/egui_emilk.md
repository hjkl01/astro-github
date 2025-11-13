---
title: egui
---

# egui

## 项目简介

egui 是一个简单、快速且高度可移植的即时模式 GUI 库，用 Rust 编写。它专为易用性和性能而设计，支持桌面、Web 和移动平台。

## 主要功能

- **即时模式**：无需管理状态，UI 在每一帧中重新构建
- **易移植**：支持 Windows、macOS、Linux、Web（通过 WebAssembly）和移动设备
- **高性能**：低 CPU 和内存使用，适合游戏和实时应用
- **丰富小部件**：按钮、滑块、文本输入、图像、布局等
- **自定义样式**：可自定义主题、字体和外观
- **集成简单**：易于集成到现有 Rust 项目中

## 用法

### 安装

在 `Cargo.toml` 中添加：

```toml
[dependencies]
egui = "0.24"
```

对于 Web 支持，添加 `eframe`：

```toml
eframe = "0.24"
```

### 基本示例

```rust
use eframe::egui;

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "My egui App",
        options,
        Box::new(|_cc| Box::new(MyApp::default())),
    )
}

#[derive(Default)]
struct MyApp {
    name: String,
    age: u32,
}

impl eframe::App for MyApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Hello World!");
            ui.horizontal(|ui| {
                ui.label("Your name: ");
                ui.text_edit_singleline(&mut self.name);
            });
            ui.add(egui::Slider::new(&mut self.age, 0..=120).text("age"));
            if ui.button("Click each year").clicked() {
                self.age += 1;
            }
            ui.label(format!("Hello '{}', age {}", self.name, self.age));
        });
    }
}
```

### 运行

```bash
cargo run
```

## 文档与资源

- 官方文档：<https://emilk.github.io/egui/>
- 代码仓库：<https://github.com/emilk/egui>
- 示例项目：<https://github.com/emilk/egui/tree/master/examples>
- 社区讨论：Discord、Rust 用户论坛

## 结语

egui 通过即时模式简化 UI 开发，保持高性能且易于集成。无论是游戏 UI、图形工具，还是调试面板，都能在 **Rust** 生态中快速实现。
