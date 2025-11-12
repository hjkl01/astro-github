---
title: repository
---

# Rerun - 多模态数据可视化工具

Rerun 是一个用于可视化多模态数据流的免费、快速、易用且易于集成的工具，使用 Rust 构建。它专门用于建模、摄取、存储、查询和查看机器人风格的数据。

## 核心功能

### 多模态数据支持

- 支持 2D/3D 数据、图像、张量、点云、文本等多种数据类型
- 时间感知的数据堆栈和可视化
- 实时数据流处理和记录

### 跨平台 SDK

提供多种编程语言的 SDK：

- **Python**: `pip install rerun-sdk`
- **Rust**: `cargo add rerun`
- **C++**: 完整的 C++ API 支持

### 可视化功能

- 实时 3D 点云可视化
- 图像和深度数据展示
- 时间序列数据图表
- 传感器数据融合显示

## 应用场景

### 机器人技术

- 机器人调试和监控
- 传感器数据可视化（RGB 相机、激光雷达、深度图像）
- 路径规划和导航可视化
- 物体检测和分割结果展示

### 计算机视觉

- 计算机视觉算法调试
- 图像处理流程可视化
- 模型训练过程监控
- 数据集创建和管理

### 其他领域

- 空间和具身 AI
- 生成媒体
- 工业处理
- 仿真
- 安全监控
- 健康医疗

## 快速开始

### Python 示例

```python
import rerun as rr  # pip install rerun-sdk

rr.init("rerun_example_app")
rr.spawn()  # 生成子进程查看器并连接

# 在"frame"时间线上设置时间
rr.set_time("frame", sequence=42)

# 记录彩色 3D 点到指定路径
rr.log("path/to/points", rr.Points3D(positions, colors=colors))
```

### 安装查看器

```bash
# Python SDK 包含查看器
pip install rerun-sdk

# 或单独安装 Rust CLI
cargo install rerun-cli --locked --features nasm
```

## 主要特性

### 实时可视化

- 支持实时数据流传输
- 网络流式传输到远程查看器
- 本地文件记录和回放

### 数据查询

- 提供 DataFrame API 进行数据查询
- 支持从记录中提取干净的数据集
- 便于创建训练和评估数据

### 开源模式

- 采用开源核心模式
- 核心功能完全开源免费
- 提供商业数据平台（针对团队需求）

## 项目状态

- **活跃开发中**：API 仍在演进，可能会有破坏性变更
- **GitHub Stars**: 9.5k+
- **支持语言**: Rust (83.5%), Python (10.2%), C++ (3.8%)
- **许可证**: Apache-2.0, MIT

## 文档和资源

- 📚 [高级文档](https://rerun.io/docs)
- ⏃ [可记录类型](https://www.rerun.io/docs/reference/types)
- ⚙️ [示例代码](https://rerun.io/examples)
- 🌊 [C++ API 文档](https://ref.rerun.io/docs/cpp)
- 🐍 [Python API 文档](https://ref.rerun.io/docs/python)
- 🦀 [Rust API 文档](https://docs.rs/rerun/)

## 使用限制

目前的一些限制：

- 实体过多时查看器性能下降
- 暂不支持透明度
- 可视化数据必须适合内存
- 大型点云（数百万点）可能较慢

## 总结

Rerun 是一个强大的多模态数据可视化工具，特别适合需要处理复杂传感器数据的机器人、计算机视觉和 AI 项目。它提供了直观的界面来理解和调试复杂的多数据流系统，是开发和研究人员的有力工具。
