---
title: LTX-Video
---

# LTX-Video

Official repository for LTX-Video

项目地址: https://github.com/Lightricks/LTX-Video

## 简介

LTX-Video 是第一个 DiT-based 视频生成模型，包含现代视频生成的所有核心能力：同步音频和视频、高保真、多性能模式、生产就绪输出、API 访问和开放访问。它可以生成高达 50 FPS 的视频，在本地 4K 分辨率下一次性同步音频。模型在大型多样视频数据集上训练，可以生成高分辨率视频，具有真实和多样化的内容。

模型支持图像到视频、多关键帧条件、基于关键帧的动画、视频扩展（向前和向后）、视频到视频转换，以及这些功能的任何组合。

## 主要特性

- **文本到视频**：高质量文本到视频生成，无需太多提示工程。
- **图像到视频**：从图像生成视频，支持多种条件。
- **视频扩展**：向前或向后扩展现有视频。
- **多关键帧条件**：使用多个图像或视频段生成视频。
- **音频同步**：生成同步音频和视频。
- **高分辨率**：支持 4K 分辨率和高达 50 FPS。
- **多种模型**：13B 和 2B 模型变体，支持蒸馏版本以提高速度。
- **控制模型**：深度、姿势、Canny 控制等。
- **集成**：ComfyUI、Diffusers 支持。

## 主要功能

- **在线推理**：通过 LTX-Studio、Fal.ai、Replicate 等平台。
- **本地运行**：使用 Python 脚本或作为库。
- **ComfyUI 集成**：推荐用于高质量生成。
- **Diffusers 集成**：使用 Hugging Face Diffusers。
- **训练**：开放源代码训练仓库用于微调。
- **社区贡献**：ComfyUI-LTXTricks、LTX-VideoQ8、TeaCache 等。

## 用法

### 安装

```bash
git clone https://github.com/Lightricks/LTX-Video.git
cd LTX-Video
python -m venv env
source env/bin/activate
python -m pip install -e .[inference]
```

### 推理

#### 图像到视频生成

```bash
python inference.py --prompt "PROMPT" --conditioning_media_paths IMAGE_PATH --conditioning_start_frames 0 --height HEIGHT --width WIDTH --num_frames NUM_FRAMES --seed SEED --pipeline_config configs/ltxv-13b-0.9.8-distilled.yaml
```

#### 扩展视频

```bash
python inference.py --prompt "PROMPT" --conditioning_media_paths VIDEO_PATH --conditioning_start_frames START_FRAME --height HEIGHT --width WIDTH --num_frames NUM_FRAMES --seed SEED --pipeline_config configs/ltxv-13b-0.9.8-distilled.yaml
```

#### 作为库使用

```python
from ltx_video.inference import infer, InferenceConfig

infer(
    InferenceConfig(
        pipeline_config="configs/ltxv-13b-0.9.8-distilled.yaml",
        prompt=PROMPT,
        height=HEIGHT,
        width=WIDTH,
        num_frames=NUM_FRAMES,
        output_path="output.mp4",
    )
)
```

### ComfyUI 集成

请访问 [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)。

### Diffusers 集成

请查看 [官方文档](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video)。

## 模型用户指南

### 提示工程

专注于详细、按时间顺序的动作和场景描述。包括具体运动、外观、相机角度和环境细节 - 都在一个流动的段落中。从动作开始，直接保持描述字面和精确。像电影摄影师描述拍摄列表一样思考。保持在 200 字以内。

### 参数指南

- 分辨率预设：更高分辨率用于详细场景，更低用于更快生成和简单场景。
- 种子：保存种子值以重新创建您喜欢的特定样式或构图。
- 指导尺度：3-3.5 是推荐值。
- 推理步骤：更多步骤（40+）用于质量，更少步骤（20-30）用于速度。

## 许可证

Apache-2.0 License
