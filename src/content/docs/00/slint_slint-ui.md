---
title: Slint
---

# Slint

## 简介

Slint 是一个开源的声明式 GUI 工具包，用于构建原生用户界面，适用于嵌入式系统、桌面和移动平台。它使用简单的标记语言来定义用户界面。

## 功能

- 声明式 UI 设计：使用 .slint 标记语言定义界面布局和组件。
- 跨平台支持：支持桌面（Windows、macOS、Linux）、嵌入式系统和移动平台。
- 多语言绑定：支持 Rust、C++、Python、Node.js 等编程语言。
- 高性能渲染：优化的渲染引擎，确保流畅的用户体验。
- 丰富的组件库：提供标准组件，如按钮、文本、列表等。
- 实时预览：支持在开发过程中实时预览 UI 更改。

## 用法

### Rust 示例

1. 在 `Cargo.toml` 中添加依赖：

```toml
[dependencies]
slint = "1.0"
```

2. 创建 `.slint` 文件（例如 `main.slint`）：

```slint
export component MainWindow inherits Window {
    title: "Hello World";
    width: 400px;
    height: 300px;

    Text {
        text: "Hello, Slint!";
        horizontal-alignment: center;
        vertical-alignment: center;
    }
}
```

3. 在 `main.rs` 中加载和运行：

```rust
slint::include_modules!();

fn main() -> Result<(), slint::PlatformError> {
    let main_window = MainWindow::new()?;
    main_window.run()
}
```

运行命令：

```shell
cargo run
```

### C++ 示例

1. 使用 CMake 配置项目：

```cmake
cmake_minimum_required(VERSION 3.21)
project(my_application LANGUAGES CXX)

include(FetchContent)
FetchContent_Declare(
    Slint
    GIT_REPOSITORY https://github.com/slint-ui/slint.git
    GIT_TAG release/1
    SOURCE_SUBDIR api/cpp
)
FetchContent_MakeAvailable(Slint)

add_executable(my_application main.cpp)
slint_target_sources(my_application my_application_ui.slint)
target_link_libraries(my_application PRIVATE Slint::Slint)
```

2. 创建 `.slint` 文件和 `main.cpp`。

3. 构建和运行：

```shell
mkdir build && cd build
cmake ..
cmake --build .
./my_application
```

### Python 示例

1. 安装依赖：

```shell
pip install slint
```

2. 创建 `main.py`：

```python
import slint

def main():
    window = slint.Window(ui_file="ui/app-window.slint")
    window.run()

if __name__ == "__main__":
    main()
```

### Node.js 示例

1. 安装依赖：

```shell
npm install slint-ui
```

2. 创建 `index.js`：

```javascript
import * as slint from 'slint-ui';
let ui = slint.loadFile(new URL('main.slint', import.meta.url));
let main = new ui.Main();
main.run();
```

更多示例和详细文档请参考官方文档：[https://slint.dev/](https://slint.dev/)
