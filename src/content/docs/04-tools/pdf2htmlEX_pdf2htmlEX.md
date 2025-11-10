---
title: pdf2htmlEX
---

# pdf2htmlEX 项目

## 项目地址
[https://github.com/pdf2htmlEX/pdf2htmlEX](https://github.com/pdf2htmlEX/pdf2htmlEX)

## 主要特性
pdf2htmlEX 是一个开源工具，用于将 PDF 文件转换为 HTML 格式。它专注于保留 PDF 的视觉布局、字体、图像和结构，支持高保真度的转换。主要特性包括：
- **像素级精确渲染**：生成的 HTML 页面在视觉上与原 PDF 几乎相同，支持缩放而不失真。
- **字体嵌入**：自动嵌入 PDF 中的字体，确保跨平台一致性。
- **图像和矢量图形支持**：保留 PDF 中的图像、渐变和路径，支持 SVG 输出。
- **多页支持**：处理多页 PDF，并生成独立的 HTML 文件或单文件输出。
- **CSS 优化**：使用 CSS3 实现布局和样式，兼容现代浏览器。
- **轻量级输出**：生成的 HTML 文件体积较小，便于网页集成。
- **跨平台兼容**：支持 Linux、macOS 和 Windows（通过构建）。

## 主要功能
- **PDF 到 HTML 转换**：核心功能是将 PDF 文档转换为可交互的 HTML，支持文本选择、搜索和打印。
- **布局保留**：保持原 PDF 的页面布局、列式结构和边距。
- **元数据处理**：提取 PDF 元数据，如标题、作者，并嵌入 HTML。
- **自定义选项**：支持调整分辨率、背景颜色、页面大小等参数。
- **批量处理**：可通过脚本处理多个 PDF 文件。
- **集成支持**：适用于网页应用、文档管理系统或静态站点生成。

## 用法
pdf2htmlEX 需要编译安装（依赖 C++ 和相关库，如 Poppler 和 Cairo）。安装后，使用命令行工具 `pdf2htmlEX` 执行转换。

### 基本用法
1. **安装**：从 GitHub 克隆仓库，遵循 README 中的构建指南（例如，使用 CMake 和 Make）。
2. **简单转换**：
   ```
   pdf2htmlEX input.pdf output.html
   ```
   这将生成 `output.html` 文件及其相关资源（如 CSS 和图像）。

3. **常用选项**：
   - `-s`：单文件输出（所有页面合并到一个 HTML）。
   - `--zoom 1.3`：设置缩放比例（默认 1.3）。
   - `--page 1-5`：仅转换指定页面范围。
   - `--dest-dir ./output`：指定输出目录。
   - `--optimize-images`：优化图像以减小文件大小。
   - 示例：
     ```
     pdf2htmlEX --zoom 1.5 --dest-dir ./html_out input.pdf
     ```

详细用法请参考项目 README 和 man 页。适用于开发者或需要 PDF 网页化的场景。