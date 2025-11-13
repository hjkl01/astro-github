---
title: adb-enhanced
---

# adb-enhanced 项目

## 项目地址

[https://github.com/ashishb/adb-enhanced](https://github.com/ashishb/adb-enhanced)

## 主要特性

ADB-Enhanced 是 Android 测试和开发的瑞士军刀工具。它提供命令行界面来触发各种场景，如屏幕旋转、电池节省模式、数据节省模式、打盹模式以及权限的授予和撤销。它是 ADB 的包装器，而不是替代品。主要特性包括：

- **设备配置**：控制飞行模式、移动数据、电池节省、打盹模式等。
- **权限管理**：授予或撤销应用的运行时权限，如存储、相机、位置等。
- **应用交互**：启动、停止、清除数据、备份应用数据。
- **设备和应用信息**：获取详细的设备规格和应用信息，包括权限、版本等。
- **文件操作**：无需 root 即可访问和操作应用数据目录。
- **媒体处理**：截屏、录屏、录制视频。
- **其他功能**：旋转屏幕、输入文本、安装应用、模拟按键等。

## 主要功能

- **设备管理**：自动检测连接设备，支持多设备并行操作，包括重启、卸载应用和文件传输。
- **调试工具**：实时日志查看、CPU/内存监控、应用崩溃分析。
- **媒体处理**：快速截取屏幕、录制视频，并支持直接拉取到本地。
- **高级功能**：模拟输入事件（如点击、滑动）、网络模拟和应用性能基准测试。
- **集成扩展**：可与 Android Studio 或其他 IDE 结合使用，提升开发效率。

## 用法

1. **安装**：
   - 推荐：`sudo pip3 install adb-enhanced`
   - Mac OS：`brew install adb-enhanced`
   - 注意：需要 Python 3，支持 Windows、macOS 和 Linux。

2. **基本用法**：
   - 开启打盹模式：`adbe doze on`
   - 关闭移动数据：`adbe mobile-data off`
   - 开启电池节省：`adbe battery saver on`
   - 截屏：`adbe screenshot screenshot.png`
   - 录屏：`adbe screenrecord video.mp4`（按 Ctrl+C 停止）
   - 授予权限：`adbe permissions grant com.example storage`
   - 撤销权限：`adbe permissions revoke com.example storage`
   - 启动应用：`adbe start com.example`
   - 停止应用：`adbe force-stop com.example`
   - 清除应用数据：`adbe clear-data com.example`
   - 获取设备信息：`adbe devices`
   - 获取应用信息：`adbe app info com.example`

3. **高级用法**：
   - 查看文件：`adbe ls /data/data/com.example`
   - 复制文件：`adbe pull /sdcard/file.txt`
   - 推送文件：`adbe push file.txt /sdcard/`
   - 旋转屏幕：`adbe rotate landscape`
   - 输入文本：`adbe input-text "hello"`
   - 安装 APK：`adbe install app.apk`

更多详情请参考项目 README。
