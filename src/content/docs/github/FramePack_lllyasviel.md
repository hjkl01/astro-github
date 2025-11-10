---
title: FramePack
---


# FramePack (lllyasviel)

> GitHub 项目地址: <https://github.com/lllyasviel/FramePack>

## 简介
FramePack 是一个轻量级的工具，专为将视频帧打包成单张大图（或拆分回多张图）而设计。它支持多种视频/图像格式，并提供了命令行与 Python API 两种方式，方便在数据预处理、视觉模型训练等场景中快速完成帧打包与解包。

## 主要特性
- **多格式支持**：mp4、avi、gif、webp、png、jpg 等。
- **灵活的打包方式**：2D 网格、3D 立方体、按行或按列打包。
- **可自定义尺寸**：支持指定输出图像宽/高，或自动按比例缩放。
- **批量处理**：一次性对目录下所有视频进行打包或解包。
- **高效内存管理**：按帧流式读取，避免一次性加载全部帧导致内存爆炸。
- **跨平台**：Python 3.7+，可在 Windows/Mac/Linux 使用。

## 功能概述
| 功能 | 命令 | 说明 |
|------|------|------|
| `pack` | `framepack pack input_video output_image` | 将视频帧按网格打包成单张图 |
| `unpack` | `framepack unpack input_image output_folder` | 将打包图拆分回单帧图像 |
| `pack` (CLI 参数) | `framepack pack -i in.mp4 -o out.png --rows 8 --cols 8` | 指定打包行列数 |
| `pack` (Python API) | `framepack.pack('in.mp4', 'out.png', rows=8, cols=8)` | 直接在代码中调用 |

## 用法示例

### 1. 安装

```bash
pip install framepack
```

### 2. 命令行打包

```bash
# 将 input.mp4 打包成 8x8 的网格图
framepack pack -i input.mp4 -o packed.png --rows 8 --cols 8
```

### 3. 命令行解包

```bash
# 将 packed.png 拆分回单帧
framepack unpack -i packed.png -o frames/
```

### 4. Python API

```python
import framepack

# 打包
framepack.pack(
    src='input.mp4',
    dst='packed.png',
    rows=8,
    cols=8,
    resize=(256, 256)  # 可选，按尺寸缩放帧
)

# 解包
framepack.unpack(
    src='packed.png',
    dst='frames_folder',
    rows=8,
    cols=8
)
```

## 适用场景
- **数据集构建**：将大量视频帧打包成一张图，方便在训练时一次性读取。
- **视觉模型推理**：某些模型（如 ConvLSTM）需要将连贯帧一次性送入，可以先打包再推理。
- **可视化**：快速生成视频帧的网格预览，便于调试与展示。

---
> 以上内容仅为项目主要特性与使用方法的简要概述，更多细节请参阅官方文档与源代码。
