
---
title: rust-clippy
---


# rust-clippy

**项目地址**: https://github.com/rust-lang/rust-clippy

## 主要特性

- 通过大量 lint 检查，帮助开发者提升代码质量与可维护性  
- 与 Cargo 集成，使用 `cargo clippy` 一键执行  
- 支持 Rust 标准库、语言特性以及第三方 crate 相关检查  
- 提供静态分析、性能建议、错误防护、代码风格规范等多维度 lint

## 关键功能

| 类型 | 说明 | 示例 |
|------|------|------|
| **Correctness** | 检测常见错误（如不必要的 clone、潜在的空指针） | `clippy::needless_borrow` |
| **Performance** | 推荐更高效实现 | `clippy::needless_borrows_for_generic_args` |
| **Pedantic** | 严格编码规范 | `clippy::needless_return` |
| **Style** | 代码风格改进 | `clippy::redundant_clone` |
| **Complexity** | 代码复杂度警告 | `clippy::cognitive_complexity` |

## 使用方法

1. **安装 clippy**  
   ```bash
   rustup component add clippy
   ```

2. **在项目中启用**（可选）  
   ```toml
   # Cargo.toml
   [dev-dependencies]
   clippy = { version = "0.1", optional = true }
   ```

3. **运行**  
   ```bash
   cargo clippy
   ```

4. **忽略或更改规则**  
   ```rust
   #[allow(clippy::needless_borrow)]
   fn foo(x: &i32) { /* ... */ }
   ```

   或在代码中 `#[deny(clippy::pedantic)]` 强制某一规则。

5. **自定义配置**  
   在项目根目录创建 `clippy.toml`，例如：  
   ```toml
   pedantic = { allow = ["clippy::needless_return"] }
   ```

## 小贴士

- `cargo clippy -- -D warnings` 把所有 warning 当成 error 处理  
- `cargo clippy -- -A clippy::all` 暂时禁用所有 lint  
- 使用 `--tests` 检查测试代码中的问题  
- 可以结合 CI（GitHub Actions 等）自动化 lint 检查

---

**更多信息**：请查看官方仓库中的 [README](https://github.com/rust-lang/rust-clippy#rust-clippy) 与 [文档](https://rust-lang.github.io/rust-clippy/)。
