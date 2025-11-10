---
title: open-notebook
---


# Open Notebook（lfnovo/open-notebook）

**项目地址**: https://github.com/lfnovo/open-notebook

## 主要特性

- **多语言支持**：支持中文、英文、日语等多种语言的笔记内容。
- **Markdown 编辑**：内置 Markdown 语法高亮与预览，支持图像、表格、代码块等。
- **实时同步**：通过 GitHub Gist 或自建服务器实现笔记的云同步。
- **插件化架构**：可通过插件扩展功能，如导出为 PDF、生成目录、代码执行等。
- **离线模式**：本地存储笔记，网络不佳时仍可编辑。

## 主要功能

| 功能 | 说明 |
|------|------|
| 创建/编辑笔记 | 支持 Markdown 语法、代码高亮、图片插入 |
| 版本控制 | 通过 Git 自动提交，支持查看历史版本 |
| 搜索 | 全文搜索、标签搜索 |
| 导出 | PDF、HTML、Markdown 原始文件 |
| 扩展插件 | 代码运行、图表绘制、任务管理等 |
| 主题切换 | 多种主题可选，支持自定义 CSS |
| 共享 | 通过 Gist 或自建服务器分享笔记链接 |

## 用法

1. **安装**  
   ```bash
   npm install -g open-notebook
   ```

2. **初始化仓库**  
   ```bash
   open-notebook init
   ```

3. **创建笔记**  
   ```bash
   open-notebook new "My First Note"
   ```

4. **编辑笔记**  
   ```bash
   open-notebook edit "My First Note"
   ```

5. **同步**  
   ```bash
   open-notebook sync
   ```

6. **导出**  
   ```bash
   open-notebook export "My First Note" --format pdf
   ```

7. **插件使用**  
   ```bash
   open-notebook plugin install <plugin-name>
   ```

## 配置文件

- `config.yaml`：全局配置（同步地址、主题、插件等）
- `notes/`：存放所有笔记文件
- `plugins/`：插件目录

> 详细使用说明请参阅项目文档或 `open-notebook --help`。  
