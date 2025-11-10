---
title: Real Video Enhancer
---

# REAL-Video-Enhancer

## 功能介绍

REAL Video Enhancer 是一个重新设计和增强的视频处理工具，基于原始的 Rife ESRGAN App，为 Linux、Windows 和 MacOS 提供便捷的视频帧插值（interpolation）和上采样（upscaling）功能。它是 Flowframes 或 enhancr 等过时软件的替代品。

### 主要功能

- **帧插值（Interpolation）**：将视频帧率提高，例如从 24FPS 提升到 48FPS，使用 RIFE、GMFSS、IFRNet 等模型。
- **上采样（Upscaling）**：提高视频分辨率，例如从 1920x1080 提升到 3840x2160，使用 Real-ESRGAN、SPAN 等模型。
- **解压缩（Decompression）**：使用 DeH264 模型优化 H.264 视频。
- **降噪（Denoise）**：使用 DRUnet、DnCNN 等模型去除视频噪声。
- **场景变化检测**：保留锐利的过渡。
- **预览功能**：显示最新渲染帧。
- **多后端支持**：TensorRT（NVIDIA GPU）、PyTorch（CUDA/ROCm）、NCNN（Vulkan）。
- **跨平台**：支持 Windows 10/11、Ubuntu 22.04+、MacOS 14+。
- **Discord RPC**：集成 Discord 状态显示。

### 硬件要求

- **最低配置**：双核 x64 CPU、4GB VRAM（NCNN）、16GB RAM、1GB 存储。
- **推荐配置**：四核 x64 CPU、NVIDIA RTX GPU（8GB VRAM）、32GB RAM、16GB 存储。

## 用法

1. **下载和安装**：
   - 从 GitHub Releases 下载最新版本的可执行文件。
   - 支持 Windows、Linux（Flatpak）和 MacOS。

2. **运行应用**：
   - 启动 REAL-Video-Enhancer.exe 或相应平台的二进制文件。
   - 选择输入视频文件。

3. **配置处理选项**：
   - **插值**：选择模型（如 RIFE 4.22）、目标帧率。
   - **上采样**：选择模型（如 4x-SPANkendata）、目标分辨率。
   - **降噪/解压缩**：启用相应选项。
   - 选择后端（TensorRT、NCNN 等，根据硬件）。

4. **开始处理**：
   - 点击“开始”按钮。
   - 应用将处理视频并输出增强版。
   - 使用预览功能监控进度。

5. **高级选项**：
   - 调整场景检测阈值。
   - 自定义输出路径和格式。

### 注意事项

- TensorRT 后端首次运行时会进行优化，可能需要时间。
- 确保 GPU 驱动和 Vulkan 支持（NCNN）。
- 对于 ROCm，参考官方 Wiki 解决常见问题。
- 如果遇到内存错误，尝试降低分辨率或使用 Colab Notebook。

更多详情请参考 [GitHub 仓库](https://github.com/TNTwise/REAL-Video-Enhancer)。
