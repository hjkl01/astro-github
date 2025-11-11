---
title: Genymotion
---

# Genymotion ARM Translation 项目

## 项目地址

[GitHub 项目地址](https://github.com/m9rco/Genymotion_ARM_Translation)

## 主要特性

- **ARM 架构翻译支持**：该项目提供了一个翻译层，使 Genymotion 模拟器能够在 x86 架构的宿主机上运行 ARM 版本的 Android 应用。通过二进制翻译技术，将 ARM 指令转换为 x86 指令，实现无缝兼容。
- **性能优化**：优化了翻译过程，减少了运行时的开销，支持高效模拟 ARM 应用的执行，提高了模拟器的整体性能。
- **兼容性增强**：适用于需要运行 ARM-only 应用的场景，如某些游戏或特定硬件依赖的应用，而无需物理 ARM 设备。
- **开源与易集成**：基于开源工具构建，便于开发者自定义和扩展，支持 Genymotion 的标准虚拟机环境。

## 功能

- **翻译引擎**：核心功能是实时翻译 ARM 二进制代码为 x86 可执行代码，确保应用在模拟器中正常运行。
- **应用安装与运行**：允许用户直接在 Genymotion 中安装和启动 ARM APK 文件，而无需额外的修改。
- **调试支持**：集成日志和调试工具，帮助开发者诊断 ARM 应用在 x86 环境下的兼容性问题。
- **多架构支持**：除了 ARM，还可扩展到其他架构的翻译需求，增强模拟器的多功能性。

## 用法

1. **安装 Genymotion**：确保已安装最新版本的 Genymotion 模拟器，并创建一个 Android 虚拟设备（推荐 x86_64 架构）。
2. **克隆项目**：在终端运行 `git clone https://github.com/m9rco/Genymotion_ARM_Translation.git` 下载项目文件。
3. **构建与安装**：进入项目目录，运行 `./build.sh`（或相应构建脚本）编译翻译层。然后，使用 `adb install` 或 Genymotion 的拖拽功能安装 ARM APK 到模拟器。
4. **启用翻译**：启动 Genymotion VM 时，通过项目提供的配置脚本（如 `enable_translation.sh`）激活 ARM 翻译模式。运行应用时，翻译层将自动介入。
5. **测试与调试**：在模拟器中启动应用，若遇问题，查看项目日志文件（通常在 `/tmp/genymotion_logs`）进行排查。重启 VM 以应用更改。
6. **注意事项**：确保宿主机有足够的资源（CPU/RAM），并仅用于合法的开发测试。项目可能需要 root 权限或特定依赖如 QEMU 工具链。

## 常见问题解决

### APK 安装失败

如果安装 ARM APK 时出现错误消息：

```
An error occured while deploying the file.
This probably means that the app contains ARM native code and your Genymotion device cannot run ARM instructions. You should either build your native code to x86 or install an ARM translation tool in your device.
```

1. 验证 ARM_Translation 是否成功安装。
   - 通过 ADB shell 运行 `getprop ro.product.cpu.abilist`，如果显示 `x86,armeabi-v7a,armeabi`，则安装成功。
2. 检查 APK 是否支持 armv7。
   - 运行 `unzip -l YOUR_APP.apk | grep -o ' lib/[^/]*/' | uniq`。如果只有 `lib/arm64-v8a/`，则不支持 armv7，需要 armv8 翻译工具。
