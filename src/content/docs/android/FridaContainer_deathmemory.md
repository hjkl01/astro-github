---
title: FridaContainer
---

# FridaContainer 项目

**GitHub 项目地址:** [https://github.com/deathmemory/FridaContainer](https://github.com/deathmemory/FridaContainer)

## 主要特性
FridaContainer 是一个基于 Frida 框架的容器化工具，主要用于 Android 应用的动态插桩和逆向工程。它提供了一个隔离的容器环境，支持 Frida 的脚本注入、钩子函数和运行时操纵功能。核心特性包括：
- **容器化隔离**：在独立容器中运行 Frida 脚本，避免对宿主机环境的干扰。
- **跨平台支持**：兼容 Android 设备和模拟器，支持 ARM 和 x86 架构。
- **自动化注入**：简化 Frida 脚本的加载和执行过程，支持批量操作。
- **安全性增强**：内置沙箱机制，防止脚本执行时的潜在风险。
- **模块化设计**：易于扩展，支持自定义 Frida 钩子和插件。

## 主要功能
- **动态分析**：实时监控和修改应用运行时行为，如函数调用、内存读写和网络请求。
- **逆向工程**：用于绕过应用的反调试机制、加密算法破解或协议分析。
- **脚本管理**：支持 JavaScript 脚本的编写、加载和调试，提供 API 接口简化复杂操作。
- **设备桥接**：通过 ADB 或无线连接与目标设备交互，实现远程 Frida 操作。
- **日志与调试**：内置日志记录和可视化工具，便于追踪脚本执行过程。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/deathmemory/FridaContainer.git`
   - 安装 Frida：`pip install frida-tools`
   - 确保 Android 设备已 root 或启用 USB 调试。

2. **基本启动**：
   - 进入项目目录：`cd FridaContainer`
   - 运行容器：`python main.py --device <device_id> --app <package_name>`
   - 示例：`python main.py --device emulator-5554 --app com.example.app`

3. **加载脚本**：
   - 编写 Frida 脚本（.js 文件），如钩子函数示例：
     ```javascript
     Java.perform(function() {
         var MainActivity = Java.use("com.example.MainActivity");
         MainActivity.onCreate.overload('android.os.Bundle').implementation = function(bundle) {
             console.log("onCreate hooked!");
             this.onCreate(bundle);
         };
     });
     ```
   - 注入脚本：`python inject.py --script hook.js --pid <process_id>`

4. **高级用法**：
   - 批量注入：使用 `batch_inject.py` 处理多个应用。
   - 自定义配置：编辑 `config.json` 文件调整容器参数，如端口和超时设置。
   - 停止容器：`python stop.py --device <device_id>`

详细文档请参考仓库的 README.md 文件。