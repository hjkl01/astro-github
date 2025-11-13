---
title: atuin
---

# Atuin 项目

## 项目地址

[GitHub 项目地址](https://github.com/atuinsh/atuin)

## 主要特性

- **魔幻 Shell 历史**：将现有 shell 历史替换为 SQLite 数据库，记录额外上下文。
- **加密同步**：可选的全加密同步，在机器之间同步历史记录。
- **跨平台**：支持多种 shell，如 zsh、bash、fish、nushell、xonsh。
- **统计分析**：计算统计数据，如最常用命令。
- **搜索界面**：全屏历史搜索 UI，支持过滤模式。
- **Quick-jump**：使用 Alt+数字快速跳转到之前项目。
- **Filter modes**：通过 Ctrl+R 切换过滤模式；仅从当前会话、目录或全局搜索历史。
- **Execute and edit**：Enter 执行命令，Tab 编辑命令。

## 主要功能

- **历史记录**：存储命令、退出码、持续时间、时间、主机名等。
- **搜索和导航**：使用 Ctrl+R 搜索历史，按 Alt+数字跳转到之前项目。
- **同步**：通过 Atuin 服务器加密同步历史（可选自托管）。
- **导入历史**：从现有 shell 历史文件导入。
- **统计**：查看最常用命令等统计信息。

## 用法

1. **安装**：
   - 使用官方安装脚本：`curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh`
   - 或使用包管理器：`cargo install atuin`（Rust），或从 [GitHub Releases](https://github.com/atuinsh/atuin/releases) 下载。

2. **注册和同步**（可选）：
   - `atuin register -u <USERNAME> -e <EMAIL>`
   - `atuin import auto`
   - `atuin sync`

3. **基本使用**：
   - 重启 shell 后，Ctrl+R 打开搜索界面。
   - 使用箭头键导航，Enter 执行命令，Tab 编辑。
   - 使用 Alt+数字跳转到之前项目。
   - 通过 Ctrl+R 切换过滤模式。

4. **高级用法**：
   - 搜索特定命令：`atuin search --exit 0 make`
   - 查看统计：`atuin stats`

更多细节请参考 [官方文档](https://docs.atuin.sh/) 和 GitHub 仓库的 README 文件。
