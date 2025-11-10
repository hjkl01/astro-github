---
title: Wild
---

# Wild Linker

## 项目简介

Wild 是一个非常快速的 Linux 链接器，旨在用于迭代开发。其最终目标是实现增量链接，目前虽然尚未实现，但即使在非增量模式下也已经相当快速。

## 功能特性

- **高性能链接**：专注于快速链接，适合开发迭代
- **平台支持**：
  - x86-64 on Linux
  - ARM64 on Linux
  - RISC-V (riscv64gc) on Linux
- **输出格式支持**：
  - 静态链接非重定位二进制
  - 静态链接位置无关二进制 (static-PIE)
  - 动态链接二进制
  - 共享对象 (.so 文件)
- **Rust 支持**：支持 Rust proc-macros
- **调试信息**：支持调试信息
- **并行处理**：支持 GNU jobserver
- **链接器脚本**：基本链接器脚本支持（section mapping, keeping sections, alignment, defining start/stop symbols）

## 安装方法

### 从 GitHub Releases 安装

从 [releases 页面](https://github.com/davidlattimore/wild/releases) 下载 tarball，解压并将 `wild` 二进制文件复制到 PATH 中。

### 使用 Cargo Binstall

如果安装了 [cargo-binstall](https://github.com/cargo-bins/cargo-binstall)：

```bash
cargo binstall wild-linker
```

### 从 Crates.io 构建最新发布版

```bash
cargo install --locked wild-linker
```

### 从 Git Head 构建

构建并安装最新的未发布代码：

```bash
cargo install --locked --bin wild --git https://github.com/davidlattimore/wild.git wild-linker
```

### Nix

参考 [nix/nix.md](https://github.com/davidlattimore/wild/blob/main/nix/nix.md)

## 用法

### 作为默认链接器

要在 Rust 项目中使用 Wild 作为默认链接器，在 `~/.cargo/config.toml` 中添加：

Linux 上：

```toml
[target.x86_64-unknown-linux-gnu]
linker = "clang"
rustflags = ["-C", "link-arg=--ld-path=wild"]
```

Illumos 上：

```toml
[target.x86_64-unknown-illumos]
# Absolute path to clang - on OmniOS this is likely something like /opt/ooce/bin/clang.
linker = "/usr/bin/clang"

rustflags = [
    # Will silently delegate to GNU ld or Sun ld unless the absolute path to Wild is provided.
    "-C", "link-arg=-fuse-ld=/absolute/path/to/wild"
]
```

### 在 CI 中使用

在 CI 中使用 Wild 作为 Rust 代码的链接器，参考 [wild-action](https://github.com/davidlattimore/wild-action)。

### 链接 Rust 代码

使用以下命令构建和测试使用 Wild 的 crate：

```bash
RUSTFLAGS="-Clinker=clang -Clink-args=--ld-path=wild" cargo test
```

### 验证链接器

安装 `readelf`，然后运行：

```bash
readelf -p .comment my-executable
```

查找类似行：

```
Linker: Wild version 0.1.0
```

或者使用：

```bash
strings my-executable | grep 'Linker:'
```

## 基准测试

Wild 的目标是通过增量链接实现极高速度。目前在非增量链接和初始链接时也尽可能快速。

详细基准测试信息参考 [BENCHMARKING.md](https://github.com/davidlattimore/wild/blob/main/BENCHMARKING.md)。

Wild 在超过 8 个线程时性能不佳，这是正在调查和改进的问题。

## 贡献

贡献信息参考 [CONTRIBUTING.md](https://github.com/davidlattimore/wild/blob/main/CONTRIBUTING.md)。

设计概述参考 [DESIGN.md](https://github.com/davidlattimore/wild/blob/main/DESIGN.md)。

## 聊天服务器

Wild 相关讨论使用 Zulip 服务器：[wild.zulipchat.com](https://wild.zulipchat.com/join/bbopdeg6howwjpaiyowngyde/)。

## 进一步阅读

更多关于 Wild 链接器的文章在 [David 的博客](https://davidlattimore.github.io/) 上。

## 赞助

如果您想 [赞助此项目](https://github.com/sponsors/davidlattimore)，将不胜感激。赞助越多，我就能越长时间全职工作于此项目。

## 许可证

根据 [Apache License, Version 2.0](https://github.com/davidlattimore/wild/blob/main/LICENSE-APACHE) 或 [MIT license](https://github.com/davidlattimore/wild/blob/main/LICENSE-MIT) 授权。
