
---
title: Depixelization_poc
---

# Depixelization PoC（spipm）

**项目地址**：<https://github.com/spipm/Depixelization_poc>  

---

## 📌 项目概述  
Depixelization_poc 是一个基于深度学习和图像处理技术的 pixel 化图像恢复演示项目。该仓库实现了一个简易的获取 pixel 化图像、执行超分辨率重建以及去像素化后输出高质量图像的完整流程，目的是验证相关算法在单纯 pixel 化图片上的效果。

---

## 🎯 主要特性  
| # | 功能 | 说明 |
|---|------|------|
| 1 | **图片读取与预处理** | 支持常见的 PNG/JPG/ BMP 格式，通过 `Pillow` 读取并做必要归一化。 |
| 2 | **像素化（可选）** | 通过可配置的 `pixel_size` 参数手动将清晰图像像素化，适用于演示或数据生成。 |
| 3 | **超分辨率重建** | 采用 `torch.nn.Upsample`（或可按需替换更高级的 SR 模型）将像素化图像放大至原始尺寸。 |
| 4 | **去像素化后处理** | 通过 `Gaussian blur` / `Median filter` 等传统算法去除残留粗糙边缘，提升视觉质量。 |
| 5 | **命令行工具** | 简单易用的 CLI，支持选择输入、输出路径、像素化大小等参数。 |
| 6 | **可扩展性** | 结构清晰，后续可轻松集成先进的 GAN / Transformer SR 模型，只需替换 `models/` 下的 `depixelizer.py` 。 |

---

## ⚙️ 功能模块

| 模块 | 主要文件 | 关键函数 |
|------|----------|----------|
| **输入/输出** | `main.py` | `load_image(path)`、`save_image(img, path)` |
| **像素化** | `utils/pixelate.py` | `pixelate(img, size)` |
| **超分辨率** | `models/depixelizer.py` | `Depixelizer.forward(img)` |
| **后处理** | `utils/postprocess.py` | `remove_noise(img)` |
| **CLI** | `cli.py` | `parse_args()`、`run()` |

---

## 🚀 使用方法

### 1. 克隆仓库  
```bash
git clone https://github.com/spipm/Depixelization_poc.git
cd Depixelization_poc
```

### 2. 安装依赖  
```bash
pip install -r requirements.txt
```
*(可根据实际情况在 `conda` 环境中安装；若无 GPU 需要的 `torch` 版本请自行调整。)*

### 3. 运行演示  
```bash
python main.py --input path/to/input_image.png \
               --output path/to/output_image.png \
               --pixel_size 8 \
               --sr_factor 4
```

| 参数 | 含义 | 默认值 |
|------|------|--------|
| `--input` | 输入图片路径 | `None`（必填） |
| `--output` | 输出图片路径 | `./output.png` |
| `--pixel_size` | 像素化尺寸（整数） | `8` |
| `--sr_factor` | 超分辨率放大倍数 | `4` |

> **提示**  
> - 若想直接对已像素化的图片进行去像素化，只需省略 `--pixel_size` 参数。  
> - `--sr_factor` 决定了输出图像尺寸与原始尺寸的比例。

### 4. 结果查看  
处理完成后，输出图片会保存在 `--output` 指定的路径下。您可以使用任何图片查看器打开，比较停着与默认超分辨率效果。

---

## 📦 依赖说明  

- `Python 3.9+`  
- `torch`（如有 GPU 支持可使用带 CUDA 的版本）  
- `Pillow`  
- `numpy`  
- `argparse`  
- `tqdm`（可选，用于进度条）  

> 如需使用更强大的 SR 模型，可自行在 `models/` 目录下替换或扩展 `Depixelizer` 类。


---  

**作者**: [spipm](https://github.com/spipm)  
**License**: MIT  

> 仅为演示与 PoC，功能上具有一定实验性。欢迎 Fork、Issue 或 Pull Request 进行改进。