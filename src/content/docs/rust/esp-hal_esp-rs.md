---
title: esp-hal
---

# esp-hal

## 项目简介

esp-hal 是 Espressif 设备的裸机 (`no_std`) 硬件抽象层 (Hardware Abstraction Layer)。它为 ESP32 系列微控制器提供低级硬件访问接口，支持多种 ESP32 设备。

## 支持的设备

esp-hal 对以下设备提供不同程度的支持：

- **ESP32 系列**: ESP32
- **ESP32-C 系列**: ESP32-C2, ESP32-C3, ESP32-C6
- **ESP32-H 系列**: ESP32-H2
- **ESP32-S 系列**: ESP32-S2, ESP32-S3

此外，通过 [esp-lp-hal](https://github.com/esp-rs/esp-hal/tree/main/esp-lp-hal) 包提供对 ESP32-C6、ESP32-S2 和 ESP32-S3 上低功耗 RISC-V 核心的有限编程支持。

## 主要功能

- 提供裸机硬件抽象层，无需标准库 (`no_std`)
- 支持多种 ESP32 系列微控制器
- 包含多个相关 crate，如 esp-alloc、esp-backtrace、esp-config 等
- 提供示例代码和测试套件
- 支持低功耗核心编程

## 使用方法

### 环境准备

1. 安装 Rust 工具链
2. 安装 ESP32 开发工具链
3. 配置目标设备

### 基本用法

1. **添加依赖**:
   在 `Cargo.toml` 中添加 esp-hal 依赖：

   ```toml
   [dependencies]
   esp-hal = "1.0"
   ```

2. **初始化 HAL**:

   ```rust
   use esp_hal::prelude::*;

   let peripherals = esp_hal::init(esp_hal::Config::default());
   ```

3. **使用外设**:
   ```rust
   // 示例：使用 GPIO
   let mut led = peripherals.GPIO2.into_push_pull_output();
   led.set_high().unwrap();
   ```

### 开发指南

- 阅读 [The Rust on ESP Book](https://docs.espressif.com/projects/rust/book/) 了解 ESP 设备上的 Rust 开发
- 参考 [官方文档](https://docs.espressif.com/projects/rust/) 了解 HAL 使用详情
- 查看 [示例代码](https://github.com/esp-rs/esp-hal/tree/main/examples) 学习具体用法
- 注意使用与 esp-hal 版本匹配的示例标签，如 [esp-hal-v1.0.0](https://github.com/esp-rs/esp-hal/tree/esp-hal-v1.0.0/examples)

### 构建和运行

```bash
# 构建项目
cargo build --release

# 运行示例
cargo run --example hello_world
```

## 许可证

本项目采用 Apache-2.0 或 MIT 许可证。
