
---
title: RustPython
---

# RustPython

**GitHub 项目地址**  
[https://github.com/RustPython/RustPython](https://github.com/RustPython/RustPython)

## 主要特性

- **速度与安全并重**：使用 Rust 编写的 Python 解释器，结合 JIT 技术实现高性能执行。
- **完整的标准库实现**：覆盖大部分 CPython 标准库，可直接使用常见的 Python 模块。
- **可嵌入使用**：提供 API，支持将 RustPython 嵌入到 Rust 项目中，或作为可执行文件使用。
- **持续发展**：活跃的社区维护，持续对新特性和兼容性进行改进。
- **跨平台**：支持 Windows、Linux、macOS 及 WebAssembly 环境。

## 主要功能

| 项目 | 功能说明 |
|------|----------|
| **解释器引擎** | 运行 .py 文件、交互式 REPL、执行字符串代码 |
| **JIT 编译** | 可选的 LLVM/JIT 编译器，提高热点代码执行速度 |
| **模块系统** | 完整的 import 系统，支持自定义扩展和 C/C++ 模块（通过 FFI） |
| **标准库** | os、sys、math、datetime 等常用模块 |
| **可交互性** | 标准 REPL，支持输入历史、自动补全 |
| **调试工具** | 支持 `pdb` 调试、堆栈追踪，以及 Rust 调试接口 |
| **WebAssembly** | 编译为 WASM，可在浏览器中运行 Python 代码 |

## 用法

### 1. 直接使用可执行文件

```bash
# 克隆项目
git clone https://github.com/RustPython/RustPython
cd RustPython

# 配置 rustup 并打开项目
rustup override set stable

# 编译并安装 CLI
cargo install --path .

# 运行 Python 脚本
rustpython my_script.py
```

### 2. 交互式 REPL

```bash
rustpython
```

按 `Ctrl+Z(Windows)` 或 `Ctrl+D(Linux/macOS)` 退出。

### 3. 嵌入到 Rust 项目

```toml
# Cargo.toml
[dependencies]
rustpython-compiler = "0.1"
rustpython-vm = "0.1"          # 或 version 对应
```

```rust
use rustpython_vm as vm;
use rustpython_vm::Interpreter;

fn main() {
    let interpreter = Interpreter::new();
    let res = interpreter.run_context(
        "print('Hello from RustPython!')",
        &[],
    );
    println!("Result: {:?}", res);
}
```

### 4. 启用 JIT 编译

```bash
RUSTPYTHON_JIT=1 rustpython my_script.py
```

### 5. 在 WebAssembly 中使用

```bash
cargo build --target wasm32-unknown-unknown
```

然后在前端通过 JavaScript 调用：

```js
import init, { run } from './pkg/rustpython.js';

(async () => {
  await init();
  run("print('Hello WASM')")
})();
```

## 贡献

- Fork 项目，提交 Pull Request。
- 查看 `CONTRIBUTING.md` 获取详细流程。
- 关注 `issues`、`pull requests` 以及 `issues` 目录中的 [Roadmap](https://github.com/RustPython/RustPython/labels/roadmap)。

---

> 文件存放路径: **src/content/docs/00/RustPython_RustPython.md**