
---
title: buildozer
---

# Buildozer 项目描述

## 项目地址
[https://github.com/kivy/buildozer](https://github.com/kivy/buildozer)

## 主要特性
Buildozer 是一个用于 Python/Kivy 应用的自动化构建工具，主要针对移动平台（如 Android 和 iOS）的打包。它具有以下核心特性：
- **自动化打包**：无需手动配置复杂的构建环境，即可将 Python 应用打包成 APK（Android）或 IPA（iOS）文件。
- **跨平台支持**：主要支持 Android 和 iOS，支持 Kivy 框架的应用打包，也可扩展到其他 Python 项目。
- **依赖管理**：自动下载和集成 Python 依赖库，支持 requirements.txt 文件定义依赖。
- **配置简单**：使用单一的 `buildozer.spec` 配置文件管理应用标题、包名、图标、权限等设置。
- **多架构支持**：支持 ARM 和 x86 等不同设备架构的构建。
- **开源免费**：基于 Python 开发，MIT 许可，社区活跃。

## 主要功能
- **应用打包**：将 Python 脚本和资源文件转换为可安装的移动应用包。
- **环境初始化**：自动安装必要的工具链，如 Android SDK、NDK 等。
- **调试与优化**：支持 release 和 debug 模式构建，提供日志输出和错误诊断。
- **自定义扩展**：允许用户通过 spec 文件自定义构建规则、添加原生代码或插件。
- **虚拟环境集成**：兼容 venv 或其他 Python 环境，确保依赖隔离。

## 用法
1. **安装 Buildozer**：
   - 确保已安装 Python 3 和 Kivy。
   - 使用 pip 安装：`pip install buildozer`。
   - 对于 Android 构建，还需安装 Java JDK、Android SDK 等（Buildozer 会引导初始化）。

2. **初始化项目**：
   - 在项目根目录运行：`buildozer init`，这会生成 `buildozer.spec` 配置文件。
   - 编辑 `buildozer.spec`：设置应用名称（title）、包名（package.name）、版本、依赖（requirements）、权限（android.permissions）等。

3. **构建应用**：
   - 对于 Android：运行 `buildozer android debug`（调试版）或 `buildozer android release`（发布版）。首次运行会下载依赖，可能需数小时。
   - 对于 iOS：运行 `buildozer ios debug`（需 macOS 环境和 Xcode）。
   - 输出文件位于 `bin/` 目录下，例如 `myapp-1.0-debug.apk`。

4. **常见命令**：
   - `buildozer -v android debug`：详细日志构建。
   - `buildozer android clean`：清理构建缓存。
   - `buildozer android update`：更新依赖。

注意：Android 构建推荐在 Linux 或 macOS 上进行；iOS 仅限 macOS。遇到问题时，检查 spec 文件和日志输出。