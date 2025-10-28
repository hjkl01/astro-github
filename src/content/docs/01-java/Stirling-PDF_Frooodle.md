
---
title: Stirling-PDF
---

# Stirling-PDF 项目

**项目地址：** [https://github.com/Frooodle/Stirling-PDF](https://github.com/Frooodle/Stirling-PDF)

## 主要特性
Stirling-PDF 是一个开源的 Web 应用，专注于 PDF 文件的处理和操作。它基于 Java Spring Boot 框架构建，支持 Docker 部署，提供用户友好的界面，无需安装复杂软件即可处理 PDF。核心特性包括：
- **隐私优先**：所有 PDF 处理在本地服务器上进行，不上传到云端，确保数据安全。
- **多功能集成**：支持超过 50 种 PDF 操作工具，包括合并、拆分、转换等。
- **易于部署**：通过 Docker 或直接运行 JAR 文件快速启动，支持自定义配置。
- **响应式设计**：界面适配桌面和移动设备，支持多语言（包括中文）。
- **开源免费**：MIT 许可，社区驱动，允许自定义扩展。

## 主要功能
项目提供丰富的 PDF 处理功能，涵盖基本编辑到高级转换：
- **基本编辑**：合并多个 PDF、拆分 PDF 为单页或范围、旋转页面、添加/删除页面。
- **转换工具**：将 PDF 转换为图像（PNG/JPG）、Word（DOCX）、Excel（XLSX）、PowerPoint（PPTX）等；反之亦然（如图像转 PDF）。
- **文本与元数据**：提取 PDF 文本、添加水印、设置 PDF 元数据（标题、作者等）、压缩 PDF 以减小文件大小。
- **高级操作**：数字签名 PDF、修复损坏 PDF、OCR 文本识别（需额外配置）、重排序页面。
- **其他工具**：生成 PDF 缩略图、转换为 Grayscale、添加页眉/页脚、保护 PDF（加密/解密）。

这些功能通过简单的拖拽或文件上传实现，支持批量处理。

## 用法
### 部署
1. **使用 Docker（推荐）**：
   - 拉取镜像：`docker pull frooodle/stirling-pdf`
   - 运行容器：`docker run -d -p 8080:8080 --name stirling-pdf frooodle/stirling-pdf`
   - 访问：浏览器打开 `http://localhost:8080`。

2. **直接运行 JAR**：
   - 下载最新 release 的 JAR 文件。
   - 运行：`java -jar Stirling-PDF.jar`（需 Java 17+）。
   - 访问本地端口（默认 8080）。

3. **自定义配置**：
   - 编辑 `application.properties` 文件调整端口、语言、启用/禁用功能。
   - 支持环境变量配置，如 Docker 中的 `-e DOCKER_ENABLE_SECURITY=false` 以禁用安全检查。

### 使用步骤
1. **启动应用**：部署后，在浏览器访问 Web 界面。
2. **上传文件**：选择左侧工具栏中的功能（如“合并 PDF”），上传一个或多个 PDF 文件。
3. **配置选项**：根据工具调整参数，例如选择页面范围或转换格式。
4. **处理并下载**：点击“处理”按钮，等待完成后下载结果文件。
5. **高级用法**：对于 API 集成，可通过 RESTful API 调用功能（详见项目文档）；支持 CLI 模式处理批量任务。

项目文档详尽，建议查看 GitHub 上的 README 以获取最新更新和故障排除。