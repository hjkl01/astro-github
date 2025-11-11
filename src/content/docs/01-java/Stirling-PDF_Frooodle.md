---
title: Stirling-PDF
---

---

## title: Stirling-PDF

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

Stirling-PDF 提供超过 50 种 PDF 操作工具，支持并行文件处理、暗色模式、自定义下载选项、自动化管道（Pipelines）、API 集成、可选登录认证、企业级 SSO 等特性。核心功能包括：

- **组织 (Organise)**：合并 PDF、拆分 PDF、提取页面、裁剪 PDF、旋转、调整页面大小、多页布局、PDF 转单页大图、重新排列页面。
- **转换为 PDF**：图像转 PDF、文件转 PDF、HTML 转 PDF、Markdown 转 PDF、CBZ 转 PDF、CBR 转 PDF、邮件转 PDF、矢量图像转 PDF。
- **从 PDF 转换**：PDF 转 Word、PDF 转图像、PDF 转 RTF、PDF 转演示文稿、PDF 转 CSV、PDF 转 XML、PDF 转 HTML、PDF 转 PDF/A、PDF 转 Markdown、PDF 转 CBZ、PDF 转 CBR、PDF 转矢量图像。
- **签名与安全**：添加签名、移除密码、添加水印、证书签名、添加印章、自动红笔、更改权限、添加密码、移除证书签名、清理 PDF 安全问题、验证签名。
- **查看与编辑**：OCR/清理扫描、添加图像、提取图像、更改元数据、获取所有 PDF 信息、高级颜色选项、比较 PDF、添加页码、压平、移除注释、移除空白页、移除图像、查看/编辑 PDF、解锁 PDF 表单。
- **高级**：压缩、管道、调整颜色/对比度、自动重命名 PDF 文件、自动拆分页、检测/拆分扫描照片、叠加 PDF、修复、显示 JavaScript、按大小/计数自动拆分、按章节拆分 PDF、按部分拆分 PDF、扫描仪效果、编辑目录。
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
5. **高级用法**：
   - **API 集成**：通过 RESTful API 调用功能，支持外部脚本集成。
   - **自动化管道**：创建自定义管道，自动化运行多个功能。
   - **认证与企业功能**：启用登录认证、SSO（单点登录）、数据库备份导入。
   - **CLI 模式**：命令行模式处理批量任务。
     项目文档详尽，建议查看 [docs.stirlingpdf.com](https://docs.stirlingpdf.com/) 以获取最新更新、配置选项和故障排除。
