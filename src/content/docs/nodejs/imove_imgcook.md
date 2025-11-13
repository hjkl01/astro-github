---
title: imove
---

# iMove 项目描述

**项目地址:** [https://github.com/imgcook/imove](https://github.com/imgcook/imove)

## 主要特性
iMove 是一个开源的图像处理和转换工具，专注于自动化图像优化和批量处理。主要特性包括：
- **图像格式转换**：支持多种图像格式（如 PNG、JPEG、WebP）的互转，提高兼容性和加载速度。
- **图像压缩**：智能压缩算法，减少文件大小而不显著降低质量，适用于 Web 开发和移动应用。
- **批量处理**：一次性处理多个图像文件，支持文件夹导入和导出。
- **自动化脚本支持**：集成 Node.js 环境，可通过脚本自定义处理流程。
- **插件扩展**：提供插件接口，便于用户扩展自定义功能，如水印添加或滤镜应用。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统运行。

## 主要功能
- **格式优化**：自动检测并优化图像格式，例如将 PNG 转换为 WebP 以提升网页性能。
- **质量控制**：用户可设置压缩质量级别（低、中、高），并预览效果。
- **元数据处理**：移除或编辑图像的 EXIF 元数据，保护隐私。
- **集成 CLI**：命令行界面（CLI）支持，便于 CI/CD 管道集成。
- **GUI 界面**：图形用户界面（GUI）版本，提供拖拽式操作，适合非开发者用户。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/imgcook/imove.git`
   - 进入目录：`cd imove`
   - 安装依赖：`npm install`

2. **CLI 用法**（命令行）：
   - 基本转换：`imove convert input.jpg output.webp --quality 80`
   - 批量压缩：`imove batch /path/to/folder --format webp --compress`
   - 帮助：`imove --help`

3. **GUI 用法**（图形界面）：
   - 运行：`npm start` 或双击可执行文件。
   - 拖拽图像或文件夹到界面，选择输出格式和选项，点击“处理”。

4. **自定义脚本**：
   - 编辑 `config.js` 文件定义处理规则。
   - 运行：`node process.js`

详细文档请参考项目 README.md 文件。