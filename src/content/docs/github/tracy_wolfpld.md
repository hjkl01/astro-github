---
title: tracy
---

# Tracy Profiler

Tracy 是一个实时、纳秒分辨率、远程遥测、混合帧和采样分析器，专为游戏和其他应用程序设计。它支持对 CPU（直接支持 C、C++、Lua、Python 和 Fortran 集成，同时有第三方绑定如 Rust、Zig、C# 等）、GPU（支持 OpenGL、Vulkan、Direct3D 11/12、Metal、OpenCL、CUDA 等主要图形 API）、内存分配、锁、上下文切换等进行分析，并能自动将截图归属于捕获的帧。

## 功能特性

- **实时分析**：提供纳秒级分辨率的性能数据。
- **混合模式**：结合帧分析和采样分析。
- **多平台支持**：适用于各种操作系统和硬件。
- **远程遥测**：允许远程监控应用程序性能。
- **丰富的数据类型**：除了 CPU 和 GPU，还支持内存、锁等。
- **可视化界面**：提供直观的分析界面，包括时间线、火焰图等。

## 用法

1. **集成到项目**：将 Tracy 库添加到您的 C++ 项目中。可以通过 CMake 或 Meson 构建系统进行配置。
2. **标记代码**：使用 Tracy 提供的宏（如 `ZoneScoped`）标记需要分析的代码区域。
3. **运行应用程序**：启动应用程序，Tracy 会收集性能数据。
4. **查看分析结果**：使用 Tracy Profiler 工具打开捕获的数据文件，查看详细的性能分析报告。

更多详细信息，请参考 [官方文档](https://github.com/wolfpld/tracy/releases/latest/download/tracy.pdf) 和 [交互演示](https://tracy.nereid.pl/)。
