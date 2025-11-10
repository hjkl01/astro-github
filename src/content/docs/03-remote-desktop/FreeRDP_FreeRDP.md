---
title: FreeRDP
---

# FreeRDP 项目

## 项目地址
[https://github.com/FreeRDP/FreeRDP](https://github.com/FreeRDP/FreeRDP)

## 主要特性
FreeRDP 是一个开源的远程桌面协议 (RDP) 客户端库，实现了 Microsoft RDP 协议的完整功能。它支持跨平台开发，包括 Windows、Linux、macOS 和 Android 等操作系统。主要特性包括：
- **协议兼容性**：完全支持 RDP 协议的多个版本（如 RDP 5.x 到 10.x），包括安全通道、多媒体重定向和打印机重定向。
- **高性能**：优化了网络传输，支持硬件加速、音频/视频流和智能卡认证。
- **模块化设计**：提供核心库、客户端工具和服务器实现，便于集成到其他应用中。
- **安全增强**：集成 TLS/SSL 支持、NLA（网络级认证）和 CredSSP（凭据委派安全数据包支持）。
- **多平台支持**：通过 CMake 构建系统，支持多种编译器和架构。
- **扩展功能**：包括 RD Gateway 支持、USB 重定向和多监视器配置。

## 主要功能
- **客户端功能**：允许用户从本地设备连接到远程 Windows 服务器，实现桌面共享、文件传输和资源访问。
- **服务器功能**：提供 RDP 服务器实现，支持模拟 Windows RDP 服务器，用于测试或 Linux 环境下的 RDP 服务。
- **库集成**：作为 C 语言库，可嵌入到自定义应用中，支持 API 调用以实现 RDP 连接管理、事件处理和图形渲染。
- **工具集**：内置命令行工具如 `xfreerdp`（X11 客户端）、`wfreerdp`（Windows 客户端）和 `sfreerdp`（服务器），用于快速部署和调试。
- **自定义扩展**：支持插件架构，允许开发者添加自定义通道或协议扩展。

## 用法
### 安装
1. **从源代码构建**（推荐）：
   - 克隆仓库：`git clone https://github.com/FreeRDP/FreeRDP.git`
   - 安装依赖：如 CMake、OpenSSL、libx11（针对 Linux）。
   - 构建：`mkdir build && cd build && cmake .. && make && sudo make install`

2. **预编译包**：
   - Ubuntu/Debian：`sudo apt install freerdp2-x11`
   - Windows：通过 vcpkg 或 MSYS2 安装。
   - macOS：使用 Homebrew `brew install freerdp`。

### 基本用法
- **连接远程桌面**（使用 xfreerdp 命令行工具）：
  ```
  xfreerdp /v:remote-host:3389 /u:username /p:password /size:1024x768
  ```
  - `/v`：指定服务器地址和端口（默认 3389）。
  - `/u` 和 `/p`：用户名和密码。
  - `/size`：设置分辨率。
  - 其他选项：`/sec:nla`（启用 NLA 认证）、`/clipboard`（启用剪贴板重定向）、`/drive:share,drive`（共享本地驱动器）。

- **图形界面**：在支持的环境中，使用 Remmina 或 rdesktop 等前端工具集成 FreeRDP 库。

- **服务器模式**（使用 sfreerdp）：
  ```
  sfreerdp-server -f -D
  ```
  - `-f`：全屏模式，`-D`：守护进程模式。

- **API 集成**（C 代码示例）：
  ```c
  #include <freerdp/freerdp.h>
  int main() {
      freerdp* instance = freerdp_new();
      // 配置连接参数
      rdpSettings* settings = instance->settings;
      settings->ServerHostname = "remote-host";
      settings->Username = "username";
      settings->Password = "password";
      // 连接
      if (freerdp_connect(instance)) {
          // 处理事件循环
      }
      freerdp_free(instance);
      return 0;
  }
  ```
  编译时链接 FreeRDP 库：`gcc example.c -lfreerdp -o example`。

更多高级用法和配置，请参考项目 Wiki 或官方文档。