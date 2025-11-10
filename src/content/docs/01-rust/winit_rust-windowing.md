---
title: winit
---

**Repository**  
> https://github.com/rust-windowing/winit

# winit – Rust 窗口创建与事件处理库

## 主要特性

- **跨平台支持**：Windows、macOS、Linux (X11, Wayland, XCB 等)。
- **无外部依赖**：纯 Rust 编写，只有必要的 C 绑定。
- **事件循环**：异步事件驱动，支持键盘、鼠标、触摸、窗口状态变化等。
- **窗口创建与管理**：`WindowBuilder` 提供丰富的窗口属性设置（大小、标题、样式、全屏、透明等）。
- **多显示器管理**：访问所有监视器信息，获取 DPI、尺寸、位置。
- **软/硬件支持**：支持硬件缩放、系统主题、全屏模式、窗口聚焦等。
- **原生功能**：剪贴板、光标、设备像素比、锁定壁垒、时间同步等。
- **事件处理**：键盘/鼠标事件、触摸手势、滚轮、双击等细粒度事件。

## 核心功能

| 功能 | 主要 API |
|------|----------|
| **创建事件循环** | `EventLoop<T>` |
| **创建窗口** | `WindowBuilder` → `Window` |
| **监听系统事件** | `Event<T>`、`WindowEvent`、`DeviceEvent` |
| **温柔关闭** | `ControlFlow`（`wait`, `wait_timeout`, `exit`） |
| **多显示器查询** | `MonitorHandle`, `video_mode` |
| **剪贴板操作** | `ClipboardManager` |
| **光标控制** | `CursorIcon`, `hide`, `show`, `set_position` |
| **高 DPI 与缩放** | `scale_factor`, `logical_size`, `physical_size` |

## 上手用法

### 1️⃣ Cargo.toml

```toml
[dependencies]
winit = "0.29"   # 依赖最新版
```

### 2️⃣ 创建窗口与事件循环

```rust
use winit::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
    window::WindowBuilder,
};

fn main() {
    // 创建事件循环
    let event_loop = EventLoop::new();

    // 创建窗口
    let window = WindowBuilder::new()
        .with_title("winit 示例窗口")
        .with_inner_size(winit::dpi::LogicalSize::new(800.0, 600.0))
        .build(&event_loop)
        .expect("无法创建窗口");

    // 进入事件循环
    event_loop.run(move |event, _, control_flow| {
        *control_flow = ControlFlow::Wait;

        match event {
            Event::WindowEvent { event, .. } => match event {
                // 处理键盘事件
                WindowEvent::KeyboardInput { input, .. } => {
                    if input.virtual_keycode == Some(winit::event::VirtualKeyCode::Escape) {
                        *control_flow = ControlFlow::Exit;
                    }
                }
                // 检测窗口关闭
                WindowEvent::CloseRequested => *control_flow = ControlFlow::Exit,
                _ => {}
            },
            _ => {}
        }
 });
}
```

### 3️⃣ 高 DPI 与多显示器

```rust
for monitor in event_loop.available_monitors() {
    println!("<<{0}>>:{}", monitor.name().unwrap_or_default());
    println!("  Physical size: {}x{}", monitor.size().width, monitor.size().height);
    println!("  Logical size: {:?} at scale factor {}", monitor.size(), monitor.scale_factor());
}
```

## 参考

- 官方文档: https://docs.rs/winit/latest/winit/
- 示例代码仓库: https://github.com/rust-windowing/winit/tree/main/examples

--- 

> 任何进一步的问题请参考官方仓库与文档。