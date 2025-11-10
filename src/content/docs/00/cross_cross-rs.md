---
title: cross
---

# cross

## 功能介绍

`cross` 是一个用于 Rust crates 的“零设置”交叉编译和“交叉测试”工具。它提供了一个完整的环境，包括交叉工具链和交叉编译库，能够生成最可移植的二进制文件。

主要功能：

- **零设置交叉编译**：无需修改系统安装，直接提供所有必要的组件。
- **交叉测试**：支持为非 x86_64 和 i686 架构测试 crates，使用 QEMU 模拟。
- **多渠道支持**：兼容 Rust 的 stable、beta 和 nightly 版本。
- **容器化**：基于 Docker 或 Podman，提供隔离的编译环境。

## 用法

### 安装

首先确保安装了依赖：

- [rustup](https://rustup.rs/)
- Docker 或 Podman（推荐 Docker 20.10+ 或 Podman 3.4.0+）
- Linux 内核支持 binfmt_misc（用于交叉测试）

安装 `cross`：

```bash
cargo install cross --git https://github.com/cross-rs/cross
```

### 基本使用

`cross` 的 CLI 与 Cargo 完全相同，但运行在容器中。

启动 Docker 守护进程（Linux）：

```bash
sudo systemctl start docker
```

交叉编译示例：

```bash
# 编译为 ARM64 Linux
cross build --target aarch64-unknown-linux-gnu

# 测试 MIPS64 架构
cross test --target mips64-unknown-linux-gnuabi64

# 发布构建 PowerPC
cross rustc --target powerpc-unknown-linux-gnu --release -- -C lto
```

### 配置

可以通过多种方式配置 `cross`：

1. 在 `Cargo.toml` 中添加 `[workspace.metadata.cross]` 表
2. 使用 `Cross.toml` 文件
3. 设置 `CROSS_CONFIG` 环境变量指定配置文件位置
4. 通过环境变量配置

示例配置（在 `Cargo.toml` 中）：

```toml
[workspace.metadata.cross.target.aarch64-unknown-linux-gnu]
pre-build = [
    "dpkg --add-architecture $CROSS_DEB_ARCH",
    "apt-get update && apt-get --assume-yes install libssl-dev:$CROSS_DEB_ARCH"
]
```

### 支持的目标平台

`cross` 支持众多目标平台，包括但不限于：

- ARM 系列：aarch64, armv7, thumbv7 等
- MIPS 系列：mips, mips64, mipsel 等
- PowerPC：powerpc, powerpc64, powerpc64le
- RISC-V：riscv64gc
- x86：i586, i686
- 其他：s390x, sparc64, loongarch64 等

详细支持列表和测试状态请参考项目文档。

### 调试

使用 `QEMU_STRACE=1` 环境变量可以获取系统调用的回溯：

```bash
QEMU_STRACE=1 cross run --target aarch64-unknown-linux-gnu
```

### Docker in Docker

在容器内运行 `cross` 时，需要设置 `CROSS_CONTAINER_IN_CONTAINER=true` 并挂载 Docker socket。

更多详细信息请参考 [GitHub 仓库](https://github.com/cross-rs/cross) 和 [Wiki](https://github.com/cross-rs/cross/wiki)。
