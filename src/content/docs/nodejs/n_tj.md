---
title: n
---

# n 项目

## 项目地址
[https://github.com/tj/n](https://github.com/tj/n)

## 主要特性
- **Node.js 版本管理器**：n 是一个简单高效的工具，用于在同一系统上安装和管理多个 Node.js 版本。
- **轻量级设计**：无需复杂的依赖或全局安装，支持快速切换 Node.js 版本。
- **跨平台支持**：适用于 macOS、Linux 和 Windows（通过 WSL 或类似环境）。
- **自动下载与安装**：从官方 Node.js 源自动获取并安装指定版本，支持 LTS 和稳定版。
- **版本隔离**：每个 Node.js 版本独立安装，避免版本冲突。

## 主要功能
- 安装特定 Node.js 版本。
- 切换当前活跃的 Node.js 版本。
- 列出已安装的版本。
- 卸载不需要的版本。
- 支持使用 `.nvmrc` 文件自动切换版本（类似于 nvm）。

## 用法
1. **安装 n**：
   ```bash
   curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n
   bash n
   ```

2. **安装最新稳定版 Node.js**：
   ```bash
   n stable
   ```

3. **安装特定版本**：
   ```bash
   n 18.17.0  # 示例版本
   ```

4. **切换到指定版本**：
   ```bash
   n use 18.17.0
   ```

5. **列出已安装版本**：
   ```bash
   n
   ```

6. **卸载版本**：
   ```bash
   n uninstall 18.17.0
   ```

7. **安装 LTS 版本**：
   ```bash
   n lts
   ```

更多详情请参考项目 README。