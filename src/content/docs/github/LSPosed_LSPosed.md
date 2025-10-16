
---
title: LSPosed
---

# LSPosed 项目

**GitHub 项目地址:** [https://github.com/LSPosed/LSPosed](https://github.com/LSPosed/LSPosed)

## 主要特性
LSPosed 是一个开源的 Android Xposed 框架实现，专为现代 Android 系统设计。它基于 Zygisk（Magisk 的一个模块）运行，支持 Android 8.0 及以上版本。主要特性包括：
- **模块化 Hook 机制**：允许开发者通过 Xposed API 注入和修改应用程序行为，而不需 root 权限修改 APK。
- **Zygisk 集成**：无缝集成 Magisk 的 Zygisk 功能，提供更稳定的运行环境，避免传统 Xposed 的兼容性问题。
- **模块管理**：内置模块加载器，支持动态启用/禁用模块，并提供黑白名单功能以控制应用范围。
- **高兼容性**：优化了对 Android 12+ 版本的支持，包括 Scoped Storage 和 ART 运行时改进。
- **开源与社区驱动**：基于 Apache 2.0 许可，社区活跃，提供持续更新和 bug 修复。

## 主要功能
- **应用 Hook**：拦截和修改应用运行时行为，例如自定义 UI、注入代码或绕过限制。
- **模块支持**：兼容大多数 Xposed 模块，如 EdXposed 或 Riru 生态中的工具，用于广告屏蔽、隐私保护或性能优化。
- **安全沙箱**：运行在 Zygisk 进程中，减少对系统的影响，提高安全性。
- **日志与调试**：提供详细的日志记录和调试工具，帮助开发者诊断问题。
- **无痕安装**：不修改系统分区，支持 OTA 更新。

## 用法
1. **前提条件**：
   - 设备需已 root 并安装 Magisk v24.0+。
   - 启用 Zygisk（在 Magisk Manager 中设置）。

2. **安装步骤**：
   - 从 GitHub Releases 下载最新 LSPosed Zygisk 模块（.zip 文件）。
   - 在 Magisk Manager 中安装该模块，重启设备。
   - 安装 LSPosed Manager APK（从 Releases 下载），授予必要权限（如 Accessibility 服务）。

3. **使用流程**：
   - 打开 LSPosed Manager，浏览并安装 Xposed 模块（从仓库或 APK 安装）。
   - 在“模块”页面启用所需模块。
   - 在“范围”页面选择要应用模块的目标应用（支持全局或特定 app）。
   - 重启设备或目标应用以生效。
   - 通过 Manager 查看模块状态、日志，并管理更新。

4. **注意事项**：
   - 某些模块可能需额外配置；备份数据以防不兼容。
   - 如遇问题，检查 Magisk 日志或社区论坛（XDA 或 GitHub Issues）。
   - 不推荐用于生产环境，仅限开发或个性化使用。