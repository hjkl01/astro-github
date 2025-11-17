---
title: xmake
---

## 功能介绍

xmake 是一个基于 Lua 脚本语言的跨平台构建工具。它非常轻量级，除了标准库外没有其他依赖。使用 `xmake.lua` 文件来维护项目构建，具有简单易读的语法。

xmake 可以直接构建源代码（类似于 Make 或 Ninja），也可以生成项目文件（如 CMake 或 Meson）。它还内置了包管理系统，帮助用户集成 C/C++ 依赖。

xmake 的核心公式可以表示为：

```
Xmake = 构建后端 + 项目生成器 + 包管理器 + [远程|分布式] 构建 + 缓存
```

虽然不够精确，但可以这样理解：

```
Xmake ≈ Make/Ninja + CMake/Meson + Vcpkg/Conan + distcc + ccache/sccache
```

## 主要特性

- 简单而灵活的配置语法
- 快速、无依赖的安装
- 支持大多数平台的轻松编译
- 支持交叉编译，并智能分析交叉工具链信息
- 极快的并行编译支持
- 支持 C++ 模块（C++20 新特性）
- 内置跨平台 C/C++ 依赖包管理器
- 支持多语言编译，包括混合语言项目
- 丰富的插件支持，各种项目生成器（Visual Studio、Makefiles、CMake、`compile_commands.json`）
- REPL 交互式执行支持
- 增量编译支持，自动分析头文件依赖
- 内置工具链管理
- 大量扩展模块
- 远程编译支持
- 分布式编译支持
- 本地和远程构建缓存支持

## 支持的平台

- Windows (x86, x64, arm, arm64, arm64ec)
- macOS (i386, x86_64, arm64)
- Linux (i386, x86_64, arm, arm64, riscv, mips, 390x, sh4 ...)
- \*BSD (i386, x86_64)
- Android (x86, x86_64, armeabi, armeabi-v7a, arm64-v8a)
- iOS (armv7, armv7s, arm64, i386, x86_64)
- 其他平台如 WatchOS、AppleTVOS、AppleXROS、MSYS、MinGW、Cygwin、Wasm、Haiku、Harmony 等

## 支持的工具链

xmake 支持大量工具链，包括但不限于：xcode、msvc、clang-cl、yasm、clang、go、dlang、dmd、ldc、gdc、gfortran、zig、sdcc、cuda、ndk、rust、swift、llvm、cross、nasm、gcc、mingw、gnu-rm、envs、fasm、tinycc、emcc、icc、ifort、ifx、muslcc、fpc、wasi、nim、circle、armcc、armclang、c51、icx、dpcpp、masm32、iverilog、verilator、cosmocc、hdk、ti-c2000、ti-c6000、iararm、kotlin-native。

## 支持的语言

- C 和 C++
- Objective-C 和 Objective-C++
- Swift
- 汇编
- Golang
- Rust
- Dlang
- Fortran
- Cuda
- Zig
- Vala
- Pascal
- Nim
- Verilog
- FASM
- NASM
- YASM
- MASM32
- Cppfront
- Kotlin

## 安装方法

### 使用 cURL

```bash
curl -fsSL https://xmake.io/shget.text | bash
```

### 使用 Wget

```bash
wget https://xmake.io/shget.text -O - | bash
```

### 使用 PowerShell

```powershell
irm https://xmake.io/psget.text | iex
```

其他安装方法请参考[安装指南](https://xmake.io/guide/quick-start.html#installation)。

## 基本用法

### 创建简单项目

在 `xmake.lua` 文件中定义目标：

```lua
target("console")
    set_kind("binary")
    add_files("src/*.c")
```

### 构建项目

```bash
xmake
```

### 运行目标

```bash
xmake run console
```

### 调试目标

```bash
xmake run -d console
```

### 配置平台

```bash
xmake f -p [windows|linux|macosx|android|iphoneos ...] -a [x86|arm64 ...] -m [debug|release]
xmake
```

### 菜单配置

```bash
xmake f --menu
```

## 包管理

xmake 内置了强大的包管理系统，可以自动下载和构建依赖。

### 添加依赖

```lua
add_requires("tbox 1.6.*", "zlib", "libpng ~1.6")
```

### 在目标中使用包

```lua
target("test")
    set_kind("binary")
    add_files("src/*.c")
    add_packages("tbox", "zlib", "libpng")
```

### 支持的包仓库

- 官方包仓库 [xmake-repo](https://github.com/xmake-io/xmake-repo)
- 第三方仓库如 Conan、Conda、Vcpkg、Homebrew 等

## 项目类型支持

xmake 支持多种项目类型：

- 静态库
- 共享库
- 控制台/CLI 应用程序
- CUDA 程序
- Qt 应用程序
- WDK 驱动程序 (umdf/kmdf/wdm)
- WinSDK 应用程序
- MFC 应用程序
- Darwin 应用程序（支持 metal）
- 框架和包 (Darwin)
- SWIG 模块
- LuaRocks 模块
- Protobuf 程序
- Lex/Yacc 程序
- Linux 内核模块

## 示例

### 调试和发布配置

```lua
add_rules("mode.debug", "mode.release")

target("console")
    set_kind("binary")
    add_files("src/*.c")
    if is_mode("debug") then
        add_defines("DEBUG")
    end
```

### 自定义脚本

```lua
target("test")
    set_kind("binary")
    add_files("src/*.c")
    after_build(function (target)
        print("hello: %s", target:name())
        os.exec("echo %s", target:targetfile())
    end)
```

### Qt QuickApp 程序

```lua
target("test")
    add_rules("qt.quickapp")
    add_files("src/*.cpp")
    add_files("src/qml.qrc")
```

### CUDA 程序

```lua
target("test")
    set_kind("binary")
    add_files("src/*.cu")
    add_cugencodes("native")
    add_cugencodes("compute_35")
```

更多示例请参考[官方文档](https://xmake.io/guide/)。
