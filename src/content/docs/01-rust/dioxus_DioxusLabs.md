---
title: dioxus
---

# Dioxus

## 项目简介

Dioxus 是一个用于构建跨平台用户界面的 Rust 框架，支持 Web、桌面、移动等多个平台，使用单一代码库。它提供了零配置设置、热重载和基于信号的状态管理。

## 主要功能

- **跨平台支持**：使用单一代码库构建 Web、桌面和移动应用
- **信号-based 状态管理**：高效的状态管理机制，支持响应式更新
- **热重载**：开发时支持快速迭代和调试
- **零配置设置**：简化项目初始化和配置
- **丰富的 Hooks**：提供 `use_signal`、`use_effect`、`use_future`、`use_resource` 等用于状态和副作用管理
- **RSX 宏**：类似 JSX 的语法用于定义 UI 组件

## 安装和使用

### 安装 Dioxus CLI

```bash
cargo install dioxus-cli
```

或安装开发版本：

```bash
cargo install --git https://github.com/DioxusLabs/dioxus dioxus-cli
```

### 创建新项目

使用 CLI 创建新项目：

```bash
dx new my-app
cd my-app
dx serve
```

### 基本用法示例

#### 计数器应用

```rust
use dioxus::prelude::*;

fn main() {
    dioxus::launch(App);
}

#[component]
fn App() -> Element {
    let mut count = use_signal(|| 0);

    rsx! {
        div { "Count: {count}" }
        button { onclick: move |_| count += 1, "Increment" }
        button { onclick: move |_| count -= 1, "Decrement" }
    }
}
```

#### 使用信号管理状态

```rust
use dioxus::prelude::*;

#[component]
fn App() -> Element {
    let name = use_signal(|| "world");

    rsx! { "hello {name}!" }
}
```

#### 异步数据获取

```rust
use dioxus::prelude::*;

async fn fetch_data() -> String {
    // 模拟网络请求
    "Data fetched successfully!".to_string()
}

fn DataFetcher(cx: Scope) -> Element {
    let data_future = use_future(cx, || async {
        fetch_data().await
    });

    let content = match data_future.result() {
        Some(Ok(data)) => rsx! { p { "{data}" } },
        Some(Err(e)) => rsx! { p { "Error: {e:?}" } },
        None => rsx! { p { "Loading..." } },
    };

    cx.render(rsx! {
        div {
            h2 { "Data Fetching Example" }
            content
        }
    })
}
```

#### 组件组合

```rust
use dioxus::prelude::*;

#[component]
fn Greeting(name: String) -> Element {
    rsx! { p { "Hello, {name}!" } }
}

#[component]
fn App() -> Element {
    rsx! {
        Greeting { name: "World".to_string() }
    }
}
```

## 更多资源

- [官方文档](https://dioxuslabs.com/)
- [GitHub 仓库](https://github.com/DioxusLabs/dioxus)
