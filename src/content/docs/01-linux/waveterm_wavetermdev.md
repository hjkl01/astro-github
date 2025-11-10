---
title: waveterm
---

# waveterm

项目地址: https://github.com/wavetermdev/waveterm

## 项目简介
waveterm 是一个现代化的终端模拟器，采用 Electron + xterm.js 构建，目标是提供轻量、可定制、跨平台的终端体验。它支持多标签、分屏、SSH/SFTP、插件化扩展、主题切换等功能。

## 主要特性
- **多标签与分屏**：支持在同一窗口打开多个终端会话，支持水平/垂直拆分。
- **SSH / SFTP**：内置 SSH 客户端，支持文件传输、目录同步。
- **插件系统**：通过插件机制扩展功能，例如自动补全、脚本执行等。
- **主题与皮肤**：内置多种主题，可自由切换；支持自定义配色。
- **快捷键与命令行**：提供丰富的快捷键，支持自定义快捷键。
- **弹性布局**：可拖拽调整终端窗口大小，支持最大化/恢复。

## 功能概览
| 功能 | 描述 |
|------|------|
| **终端交互** | 直接在应用中执行 shell 命令，支持多种 shell（bash, zsh, powershell 等）。 |
| **文件管理** | 通过 SFTP 在终端内浏览、上传、下载文件。 |
| **插件开发** | 通过提供的 API 开发自定义插件，添加新功能。 |
| **配置管理** | 支持 JSON/YAML 配置文件，便于自动化部署。 |

## 快速使用
1. **克隆仓库**  
   ```bash
   git clone https://github.com/wavetermdev/waveterm.git
   cd waveterm
   ```

2. **安装依赖**  
   ```bash
   npm install
   ```

3. **运行**  
   ```bash
   npm start
   ```

4. **打包**  
   ```bash
   npm run build
   ```

5. **配置 SSH**  
   在 `~/.waveterm/ssh_config.json` 添加 SSH 连接信息，启动后即可通过 GUI 连接。

## 文档与支持
- **官方文档**：见仓库根目录的 `README.md` 与 `docs/` 目录。  
- **社区支持**：在 GitHub Issues 讨论问题，或加入官方 Discord/Slack。  

## 结语
waveterm 旨在以现代化 UI 提供稳定、高效的终端体验，适合开发者、系统管理员甚至日常使用。欢迎贡献代码或提交 Issue。