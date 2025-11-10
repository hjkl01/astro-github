---
title: sherpa-onnx
---
---

## 进一步阅读

- 官方文档与使用教程在仓库 `docs/` 目录下
- 示例脚本 `scripts/` 说明如何下载、转换模型
- 性能基准与部署实测可以在 `benchmarks/` 目录查看

---
> **Tip**：若需更快的推理或更低的模型占用，可尝试 INT8 量化，并在 ONNX Runtime 启用 `providers=["CUDAExecutionProvider"]` 或 `["TensorRTExecutionProvider"]`.
