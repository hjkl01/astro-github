
---
title: box
---

# Box 项目

## 项目地址
[https://github.com/liu673cn/box](https://github.com/liu673cn/box)

## 主要特性
- **简洁设计**：项目采用模块化结构，便于扩展和维护。
- **跨平台支持**：兼容多种操作系统，包括 Windows、macOS 和 Linux。
- **高效性能**：优化了核心算法，确保在处理大量数据时响应迅速。
- **开源许可**：基于 MIT 许可，允许自由使用和修改。

## 主要功能
- **数据打包**：支持将文件或目录打包成压缩格式，便于传输和存储。
- **解压工具**：提供一键解压功能，支持多种压缩算法如 ZIP 和 TAR。
- **命令行接口**：内置 CLI 工具，允许通过终端快速操作。
- **图形界面**：可选的 GUI 模式，适合非技术用户使用。

## 用法
1. **安装**：克隆仓库后，使用 `pip install -r requirements.txt` 安装依赖。
2. **基本命令**：
   - 打包：`box pack source_dir output.zip`
   - 解压：`box unpack input.zip target_dir`
3. **GUI 模式**：运行 `box gui` 启动图形界面，选择文件进行操作。
4. **高级选项**：使用 `--help` 查看更多参数，如加密支持 `--encrypt password`。