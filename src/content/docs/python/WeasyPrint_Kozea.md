---
title: WeasyPrint
---

# WeasyPrint 项目

## 项目地址
[https://github.com/Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint)

## 主要特性
WeasyPrint 是一个开源的 Python 库，用于将 HTML 和 CSS 转换为 PDF 文档。它严格遵守 CSS 标准，支持现代 Web 布局技术，如 Flexbox、Grid 和浮动布局。主要特性包括：
- **高保真渲染**：基于 Web 标准生成 PDF，确保输出与浏览器渲染一致。
- **CSS 支持**：全面支持 CSS2 和 CSS3 规范，包括媒体查询、字体嵌入和页面边距。
- **图像和资源处理**：自动处理本地和远程图像、SVG 和其他 Web 资源。
- **可扩展性**：支持自定义字体、颜色管理和页面断点控制。
- **无依赖浏览器**：无需安装浏览器引擎，纯 Python 实现，依赖 Cairo 和 Pango 等库。
- **开源免费**：MIT 许可，适用于个人和商业项目。

## 主要功能
- **HTML 到 PDF 转换**：将 HTML 文件或字符串直接转换为 PDF，支持复杂的样式和布局。
- **样式应用**：应用 CSS 样式表，实现打印友好布局，如页眉、页脚和分页。
- **资源嵌入**：自动嵌入字体、图像和样式，生成独立的 PDF 文件。
- **批量处理**：支持脚本化处理多个文档，适合自动化工作流。
- **调试工具**：提供调试模式，检查渲染问题和 CSS 应用。

## 用法
WeasyPrint 可以通过 pip 安装：`pip install weasyprint`。基本用法如下（Python 代码示例）：

```python
from weasyprint import HTML

# 从 HTML 文件生成 PDF
HTML('input.html').write_pdf('output.pdf')

# 从 HTML 字符串生成 PDF
html_content = '<html><body><h1>Hello, WeasyPrint!</h1></body></html>'
HTML(string=html_content).write_pdf('output.pdf')

# 应用 CSS 样式
css = 'h1 { color: red; }'
HTML('input.html').with_stylesheet(css).write_pdf('output.pdf')

# 高级选项：指定页面大小和方向
HTML('input.html').write_pdf('output.pdf', stylesheets=None, 
                             page_size='A4', 
                             orientation='portrait')
```

更多用法详见官方文档：https://weasyprint.readthedocs.io/。需安装系统依赖如 Cairo 和 Pango（Linux: `apt install python3-dev build-essential libcairo2-dev libpango1.0-dev`）。