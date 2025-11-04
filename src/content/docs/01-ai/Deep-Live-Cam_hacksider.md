
---
title: Deep-Live-Cam
---


# Deep Live Cam

**项目地址**  
<https://github.com/hacksider/Deep-Live-Cam>

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **实时人脸替换** | 通过摄像头捕捉目标人脸，并在屏幕上实时叠加到另一张人脸图像/视频流。 |
| **基于稳定扩散（Stable Diffusion）** | 利用预训练的 Stable Diffusion 模型进行人脸细节合成与生成。 |
| **低延迟** | 采用高效的前向推理和 GPU 加速，延迟可低于 30 ms。 |
| **多目标支持** | 支持单人、多人目标人脸的捕捉与替换，阵列中的每个目标都能独立映射。 |
| **自定义 LoRA 训练** | 允许用户使用 LoRA 进行细粒度微调，以适配特定风格或人脸特征。 |
| **兼容多平台** | 运行在 Windows / Linux / macOS，支持 Python 3.10+ 与常见深度学习框架。 |

---

## 主要功能

1. **Live 视频捕获**  
   - 从摄像头或本地视频文件拉流。  
   - 实时检测并跟踪人脸框。  

2. **人脸检测 & 对齐**  
   - 使用 `dlib` 或 `MTCNN` 进行面部关键点检测。  
   - 生成对齐后的人脸图像以供模型输入。  

3. **Diffusion 推理**  
   - 将目标人脸作为条件提示，调用 `stable-diffusion-v1-5` 生成替换图像。  
   - 支持 `LoRA` 权重叠加，提升细节还原率。  

4. **实时渲染**  
   - 将生成的图像以全局遮罩方式叠加到背景视频。  
   - 保持目标人脸位置、姿态与色彩一致。  

5. **自定义配置**  
   - `config.yaml` 中可调整 `guidance_scale`、`steps`、`width/height` 等参数。  
   - 可绑定快捷键切换目标人脸或切换模型。  

---

## 用法

> **前提**：已安装 Python 3.10+，CUDA (GPU) 与相关依赖。

```bash
# 1. 克隆仓库
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam

# 2. 创建并激活虚环境
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 下载模型
python download_models.py

# 5. 启动实时人脸替换
#    - --source：目标人脸图片/视频路径
#    - --device：cuda/gpu
#    - --resolution：输出分辨率
python main.py --source "assets/target_face.jpg" --device cuda --resolution 512
```

### 常用命令行参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `--source` | `None` | 目标人脸图像或视频文件路径 |
| `--device` | `cuda` | 选择 `cuda`, `cpu`, `mps` |
| `--steps` | `30` | Diffusion 采样步数，步数越多图像质量越好 |
| `--guidance_scale` | `7.5` | 指导尺度，控制生成图像与条件的贴合程度 |
| `--resolution` | `512` | 输入/输出图像分辨率（--lora` | `None` | LoRA 权重文件路径，可选 |

### 示例

```bash
# 1. 只替换摄像头人脸为目标人脸
python main.py --source "target_face.png"

# 2. 将目标人脸从本地视频转出并替换
python main.py --source "target_video.mp4" --resolution 640 --steps 45

# 3. 使用 LoRA 进一步调优
python main.py --source "target_face.png" --lora "lora_weights.safetensors"
```

---

## 说明

- **性能**：在 RTX 3090 上，平均 FPS 在 25–30 之间，延迟约 20–30 ms。  
- **扩展**：可通过 `config.yaml` 修改默认行为，添加自定义模型或后处理策略。  
- **贡献**：欢迎 Issue 与 Pull Request，尤其是更高效的模型、更加稳健的跟踪技术或跨平台支持。  

---