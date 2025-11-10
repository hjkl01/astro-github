---
title: typst
---


# typst

> 项目地址: <https://github.com/typst/typst>

## 项目简介
Typst 是一款现代化、类型安全的排版系统，旨在为技术文档、论文、书籍等提供简洁、高效、可声明的写作体验。它使用类似 LaTeX 的语法，但拥有更友好的错误提示、更快的编译速度以及更易扩展的插件机制。

## 主要特性
| 特色 | 描述 |
|------|------|
| **语法清晰** | 类似 Markdown 的直观写法，减少排版逻辑的学习成本 |
| **强类型系统** | 内置严格类型检查，编译时报错定位更精准 |
| **模块化布局** | 支持自定义页面布局、分栏、表格、列表等多种排版模式 |
| **数学公式** | 原生支持 Unicode、LaTeX 风格公式，生成高质量 PDF |
| **图形绘制** | 原生图形编辑（坐标系、路径、渲染）与外部图像融合 |
| **跨平台** | 支持 Windows、macOS、Linux，生成 PDF、HTML、SVG 等输出 |
| **插件生态** | 通过 `typst.toml` 轻松集成 Markdown、SVG、Image 等插件 |
| **官方支持** | 位置、尺寸、颜色、边距等属性支持 CSS-like 语法，易于自定义 |

## 主要功能
- **文本排版**：段落、标题、列表、引用、代码块等。
- **数学排版**：公式编号、对齐、分数、根式、矩阵等。
- **表格与列表**：多列表格、长表格分页、项目符号列表、编号列表。
- **图形绘制**：使用 `draw`、`path` 等指令绘制矢量图形。
- **页面设置**：页边距、纸张大小、章节页眉页脚自定义。
- **引用与索引**：交叉引用、目录、索引、索引关键词。
- **图片嵌入**：支持 PNG、JPEG、SVG、TIFF 等格式。
- **代码高亮**：内置或通过插件实现多语言语法高亮。

## 基本用法

1. **安装**  
   ```bash
   cargo install typst
   ```

2. **编写文档**  
   ```typst
   #title My Document
   #author Alice

   #h1 创建 Typst 文档

   Typst 允许你使用类似于 Markdown 的语法编写文档。以下是一个简单示例：

   #h2 文本段落
   这是一个普通的段落。

   #h2 列表
   - 项目一
   - 项目二

   #h2 数学公式
   \[
     E = mc^2
   \]
   ```

3. **编译生成 PDF**  
   ```bash
   typst compile main.typ
   ```

4. **插件使用**  
   在项目根目录下创建 `typst.toml`，配置插件。  
   ```toml
   # typst.toml
   [plugins]
   markdown = { path = "node_modules/typst-plugin-md" }
   ```

5. **查看帮助**  
   ```bash
   typst --help
   ```

## 快速上手实例

```typst
#title Typst 快速入门
#author Typst 社区

#h1 章节 1: 文本段落
这是第一段文字，包含 **加粗**、*斜体* 与 `代码`。

#h2 章节 2: 列表
- 动态列表
- 可交互

#h2 章节 3: 数学公式
\[
f(x) = \int_{0}^{x} e^{-t^2} dt
\]

#h2 章节 4: 图片
#image{example.png}
```

> 运行 `typst compile example.typ` 可得到 PDF 输出。

## 结语
Typst 集成了现代排版、类型安全与插件化的优势，适用于学术论文、技术手册、书籍与短文档的快速排版。欢迎在 GitHub 上查看源码、提交 issue 或 PR，参与社区共建。