---
title: cs2-dumper
---

# CS2 Dumper (a2x)

- 项目地址: [https://github.com/a2x/cs2-dumper](https://github.com/a2x/cs2-dumper)

## 项目概述
CS2 Dumper 是一款为 Counter‑Strike 2 开发的内存读取与结构导出工具。它通过对游戏进程的模式扫描与读取，自动收集并生成 `client.dll` 与 `engine.dll` 中的类与字段偏移量，帮助开发者快速获取与 CS2 相关的内存结构信息。

## 主要特性
| 特色 | 说明 |
|------|------|
| **自动化偏移量收集** | 通过内存扫描与符号解析，自动获取各类结构（如 `CBaseEntity`, `CBasePlayer`, `CBaseViewModel` 等）的字段偏移。 |
| **多文件导出** | 支持导出 JSON、C++ 头文件、Python 模块等多种格式，方便不同语言项目使用。 |
| **模块化设计** | 可单独使用 `offsets`, `scanner`, `memory` 等子模块，适配自定义项目。 |
| **跨平台** | 目前支持 Windows（使用 `ReadProcessMemory`），后续可扩展至 Linux。 |
| **可配置插件** | 通过配置文件可自定义扫描模式、输出路径及导出格式。 |

## 功能模块
- **memory**：封装进程内存读取、写入与权限管理。
- **scanner**：实现字节模式扫描、签名匹配与地址定位。
- **offsets**：根据已知符号与签名自动生成字段偏移信息。
- **exporter**：将偏移信息导出为多种可直接使用的文件格式。

## 使用方法

### 1. 克隆仓库
```bash
git clone https://github.com/a2x/cs2-dumper.git
cd cs2-dumper
```

### 2. 编译
```bash
# 需要 C++17 兼容编译器
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make
```

### 3. 运行
```bash
# 直接运行已编译的可执行文件
./cs2-dumper [options]

# 常用参数
--pid <pid>          指定目标进程的 PID
--output <path>      指定导出文件路径（默认 ./offsets.json）
--format <json|cpp>  指定导出格式
--verbose            打印详细调试信息
```

### 4. 典型示例
```bash
# 获取当前运行的 CS2 进程 PID
pid=$(pgrep cs2.exe)

# 生成 JSON 偏移文件
./cs2-dumper --pid $pid --output ./cs2_offsets.json

# 生成 C++ 头文件
./cs2-dumper --pid $pid --format cpp --output ./cs2_offsets.hpp
```

## 常见问题
- **无法找到进程**：请确认 `cs2.exe` 正在运行且拥有足够权限（管理员/以 `SYSTEM` 身份运行）。
- **偏移量不准确**：可能是由于游戏更新导致签名失效，需手动更新 `signatures.json`。
- **编译失败**：请检查 CMake 版本与编译器是否支持 C++17，Windows 下需安装 MSVC 或 MinGW。

## 贡献
欢迎提交 Issue 与 Pull Request，帮助完善签名库与导出格式。请参阅 `CONTRIBUTING.md`。

--- 

> 此文件用于 `src/content/docs/00/cs2-dumper_a2x.md`。  
> 如需进一步帮助，请查看项目根目录下的 `README.md` 或官方 Wiki。