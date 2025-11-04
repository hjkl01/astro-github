
---
title: label-studio
---

# HumanSignal/Label Studio

> 项目地址: https://github.com/HumanSignal/label-studio

## 主要特性

- **多任务数据标注**  
  支持文本、图像、音频、视频、表格、时序数据等多种数据类型，能够完成分类、分割、检测、关键点检测、关系抽取等多种标注任务。

- **可视化 Web 界面**  
  通过浏览器即可完成标注，界面可高度自定义（任务模板、UI 组件、颜色主题等），支持多用户协作、权限管理与审计日志。

- **灵活的数据接入**  
  支持 CSV、JSON、XML、TSV、S3、SFTP、数据库等多种数据源；可通过 API 或 SDK 直接上传数据。

- **模型驱动标注**  
  与机器学习模型无缝集成，支持自动标注、主动学习、模型回传等功能，提升标注效率。

- **多种导出格式**  
  支持 COCO、Pascal VOC、YOLO、LabelMe、CVAT、JSON、CSV、XML 等标准格式，方便与训练框架对接。

- **插件与扩展**  
  支持自定义插件（如自定义验证、自动化脚本、第三方 API 集成），可通过 Docker 或 Kubernetes 部署。

- **多语言 & 多账号**  
  支持多语言 UI 与多账号登录，满足全球团队协作需求。

## 功能列表

| 功能 | 说明 |
|------|------|
| **项目管理** | 创建/删除/复制项目，设置任务类型、字段、标签集、机器学习模型 |
| **任务分配** | 自动/手动分配任务，支持批量上传与下载 |
| **标注工具** | 文字高亮、边框框选、点标记、多边形、曲线、时间轴、多图像拼接等 |
| **模型集成** | 通过 REST API 调用外部模型，支持 TensorFlow、PyTorch、Hugging Face、OpenAI 等 |
| **数据版本控制** | 标注数据与原始数据版本同步，支持回滚 |
| **统计报表** | 实时统计标注进度、质量、时长，导出报表 |
| **安全与合规** | GDPR、HIPAA 合规选项，细粒度权限控制 |

## 快速使用

1. **安装**  
   ```bash
   pip install label-studio
   ```

2. **启动**  
   ```bash
   label-studio
   ```
   默认在 `http://localhost:8080/` 访问。

3. **创建项目**  
   - 通过 Web UI → “Create new project”。  
   - 或使用命令行  
     ```bash
     label-studio create "My Project" --type image_classifier
     ```

4. **导入数据**  
   ```bash
   label-studio import data.json
   ```
   `data.json` 需要符合项目定义的字段。

5. **模型集成（示例）**  
   ```bash
   label-studio ml start my_model --model-id my-model-id
   ```

6. **导出标注结果**  
   ```bash
   label-studio export --format coco > annotations.json
   ```

7. **Docker 部署**  
   ```bash
   docker run -p 8080:8080 -v $(pwd)/data:/data heartexlabs/label-studio:latest
   ```

## 参考文档

- 官方文档: https://labelstud.io/
- API 参考: https://labelstud.io/api
- 插件开发: https://labelstud.io/plugins

---