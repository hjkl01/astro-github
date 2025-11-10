---
title: Kronos
---

# Kronos 项目

## 项目地址

[GitHub 项目地址](https://github.com/shiyu-coder/Kronos)

## 主要特性

- **金融市场语言的基础模型**：Kronos 是第一个开源的基础模型，专门用于金融 K 线序列，基于超过 45 个全球交易所的数据进行预训练。
- **两阶段框架**：使用专门的分词器量化连续的多维 K 线数据（OHLCV）为分层离散令牌，然后使用大型自回归 Transformer 进行预训练。
- **多种模型规模**：提供不同容量的预训练模型（mini、small、base、large），以适应不同的计算和应用需求。
- **实时演示**：提供实时演示，展示 BTC/USDT 交易对未来 24 小时的预测结果。

## 主要功能

- **预测功能**：支持对金融 K 线数据进行预测，包括开盘价、最高价、最低价、收盘价、成交量和成交额。
- **批量预测**：支持对多个时间序列进行并行预测，提高效率。
- **微调支持**：提供完整的微调管道，支持在自己的数据集上微调 Kronos 模型。
- **可视化**：内置预测结果可视化，比较真实数据与模型预测。
- **模型动物园**：提供多个预训练模型，从小型到大型，满足不同需求。

## 用法

1. **安装**：
   - 克隆仓库：`git clone https://github.com/shiyu-coder/Kronos.git`
   - 安装依赖：`pip install -r requirements.txt`

2. **快速开始**：
   - 加载模型和分词器：
     ```python
     from model import Kronos, KronosTokenizer, KronosPredictor
     tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
     model = Kronos.from_pretrained("NeoQuasar/Kronos-small")
     predictor = KronosPredictor(model, tokenizer, device="cuda:0")
     ```
   - 进行预测：
     ```python
     pred_df = predictor.predict(df=x_df, x_timestamp=x_timestamp, y_timestamp=y_timestamp, pred_len=120)
     ```

3. **微调**：
   - 准备数据：使用 Qlib 或其他工具准备 A 股市场数据。
   - 运行微调：`torchrun --standalone --nproc_per_node=NUM_GPUS finetune/train_tokenizer.py` 然后 `finetune/train_predictor.py`。

4. **演示**：
   - 实时演示：[https://shiyu-coder.github.io/Kronos-demo/](https://shiyu-coder.github.io/Kronos-demo/)

更多详细用法请参考项目 README 文件。
