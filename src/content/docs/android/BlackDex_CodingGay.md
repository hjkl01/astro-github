---
title: BlackDex
---

# BlackDex 项目

**GitHub 项目地址:** [https://github.com/CodingGay/BlackDex](https://github.com/CodingGay/BlackDex)

## 主要特性
BlackDex 是一个基于 Frida 的 Android 应用逆向工程工具，主要特性包括：
- **动态插桩与 Hook**：利用 Frida 框架实现对 Android 应用的运行时动态分析，支持 Hook Java、Native 和 ART 层面的方法调用。
- **反反调试与反检测**：内置多种绕过应用反调试机制的功能，如绕过 SSL Pinning、Root 检测和 Frida 检测。
- **脚本自动化**：支持加载自定义 JavaScript 脚本，实现自动化逆向任务，例如数据抓取、协议分析和行为修改。
- **跨平台支持**：适用于 Android 设备和模拟器，支持 ARM、x86 等多种架构。
- **模块化设计**：提供插件式扩展，便于开发者自定义功能。

## 主要功能
- **应用 Hook**：拦截和修改应用中的关键函数，例如网络请求、加密解密和 UI 操作。
- **内存分析**：实时查看和编辑应用的内存数据，支持字符串搜索和二进制修改。
- **协议逆向**：捕获并分析应用的通信协议，包括 HTTP/HTTPS 和自定义二进制协议。
- **自动化脚本**：内置脚本模板，用于快速实现常见逆向场景，如登录绕过或数据提取。
- **日志与调试**：详细的日志输出和调试界面，便于跟踪 Hook 过程和错误诊断。

## 用法
1. **环境准备**：
   - 安装 Python 3.x 和 Frida 工具链（frida-tools）。
   - 在 Android 设备上安装 Frida Server（需 Root 或使用无 Root 方案）。
   - 克隆项目：`git clone https://github.com/CodingGay/BlackDex.git`。

2. **基本启动**：
   - 运行命令：`python blackdex.py -U -f com.example.app`（-U 表示 USB 设备，-f 指定目标应用包名）。
   - 项目会自动注入 Frida 脚本到目标应用。

3. **加载脚本**：
   - 使用 `--script` 参数加载自定义 JS 脚本：`python blackdex.py -U -f com.example.app --script myscript.js`。
   - 内置脚本示例位于项目 `scripts/` 目录，可直接使用或修改。

4. **高级选项**：
   - 绕过检测：添加 `--bypass` 参数启用反反调试模式。
   - 指定端口：`--port 27042` 用于自定义 Frida Server 端口。
   - 帮助命令：`python blackdex.py --help` 查看完整参数。

注意：使用前确保设备兼容性，并遵守相关法律法规，仅用于合法逆向研究。