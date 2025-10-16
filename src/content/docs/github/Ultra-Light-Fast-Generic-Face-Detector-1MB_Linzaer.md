
---
title: Ultra-Light-Fast-Generic-Face-Detector-1MB
---

# Ultra-Light-Fast-Generic-Face-Detector-1MB

## 项目地址
[GitHub 项目地址](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)

## 主要特性
- **超轻量级设计**：模型大小仅1MB，非常适合资源受限的设备，如移动端或嵌入式系统。
- **高速度检测**：实时人脸检测，支持快速推理，适用于视频流和实时应用。
- **通用性强**：基于轻量级网络架构，能在各种光照、角度和遮挡条件下检测人脸。
- **高效准确**：在保持低计算成本的同时，提供较高的检测精度，适用于工业级应用。
- **开源易集成**：使用Python和ONNX等框架，支持跨平台部署。

## 主要功能
- **人脸检测**：从图像或视频中自动识别并定位人脸位置，支持多张人脸同时检测。
- **实时处理**：集成到摄像头或视频流中，实现即时人脸检测。
- **模型导出与推理**：支持将模型导出为ONNX格式，便于在不同框架中使用；提供预训练模型进行快速推理。
- **自定义训练**：允许用户基于数据集微调模型，提升特定场景下的性能。
- **边界框输出**：检测结果包括人脸的边界框坐标、置信度分数，便于后续处理如人脸识别。

## 用法
1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB.git`
   - 安装依赖：`pip install -r requirements.txt`（包括OpenCV、ONNX Runtime等）。

2. **下载模型**：
   - 从仓库的Releases或模型链接下载预训练模型文件（如RFB-320模型）。

3. **运行检测**：
   - **单张图像**：使用`python demo_image.py --model path/to/model.onnx --image path/to/image.jpg`，输出检测结果图像。
   - **视频或摄像头**：运行`python demo_video.py --model path/to/model.onnx --input path/to/video.mp4` 或直接使用摄像头（无input参数）。
   - 参数说明：
     - `--model`：指定模型路径。
     - `--input`：输入图像或视频路径（可选，默认为摄像头）。
     - `--threshold`：置信度阈值，默认0.7，可调整以过滤低置信度检测。

4. **自定义部署**：
   - 集成到其他项目：导入`face_detector.py`模块，调用`detect_faces(image)`函数返回检测结果。
   - 训练新模型：准备WIDER FACE数据集，运行训练脚本`train.py`，然后导出ONNX模型。

更多细节请参考仓库的README文档。