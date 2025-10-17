
---
title: PyOxidizer
---

# PyOxidizer 项目

**项目地址:** [https://github.com/indygreg/PyOxidizer](https://github.com/indygreg/PyOxidizer)

## 主要特性

PyOxidizer 是一个使用 Rust 编写的工具，用于构建和分发 Python 应用程序。它将 Python 解释器、标准库和第三方依赖打包成单个可执行文件，支持 Windows、macOS 和 Linux 平台。主要特性包括：

- **嵌入式 Python 解释器**：将 Python 解释器直接嵌入到可执行文件中，无需安装 Python 环境。
- **零依赖分发**：生成的二进制文件自包含，不依赖系统 Python 安装或外部库路径。
- **跨平台支持**：支持多操作系统和架构，简化跨平台分发。
- **自定义配置**：通过 TOML 配置文件定义 Python 环境、包管理和资源嵌入。
- **性能优化**：使用 Rust 的高效性，启动速度快，支持静态链接以减少运行时依赖。
- **安全性提升**：避免动态链接库的漏洞，支持代码签名和沙箱化。

## 主要功能

- **打包 Python 应用**：将 Python 脚本、模块和依赖打包成独立的可执行文件。
- **资源管理**：嵌入数据文件、DLL 或其他资源到二进制中，支持虚拟文件系统。
- **依赖解析**：自动处理 pip 包和 Python 标准库的集成。
- **构建自动化**：集成 Cargo（Rust 构建工具），支持 CI/CD 管道。
- **调试支持**：提供工具查看嵌入的 Python 环境和资源。
- **扩展性**：允许自定义 Rust 代码与 Python 交互，实现高性能组件。

## 用法

1. **安装 PyOxidizer**：
   - 确保安装 Rust（通过 rustup）。
   - 克隆仓库：`git clone https://github.com/indygreg/PyOxidizer.git`。
   - 构建：`cargo build --release`。

2. **创建配置文件**（`pyoxidizer.bzl` 或 TOML 文件）：
   ```
   [python-interpreter]
   name = "main"
   executable = "python3.dll"  # Windows 示例

   [[python-package]]
   name = "mypackage"
   install = ["mypackage"]

   [build]
   executable = "myapp.exe"
   ```

3. **构建应用**：
   - 运行 `pyoxidizer build` 生成可执行文件。
   - 对于自定义项目：使用 `cargo pyoxidizer` 集成到 Rust 项目中。

4. **运行和分发**：
   - 直接执行生成的二进制文件（如 `myapp.exe`）。
   - 测试：`./myapp` 或在目标平台验证无依赖运行。

更多细节参考项目文档和示例。