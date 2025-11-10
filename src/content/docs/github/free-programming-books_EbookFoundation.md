---
title: free-programming-books
---

# EbookFoundation/free-programming-books

**项目地址**  
<https://github.com/EbookFoundation/free-programming-books>

## 项目简介
- 一个聚合了大量免费编程书籍与资料的开源项目。  
- 由社区维护，涵盖 50+ 编程语言、数据结构、算法、机器学习等领域。  
- 采用 Markdown 结构化列表，便于搜索与离线阅读。

## 主要特性
1. **完整分类**  
   - 按语言、技术方向、难度级别划分，目录层级清晰。  
2. **丰富资源**  
   - 官方书籍、PDF、EPUB、网页版、视频教程等多种格式。  
   - 兼顾国内与国外教材。  
3. **社区维护**  
   - 通过 Issue 或 PR 提交更新、纠错、补全链接。  
   - `CONTRIBUTING.md` 指导贡献流程。  
4. **离线可读**  
   - 直接克隆后即可在任何 Markdown 阅读器中浏览。  
   - 可生成打印版 PDF 或 DOCX。  
5. **多平台链接**  
   - 支持 GitHub Gist、Google Drive、Amazon S3 等托管方式。  
   - 结构对应 `[link]` 与 `[download]`。

## 目录结构示例
```
free-programming-books/
├─ README.md
├─ CONTRIBUTING.md
├─ license.md
├─ 01-programming-languages/
│   ├─ python/
│   │  ─ _books.md
│   │   └─ _index.md
│   └─ java/
│       ├─ _books.md
│       └─ _index.md
└─ 02-misc/
    ├─ _books.md
    └─ _index.md
```

每个主题文件（如 `_books.md`）包含：
```markdown
- [《Effective Python》](https://link) – 经典 Python 编程技巧  
- [《JavaScript: The Good Parts》](https://link) – JS 核心理念
```

## 如何使用
1. **克隆仓库**  
   ```bash
   git clone https://github.com/EbookFoundation/free-programming-books.git
   ```

2. **阅读内容**  
   - 打开根目录的 `README.md`，获取整体目录。  
   - 按需打开对应语言文件夹中的 `_books.md` 查看书籍列表。

3. **离线阅读**  
   - 用 VSCode / Typora / Mark Text 打开 Markdown 文件。  
   - 或使用 Pandoc 转为 PDF：  
     ```bash
     pandoc README.md -o free_programming_books.pdf
     ```

4. **贡献内容**  
   - Fork → 修改文件 → 提交 PR，遵循 `CONTRIBUTING.md` 指南。  

5. **搜索功能**  
   - 克隆后使用 `ripgrep`：  
     ```bash
     rg "机器学习" .
     ```

## 其它资源
- 官方网站: <https://github.com/EbookFoundation/free-programming-books>  
- 讨论区: <https://github.com/EbookFoundation/free-programming-books/discussions>  
- 语义化标签: `free-books`, `open-source`, `programming guide`

> 该项目持续更新，欢迎社区成员一起完善。