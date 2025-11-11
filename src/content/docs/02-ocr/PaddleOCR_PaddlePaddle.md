---
title: PaddleOCR
---

# PaddleOCR 项目

**GitHub 项目地址:** [https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

## 主要特性

PaddleOCR 是由百度 PaddlePaddle 团队开发的一个多语言、多场景的开源 OCR（光学字符识别）工具包。它基于深度学习框架 PaddlePaddle，支持多种文本检测和识别模型，具有以下核心特性：

- **多语言支持**：内置 100+ 种语言的识别模型，包括中文、英文、日文、韩文等，支持简体/繁体中文混合识别。
- **高精度与高效**：采用 PP-OCRv5 系列模型，精度高、速度快，适用于服务器、移动端和边缘设备。
- **端到端支持**：从文本检测、方向分类到识别的全流程优化，支持轻量级模型，推理速度可达毫秒级。
- **易集成**：提供 Python、C++、Java 等多种接口，支持 Docker 部署，便于嵌入到各种应用中。
- **开源与社区驱动**：完全开源，Apache-2.0 许可，社区活跃，提供预训练模型和自定义训练工具。

## 主要功能

- **文本检测**：使用 DB（Differentiable Binarization）或 EAST 等算法检测图像中的文本区域，支持弯曲文本和复杂布局。
- **文本识别**：基于 CRNN 或 SVTR 架构的识别模型，支持字典约束和 CTC 解码，实现高准确率字符识别。
- **方向分类**：自动检测文本方向（0°/90°/180°/270°），处理旋转图像。
- **表格识别**：集成 PP-StructureV3 模块，支持表格结构解析和 Excel 输出。
- **关键信息提取（KIE）**：用于文档如身份证、发票的结构化信息抽取。
- **文档解析**：使用 PaddleOCR-VL 模型，将文档转换为结构化数据，支持 Markdown 和 JSON 输出。
- **文档理解**：集成 PP-ChatOCRv4，支持智能问答和信息提取。
- **文档翻译**：支持多语言文档翻译。
- **模型训练与优化**：提供数据标注工具、训练脚本和量化/剪枝功能，支持自定义数据集训练。
- **多平台部署**：支持 CPU/GPU/ARM 等硬件，集成 Paddle Lite 用于移动端部署。

## 用法

### 安装

1. 确保安装 Python 3.7+ 和 PaddlePaddle（CPU/GPU 版本）。
   ```
   pip install paddlepaddle  # CPU 版本
   pip install paddleocr
   ```

### 快速使用（Python 示例）

1. **命令行推理**：

   ```
   paddleocr ocr -i ./image.jpg --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False  # 中文识别
   ```

2. **Python API 使用**：

   ```python
   from paddleocr import PaddleOCR

   # 初始化 OCR 模型（首次运行会自动下载模型）
   ocr = PaddleOCR(use_doc_orientation_classify=False, use_doc_unwarping=False, use_textline_orientation=False)

   # 进行推理
   result = ocr.predict('image.jpg')
   for res in result:
       res.print()
       res.save_to_img("output")
       res.save_to_json("output")
   ```

3. **文档解析（PP-StructureV3）**：

   ```python
   from paddleocr import PPStructureV3

   pipeline = PPStructureV3(use_doc_orientation_classify=False, use_doc_unwarping=False)
   output = pipeline.predict('document.jpg')
   for res in output:
       res.print()
       res.save_to_json("output")
       res.save_to_markdown("output")
   ```

4. **文档理解（PP-ChatOCRv4）**：

   ```python
   from paddleocr import PPChatOCRv4Doc

   # 配置聊天机器人和检索器
   chat_bot_config = {
       "module_name": "chat_bot",
       "model_name": "ernie-3.5-8k",
       "base_url": "https://qianfan.baidubce.com/v2",
       "api_type": "openai",
       "api_key": "your_api_key",
   }

   pipeline = PPChatOCRv4Doc(use_doc_orientation_classify=False, use_doc_unwarping=False)
   visual_predict_res = pipeline.visual_predict('document.jpg', use_common_ocr=True, use_seal_recognition=True, use_table_recognition=True)

   # 构建向量并聊天
   vector_info = pipeline.build_vector([res["visual_info"] for res in visual_predict_res], retriever_config=retriever_config)
   chat_result = pipeline.chat(key_list=["关键信息"], visual_info=[res["visual_info"] for res in visual_predict_res], vector_info=vector_info, chat_bot_config=chat_bot_config, retriever_config=retriever_config)
   print(chat_result)
   ```

5. **文档解析（PaddleOCR-VL）**：

   ```python
   from paddleocr import PaddleOCRVL

   pipeline = PaddleOCRVL()
   output = pipeline.predict("document.jpg")
   for res in output:
       res.print()
       res.save_to_json("output")
       res.save_to_markdown("output")
   ```

### 高级用法

- **多语言切换**：通过 `lang` 参数指定，如 `lang='en'` 为英文。
- **表格/布局分析**：使用 PP-StructureV3 模块。
- **部署**：使用 Paddle Inference 或 Paddle Lite 进行高效部署，支持 ONNX 导出。

更多细节请参考项目 README 和文档。
