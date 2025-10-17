
---
title: code-server
---

# code-server 项目

## 项目地址
[GitHub 项目地址](https://github.com/coder/code-server)

## 主要特性
code-server 是一个开源项目，它允许用户在浏览器中运行 Visual Studio Code (VS Code)，无需安装桌面版本。主要特性包括：
- **浏览器访问**：通过 Web 界面在任何设备上访问完整的 VS Code 编辑器，支持远程开发。
- **自托管**：用户可以轻松在自己的服务器、Docker 容器或本地机器上部署，支持 Linux、macOS 和 Windows。
- **扩展支持**：兼容 VS Code 的所有扩展，包括语言服务器、主题和调试工具。
- **安全性**：内置认证和 HTTPS 支持，确保远程访问的安全性。
- **性能优化**：支持 GPU 加速和资源隔离，适合开发和团队协作。
- **跨平台**：无需本地安装 VS Code，即可在浏览器中实现代码编辑、终端使用和 Git 集成。

## 主要功能
- **代码编辑**：提供完整的 VS Code 体验，包括语法高亮、自动完成、代码折叠和多标签编辑。
- **终端集成**：内置终端，支持 shell 命令执行、任务运行和调试。
- **协作功能**：支持实时协作编辑（通过扩展），适用于团队开发。
- **自定义配置**：允许修改 VS Code 设置、快捷键和插件管理。
- **部署选项**：支持 Docker 一键部署、npm 安装或从源代码构建，适用于云服务器如 AWS、GCP 或本地环境。

## 用法
1. **安装**：
   - 使用 Docker（推荐）：运行命令 `docker run -it -p 8080:8080 -v "${PWD}:/home/coder/project" coder/code-server`，然后在浏览器访问 `http://localhost:8080`。
   - 通过 npm：安装 Node.js 后，运行 `npm install -g code-server`，然后启动 `code-server`。
   - 从二进制文件：从 GitHub Releases 下载对应平台的二进制文件，解压并运行 `./code-server`。

2. **启动和访问**：
   - 启动服务器后，默认在 `http://localhost:8080` 访问。首次访问需设置密码（通过环境变量 `PASSWORD` 配置）。
   - 配置 HTTPS：使用 `--cert` 和 `--cert-key` 参数或环境变量启用 SSL。

3. **基本使用**：
   - 打开浏览器，输入服务器地址，登录后即可使用 VS Code 界面。
   - 挂载本地目录：在启动时使用 `-v`（Docker）或工作区设置来访问文件。
   - 安装扩展：在浏览器 VS Code 中直接搜索并安装扩展。
   - 停止服务器：使用 Ctrl+C 或 Docker stop 命令。

更多细节请参考项目文档：https://coder.com/docs/code-server