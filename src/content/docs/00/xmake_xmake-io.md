
---
title: xmake
---

# xmake 项目说明

> **项目地址**: <https://github.com/xmake-io/xmake>

## 项目简介
xmake 是一款基于 Lua 的现代化、跨平台 C/C++/C/Objective-C/Swift 等语言构建工具，旨在使项目编译与管理变得简单、高效。它拥有**轻量、易学、易扩展**的特性，适合个人开发者、项目雏形以及企业级生产环境。

## 主要特性
- ⭐ **脚本式配置**  
  使用 `xmake.lua` 以 Lua 语言编写构建脚本，配置更加直观、可读性好。
- 🚀 **跨平台构建**  
  原生支持 Windows、Linux、macOS、Android、iOS 等主流平台，完全依赖平台无关的编译流程。
- 🔄 **插件化与扩展**  
  通过 `xmake` 生态插件（如 `gitversion`, `sc", `systeminfo` 等）快速加入功能，支持自定义插件。
- 🔧 **减少繁琐的 Makefile/ CMake**  
  自动生成 GCC、Clang、MSVC 的编译器命令，避免繁杂的工具链配置。
- 📦 **依赖管理**  
  内置包管理 (`xmake deps`) 支持本地仓库、HTTP、Git、SVN 等多种来源。
- 📦️ **动态链接库与静态库**  
  一键切换两种链接类型，支持多目标构建。
- ⚙️ **命令行工具**  
  `xmake`, `xmake build`, `xmake xrepo`, `xmake deps` 等简短命令让操作一次即懂。
- 🔗 **外部 SDK 与工具链集成**  
  支持快速对接 iOS/Android NDK, VS, Xcode, Visual Studio Code 等 IDE。

## 核心功能
| 功能 | 说明 |
|------|------|
| **快速生成基本项目** | `xmake create -type=cpp -d myproj` |
| **编译调试** | `xmake` (编译) / `xmake run` (直接运行) / `xmake consult` (交互式调试) |
| **多配置** | `xmake config -m release` 或 `xmake config -m debug` |
| **交叉编译** | 配置 toolchain 并 `xmake config -t armv7-linux-gnueabihf` |
| **插件系统** | 通过 `xmake repo add` 添加插件仓库；`xmake plugin update` 安装。 |
| **依赖自动拉取** | `xmake deps` 下载、编译并链接第三方库。 |
| **静态分析** | `xmake linter` 与 `xmake todo` 进行代码质量检查。 |
| **生成 IDE 项目文件** | `xmake project --ide=vs` 或 `--ide=code` |

## 用法示例

```bash
# 基本编译
xmake

# 编译并运行
xmake run myapp

# 设置调试模式
xmake config -m debug
xmake build myapp -v

# 交叉编译到 ARM
xmake config -t armv7-linux-gnueabihf
xmake build myapp

# 添加并使用插件
xmake repo add xmake-plugins https://github.com/xmake-io/xmake-repo
xmake plugin update
xmake plugin install gitversion
```

> 详情请参阅官方文档: <https://xmake.io/>  

---