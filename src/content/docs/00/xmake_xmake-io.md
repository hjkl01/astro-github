---
title: xmake
---

# xmake

## Introduction

xmake is a cross-platform build utility based on Lua. It is lightweight, has no dependencies outside the standard library, and uses `xmake.lua` to maintain project builds with simple and readable syntax.

xmake can be used to directly build source code (like with Make or Ninja), or it can generate project source files like CMake or Meson. It also has a built-in package management system to help users integrate C/C++ dependencies.

## Features

- Simple and flexible configuration grammar
- Fast, dependency-free installation
- Easy compilation for all supported platforms
- Cross-compilation support with intelligent analysis of cross toolchain information
- Extremely fast parallel compilation support
- Supports C++ modules (new in C++20)
- Supports cross-platform C/C++ dependencies with built-in package manager
- Multi-language compilation support including mixed-language projects
- Rich plugin support with various project generators (e.g., Visual Studio, Makefiles, CMake, compile_commands.json)
- REPL interactive execution support
- Incremental compilation support with automatic analysis of header files
- Built-in toolchain management
- A large number of expansion modules
- Remote compilation support
- Distributed compilation support
- Local and remote build cache support

## Supported Platforms

- Windows (x86, x64, arm, arm64, arm64ec)
- macOS (i386, x86_64, arm64)
- Linux (i386, x86_64, arm, arm64, riscv, mips, 390x, sh4 ...)
- \*BSD (i386, x86_64)
- Android (x86, x86_64, armeabi, armeabi-v7a, arm64-v8a)
- iOS (armv7, armv7s, arm64, i386, x86_64)
- WatchOS (armv7k, i386)
- AppleTVOS (armv7, arm64, i386, x86_64)
- AppleXROS (arm64, x86_64)
- MSYS (i386, x86_64)
- MinGW (i386, x86_64, arm, arm64)
- Cygwin (i386, x86_64)
- Wasm (wasm32, wasm64)
- Haiku (i386, x86_64)
- Harmony (x86_64, armeabi-v7a, arm64-v8a)
- Cross (cross-toolchains ..)

## Installation

### With cURL

```bash
curl -fsSL https://xmake.io/shget.text | bash
```

### With Wget

```bash
wget https://xmake.io/shget.text -O - | bash
```

### With PowerShell

```powershell
irm https://xmake.io/psget.text | iex
```

For other installation methods, visit the [Installation Guide](https://xmake.io/guide/quick-start.html#installation).

## Basic Usage

### Create a Simple Project

Create a file named `xmake.lua` in your project root:

```lua
target("console")
    set_kind("binary")
    add_files("src/*.c")
```

This creates a new target `console` of kind `binary`, and adds all the files ending in `.c` in the `src` directory.

### Build a Project

```bash
xmake
```

### Run Target

```bash
xmake run console
```

### Debug Target

```bash
xmake run -d console
```

### Configure Platform

```bash
xmake f -p [windows|linux|macosx|android|iphoneos ..] -a [x86|arm64 ..] -m [debug|release]
xmake
```

### Menu Configuration

```bash
xmake f --menu
```

## Package Dependencies

Add dependencies in `xmake.lua`:

```lua
add_requires("tbox 1.6.*", "zlib", "libpng ~1.6")
```

This adds a requirement of tbox v1.6, zlib (any version), and libpng v1.6.

The official xmake package repository exists at: [xmake-repo](https://github.com/xmake-io/xmake-repo)

## Supported Languages

- C and C++
- Objective-C and Objective-C++
- Swift
- Assembly
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

## Examples

### Debug and Release Profiles

```lua
add_rules("mode.debug", "mode.release")

target("console")
    set_kind("binary")
    add_files("src/*.c")
    if is_mode("debug") then
        add_defines("DEBUG")
    end
```

### Automatic Integration of Dependent Packages

```lua
add_requires("tbox >1.6.1", "libuv master", "vcpkg::ffmpeg", "brew::pcre2/libpcre2-8")
add_requires("conan::openssl/1.1.1g", {alias = "openssl", optional = true, debug = true})

target("test")
    set_kind("binary")
    add_files("src/*.c")
    add_packages("tbox", "libuv", "vcpkg::ffmpeg", "brew::pcre2/libpcre2-8", "openssl")
```

### Qt QuickApp Program

```lua
target("test")
    add_rules("qt.quickapp")
    add_files("src/*.cpp")
    add_files("src/qml.qrc")
```

### Cuda Program

```lua
target("test")
    set_kind("binary")
    add_files("src/*.cu")
    add_cugencodes("native")
    add_cugencodes("compute_35")
```

For more examples and documentation, visit [xmake.io](https://xmake.io).
