
---
title: zfile
---

# zfile 项目

**GitHub 项目地址**: [https://github.com/zhaojun1998/zfile](https://github.com/zhaojun1998/zfile)

## 主要特性
zfile 是一个基于 Spring Boot 和 Vue.js 开发的开源文件管理平台，具有以下核心特性：
- **简洁易用的界面**：采用现代化的前端设计，支持拖拽上传、预览等操作，提供直观的文件浏览体验。
- **多存储支持**：兼容本地存储、云存储（如阿里云 OSS、腾讯云 COS、OneDrive、Google Drive 等），灵活扩展存储后端。
- **权限管理**：支持用户角色管理、文件权限控制，确保数据安全。
- **文件预览与编辑**：内置多种文件预览功能，包括图片、文档、视频等，支持在线编辑 Markdown 和 Office 文件。
- **分享与协作**：文件分享链接生成、访问统计、协作编辑等功能，便于团队使用。
- **插件化架构**：支持自定义插件扩展，如水印、转码、OCR 识别等。
- **高性能**：优化了文件上传下载速度，支持断点续传和大文件处理。
- **跨平台部署**：支持 Docker 一键部署，适用于 Linux、Windows 等环境。

## 主要功能
- **文件管理**：上传、下载、删除、重命名、移动、复制文件和文件夹。
- **搜索与排序**：全文搜索、标签管理、按时间/大小/类型排序。
- **用户系统**：注册登录、个人空间、群组管理。
- **监控与日志**：操作日志记录、性能监控、错误报告。
- **API 接口**：提供 RESTful API，支持第三方集成。
- **移动端适配**：响应式设计，支持手机访问。

## 用法
1. **环境准备**：
   - 确保安装 Java 8+ 和 Node.js（用于构建前端）。
   - 克隆仓库：`git clone https://github.com/zhaojun1998/zfile.git`。

2. **后端部署**：
   - 进入 `zfile-server` 目录，运行 `mvn clean package` 打包。
   - 配置 `application.yml` 文件，包括数据库（MySQL/H2）、存储类型等。
   - 启动：`java -jar zfile-server.jar`。
   - 默认访问地址：`http://localhost:8080`。

3. **前端部署**：
   - 进入 `zfile-web` 目录，运行 `npm install` 和 `npm run build`。
   - 将构建后的文件复制到后端 static 目录，或单独部署 Nginx 代理。

4. **Docker 部署**（推荐）：
   - 拉取镜像：`docker pull zhaojun1998/zfile:latest`。
   - 运行容器：`docker run -d -p 8080:8080 --name zfile zhaojun1998/zfile:latest`。
   - 配置卷挂载以持久化数据。

5. **使用步骤**：
   - 浏览器访问部署地址，注册管理员账号。
   - 登录后，创建存储策略，选择本地或云存储。
   - 上传文件，通过 Web 界面管理，或使用 API 集成。
   - 自定义插件：在 `zfile-plugin` 目录开发并加载。

更多详情请参考项目 README 和 Wiki 文档。