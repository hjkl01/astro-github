
---
title: linuxdeploy
---

# linuxdeploy 项目

**GitHub 项目地址：** [https://github.com/meefik/linuxdeploy](https://github.com/meefik/linuxdeploy)

## 主要特性
- **跨平台支持**：linuxdeploy 是一个工具，用于将 Linux 应用程序打包成可移植的 AppImage、Flatpak 或 Snap 格式，支持在不同 Linux 发行版之间无缝运行，而无需依赖特定系统的包管理器。
- **自动化部署**：它自动处理应用程序的依赖项、库文件和资源打包，确保生成的包自包含且独立运行。
- **多格式输出**：支持生成 AppImage（单文件可执行包）、Flatpak（沙箱化应用）和 Snap（类似容器化的包），便于分发和安装。
- **插件系统**：提供插件扩展功能，如处理 Qt、GTK、Python 等特定框架的依赖，以及桌面集成、图标和元数据管理。
- **轻量级**：基于简单脚本实现，无需复杂构建环境，适合开发者快速部署应用。

## 主要功能
- **依赖解析**：自动检测并捆绑应用程序所需的动态库、字体和配置文件。
- **沙箱与隔离**：在 Flatpak 和 Snap 模式下，提供应用沙箱化，确保安全性和隔离。
- **元数据管理**：自动生成桌面文件、图标和 MIME 类型支持，实现与系统的集成。
- **自定义配置**：支持通过 YAML 或命令行选项自定义打包过程，包括排除特定文件或添加额外资源。
- **测试与验证**：内置工具验证生成的包是否完整，并在不同环境中运行。

## 用法
1. **安装**：从 GitHub Releases 下载最新二进制文件，或通过包管理器安装（如 `apt install linuxdeploy`）。
2. **基本命令**：
   - 生成 AppImage：`linuxdeploy --appdir AppDir/ -e executable -d desktopfile.desktop -i icon.png --output appimage`
   - 生成 Flatpak：`linuxdeploy --appdir AppDir/ --output flatpak --app-id com.example.app`
   - 生成 Snap：`linuxdeploy --appdir AppDir/ --output snap`
3. **准备 AppDir**：创建一个 `AppDir/` 目录，将应用程序二进制文件、库和资源放入 `usr/bin/`、`usr/lib/` 等子目录。
4. **运行打包**：在 AppDir 目录下执行命令，工具会自动处理其余部分。
5. **高级用法**：使用 `--plugin qt` 处理 Qt 应用，或 `--create-desktop-integration` 添加系统集成。详细文档见项目 README。