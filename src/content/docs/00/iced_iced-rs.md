---
title: Iced
---

# Iced

A cross-platform GUI library for Rust, inspired by Elm.

## Features

- Simple, easy-to-use, batteries-included API
- Type-safe, reactive programming model
- Cross-platform support (Windows, macOS, Linux, and the Web)
- Responsive layout
- Built-in widgets (including text inputs, scrollables, and more!)
- Custom widget support (create your own!)
- Debug overlay with performance metrics
- First-class support for async actions (use futures!)
- Modular ecosystem split into reusable parts:
  - A renderer-agnostic native runtime enabling integration with existing systems
  - Two built-in renderers leveraging `wgpu` and `tiny-skia`
    - `iced_wgpu` supporting Vulkan, Metal and DX12
    - `iced_tiny_skia` offering a software alternative as a fallback
  - A windowing shell

## Usage

Inspired by The Elm Architecture, Iced expects you to split user interfaces into four different concepts:

- **State** — the state of your application
- **Messages** — user interactions or meaningful events that you care about
- **View logic** — a way to display your state as widgets that may produce messages on user interaction
- **Update logic** — a way to react to messages and update your state

### Example: A Simple Counter

We start by modelling the **state** of our application:

```rust
#[derive(Default)]
struct Counter {
    value: i32,
}
```

Next, we need to define the possible user interactions of our counter: the button presses. These interactions are our **messages**:

```rust
#[derive(Debug, Clone, Copy)]
pub enum Message {
    Increment,
    Decrement,
}
```

Now, let's show the actual counter by putting it all together in our **view logic**:

```rust
use iced::widget::{button, column, text, Column};

impl Counter {
    pub fn view(&self) -> Column<Message> {
        // We use a column: a simple vertical layout
        column![
            // The increment button. We tell it to produce an
            // `Increment` message when pressed
            button("+").on_press(Message::Increment),

            // We show the value of the counter here
            text(self.value).size(50),

            // The decrement button. We tell it to produce a
            // `Decrement` message when pressed
            button("-").on_press(Message::Decrement),
        ]
    }
}
```

Finally, we need to be able to react to any produced **messages** and change our **state** accordingly in our **update logic**:

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

And that's everything! We just wrote a whole user interface. Let's run it:

```rust
fn main() -> iced::Result {
    iced::run("A cool counter", Counter::update, Counter::view)
}
```

Iced will automatically:

1. Take the result of our **view logic** and layout its widgets.
2. Process events from our system and produce **messages** for our **update logic**.
3. Draw the resulting user interface.

Read the [book](https://book.iced.rs/), the [documentation](https://docs.rs/iced/), and the [examples](https://github.com/iced-rs/iced/tree/master/examples#examples) to learn more!
