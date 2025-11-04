
---
title: REAL-Video-Enhancer
---


---
title: REAL-Video-Enhancer
description: 中文项目说明
---

# REAL-Video-Enhancer

> GitHub 地址: <https://github.com/TNTwise/REAL-Video-Enhancer>

---

## 主要特性

| 序号 | 特性 | 简述 |
|------|------|------|
| 1 | **4× 视频超分辨率** | 基于 Real‑ESRGAN 的模型，支持将视频分辨率提升至原始 4 倍。 |
| 2 | **去模糊与降噪** | 在超分的同时，利用去模糊网络恢复运动模糊帧，去除噪点。 |
| 3 | **实时推理** | 支持 GPU/CPU 推理，利用多线程与显存复用实现接近实时的处理速度。 |
| 4 | **FFmpeg 集成** | 通过 ffmpeg 直接读取和写入视频流，避免手动拆帧/合帧。 |
| 5 | **可插件化** | 通过配置文件便捷切换不同模型或自定义模型路径。 |
| 6 | **可视化进度** | 命令行显示进度条与处理时间统计，便于监控批量任务。 |

---

## 核心功能

1. **视频解压与拆帧**  
   - 使用 `ffmpeg` 抽取视频帧，转化为 `png/img` 格式。  
   - 支持多种编码格式（H.264、H.265、VP9 等）。

2. **帧级超分**  
   - 调用 `RealESRGAN` 推理器，对每帧进行 4× 超分。  
   - 支持批量推理，配置 `batch_size` 以平衡速度与显存。  

3. **帧级去模糊 & 降噪**  
   - 在超分后对帧做去模糊处理。  
   - 对低光/噪点视频可启用降噪模块。

4. **视频重组**  
   - 将处理后的帧回写为视频，保持原始帧率与音频。  
   - 可输出多种分辨率（原始、2×、4×等）。

5. **配置驱动**  
   - `config.yaml` 定义模型路径、推理设备、批量大小、帧率等。  
   - 可以通过 CLI 动态覆盖任何配置项。

---

## 使用方法

> 下面以命令行为例，演示完整的安装与推理流程。

### 1. 克隆仓库

```bash
git clone https://github.com/TNTwise/REAL-Video-Enhancer.git
cd REAL-Video-Enhancer
```

### 2. 安装依赖

> 必须 Python 3.8+，并已安装 PyTorch（带 CUDA 支持时请根据 GPU 版本匹配）。  
> 推荐使用 `conda` 或 `pip`：

```bash
# pip 安装
pip install -r requirements.txt

# 如果想要 GPU 版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 3. 下载预训练模型

> 预训练模型已放在 `models/` 目录下。若缺失，可手动下载：

```bash
# 示例：下载 4x RealESRGAN 模型
wget -P models/ https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.1/RealESRGAN_x4plus.pth
```

### 4. 运行视频增强

```bash
python main.py \
    --config config.yaml \
    --input videos/input.mp4 \
    --output videos/output.mp4 \
    --device cuda \
    --batch 8
```

**参数说明**

| 参数 | 默认值 | 作用 |
|------|--------|------|
| `--config` | `config.yaml` | 配置文件路径 |
| `--input` | | 输入视频路径 |
| `--output` | | 输出视频路径 |
| `--device` | `cuda` | 推理设备cpu/cuda） |
| `--batch` | `4` | 每批处理帧数 |
| `--scale` | `4x` | 目标放大倍数 |
| `--denoise` | `false` | 是否开启降噪 |
| `--deblur` | `true` | 是否开启去模糊 |

> 可在 `config.yaml` 里一次性设置所有参数，直接执行：

```bash
python main.py --config config.yaml
```

### 5. 批量处理（可选）

> 若有多段视频，可脚本化批量处理：

```bash
python batch_process.py --input_dir videos/raw/ --output_dir videos/processed/ --config config.yaml
```

---

## 结合示例

```bash
# 1. 简单四倍放大
python main.py --input raw/video1.mp4 --output out/video1_4x.mp4

# 2. 四倍放大 + 去模糊 + 降噪
python main.py --input raw/video2.mp4 --output out/video2_enhanced.mp4 \
               --denoise true --deblur true
```

---

## 常见问题

| 关键字 | 解决办法 |
|--------|----------|
| `cuda out of memory` | 减小 `--batch` 或使用 `torch.cuda.empty_cache()` |
| `ffmpeg: No such file` | 确认已安装 ffmpeg 并加入 PATH |
| `torchvision.errors.UnsupportedImageType` | 检查图像格式，必要时添加 `--format png` |

> 更多细节请查看 `docs/` 目录下的帮助文件。

---

> **提示**  
> - 若想自研模型，只需将 `.pth` 放到 `models/` 并在 `config.yaml` 指定 `model_path`。  
> - 代码已兼容多显示卡，使用 `--device cuda:0,1` 可并行推理。

---

### 项目地址

> https://github.com/TNTwise/REAL-Video-Enhancer

---

```python
# Example: config.yaml
model:
  path: "models/RealESRGAN_x4plus.pth"
  scale: 4
device: "cuda"
batch_size: 8
denoise: true
deblur: true
