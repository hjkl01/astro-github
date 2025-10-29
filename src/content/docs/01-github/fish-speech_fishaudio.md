
---
title: fish-speech
---


# Fish Speech

**项目地址**  
<https://github.com/fishaudio/fish-speech>

---

## 一、项目概述  
Fish Speech 是一个基于 PyTorch 的轻量级语音识别框架，专为快速原型验证与模型训练设计。它提供了完整的数据处理、模型定义、训练、评估与推理工具，支持多种声学模型（如 CNN‑RNN‑CTC、Transformer、Wav2Vec2 等），并兼容 torchaudio、fairseq 等主流库。

## 二、主要特性

| 特性 | 简述 |
|------|------|
| **数据预处理** | 自动采样率转换、特征提取（MFCC / MelSpectrogram / raw audio）、数据增强（随机时间伸缩、幅度扰动、回声） |
| **灵活模型接口** | 可直接使用 `torch.nn.Module` 继承实现；内置常用模型如 `ConformerCTC`、`TransformerCTC`、`Wav2Vec2` |
| **训练脚本** | 开箱即用的训练/验证脚本，支持多 GPU / 数据并行、分布式训练，自动日志与结果可视化（TensorBoard） |
| **推理 API** | 简易 `predict` 函数，支持批量推理、实时语音输入（Webcam / 麦克风） |
| **评估工具** | 计算 Word Error Rate (WER)、Character Error Rate (CER)、实时反馈可视化 |
| **跨平台** | 纯 Python + PyTorch，基于 Conda / Pip，支持 Linux、macOS、Windows |
| **易于扩展** | 用户可通过继承 `Dataset`、`Aligner` 或添加自定义 `DataLoader` 进行高级定制 |

## 三、核心文件结构

```
fish-speech/
├── fish_speech/
│   ├── models/            # 模型实现
│   ├── data/              # 数据处理、DataLoader
│   ├── train.py           # 训练入口
│   ├── eval.py            # 评估入口
│   └── infer.py           # 推理入口
├── examples/              # 示例脚本
├── requirements.txt
└── README.md
```

## 四、快速使用示例

1. **安装依赖**

```bash
# 推荐使用conda环境
conda create -n fish-speech python=3.10 -y
conda activate fish-speech

pip install -r requirements.txt
```

2. **准备数据**

```bash
# 采用 LJSpeech 3.0 示例
mkdir -p data
# 下载并解压 LJSpeech（或自行替换为自有数据）
wget -P data https://keila.org/data/LJSpeech-1.1.tar.bz2
tar -xvf data/LJSpeech-1.1.tar.bz2 -C data
```

3. **训练模型**

```bash
python fish_speech/train.py \
    --config configs/conformer_ctc.yaml \
    --batch-size 32 \
    --lr 5e-4 \
    --epochs 30 \
    --data-dir data \
    --output-dir output/
```

4. **评估模型**

```bash
python fish_speech/eval.py \
    --model-path output/model_epoch30.pt \
    --dev-dir data/dev \
    --test-dir data/test
```

5. **实时推理**

```bash
# 录制 5 秒语音
arecord -d 5 -f cd -r 16000 test.wav

# 推理
python fish_speech/infer.py \
    --model-path output/model_epoch30.pt \
    --audio-file test.wav
```

## 五、使用自
from fish_speech.data import AudioDataset torch.utils.data import DataLoader

class MySpeechDataset(AudioDataset):
    def __init__(self, yaml_path, mode='train'):
        super().__init__(yaml_path, mode)

    def _collate_fn(self, batch):
        # 自定义 collate, 例如将 logits 与 target 对齐
        ...

dataset = MySpeechDataset('config.yaml', mode='train')
dataloader = DataLoader(dataset, batch_size=32, collate_fn=dataset._collate_fn, num_workers=4)
```

## 六、贡献与支持

- Fork → Pull Request  
- Issues 反馈  
- 通过 `pip install fish-speech` 直接安装（已发布至 PyPI）

> 该文档仅供调用者快速上手，详细内容请参考官方 README 与 API 文档。

``` 

所在文件路径: `src/content/docs/00/fish-speech_fishaudio.md`.