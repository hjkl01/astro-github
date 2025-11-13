---
title: waifu2x
---

## 功能介绍

waifu2x 是一个用于动漫风格艺术的图像超分辨率工具，使用深度卷积神经网络（Deep Convolutional Neural Networks）来放大图像并减少噪声。它不仅适用于动漫，还支持照片处理。该项目旨在通过AI技术提升图像质量，特别是针对低分辨率或有噪声的图像进行优化。

主要功能包括：

- **噪声减少**：支持不同级别的噪声去除（level 0-3）。
- **图像放大**：支持2倍放大（2x upscaling）。
- **组合处理**：噪声减少与放大相结合。
- **批量处理**：支持批量转换多个图像。
- **Web应用**：提供本地Web界面进行图像处理。
- **模型训练**：允许用户训练自己的模型。

项目提供了在线演示：[https://waifu2x.udp.jp/](https://waifu2x.udp.jp/)（云版本）和 [https://unlimited.waifu2x.net/](https://unlimited.waifu2x.net/)（浏览器版本）。

## 用法

### 安装

waifu2x 基于 Torch7 和 CUDA，需要NVIDIA GPU支持。以下是简要安装步骤（以Ubuntu为例）：

1. 安装CUDA：从NVIDIA官网下载并安装CUDA工具包。
2. 安装依赖包：
   ```
   sudo apt-get install libsnappy-dev libgraphicsmagick1-dev libssl1.0-dev
   ```
3. 安装Torch7：参考Torch官方文档安装。
4. 克隆项目并安装Lua模块：
   ```
   git clone --depth 1 https://github.com/nagadomi/waifu2x.git
   cd waifu2x
   ./install_lua_modules.sh
   ```

### 命令行使用

#### 噪声减少

```
th waifu2x.lua -m noise -noise_level 1 -i input_image.png -o output_image.png
```

- `-noise_level`：噪声级别（0-3），0为最低，3为最高。

#### 2倍放大

```
th waifu2x.lua -m scale -i input_image.png -o output_image.png
```

#### 噪声减少 + 2倍放大

```
th waifu2x.lua -m noise_scale -noise_level 1 -i input_image.png -o output_image.png
```

#### 批量转换

```
find /path/to/imagedir -name "*.png" -o -name "*.jpg" > image_list.txt
th waifu2x.lua -m scale -l ./image_list.txt -o /path/to/outputdir/prefix_%d.png
```

#### 使用照片模型

添加 `-model_dir models/photo` 参数：

```
th waifu2x.lua -model_dir models/photo -m scale -i input_image.png -o output_image.png
```

### Web应用

启动本地Web服务器：

```
th web.lua
```

访问 [http://localhost:8812/](http://localhost:8812/) 进行图像处理。

### 视频处理

waifu2x 还支持视频帧的处理，通过提取帧、处理图像、再合成视频的方式。

### 注意事项

- 需要NVIDIA GPU和CUDA支持。
- 如果有cuDNN库，可以使用 `-force_cudnn 1` 参数加速。
- 如果遇到GPU内存不足，可以使用 `-crop_size` 参数（如 `-crop_size 128`）分块处理。
- 对于Windows用户，推荐使用第三方实现如 waifu2x-caffe 或 waifu2x-ncnn-vulkan。

更多详细信息请参考项目的GitHub页面：[https://github.com/nagadomi/waifu2x](https://github.com/nagadomi/waifu2x)。
