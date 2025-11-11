---
title: zig
---

# Zig

Zig 是一个通用编程语言和工具链，旨在维护健壮、最优和可重用的软件。它提供了现代化的编译器功能，支持跨平台开发，并强调安全性、性能和简洁性。

## 主要功能

- **通用编程语言**：支持系统编程、应用开发等各种场景。
- **工具链**：包括编译器、链接器和调试工具，无需外部依赖即可构建项目。
- **跨平台支持**：可编译到多种目标平台，如 Linux、macOS、Windows 等。
- **内存安全**：通过编译时检查和运行时保护机制减少错误。
- **标准库**：提供丰富的标准库，支持文件 I/O、网络、并发等。
- **C 互操作**：可以轻松调用 C 代码，并与现有 C 项目集成。

## 用法

### 安装

1. **下载预构建二进制**：从 [ziglang.org/download](https://ziglang.org/download) 下载适合你平台的版本。
2. **从包管理器安装**：支持多种包管理器，如 Homebrew、APT 等。详情见 [GitHub Wiki](https://github.com/ziglang/zig/wiki/Install-Zig-from-a-Package-Manager)。
3. **从源码构建**：需要 CMake 和 LLVM。运行以下命令：

   ```bash
   mkdir build
   cd build
   cmake ..
   make install
   ```

### 基本用法

- **创建项目**：使用 `zig init-exe` 创建可执行项目，或 `zig init-lib` 创建库项目。
- **编译代码**：运行 `zig build` 构建项目。
- **运行程序**：编译后直接运行生成的可执行文件。
- **测试**：使用 `zig test` 运行测试。
- **文档**：运行 `zig std` 打开标准库文档浏览器。

### 示例代码

```zig
const std = @import("std");

pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}
```

保存为 `main.zig`，然后运行 `zig run main.zig`。

## 文档和资源

- [官方文档](https://ziglang.org/documentation/)
- [语言参考](https://ziglang.org/documentation/master/)
- [GitHub 仓库](https://github.com/ziglang/zig)
- [社区](https://github.com/ziglang/zig/wiki/Community)

Zig 仍在快速发展中，适合对性能和安全性有高要求的开发者。
