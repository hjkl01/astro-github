---
title: Iced
---

# Iced

一个受 Elm 启发的 Rust 跨平台 GUI 库。

## 特性

- 简单、易用、开箱即用的 API
- 类型安全、响应式编程模型
- 跨平台支持（Windows、macOS、Linux 和 Web）
- 响应式布局
- 内置小部件（包括文本输入、可滚动等！）
- 自定义小部件支持（创建自己的！）
- 带有性能指标的调试覆盖层
- 对异步操作的一流支持（使用 futures！）
- 模块化生态系统，分为可重用部分：
  - 启用与现有系统集成的渲染器无关的原生运行时
  - 两个内置渲染器，利用 `wgpu` 和 `tiny-skia`
    - `iced_wgpu` 支持 Vulkan、Metal 和 DX12
    - `iced_tiny_skia` 作为后备提供软件替代方案
  - 一个窗口外壳

## 用法

受 Elm 架构启发，Iced 期望您将用户界面分为四个不同的概念：

- **状态** — 应用程序的状态
- **消息** — 用户交互或您关心的有意义事件
- **视图逻辑** — 将状态显示为小部件的方式，这些小部件可能在用户交互时产生消息
- **更新逻辑** — 对消息做出反应并更新状态的方式

### 示例：一个简单的计数器

我们从建模应用程序的**状态**开始：

```rust
#[derive(Default)]
struct Counter {
    value: i32,
}
```

接下来，我们需要定义计数器的可能用户交互：按钮按下。这些交互是我们的**消息**：

```rust
#[derive(Debug, Clone, Copy)]
pub enum Message {
    Increment,
    Decrement,
}
```

现在，让我们通过在**视图逻辑**中将它们组合在一起来显示实际计数器：

```rust
use iced::widget::{button, column, text, Column};

impl Counter {
    pub fn view(&self) -> Column<Message> {
        // 我们使用一个列：一个简单的垂直布局
        column![
            // 增量按钮。我们告诉它在按下时产生一个
            // `Increment` 消息
            button("+").on_press(Message::Increment),

            // 我们在这里显示计数器的值
            text(self.value).size(50),

            // 减量按钮。我们告诉它在按下时产生一个
            // `Decrement` 消息
            button("-").on_press(Message::Decrement),
        ]
    }
}
```

最后，我们需要能够对任何产生的**消息**做出反应，并相应地改变我们的**状态**在我们的**更新逻辑**中：

```rust
impl Counter {
    // ...

    pub fn update(&mut self, message: Message) {
        match message {
            Message::Increment => {
                self.value += 1;
            }
            Message::Decrement => {
                self.value -= 1;
            }
        }
    }
}
```

就是这样！我们刚刚写了一个完整的用户界面。让我们运行它：

```rust
fn main() -> iced::Result {
    iced::run("A cool counter", Counter::update, Counter::view)
}
```

Iced 将自动：

1. 获取我们的**视图逻辑**的结果并布局其小部件。
2. 处理来自系统的事件并为我们的**更新逻辑**产生**消息**。
3. 绘制结果用户界面。

阅读 [book](https://book.iced.rs/)、[documentation](https://docs.rs/iced/) 和 [examples](https://github.com/iced-rs/iced/tree/master/examples#examples) 以了解更多！
