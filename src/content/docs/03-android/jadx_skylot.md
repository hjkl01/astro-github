
---
title: jadx
---

# Jadx 项目

**GitHub 项目地址:** [https://github.com/skylot/jadx](https://github.com/skylot/jadx)

## 主要特性
Jadx 是一个开源的 Android DEX 和 APK 反编译工具，主要用于将 Android 应用程序的字节码转换为可读的 Java 源代码。它支持多种反编译模式，提供高效的代码分析功能。核心特性包括：
- **高精度反编译**：准确地将 DEX 文件（Dalvik Executable）转换为 Java 代码，支持资源文件（如 XML、图片）的提取。
- **图形化界面**：内置 GUI（Graphical User Interface），允许用户通过可视化界面浏览和编辑反编译后的代码。
- **命令行支持**：提供 CLI（Command Line Interface）模式，便于脚本化和批量处理。
- **代码导航**：支持代码搜索、跳转定义、调用层次结构分析等 IDE-like 功能。
- **多平台兼容**：可在 Windows、macOS 和 Linux 上运行，支持处理 APK、DEX、ARSC 等文件格式。
- **插件扩展**：可通过插件增强功能，如语法高亮和自定义反编译规则。
- **开源免费**：基于 Apache 2.0 许可，完全开源，无需付费。

## 主要功能
- **反编译 APK/DEX**：将 Android 应用包或字节码文件转换为 Java 源代码和资源文件，帮助开发者分析应用逻辑、调试或逆向工程。
- **资源解包**：提取 APK 中的 manifest、布局、字符串等资源，支持 ARSC 二进制资源文件的转换。
- **代码优化**：自动重构代码，处理混淆（如 ProGuard），并生成接近原生的 Java 代码。
- **批量处理**：支持一次性反编译多个文件或目录。
- **导出与集成**：可导出为 JAR 或直接集成到构建工具中，用于静态分析或安全审计。
- **调试支持**：提供 Smali 代码查看和基本调试功能，适用于逆向工程场景。

## 用法
### 1. 安装
- 从 GitHub Releases 下载最新版本的预编译二进制文件（jadx-gui 或 jadx CLI）。
- 确保安装 Java 8 或更高版本（推荐 OpenJDK）。
- 对于 macOS/Linux，可通过 Homebrew 或包管理器安装：`brew install jadx`。

### 2. 使用 GUI（图形界面）
- 运行 `jadx-gui` 命令或双击可执行文件启动界面。
- 点击 "File" > "Open File" 选择 APK 或 DEX 文件。
- 界面将显示反编译后的代码树状结构，支持搜索、导航和导出（File > Save All）。
- 示例：加载一个 APK 文件后，可在左侧面板浏览类结构，右侧查看源代码。

### 3. 使用 CLI（命令行）
- 基本反编译：`jadx -d output_dir input.apk`（将 APK 反编译到 output_dir 目录）。
- 指定输出格式：`jadx --deobf input.dex`（启用去混淆）。
- 提取资源：`jadx -r input.apk`（同时反编译代码和资源）。
- 高级选项：使用 `--help` 查看完整参数，如 `--show-bad-code` 显示不可恢复的代码片段。
- 批量处理：`jadx -d out/ dir/*.apk` 处理目录下所有 APK。

### 注意事项
- 对于大型 APK，反编译可能耗时较长，建议分配足够内存（通过 `-Xmx` JVM 参数）。
- 项目文档详见 GitHub Wiki，提供更多高级用法和故障排除。