---
title: uniffi-rs
---


# Uniffi-rs（Mozilla）

- **项目地址**：<https://github.com/mozilla/uniffi-rs>

## 简介
Uniffi-rs 是 Mozilla 开源的跨语言绑定生成工具，旨在让 Rust 编写的库能够无缝调用多种主流语言（如 Kotlin、Swift、JavaScript、Python 等），并保持类型安全、零拷贝和高性能。

## 主要特性
- **跨语言绑定生成**：一次编写 Rust 代码，自动生成目标语言的 FFI 接口与包装层。  
- **类型安全**：在 Rust 与目标语言之间保持完整的类型映射，避免运行时错误。  
- **零拷贝**：支持原生字符串、向量等数据结构的零拷贝传递，提高性能。  
- **易于集成**：提供 `uniffi-bindgen` CLI 与 Cargo 子命令，集成到现有构建流程。  
- **多语言支持**：官方示例已涵盖 Kotlin/Android、Swift/iOS、JavaScript/Node.js、Python、C 等。  
- **开源与社区**：MIT 许可证，活跃的社区与文档支持。

## 核心组件
| 组件 | 作用 |
|------|------|
| `uniffi` crate | Rust 侧的宏与运行时支持（如 `#[uniffi::export]`） |
| `uniffi-bindgen` | 生成绑定代码的工具，支持多语言输出 |
| `uniffi-bindgen-cli` | CLI 前端，快捷执行绑定生成命令 |
| 目标语言桥接库 | 例如 `uniffi-android`, `uniffi-ios`, `uniffi-python` 等 |

## 用法示例

### 1. 准备 Rust 代码
```rust
// src/lib.rs
use uniffi::prelude::*;

#[uniffi::export]
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

### 2. 配置 `uniffi.toml`
```toml
[uniffi]
# 生成的绑定文件存放目录
output-dir = "src/uniffi"
# 需要生成的目标语言
targets = ["kotlin", "swift", "python"]
```

### 3. 生成绑定
```bash
cargo install uniffi-bindgen
uniffi-bindgen generate src/lib.rs
# 或者使用 Cargo 子命令
cargo uniffi-bindgen generate
```

### 4. 集成到目标语言项目
- **Android**：将生成的 `uniffi-android` 模块添加为 Gradle 依赖。  
- **iOS**：将 `uniffi-ios` 框架加入 Xcode 项目。  
- **Python**：`pip install ./build/uniffi_python-*.whl`。  

## 参考文档
- 官方 GitHub Wiki: <https://github.com/mozilla/uniffi-rs/wiki>
- 示例项目: <https://github.com/mozilla/uniffi-rs/tree/main/examples>

---
> 以上内容已保存到 `src/content/docs/00/uniffi-rs_mozilla.md`。