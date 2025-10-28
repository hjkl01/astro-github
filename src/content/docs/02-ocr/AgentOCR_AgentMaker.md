
---
title: AgentOCR
---

# AgentOCR 项目

**项目地址：** [https://github.com/AgentMaker/AgentOCR](https://github.com/AgentMaker/AgentOCR)

## 主要特性
- **多模态大语言模型支持**：集成 Llama3.2-Vision 等模型，实现图像理解和文本提取的结合。
- **高精度 OCR 能力**：基于大模型的智能识别，支持复杂布局的文档、图像中的文字提取，准确率高。
- **模块化设计**：包含 OCR 核心模块、图像预处理和后处理工具，便于扩展和自定义。
- **易集成**：提供 Python API 和命令行接口，支持快速部署到各种应用场景。
- **开源免费**：MIT 许可，社区驱动，鼓励贡献和改进。

## 主要功能
- **文本检测与识别**：自动检测图像中的文本区域，并提取内容，支持多语言（包括中文）。
- **布局分析**：理解文档结构，如表格、标题、段落等，实现语义化解析。
- **图像增强**：内置预处理功能，如去噪、校正倾斜，提升识别效果。
- **批量处理**：支持文件夹批量输入，适用于大规模文档数字化。
- **可视化输出**：生成带标注的图像和 JSON 格式结果，便于验证和二次开发。

## 用法
1. **安装依赖**：
   ```
   git clone https://github.com/AgentMaker/AgentOCR.git
   cd AgentOCR
   pip install -r requirements.txt
   ```

2. **配置模型**：
   - 下载 Llama3.2-Vision 模型权重（参考 README 中的 Hugging Face 链接）。
   - 编辑 `config.py` 设置模型路径和参数。

3. **命令行用法**：
   - 单文件处理：`python main.py --image path/to/image.jpg --output result.json`
   - 批量处理：`python batch_ocr.py --input_dir /path/to/images --output_dir /path/to/results`

4. **Python API 用法**：
   ```python
   from agentocr import AgentOCR

   ocr = AgentOCR(model_path="path/to/model")
   result = ocr.process_image("path/to/image.jpg")
   print(result['text'])  # 输出提取的文本
   ```

更多细节请参考项目 README 文件。