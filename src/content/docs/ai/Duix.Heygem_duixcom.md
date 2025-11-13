---
title: Duix.Heygem
---

# Duix.Heygem 项目

**GitHub 项目地址:** [https://github.com/duixcom/Duix.Heygem](https://github.com/duixcom/Duix.Heygem/blob/main/README_zh.md)

## 主要特性
Duix.Heygem 是一个基于 Heygem 框架的开源项目，专注于高效的 AI 模型管理和部署。它支持多模态 AI 集成、轻量级容器化部署，以及自定义插件扩展。主要特性包括：
- **模块化架构**：易于扩展，支持插件系统，便于开发者自定义功能。
- **高性能推理**：优化了 AI 模型的推理速度，支持 GPU/CPU 加速。
- **多语言支持**：内置中文和英文接口，适用于全球开发者。
- **安全与隐私**：集成数据加密和访问控制机制，确保模型部署的安全性。
- **跨平台兼容**：支持 Windows、Linux 和 macOS 系统。

## 主要功能
- **AI 模型管理**：提供模型上传、版本控制和自动更新功能，支持 Hugging Face 等主流模型库。
- **API 接口**：RESTful API 设计，便于与其他应用集成，实现实时 AI 推理。
- **可视化工具**：内置 Web 界面，用于监控模型性能和日志分析。
- **自动化部署**：一键 Docker 部署，支持 Kubernetes 集群扩展。
- **插件生态**：预置图像生成、文本处理和语音识别插件，可扩展更多 AI 功能。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/duixcom/Duix.Heygem.git`
   - 进入目录：`cd Duix.Heygem`
   - 安装 Python 环境（推荐 Python 3.8+）：`pip install -r requirements.txt`

2. **配置**：
   - 编辑 `config.yaml` 文件，设置 API 密钥、模型路径和端口。
   - 示例配置：
     ```
     model_path: ./models
     api_key: your_api_key_here
     port: 8080
     ```

3. **运行项目**：
   - 启动服务器：`python main.py`
   - 访问 Web 界面：打开浏览器，输入 `http://localhost:8080`

4. **使用 API**：
   - 发送 POST 请求到 `/infer` 端点，例如使用 curl：
     ```
     curl -X POST http://localhost:8080/infer -H "Content-Type: application/json" -d '{"prompt": "Hello, AI!"}'
     ```
   - 返回 JSON 格式的推理结果。

5. **扩展插件**：
   - 在 `plugins/` 目录下添加新 Python 模块，实现自定义功能。
   - 重启服务器以加载插件。

更多详情请参考仓库中的 README_zh.md 文件。