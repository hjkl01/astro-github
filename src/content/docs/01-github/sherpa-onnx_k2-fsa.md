
---
title: sherpa-onnx
---


# Sherpa-onnx 项目（k2-fsa）

**GitHub 地址**: <https://github.com/k2-fsa/sherpa-onnx>

---

## 主要特性

- **ONNX 兼容**  
  采用 ONNX 运行时实现跨平台推理，支持 CPU、GPU、TensorRT 等多种后端。

- **实时语音识别（Streaming）**  
  支持低延迟的语音流式识别，适用于实时字幕、语音助手等场景。

- **多模型支持**  
  - Whisper（及其轻量化版本）  
  - 低精度量化模型（FP16 / INT8）  
  - 传统神经网络解码器（LSTM、GRU、CRF 等）

- **k2 图搜索解码器**  
  与 k2 结合，支持基于图的解码（WFST、DNN、DNN+LM）和探索式搜索。

- **跨语言、跨设备**  
  支持多语言模型，支持嵌入式设备（Raspberry Pi、Jetson、移动端）推理。

- **多语言 API**  
  - Python 接口（`sherpa_onnx`）  
  - C++ 接口（`sherpa-onnx`）  
  - 也提供了 Rust、JavaScript（WebAssembly）封装（正在持续更新）。

---

## 核心功能

1. **离线端到端识别**  
   - 端到端的声学模型 + 语言模型（LM）  
   - 可以按需禁用 LM 以减少资源占用

2. **语音分段与增量推理**  
   - 支持 `DecoderStream` 与 `EncoderStream` 对象，实现增量解码  
   - 可处理长音频流，无需一次性读取整个文件

3. **模型量化与加速**  
   - `fp16`、`int8` 量化模型，可通过 `onnxruntime` 开启 FP16 / INT8 模式  
   - 支持 TensorRT 1.12+ 以及 NVIDIA Ampere/Versal 等显卡

4. **轻量化部署**  
   - 通过 `sherpa-onnx --export-onnx` 可导出单模型 ONNX，减少模型数
   - 自带 `sherpa-onnx-scripts`，可自动下载、转换模型

5. **常见用例**  
   - 单语音文件批量识别  
   - 直播字幕  
   - 边缘设备离线识别（例如车载系统、语音门锁）

---

## 快速开始

### 1. 安装

```bash
# Python 用户
pip install sherpa-onnx

# C++ 用户（已编译好的二进制或从源码构建）
# 参见 repo 上的 README
```

### 2. 下载示例模型

```bash
# WhisperTiny（'tiny.en'）示例
sherpa-onnx --download-model tiny.en
```

### 3. Python 示例

```python
import sherpa_onnx

# 选择模型路径
asr = sherpa_onnx.OfflineRecognizer(
    encoder=sherpa_onnx.OnnxEncoder(
        model_file="tiny.en/encoder.onnx",
        tokens_file="tiny.en/tokens.txt",
    ),
    decoder=sherpa_onnx.OnnxDecoder(
        model_file="tiny.en/decoder.onnx",
        vocab_file="tiny.en/vocab.txt",
    ),
    tokens_file="tiny.en/tokens.txt",
)

result = asr.recognize("speech.wav")
print(result.text)
```

### 4. C++ 示例

```cpp
#include "sherpa-onnx/sherpa-onnx.h"

int main() {
  sherpa_onnx::OfflineRecognizerConfig cfg;
  cfg.encoder.model_file = "tiny.en/encoder.onnx";
  cfg.decoder.model_file = "tiny.en/decoder.onnx";
  cfg.tokens_file = "tiny.en/tokens.txt";
  cfg.vocab_file = "tiny.en/vocab.txt";

  auto recognizer = sherpa_onnx::OfflineRecognizer(cfg);
  auto result = recognizer.Recognize("speech.wav");
  std::cout << result.text << std::endl;
  return 0;
}
```

---

## 进一步阅读

- 官方文档与使用教程在仓库 `docs/` 目录下
- 示例脚本 `scripts/` 说明如何下载、转换模型
- 性能基准与部署实测可以在 `benchmarks/` 目录查看

---

> **Tip**：若需更快的推理或更低的模型占用，可尝试 INT8 量化，并在 ONNX Runtime 启用 `providers=["CUDAExecutionProvider"]` 或 `["TensorRTExecutionProvider"]`.

