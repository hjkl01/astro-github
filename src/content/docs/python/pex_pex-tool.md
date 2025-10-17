
---
title: pex
---

# PEX 项目描述

## 项目地址
[https://github.com/pex-tool/pex](https://github.com/pex-tool/pex)

## 主要特性
PEX（Python Executable）是一个用于创建独立的Python可执行文件的工具包。它将Python脚本及其依赖项打包成单个文件，便于分发和运行，而无需安装Python环境。主要特性包括：
- **单文件打包**：将Python代码、解释器和依赖库打包成一个独立的二进制文件，支持Windows、macOS和Linux平台。
- **跨平台支持**：生成的可执行文件可在目标平台上直接运行，无需额外的Python安装。
- **依赖管理**：自动处理pip安装的第三方库，确保所有依赖被包含在内。
- **轻量级**：生成的executable文件相对紧凑，适合小型应用和工具分发。
- **自定义选项**：支持添加图标、设置入口点、排除不必要的模块等高级配置。

## 主要功能
- **打包Python脚本**：将.py文件转换为.exe（Windows）或其他平台的executable。
- **处理虚拟环境**：集成venv或conda环境，简化依赖打包。
- **命令行工具**：提供CLI接口，便于自动化构建过程。
- **版本兼容**：支持Python 3.x版本，确保生成的executable与原脚本行为一致。
- **调试支持**：可选包含调试信息，便于问题排查。

## 用法
### 安装
首先克隆仓库并安装依赖：
```
git clone https://github.com/pex-tool/pex.git
cd pex
pip install -r requirements.txt
```

### 基本用法
1. **创建PEX文件**：
   使用命令行工具打包脚本：
   ```
   pex -m mymodule -o myapp.pex my_script.py
   ```
   - `-m`：指定入口模块。
   - `-o`：输出文件路径。
   - 示例：打包一个简单的脚本`hello.py`（print("Hello, World!")）：
     ```
     pex -o hello.pex hello.py
     ```

2. **运行PEX文件**：
   直接执行生成的.pex文件：
   ```
   ./hello.pex  # Linux/macOS
   hello.pex    # Windows
   ```

3. **高级选项**：
   - 添加依赖：`pex -r requirements.txt -o app.pex main.py`
   - 平台指定：`pex --platform=linux-x86_64 -o app.pex script.py`
   - 包含资源：`pex --include-resources=images/* -o app.pex script.py`

更多细节请参考项目README文档。