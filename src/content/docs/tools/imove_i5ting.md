---
title: imove
---

# iMove 项目描述

## 项目地址
[https://github.com/i5ting/imove](https://github.com/i5ting/imove)

## 主要特性
iMove 是一个基于 Node.js 的工具，用于批量移动和管理文件。它支持递归扫描目录、过滤文件类型，并提供高效的文件迁移功能。主要特性包括：
- **批量文件移动**：支持根据规则（如文件扩展名、日期或自定义过滤器）批量移动文件到指定目录。
- **递归扫描**：自动遍历子目录，处理嵌套文件夹中的文件。
- **过滤与重命名**：内置文件过滤器，可根据模式排除或包含特定文件，并支持自动重命名以避免冲突。
- **进度监控**：实时显示移动进度和统计信息，便于跟踪大批量操作。
- **配置灵活**：通过 JSON 配置文件定义移动规则，支持命令行参数覆盖。
- **跨平台支持**：兼容 Windows、macOS 和 Linux 系统。

## 功能
- **文件迁移**：核心功能是将源目录的文件移动到目标目录，支持覆盖或跳过现有文件。
- **日志记录**：生成详细日志，记录移动操作的成功、失败和跳过情况，便于审计。
- **干跑模式**：模拟移动过程而不实际执行，用于测试规则的有效性。
- **插件扩展**：可通过自定义脚本扩展功能，如集成云存储或数据库记录。
- **错误处理**：自动处理权限问题、路径不存在等常见错误，并提供重试机制。

## 用法
1. **安装**：
   - 确保安装 Node.js（版本 >= 10）。
   - 克隆仓库：`git clone https://github.com/i5ting/imove.git`
   - 进入目录：`cd imove`
   - 安装依赖：`npm install`

2. **配置**：
   - 创建 `config.json` 文件，示例：
     ```json
     {
       "source": "/path/to/source/dir",
       "target": "/path/to/target/dir",
       "filter": "*.jpg|*.png",
       "recursive": true,
       "dryRun": false
     }
     ```
     - `source`：源目录路径。
     - `target`：目标目录路径。
     - `filter`：文件过滤模式（使用 `|` 分隔扩展名）。
     - `recursive`：是否递归子目录。
     - `dryRun`：是否仅模拟运行。

3. **运行**：
   - 基本命令：`npm start`（使用默认配置）。
   - 指定配置：`node index.js --config custom.json`。
   - 命令行覆盖：`node index.js --source /src --target /dst --filter "*.txt" --dry-run`。
   - 查看帮助：`node index.js --help`。

使用前确保目标目录有写权限。项目适用于照片、文档等文件的组织管理，适合开发者或系统管理员使用。