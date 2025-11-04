
---
title: LEANN
---


# LEANN 项目说明

> 项目地址: https://github.com/yichuan-w/LEANN

## 项目简介
LEANN（Lightweight Edge-Aware Neural Network）是一个基于 PyTorch 的轻量化图像分割/边缘检测框架。  
它通过引入边缘感知损失和注意力机制，在保持极低模型大小和推理速度的前提下，取得与传统大型模型相当的分割精度。

## 主要特性
| 特性 | 说明 |
|------|------|
| **轻量化** | 模型参数数目 < 1M，适合移动端/嵌入式设备 |
| **边缘感知** | 采用边缘辅助损失（Edge-aware Loss）提升边界精细度 |
| **可扩展** | 支持多种 backbone（MobileNetV2, EfficientNet-B0 等） |
| **多任务** | 同时完成语义分割与边缘检测 |
| **端到端训练** | 一键训练、验证、推理脚本 |
| **ONNX 导出** | 方便部署到 TensorRT、ONNX Runtime 等平台 |

## 核心功能
1. **数据处理**  
   - 支持 COCO、Cityscapes、ADE20K 等常见分割数据集  
   - 数据增强：随机裁剪、翻转、颜色抖动等

2. **模型定义**  
   - `models/` 目录下包含轻量化 backbone 与解码器实现  
   - `losses/` 提供 `EdgeAwareLoss` 与交叉熵组合

3. **训练与评估**  
   - `train.py`：一键训练，支持多 GPU、混合精度训练  
   - `eval.py`：计算 mIoU、Dice、边缘 F1 等指标

4. **推理**  
   - `infer.py`：加载已训练模型，对单张或批量图像进行分割/边缘检测  
   - 支持输出 PNG、Mask 以及可视化结果

5. **模型导出**  
   - `export.py`：将 PyTorch 模型导出为 ONNX，自动生成对应的推理脚本

## 项目结构
```
LEANN/
├─ data/              # 数据集下载脚本
├─ models/            # 模型实现
├─ losses/            # 损失函数
├─ utils/             # 工具函数
├─ train.py           # 训练入口
├─ eval.py            # 评估入口
├─ infer.py           # 推理入口
├─ export.py          # ONNX 导出
├─ requirements.txt   # 依赖
└─ README.md
```

## 快速上手

```bash
# 1. 克隆仓库
git clone https://github.com/yichuan-w/LEANN.git
cd LEANN

# 2. 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 下载并准备数据
# 例如 Cityscapes
sh scripts/download_cityscapes.sh

# 5. 训练模型
python train.py \
    --data_dir data/cityscapes \
    --batch_size 16 \
    --epochs 100 \
    --lr 1e-3 \
    --backbone mobilenetv2

# 6. 评估
python eval.py \
    --model_path checkpoints/latest.pth \
    --data_dir data/cityscapes/val

# 7. 推理单张图像
python infer.py \
    --model_path checkpoints/latest.pth \
    --image_path demo/input.jpg \
    --output_dir demo/output

# 8. 导出 ONNX
python export.py \
    --model_path checkpoints/latest.pth \
    --output_path model.onnx
```

## 贡献指南
- Fork 本仓库 → `git clone https://github.com/<your-username>/LEANN.git`  
- 开发新功能或修复 bug 后提交 PR  
- 请先添加/更新单元测试，确保 `pytest` 通过

## 联系方式
- 问题与讨论请提交 Issues  
- 代码贡献欢迎欢迎（PR）  

---  

> 本文件使用 Markdown 格式，可直接保存为 `src/content/docs/00/LEANN_yichuan-w.md`。