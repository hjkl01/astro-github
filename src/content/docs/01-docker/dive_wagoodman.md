---
title: dive
---

# Dive 项目

**GitHub 项目地址:** [https://github.com/wagoodman/dive](https://github.com/wagoodman/dive)

## 主要特性
Dive 是一个命令行工具，用于分析 Docker 镜像，帮助用户可视化和理解镜像的内部结构。它专注于 Docker 镜像的安全性和优化，提供直观的界面来检查镜像层、文件变更和潜在问题。主要特性包括：
- **可视化镜像层分析**：以树状视图显示每个镜像层的文件变更，包括添加、删除和修改的文件。
- **性能优化建议**：识别不必要的文件、重复层和潜在的安全漏洞，帮助减少镜像大小和构建时间。
- **交互式界面**：支持键盘导航和搜索，类似于文件浏览器，便于深入检查镜像内容。
- **支持多平台**：兼容 Linux、macOS 和 Windows，支持 Docker 和 OCI 镜像格式。
- **无依赖安装**：轻量级工具，通过二进制文件直接运行，无需额外依赖。

## 主要功能
- **镜像分析**：分解 Docker 镜像的每一层，显示文件系统变更、层大小和效率评分。
- **变更比较**：比较相邻层之间的差异，突出浪费的空间（如未使用的包或临时文件）。
- **安全扫描**：检测常见的安全问题，如 root 用户运行或敏感文件暴露。
- **导出报告**：生成 JSON 或文本报告，用于 CI/CD 管道集成。
- **批量处理**：支持分析多个镜像或标签。

## 用法
Dive 的用法简单，通过命令行运行。前提是安装 Docker 并确保 Dive 已下载（从 GitHub Releases 获取二进制文件）。

### 基本安装
- 下载最新版本的二进制文件，例如：
  ```
  curl -L https://github.com/wagoodman/dive/releases/latest/download/dive_*.tar.gz | tar -xz
  sudo mv dive /usr/local/bin/
  ```

### 基本用法
1. **分析单个镜像**：
   ```
   dive <image-name:tag>
   ```
   示例：`dive nginx:latest`  
   这将打开交互界面，按 `?` 查看帮助，按 `Esc` 退出。

2. **指定镜像 ID**：
   ```
   dive <image-id>
   ```

3. **非交互模式（仅报告）**：
   ```
   dive --no-ui <image-name:tag>
   ```

4. **自定义配置**：
   - 使用配置文件：`dive --config <config-file> <image-name>`  
     配置选项包括颜色主题、层过滤等。
   - 导出 JSON：`dive --json > report.json <image-name>`

5. **CI/CD 集成**：
   在脚本中运行：`dive myapp:latest || exit 1`（如果效率评分低于阈值则失败）。

更多细节请参考项目 README。