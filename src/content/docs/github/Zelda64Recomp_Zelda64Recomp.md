
---
title: Zelda64Recomp
---

# Zelda64Recomp 项目

## 项目地址
[https://github.com/Zelda64Recomp/Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp)

## 主要特性
Zelda64Recomp 是一个开源项目，专注于《塞尔达传说：时之笛》（The Legend of Zelda: Ocarina of Time，简称 OoT）N64 版本的逆向工程和重编译工具。其核心是通过反汇编和重构源代码，将原始的 N64 二进制文件转换为可编译的 C/C++ 代码，从而实现游戏的现代移植和修改。主要特性包括：
- **精确重编译**：使用 LLVM 框架实现从汇编到高级语言的转换，确保生成的代码与原版游戏行为完全一致。
- **模块化架构**：项目将游戏拆分为多个模块（如场景、实体、音频系统），便于开发者独立修改和扩展。
- **跨平台支持**：生成的代码可编译为 PC、Linux、macOS 等平台，支持高分辨率渲染和输入自定义。
- **工具集成**：内置反汇编器、符号表生成和调试工具，支持与 Decomp 项目（如 n64decomp）兼容。
- **社区驱动**：提供资产提取工具，用于从 ROM 中导出模型、纹理和声音，便于 modding 和重制。

## 主要功能
- **反编译与重构**：从 OoT 的 N64 ROM 文件中提取并重构源代码，支持特定函数或整个游戏的处理。
- **编译与构建**：将重构代码编译成可执行文件，支持自定义 Makefile 和 CMake 配置，实现原版游戏的忠实再现或增强版（如 60FPS、宽屏支持）。
- **调试与测试**：集成单元测试框架和 ROM 比较工具，确保修改后的游戏与原版无差异。
- **Mod 支持**：允许开发者注入自定义代码，例如新关卡、物品或 AI 行为。
- **资产管理**：功能包括纹理替换、模型导入和音频重采样，支持与 Unity 或 Godot 等引擎集成用于原型开发。

## 用法
1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/Zelda64Recomp/Zelda64Recomp.git`
   - 安装依赖：需要 LLVM/Clang（版本 10+）、CMake 和 Python 3。针对 Windows 用户，可使用 vcpkg；Linux 用户通过包管理器安装。
   - 获取 OoT ROM：项目要求合法的 N64 ROM 文件（例如 JP/US/EU 版本），放置在 `inputs/` 目录。

2. **基本编译流程**：
   - 配置：运行 `cmake -B build -S .` 生成构建文件。
   - 反编译：使用 `python tools/disassemble.py --rom oot.ntsc.us.z64` 处理 ROM，生成汇编和符号。
   - 重构：运行 `make` 或 `ninja` 在 build 目录编译，输出可执行文件（如 `zelda-oot`）。
   - 测试：执行 `./zelda-oot` 运行游戏，或使用 `diff` 工具比较输出与原版 ROM。

3. **高级用法**：
   - 修改代码：在 `src/` 目录编辑 C 文件（如 `src/game/main.c`），然后重新构建。
   - Modding：使用 `tools/asset_extractor.py` 导出资源，修改后通过 `include/` 路径重新导入。
   - 跨平台构建：指定目标平台，例如 `cmake -DCMAKE_TOOLCHAIN_FILE=toolchains/mingw.cmake` 用于 Windows。
   - 文档参考：查看 `README.md` 和 `docs/` 目录中的指南，常见问题在 Issues 中讨论。

注意：项目处于开发中，确保 ROM 来源合法。贡献者可通过 Pull Request 提交代码。