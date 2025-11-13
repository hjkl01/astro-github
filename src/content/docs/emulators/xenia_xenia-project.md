---
title: xenia
---

# Xenia 项目

## 项目地址
[https://github.com/xenia-project/xenia](https://github.com/xenia-project/xenia)

## 主要特性
Xenia 是一个开源的 Xbox 360 模拟器项目，旨在为现代 PC 平台（如 Windows、Linux 和 macOS）提供高保真度的 Xbox 360 游戏模拟。主要特性包括：
- **高兼容性**：支持大量 Xbox 360 游戏标题，包括热门游戏如《光环》系列、《使命召唤》和《GTA V》等，许多游戏可实现完整或近完整运行。
- **精确仿真**：模拟 Xbox 360 的 PowerPC CPU、Xenos GPU 和 Xenon 内核，提供接近原机的图形和声音效果，支持 4K 分辨率和 HDR。
- **多平台支持**：跨平台兼容，Windows 为主要平台，也支持 Vulkan、DirectX 12 等现代图形 API 以提升性能。
- **模块化设计**：开源代码允许开发者贡献和自定义，支持调试工具和性能分析。
- **社区驱动**：活跃的社区维护游戏兼容性列表（Gamelist），定期更新以修复 bug 和添加新功能。

## 功能
- **游戏运行**：加载并执行 Xbox 360 游戏镜像（ISO 或提取文件），模拟主机环境，包括控制器输入、保存状态和网络功能（部分支持）。
- **图形和音频**：使用 Vulkan 或 D3D12 渲染器，提供抗锯齿、纹理过滤等增强选项；音频通过 XAudio2 或类似 API 处理，支持立体声和环绕声。
- **调试与工具**：内置调试器、日志记录和性能监控，帮助开发者测试游戏兼容性。
- **输入支持**：兼容 Xbox 控制器、键盘和游戏手柄，支持自定义映射。
- **扩展性**：支持模组（mods）和自定义着色器，用于改进视觉效果或修复特定游戏问题。

## 用法
1. **下载与安装**：
   - 从 GitHub Releases 页面下载最新预编译版本（推荐 Canary 构建以获取最新修复）。
   - 对于 Windows，确保安装 Visual C++ Redistributable；Linux 用户需安装 Vulkan 驱动和依赖库。

2. **获取游戏文件**：
   - 合法获取 Xbox 360 游戏的 ISO 或 GOD 文件（需拥有原盘）。项目不提供游戏 ROM。

3. **运行游戏**：
   - 启动 Xenia 可执行文件（xenia-canary.exe）。
   - 使用命令行或 GUI（如果可用）加载游戏文件，例如：`xenia-canary.exe path/to/game.iso`。
   - 配置设置：通过 config.toml 文件调整图形 API、CPU 优化和输入映射。示例配置可在仓库中找到。

4. **故障排除**：
   - 检查兼容性列表（wiki 或 gamelist.txt）确认游戏支持。
   - 启用日志（-log_level debug）诊断问题。
   - 加入 Discord 社区或 GitHub Issues 寻求帮助。

注意：Xenia 仅用于合法拥有的游戏备份，使用时遵守当地法律法规。项目处于开发中，某些游戏可能有 bug 或不稳定。