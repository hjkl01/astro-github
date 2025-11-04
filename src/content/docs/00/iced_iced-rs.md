
---
title: iced
---


# iced-rs/iced

**项目地址**: [https://github.com/iced-rs/iced](https://github.com/iced-rs/iced)

---

## 概述

**iced** 是一个用 Rust 编写的跨平台 GUI 构建框架，采用现代、响应式编程模型。其灵感来自 Flutter，强调组件化、单向数据流、快速热重载和高度可组合的 UI。

---

## 主要特性

- **跨平台**  
  在 Windows、macOS、Linux、Web（WebAssembly）和移动（iOS/Android）等平台一键运行。

- **声明式 UI**  
  采用声明式组件（`Element`, `Component` 等）定义界面，自动管理 UI 纹理。

- **单向数据流**  
  GUI 通过 [`Message`] 与 `Update` 的经典 Elm 架构实现，所有状态变化都由 `update` 函数完成。

- **热重载**  
  通过 `iced::Runtime` 监听文件变化，支持修改后即刻更新 UI，提升开发效率。

- **高度可组合**  
  支持 `Container`, `Row`, `Column`, `Button`, `TextInput` 等基础组件，可自由组合。

- **可扩展**  
  提供 `PlatformRuntime`、`PlatformSettings` 等接口，便于自定义渲染器、事件处理。

- **性能与安全**  
  使用 Rust 的内存安全与并发特性，界面响应迅速，避免运行时崩溃。

---

## 关键功能

| 功能 | 说明 |
|------|------|
| **布局** | `Column`, `Row`, `Stack`, `Grid` 等多种布局方式。 |
| **组件** | `Button`, `TextInput`, `Checkbox`, `Radio`, `Slider`, `Switch` 等。 |
| **主题与样式** | `Theme`, `StyleSheet`, `Style` 接口，支持主题切换。 |
| **事件** | 自定义 `Message`、`Subscription`，监听时间、键盘、鼠标等。 |
| **特效** | `ProgressBar`, `Spinner`, `Modal`, `Popover` 等 UI 丰富组件。 |
| **应用生命周期** | `Command`、`Task`, 支持异步事件、文件 I/O。 |
| **国际化** | `iced::widget::text::FormattedText` 支持多语言与行内翻译。 |

---

## 用法

### 1. 添加依赖

```toml
[dependencies]
iced = { version = "0.10", features = ["native"] }
```

> 如果是 WebAssembly 项目，省略 `native` feature，使用 `web`。

### 2. 基础模板

```rust
use iced::{
    button, executor, Application, Command, Element, Settings, Text,
};

pub fn main() -> iced::Result {
    Counter::run(Settings::default())
}

#[derive(Default)]
struct Counter {
    value: i32,
    increment_button: button::State,
}

#[derive(Debug, Clone, Copy)]
pub enum Message {
    Increment,
}

impl Application for Counter {
    type Executor = executor::Default;
    type Message = Message;
    type Flags = ();

    fn new(_flags: ()) -> (Counter, Command<Message>) {
        (Counter::default(), Command::none())
    }

    fn title(&self) -> String {
        String::from("Counter - iced")
    }

    fn update(&mut self, msg: Message) -> Command<Message> {
        match msg {
            Message::Increment => self.value += 1,
        }
        Command::none()
    }

    fn view(&mut self) -> Element<Message> {
        let button = button::Button::new(&mut self.increment_button, Text::new("+"))
            .on_press(Message::Increment);

        Column::new()
            .spacing(20)
            .push(Text::new(self.value.to_string()))
            .push(button)
            .into()  // Element<Message>
    }
}
```

### 3. 启动

```bash
cargo run
```

> 在 WebAssembly 中可使用 `wasm-pack` 编译并部署到页面。

### 4. 热重载与自定义

```rust
// 在 `iced::Application::run` 之前，可以指定 Runtime
use iced::Runtime;

fn main() -> iced::Result {
    let runtime = Runtime::default(); // 或 `Runtime::debug()`
    Counter::run_with_runtime(runtime, Settings::default())
}
```

---

## 进一步学习

- **官方文档**：<https://github.com/iced-rs/iced/tree/latest/docs>
- **示例项目**：`examples/` 目录下包含 `todo`, `counter`, `calculator` 等完整示例。
- **社区支持**：在 Discord、Reddit、StackOverflow 等讨论 `iced` 的最佳实践。

---

**提示**：当你在使用 `iced` 时，建议把 `iced` 的 `app` 代码组织在子模块里，使用 `#[derive(Debug)]` 的 `Message` 枚举来管理状态，保持 `view` 只负责 UI 描述。

祝你编码愉快 🚀

