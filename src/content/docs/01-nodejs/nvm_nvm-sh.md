---
title: nvm
---

# NVM 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/nvm-sh/nvm)

## 主要特性
NVM (Node Version Manager) 是一个用于管理 Node.js 版本的工具，主要特性包括：
- **多版本支持**：允许用户在同一系统上安装和管理多个 Node.js 版本，并轻松切换。
- **自动切换**：根据当前项目目录自动切换到指定的 Node.js 版本（通过 `.nvmrc` 文件）。
- **易于安装和卸载**：支持从源代码或二进制包安装 Node.js 版本，并可轻松移除不需要的版本。
- **兼容性强**：支持 Unix-like 系统（如 Linux、macOS）和 Windows（通过 nvm-windows 变体）。
- **开源免费**：基于 Bash 脚本实现，轻量级且无外部依赖。

## 主要功能
- **安装 Node.js 版本**：下载并安装特定版本的 Node.js，包括 LTS（长期支持）版本和最新版本。
- **版本管理**：列出已安装版本、设置默认版本、切换当前使用的版本。
- **npm 集成**：每个 Node.js 版本对应独立的 npm 环境，避免版本冲突。
- **项目级配置**：通过 `.nvmrc` 文件指定项目所需的 Node.js 版本，实现团队协作一致性。
- **别名支持**：为常用版本创建别名，便于快速访问。

## 用法
### 安装 NVM
1. 对于 Unix-like 系统，运行以下命令：
   ```
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   ```
   或使用 wget：
   ```
   wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   ```
2. 重启终端或运行 `source ~/.bashrc`（或对应 shell 配置文件）以加载 NVM。

### 基本命令
- **安装 Node.js 版本**：`nvm install <version>`（例如：`nvm install 18.17.0` 或 `nvm install --lts`）。
- **使用特定版本**：`nvm use <version>`（例如：`nvm use 18.17.0`）。
- **设置默认版本**：`nvm alias default <version>`。
- **列出已安装版本**：`nvm list` 或 `nvm ls`。
- **列出可用版本**：`nvm ls-remote`。
- **卸载版本**：`nvm uninstall <version>`。
- **在项目中使用**：在项目根目录创建 `.nvmrc` 文件，写入所需版本（如 `18.17.0`），然后运行 `nvm use` 自动切换。

更多详情请参考项目 README。