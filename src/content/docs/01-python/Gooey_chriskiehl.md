
---
title: Gooey
---

# Gooey 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/chriskiehl/Gooey)

## 主要特性
Gooey 是一个 Python 库，用于将命令行界面 (CLI) 应用程序快速转换为图形用户界面 (GUI)，无需编写额外的代码。它基于 Tkinter 构建，支持跨平台运行。主要特性包括：
- **自动 GUI 生成**：通过简单的装饰器 `@gooey` 即可将 CLI 脚本转换为 GUI 应用。
- **参数解析集成**：无缝支持 argparse 等参数解析库，自动生成输入框、复选框、下拉菜单等控件。
- **自定义选项**：允许自定义窗口标题、图标、布局和默认值，提高用户体验。
- **简单易用**：零学习曲线，适合 CLI 开发者快速添加 GUI 支持。
- **跨平台兼容**：在 Windows、macOS 和 Linux 上运行良好。

## 主要功能
- **CLI 到 GUI 转换**：将命令行脚本的输入参数转化为图形界面元素，如文本输入、文件选择器、进度条等。
- **进度指示**：支持显示运行进度条，适用于长时间运行的任务。
- **错误处理**：内置异常捕获和用户友好错误提示。
- **输出重定向**：将 CLI 输出重定向到 GUI 的文本区域，便于查看结果。
- **多语言支持**：易于国际化，但默认英文界面。

## 用法
1. **安装**：
   使用 pip 安装库：
   ```
   pip install gooey
   ```

2. **基本用法**：
   - 导入库并使用装饰器装饰主函数。
   - 示例代码（Python 脚本）：
     ```python
     from gooey import Gooey
     import argparse

     @Gooey(required_cols=2, program_name="我的 CLI 工具")
     def main(input_file: str, output_dir: str):
         # 你的 CLI 逻辑代码
         print(f"处理文件: {input_file}")
         # ... 其他操作

     if __name__ == '__main__':
         parser = argparse.ArgumentParser()
         parser.add_argument('input_file', help='输入文件路径')
         parser.add_argument('--output_dir', default='output', help='输出目录')
         main(parser.parse_args())
     ```
   - 运行脚本：`python your_script.py`，它将自动弹出 GUI 窗口。

3. **高级用法**：
   - 添加进度：使用 `gooey.progress` 上下文管理器更新进度条。
   - 自定义菜单：通过 `Gooey` 参数配置菜单项和分组。
   - 文件选择：自动检测文件路径参数并提供浏览按钮。

更多细节请参考项目文档和示例。