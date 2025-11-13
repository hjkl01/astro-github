---
title: ali
---

# ali 项目

## 项目地址

[GitHub 项目地址](https://github.com/nakabonne/ali)

## 主要特性

- **实时负载测试工具**：ali 是一个能够进行实时分析的负载测试工具，受 vegeta 和 jplot 启发。
- **实时绘图**：内置终端界面，可以实时绘制指标。
- **多种安装方式**：支持通过 Go 安装、二进制下载、Homebrew、MacPorts、APT、RPM、Pacman、APK、Docker 等。
- **跨平台支持**：支持 Windows、macOS、Linux。

## 主要功能

- **实时分析**：支持实时绘制延迟、百分位数、字节等图表。
- **可视化攻击进度**：帮助在长时间测试中监控进度。
- **鼠标支持**：使用 termdash 可以直观操作。
- **多种选项**：支持设置速率、持续时间、并发数、超时、请求方法、请求体等。

## 用法

1. **安装**：
   - 通过 Go 安装：`go install github.com/nakabonne/ali@latest`
   - 或从 GitHub Releases 下载预编译二进制文件。
   - Homebrew：`brew install nakabonne/ali/ali`
   - MacPorts：`sudo port selfupdate && sudo port install ali`
   - APT：下载 deb 文件并安装。
   - RPM：下载 rpm 文件并安装。
   - Pacman：`pacman -S ali`
   - APK：启用 community repo 后 `apk add ali`
   - Docker：`docker run --rm -it nakabonne/ali ali`

2. **快速开始**：
   `ali http://host.xz`
   按 Enter 启动攻击，默认速率 50，持续时间 10s。

3. **选项**：
   - `-r`：请求速率每秒（默认 50）。
   - `-d`：持续时间（默认 10s）。
   - `-m`：HTTP 请求方法（默认 GET）。
   - `-b`：请求体。
   - `-H`：请求头。
   - `--debug`：调试模式。
   - 等等。

4. **图表**：
   - **延迟**：X 轴为请求计数，Y 轴为延迟毫秒。
   - **百分位数**：显示 50th、90th、95th、99th 百分位数的变化。
   - **字节**：（待定）。
   - **直方图**：（待定）。

更多详细用法请参考项目 README 文件。
