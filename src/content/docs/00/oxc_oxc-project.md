
---
title: oxc
---


---
title: "oxc - JavaScript 编译器 & 打包器"
url: /oxc-project/
date: 2025-11-01
tags: ["Rust", "JavaScript", "编译", "打包"]
---

# oxc

> 项目地址: <https://github.com/oxc-project/oxc>

## 概述

`oxc` 是一款用 Rust 编写的高性能 **JavaScript/TypeScript 编译器和打包器**。它兼容所有主流的前端语法（ES, TS, JSX, Flow 等），并提供模块解析、Tree‑Shaking、代码压缩、Source Map 生成等完整工具链。由于采用零依赖的编译器实现，`oxc` 的执行速度快、占用内存小，尤其适合 CI、构建服务器以及嵌入到其它应用中的编译需求。

## 主要特性

| # | 特性 | 说明 |
|---|------|------|
| 1 | 高速解析 & 编译 | 采用官方 V8 parser 的 Rust 绑定，实现极致解析速度 |
| 2 | 多语法支持 | 原生支持 ES ES2022, TypeScript, JSX, Flow, 以及各种 Babel 插件配置 |
| 3 | 模块解析 & 打包 | 支持 Node.js 和 ESModule 解析，进行多级依赖树构建、代码拆分 |
| 4 | Tree‑Shaking | 自动移除未使用的导出，减少最终体积 |
| 5 | 代码压缩 | 对最终输出进行 minify，保留 source map |
| 6 | 插件系统 | 通过 trait `oxc::plugin::Plugin` 可以在编译链中注入自定义逻辑 |
| 7 | 可通过 CLI 与 Rust API 双向调用 | 既能在命令行批量处理，也能在项目中直接调用 |

## 主要功能

| 功能 | 说明 | 关键 CLI 参数 |
|------|------|--------------|
| **编译** | 将代码从任何现代 JavaScript/TS 语法转换为目标 ES 版本 | `--target` (`es2015`, `es2020`, `esnext`) |
| **打包** | 生成单文件或多文件 bundle，支持代码拆分 | `--entry`, `--outfile`, `--splitting` |
| **代码压缩** | 对 JS/TS 输出进行 minify | `--minify` |
| **Source Map** | 生成映射文件 | `--source-map` |
| **插件** | 在编译过程中注入自定义处理器 | 可通过 `--plugin` 加载动态链接库或 Rust crate |

## 用法

### 1. CLI 方式

```bash
# 基础打包
oxc bundle \
  --entry ./src/index.ts \
  --outfile ./dist/bundle.js

# 打包并压缩
oxc bundle \
  --entry ./src/index.ts \
  --outfile ./dist/bundle.js \
  --minify

# 指定目标 ES 版本
oxc bundle \
  --entry ./src/index.ts \
  --outfile ./dist/bundle.js \
  --target es2015

# 生成 source map
oxc bundle \
  --entry ./src/index.ts \
  --outfile ./dist/bundle.js \
  --source-map
```

#### 常用参数

| 参数 | 作用 |
|------|------|
| `--entry` | 入口文件列表，支持 glob |
| `--outfile` | 输出文件路径 |
| `--splitting` | 启用代码拆分，生成 `chunk.*.js` |
| `--minify` | 对输出进行压缩 |
| `--source-map` | 生成对应的 source map 文件 |
| `--target` | 指定目标 JS 版本 |

### 2. Rust API 方式

```rust
use oxc::{
    bundler::{BundleOptions, Bundler},
    compiler::{Compiler, CompilerOptions},
};
use std::path::PathBuf;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 1️⃣ 配置编译器
    let compiler_opts = CompilerOptions::default();
    let compiler = Compiler::new(compiler_opts);

    // 2️⃣ 配置打包设置
    let bundle_opts = BundleOptions {
        entry: vec![PathBuf::from("./src/index.ts")],
        minify: true,
        target: oxc::targets::Target::ES2015,
        ..Default::default()
    };
   ler = Bundler::new(compiler, bundle_opts);

    // 3️⃣ 执行打包
    let output = bundler.bundle()?;
    std::fs::write("./dist/bundle.js", output)?;
    Ok(())
}
```

> **提示**：你可以将几个 `BundleOptions` 组合起来实现多入口、多体积分割的构建方案。

### 3. 插件示例

```rust
use oxc::{plugin::Plugin, tors::Scope};

pub struct RemoveConsole;

impl Plugin for RemoveConsole {
    fn transform(&self, node: &mut tokens::JsNode, _scope: &Scope) {
        // 在遍历到 console.* 的时候移除
        if node.is_console_call() {
            node.remove();
        }
    }
}
```

> 之后通过 `--plugin libremove_console.so` 在 CLI 调用时加载。

## 常见问题

| 问题 | 解答 |
|------|------|
| **为什么我使用 `--target es5` 时结果报错？** | `oxc` 目前只支持 `es2015` 及以上，若需 `es5` 请使用 `esbuild` 或自行后处理。 |
| **如何开启代码拆分？** | 使用 `--splitting` 或在 `BundleOptions` 中 `splitting: true`。 |

## 参与贡献

- Fork 并 clone 项目: `git clone https://github.com/oxc-project/oxc.git`
- 运行示例: `cargo run --bin oxc -- bundle --entry ./examples/app.js --outfile ./dist/bundle.js`
- 单元测试: `cargo test`
- 提交 PR 时请配合 lint 与格式化: `cargo fmt && cargo clippy -- -D warnings`

---

> **文件路径**: `src/content/docs/00/oxc_oxc-project.md`
