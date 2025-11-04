
---
title: cross
---

# Cross

**项目地址**  
[https://github.com/cross-rs/cross](https://github.com/cross-rs/cross)

## 主要特性

- **跨平台编译**：使用 Docker 让你在任何主机上都能编译 Rust 目标（包括裸机、ARM、aarch64 等）。
- **与 Cargo 完美集成**：使用与 Cargo 接口相同的命令行（如 `cross build`、`cross test`、`cross run`）无缝替换。
- **高效的缓存**：Docker 镜像层缓存可减少重复构建时间，支持 `--cache` 参数控制缓存行为。
- **治理第三方库**：所有依赖与编译工具均在 Docker 镜像中统一，避免环境差异导致的问题。
- **可定制镜像**：支持用户创建自定义 Docker 镜像或使用 `--image` 指定镜像，满足特定构建需求。
- **多目标支持**：内置对常见目标的支持（x86_64, armv7, aarch64, riscv64 等），并可通过 `.cargo/config.toml` 添加自定义 target。
- **安全性与可重复性**：完全基于官方 Docker 镜像，保证构建过程中依赖和工具链的一致性。

## 功能概览

| 功能 | 说明 |
|------|------|
| `cross build` | 按给定目标编译项目，生成可执行文件或库。 |
| `cross test` | 按目标运行单元测试。 |
| `cross run` | 按目标执行程序。 |
| `cross doc` | 生成项目文档。 |
| `cross bench` | 运行基准测试。 |
| `cross install` | 安装工具链或组件（仅支持部分工具）。 |
| `cross dist` | 与 cargo-dist 集成，打包发布文件。 |
| `cross init` | 为新项目生成 Dockerfile + 配置。 |

## 快速开始

```bash
# 安装 cross (需要 Docker 和 Docker Compose)
cargo install cross
# 或者直接使用 GitHub Release 发行版

# 编译当前项目为 armv7-unknown-linux-gnueabihf
cross build --target armv7-unknown-linux-gnueabihf

# 运行测试
cross test --target aarch64-unknown-linux-gnu

# 通过自定义镜像
cross build --target riscv64gc-unknown-linux-gnu --image my/custom-image:latest
```

> **注意**：  
> - Docker 必须已安装并可运行。  
> - 对于 NFS 或 CIFS 存储，需要开启 `cgroup` 或使用 `--privileged` 运行 Docker。  
> - 第一次构建会下载相应目标的 sysroot 和工具链，耗时较长，请耐心等待。

## 自定义 Docker 镜像

1. 拷贝官方基础镜像 `cross/rust-std` 或 `cross/azure-std` 作为起点。
2. 编辑 `Cargo.toml`、`.cargo/config.toml` 以添加自定义依赖或工具。
3. 通过 `cross build --image ./Dockerfile` 指定本地镜像。

```Dockerfile
FROM cross/rust-std:0.6.1

# 安装额外工具，例如 `ccache` 或 `musl-tools`
RUN apt-get update && apt-get install -y ccache musl-tools
```

## 贡献与支持

- Issues、Pull requests ：欢迎提交问题与改进建议。  
- 文档和示例：请查看仓库的 `README.md`、`examples/` 目录。  
- 成为 Maintainer：请先 Fork → PR → 通过 CI 测试。

**使用跨平台构建工具 Cross，消除多平台编译烦恼，让 Rust 程序一次构建即可运行在任何设备！**