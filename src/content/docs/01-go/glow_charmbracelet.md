
---
title: glow
---


# Charmbracelet Glow

> 项目地址: https://github.com/charmbracelet/glow

## 简介
Charmbracelet Glow 是一个轻量级的命令行 Markdown 渲染器，直接在终端中将 Markdown 文档渲染为美观的彩色输出，兼容多种终端环境。

## 主要特性
- **轻量 & 纯 Go**：不依赖外部二进制，可直接交叉编译发布。
- **终端主题**：支持多种终端主题（如 `light`, `dark`, `dracula` 等）。
- **高亮代码**：内置多语言高亮支持。
- **表格与图像**：渲染 Markdown 表格及支持 `alfred` 之类的图片占位符。
- **哈希排名**：支持 `table of contents` 与页面跳转。
- **自动缩进与格式化**：自带高级 Markdown 语法解析。

## 功能
| 功能 | 说明 |
|------|------|
| `glow file.md` | 渲染单个 Markdown 文件 |
| `glow -theme dracula file.md` | 指定终端主题 |
| `glow --linkify` | 自动将 URL 变成可点击链接 |
| `glow --max-width 80` | 限制输出宽度 |
| `glow -o out.txt file.md` | 将渲染结果输出到文件 |
| `glow -D` | 启用调试模式，展示内部解析过程 |
| `glow -V` | 查看版本信息 |

## 安装与使用
```bash
# 安装（Go）
go install github.com/charmbracelet/glow@latest

# 使用示例
glow README.md          # 渲染 README.md
glow -theme dracula README.md
glow -o rendered.txt README.md
```

## 进一步使用
- 支持 pipe 方式：`cat file.md | glow`
- 可作为其他程序的渲染后端，例如：`glow -t` 可以生成只含 Markdown 标题的目录

---

> 更多信息请参见官方文档或 GitHub 仓库。 

