
---
title: char-rnn
---


# Karpathy's char-rnn

> **项目地址**：<https://github.com/karpathy/char-rnn>

## 项目简介
Karpathy 的 char-rnn 是一个使用 Torch/Lua 实现的字符级 RNN 训练与生成模型。它展示了如何用循环神经网络（LSTM/GRU）对大文本语料进行训练，并通过采样生成连贯的文字。该项目被广泛用于教学和演示 RNN 的基本原理。

## 主要特性

- **字符级语言模型**：输入字符序列，预测下一个字符。
- **支持多层 RNN**：可配置 LSTM、GRU 以及层数。
- **GPU 加速**：可运行于 CUDA，显著提升训练速度。
- **可视化进度**：训练过程中实时打印日志与样本。
- **预训练模型**：附带几个公开语料库（如莎士比亚、Moby Dick、纽约时报）预训练模型。
- **可配置性强**：所有超参数（隐藏单元数、学习率、梯度裁剪等）都通过命令行传参。

## 功能
| 功能 | 说明 |
|------|------|
| `train.lua` | 训练脚本，可指定数据、RNN 类型、隐藏层大小、层数等 |
| `sample.lua` | 单独运行采样器，加载预训练模型并生成文本 |
| `data/` | 示例数据集，支持自行添加其他文本文件 |
| `models/` | 存储训练好的模型参数文件 |
| `shell/` | 便捷的 Shell 脚本集（`run.sh`、`train.sh` 等） |
| `plots/` | 训练指标输出到可视化图表（需 `gnuplot`） |

## 用法

> **依赖**：Torch (`th`)、cunn、cudnn、gnuplot（可选）

### 1. 克隆仓库
```bash
git clone https://github.com/karpathy/char-rnn.git
cd char-rnn
```

### 2. 准备数据
- 直接使用 `data/` 目录下的示例文件（如 `data/shakespeare.txt`）。
- 或放入自己的文本文件，并修改 `config.sh` 中的 `DATA_FILE`。

### 3. 训练模型
```bash
# 训练示例：3 层 LSTM, 128 hidden units, 50k 迭代
th train.lua -dataset data/shakespeare.txt -model lstm -layers 3 -hidden 128 -iters 50000
```

关键参数说明：
- `-dataset`：输入文本文件路径
- `-model`：`lstm` 或 `gru`
- `-layers`：网络层数
- `-hidden`：隐藏层单元数
- `-iters`：训练次数

### 4. 生成文本
```bash
# 使用已经训练好的模型（默认是最后一次保存的)
th sample.lua -model_path models/model.t7 -len 500 -cuda true
```

**参数**：
- `-model_path`：模型文件路径
- `-len`：生成字符数
- `-temp`：采样温度（0.0 为确定性，1.0 为正常随机）

### 5. 使用预训练模型
```bash
# 下载并使用已有的预训练模型
wget https://www.kaggle.com/karpathy/char-rnn-model-dl.zip
unzip char-rnn-model-dl.zip
th sample.lua -model_path models/moby_dick.t7 -len 1000
```

## 参考链接
- 官方博客文章: <http://karpathy.github.io/2015/12/20/char-rnn-tutorial/>
- 互动视频: <https://www.youtube.com/watch?v=IDZyNTHZd4Y>

--- 

> *以上内容可直接粘贴至 `src/content/docs/00/char-rnn_karpathy.md` 中进行保存。*