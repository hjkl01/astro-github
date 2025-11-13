---
title: Catten
---

# Catten

## 项目简介

Catten 是 CharlotteOS 的内核，一个实验性的现代操作系统内核。它是一个单片内核，设计灵活，希望能在多个地方使用。它借鉴了 exokernels、Plan 9 和 Fuchsia 等系统的理念，提供低级系统调用接口，并允许在之上层叠任何高层接口。

## 主要功能

- **单片内核架构**：提供低级系统调用接口，支持灵活的高层接口层叠。
- **类型安全的系统命名空间**：类似于 Fuchsia 和 Plan 9 的命名空间，但更灵活和类型安全。使用 URI 作为路径，支持通过网络访问其他主机的命名空间，无需本地挂载。
- **安全机制**：通过细粒度能力和持久强制访问控制策略确保安全。
- **多架构支持**：
  - 主要 ISA：x86_64（使用 x2APIC LAPIC 模式）
  - 次要 ISA：RISC-V64 RVA23
- **固件支持**：
  - UEFI
  - ACPI
  - SBI（仅 RISC-V）
- **硬件要求**：
  - 内存：推荐 >= 1 GiB，必需 128 MiB
  - 存储：推荐 >= 64 GiB，必需 4 GiB，支持 NVMe 和 USB Mass Storage
  - 输出：支持 UEFI GOP 的显示适配器，NS16550 UART 或 USB CDC ACM
  - 输入：PS/2、USB HID、I2C HID 键盘；UART 或 USB CDC ACM 串口
  - 网络：USB CDC NCM（以太网 over USB）

## 编程语言

- 主要用 Rust 编写
- ISA 特定汇编语言（x86_64 使用 Intel 语法，由 rustc 和 llvm-mc 实现）

## 外部依赖

- 允许经过维护者审查的 C 语言依赖
- 禁止除 Rust、C 和汇编以外的其他语言依赖
- 优先使用高质量 Rust 等价物，除非有充分理由使用外部 C 库

## 用法

Catten 仍在早期开发中，核心子系统正在积极构建。目前主要用于学习和实验目的。

### 构建和运行

1. 克隆仓库：

   ```
   git clone https://github.com/charlotte-os/Catten.git
   cd Catten
   ```

2. 安装依赖（Rust、必要的工具链等）。

3. 构建内核：

   ```
   make
   ```

4. 使用 Limine 引导加载器运行（参考 limine.conf）。

具体构建步骤和运行环境请参考仓库中的 README.md 和 Makefile。

### 贡献

欢迎贡献！请从问题跟踪器中获取任务、建议功能，或参与仓库、Discord 或 Matrix 上的讨论。

- Discord: https://discord.gg/vE7bCCKx4X
- Matrix: https://matrix.to/#/#charlotteos:matrix.org

## 许可证

本内核根据 GNU General Public License version 3.0（或您选择的任何更高版本）授权。通过贡献此项目，您同意将您的贡献仅根据相同条款授权。
