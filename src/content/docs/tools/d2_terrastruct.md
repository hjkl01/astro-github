---
title: d2
---

# D2 项目

## 项目地址
[https://github.com/terrastruct/d2](https://github.com/terrastruct/d2)

## 主要特性
D2 是一个现代化的声明式绘图语言和工具集，专为创建图表、架构图和流程图而设计。它采用声明式语法，用户只需描述图形的结构和关系，而无需手动布局。核心特性包括：
- **声明式语法**：使用简单文本描述图形元素及其连接，自动处理布局。
- **多语言支持**：支持多种输出格式，如 SVG、PNG、PDF 等，便于集成到文档或网页中。
- **主题和自定义**：内置主题系统，支持自定义颜色、形状和样式。
- **集成友好**：可作为 CLI 工具、库或 VS Code 插件使用，支持 Markdown 和其他编辑器。
- **开源免费**：基于 Apache 2.0 许可，社区驱动开发。

## 主要功能
- **自动布局**：使用先进的布局算法（如 DAG 布局）自动排列节点和边，避免手动调整。
- **形状支持**：内置多种形状（如矩形、圆形、数据库图标），并支持自定义图标。
- **连接和标签**：轻松定义节点间的箭头连接，并添加标签、注释。
- **动画和交互**：生成支持动画的图表，或导出为交互式格式。
- **脚本化和批量处理**：通过脚本生成复杂图表，适用于 CI/CD 管道或自动化文档。
- **插件生态**：支持扩展，如 Terraform、Kubernetes 等领域的专用插件。

## 用法
### 安装
1. 通过 Homebrew（macOS/Linux）：`brew install d2`
2. 通过 Go：`go install oss.terrastruct.com/d2@latest`
3. 下载预编译二进制文件从 GitHub Releases。

### 基本用法
1. **创建图表文件**：新建 `.d2` 文件，例如 `example.d2`：
   ```
   example: {
     shape: rectangle
   }
   db: {
     shape: cylinder
   }
   example -> db: connects to
   ```
   这将创建一个名为 "example" 的矩形节点连接到 "db" 的圆柱节点。

2. **渲染图表**：运行命令 `d2 example.d2 example.svg` 生成 SVG 文件。支持其他格式如 `d2 example.d2 example.png`。

3. **编辑器集成**：在 VS Code 中安装 D2 插件，即时预览和编辑。

4. **高级用法**：
   - 使用主题：`d2 -t dark example.d2 output.svg`。
   - 批量渲染：`d2 run *.d2` 处理多个文件。
   - 嵌入 Markdown：使用 `d2 -l markdown example.d2` 生成 Markdown 兼容输出。

更多细节请参考官方文档：https://d2lang.com/