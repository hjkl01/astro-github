---
title: adk-samples
---


# Google ADK Samples

- **项目地址**: https://github.com/google/adk-samples

## 主要特性与功能

| 主题 | 说明 |
|------|------|
| **多媒体** | 包含摄像头、音频、视频采集与处理示例。 |
| **传感器** | 展示加速度计、陀螺仪、磁力计等传感器的使用。 |
| **定位** | 提供基于 GPS、网络和蓝牙的定位实现。 |
| **网络** | 通过 HTTP、WebSocket、MQTT 等协议进行网络通信示例。 |
| **本地存储** | 演示 SQLite、Room、文件系统和共享首选项的使用。 |
| **多线程 & 并发** | 使用 Handler、AsyncTask、ExecutorService 等实现后台任务。 |
| **原生代码** | 展示 JNI 与 NDK 的集成与调用。 |
| **UI & 交互** | 包含自定义 View、动画、拖拽、手势识别等。 |
| **安全** | 演示数据加密、签名验证、权限管理。 |
| **测试** | 包含单元测试与 UI 测试（JUnit, Espresso）示例。 |

## 用法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/google/adk-samples.git
   ```

2. **打开 Android Studio**  
   - 选择 *File → Open*，定位到克隆后的 `adk-samples` 目录。  
   - Android Studio 会自动下载所需的 SDK、插件和 Gradle 依赖。

3. **构建与运行**  
   - 在左侧的 Project 视图中选择你想运行的 Sample（如 `CameraSample`、`LocationSample` 等）。  
   - 点击工具栏的 **Run** 按钮，或者使用 `Shift + F10`。  
   - 选择目标设备（模拟器或已连接的物理设备）。

4. **浏览源码**  
   - 每个 Sample 位于 `samples/` 目录下，按功能模块划分。  
   - 代码结构与 `app/build.gradle` 中的模块配置保持一致，方便快速定位。

5. **自定义扩展**  
   - 复制现有 Sample 并修改 `AndroidManifest.xml` 与 `build.gradle`，即可快速创建自己的演示项目。  
   - 参考 `README.md` 中的说明，添加所需的权限、依赖与实现细节。

6. **运行测试**  
   - 右键 `app` 模块 → *Run Tests*，或使用 `Ctrl + Shift + F10` 运行单元/UI 测试。  

> **提示**  
> - 确保 Android SDK 的最低版本与 Sample 中的 `compileSdk`、`minSdk` 匹配。  
> - 若遇到构建错误，可先执行 `./gradlew clean` 再重新构建。  

---  

> 以上内容可直接复制并保存为 `src/content/docs/00/adk-samples_google.md`。