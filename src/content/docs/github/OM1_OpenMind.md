---
title: OM1
---


# OM1 - OpenMind 项目

项目地址: https://github.com/OpenMind/OM1

## 项目简介  
OM1 是 OpenMind 开源的轻量级多模态 AI 框架，支持文本、图像、音频等多种数据类型的训练与推理。框架采用模块化设计，方便用户自定义模型、数据管道以及推理接口。

## 主要特性  
- **多模态支持**：文本、图像、音频统一接口  
- **模块化架构**：数据处理、模型、训练器、推理器分离  
- **轻量部署**：可直接在 CPU / GPU / Edge 设备上运行  
- **易用 API**：一键训练、推理、评估  
- **社区友好**：完整文档、示例代码、Docker 镜像  

## 功能  
| 功能 | 说明 |
|------|------|
| 数据集管理 | 支持自定义数据集格式，提供预处理工具 |
| 模型定义 | 预置 Transformer、CNN 等网络，支持自定义层 |
| 训练器 | 支持多卡、分布式、混合精度训练 |
| 推理器 | 快速加载模型，提供 RESTful API 和 CLI |
| 评估工具 | 自动化指标计算、可视化报告 |

## 用法  

### 1. 克隆仓库  
```bash
git clone https://github.com/OpenMind/OM1.git
cd OM1
```

### 2. 安装依赖  
```bash
pip install -r requirements.txt
# 或者使用 pipenv / conda
```

### 3. 训练模型  
```bash
python scripts/train.py --config configs/om1_text.yaml
```

### 4. 推理示例  
```bash
python scripts/infer.py --model_path checkpoints/om1_best.pth --input "Hello, world!"
```

### 5. 启动 RESTful API  
```bash
python api/server.py --model_path checkpoints/om1_best.pth
# 访问 http://localhost:8000/predict
```

### 6. Docker 快速部署  
```bash
docker build -t om1:latest .
docker run -p 8000:8000 om1:latest
```

## 参考文档  
- README.md  
- docs/user_guide.md  
- docs/api_reference.md
