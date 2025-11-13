---
title: boa
---


# Boa - JavaScript 引擎 (Rust 实现)

## 项目地址
[https://github.com/boa-dev/boa](https://github.com/boa-dev/boa)

## 主要特性 & 功能

| 特性 | 说明 |
|------|------|
| **ECMAScript 2020 兼容** | 完整实现 ES2020 语法与语义，支持 `async/await`、`BigInt`、`Generator`、`Proxy`、`Reflect`、`Object.seal` 等。 |
| **模块系统** | 支持 ES 模块（`import`/`export`），并提供 `CJS`（CommonJS）兼容层。 |
| **TypeScript 预处理** | 内置 `typescript` 解析器，可直接在 `boa` 中运行 TS 代码。 |
| **JIT（未来可选）** | 设计时考虑 JIT 编译，可在未来通过 `llvm` 或 `wasm` 产生零拷贝执行。 |
| **安全与可靠** | 全部用 Rust 编写，利用所有权与生命周期保证没有缓冲区溢出与内存泄漏。 |
| **灵活的嵌入式API** | 提供 `boa_engine::Context`、`boa_engine::ObjectValue` 等低级 API，方便在 Rust 项目中嵌入 JavaScript。 |
| **CLI 工具** | `boa` 二进制支持 `repl`、`eval`、`benchmark`、`ast`、`build` 等子命令，方便单文件或项目评估。 |
| **命令行 REPL** | 类似 `node` 的交互式 REPL，支持命令历史、自动补全。 |
| **性能基准** | 通过 `boa-bench` 与 `node` 对比，某些计算密集型任务 (比如 `eval`、`JSON` 解析) 甚至可匹敌或超过 `node`。 |
| **WebAssembly 输出** | 未来计划提供 `boa-wasm` 子项目，直接将 JavaScript 转换为 WebAssembly。 |
| **活跃社区** | 近 300+ 贡献者，持续跟进 ECMAScript 标准进展与 Bug 修复。 |

## 快速开始

### 1️⃣ 作为依赖嵌入到 Rust 项目
```rust
// Cargo.toml
[dependencies]
boa_engine = "0.13"   // 具体版本请参考官方文档

// main.rs
use boa_engine::{Context, JsValue};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut ctx = Context::new();
    // 简单算术
    let result = ctx.eval("1 + 2 * 3")?;
    println!("Result: {}", result);

    // 使用 JS 对象
    let obj = ctx.eval("({ foo: 'bar', arr: [1,2,3] })")?;
    if let JsValue::Object(o) = obj {
        let foo = o.get("foo")?;
        println!("foo: {}", foo);
    }

    Ok(())
}
```

### 2️⃣ 通过 Cargo 直接安装 CLI
```bash
cargo install boa
```
使用示例：
```bash
# 交互式 REPL
boa repl

# 直接评估一个 JS 文件
boa eval hello.js

# AST 可视化
boa ast hello.js
```

### 3️⃣ 运行内置基准
```bash
cargo run --release --bin boa-bench
# 或者更直接
boa benchmark
```

## 典型使用场景

| 场景 | 说明 |
|------|------|
| 服务器端脚本 | 在 Rust 编写的服务器中嵌入 JS 脚本，例如插件系统。 |
| 工具链 | 生成器、打包器、代码转换器可用 `boa` 解析/生成 JavaScript。 |
| 教学实验 | 通过 `boa` 创建可视化、交互式学习工具（例如在 Web 上演示 JavaScript 运行时）。 |
| 嵌入式系统 | 由于安全性高，可用于资源受限的嵌入式设备、IoT 芯片。 |
| WebAssembly 预处理 | 将 TypeScript/JS 转译后直接生成 WASM，轻量级前端解压。 |

## 常见问题 & 文档

- 详细的 API 文档请参见：[https://boa.dev](https://boa.dev)
- 代码示例与 FAQ 在 `examples/` 目录与 README
- 常见错误：  
  - `JSError: SyntaxError` → 语法不兼容，请检查 `boa` 版本是否与 ES20xx 对应。  
  - `TypeError: Cannot read property of undefined` → 访问未定义对象属性；请先检查 JS 代码。

## 贡献与支持

- 开源协议：MIT  
- Bug/Feature 请求：GitHub Issues  
- 社区讨论：Discord 或 Gitter（见 README）  

> **提示**：如果需要在与其它 JavaScript 运行时交互（如 `node` 脚本），建议使用 `boa_runtime::Node`, `boa_runtime::Deno` 等对应的扩展（正在开发中）。

---
**Boa** 是 Rust 生态中最接近标准化、性能平衡且安全可靠的 JavaScript 引擎，适合想要在 Rust 项目中使用脚本语言或打造自定义 JS 相关工具的开发者。祝编码愉快 🚀
