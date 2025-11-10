---
title: smithay
---

# Smithay

## 项目简介

Smithay 是一个用于创建 Wayland compositors 的 Rust 库。它提供构建 Wayland 合成器的基本构建块，支持核心 Wayland 协议、官方协议扩展以及一些外部扩展（如 wlroots 和 KDE 的扩展）。

## 主要功能

- **核心协议支持**：实现 Wayland 核心协议和官方扩展协议
- **外部扩展支持**：支持 wlroots 和 KDE 的协议扩展
- **模块化设计**：不强制使用不需要的部分，提供灵活性
- **高层次抽象**：避免低级细节，让开发者专注于高层逻辑
- **安全性**：利用 Rust 的安全特性，确保代码安全
- **文档完善**：提供详细的 API 文档和功能说明

## 使用方法

### 添加依赖

在你的 `Cargo.toml` 文件中添加 Smithay 依赖：

```toml
[dependencies]
smithay = "0.7"
```

### 基本用法

Smithay 不是一个完整的合成器框架，而是提供构建块。你需要使用其 API 来创建自己的 Wayland compositor。

例如，创建一个简单的 compositor：

```rust
use smithay::backend::drm::DrmBackend;
use smithay::wayland::compositor::CompositorHandler;
// ... 其他导入

struct MyCompositor {
    // 你的状态
}

impl CompositorHandler for MyCompositor {
    // 实现必要的 trait 方法
}
```

### 示例

Smithay 提供了一个示例 compositor：Anvil。你可以查看 [Anvil README](https://github.com/Smithay/smithay/blob/master/anvil/README.md) 了解如何运行和使用它。

### 系统依赖

在使用 Smithay 前，需要安装以下系统依赖：

- `libwayland`
- `libxkbcommon`
- `libudev`
- `libinput`
- `libgbm`
- `libseat`
- `xwayland`

## 相关项目

以下是一些使用 Smithay 的 compositor 项目：

- [Cosmic](https://github.com/pop-os/cosmic-epoch)：下一代 Cosmic 桌面环境
- [Niri](https://github.com/YaLTeR/niri)：可滚动平铺的 Wayland compositor
- [MagmaWM](https://github.com/MagmaWM/MagmaWM)：多功能可定制的 Wayland compositor

## 社区

- Matrix 聊天室：[#smithay:matrix.org](https://matrix.to/#/#smithay:matrix.org)
- IRC：#Smithay on libera.chat

## 许可证

MIT License
