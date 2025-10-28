
---
title: docker-android
---

# Docker Android 项目

## 项目地址
[https://github.com/budtmo/docker-android](https://github.com/budtmo/docker-android)

## 主要特性
- **Android 模拟器支持**：提供基于 Docker 的 Android 模拟器环境，支持多个 Android 版本（如 API 24 到 30），无需本地安装 Android Studio 或 SDK。
- **自动化测试友好**：集成 Appium、Selenium 等工具，适合移动应用自动化测试、UI 测试和 CI/CD 管道集成。
- **多设备模拟**：支持同时运行多个模拟器实例，每个实例可自定义设备配置（如分辨率、CPU、内存）。
- **浏览器访问**：通过 VNC 或 Web 界面远程访问模拟器，支持实时屏幕共享和交互。
- **轻量级部署**：容器化设计，易于在 Linux、macOS 或 Windows 上运行，减少环境依赖。
- **开源免费**：基于 MIT 许可，社区维护，包含预构建镜像。

## 主要功能
- **运行 Android 模拟器**：启动虚拟设备，支持 ARM 或 x86 架构，模拟真实手机行为。
- **应用安装与测试**：内置 ADB（Android Debug Bridge）工具，可安装 APK、执行 shell 命令、运行测试脚本。
- **集成测试框架**：兼容 Espresso、UIAutomator 等 Android 测试框架，以及跨平台工具如 Appium。
- **资源管理**：动态调整模拟器资源（如屏幕大小、方向），支持硬件加速（需主机支持）。
- **监控与日志**：提供容器日志输出、性能监控，便于调试和故障排除。
- **扩展性**：可自定义 Dockerfile，添加特定应用或插件。

## 用法
1. **安装 Docker**：确保系统已安装 Docker（推荐 Docker Compose）。
2. **克隆仓库**：
   ```
   git clone https://github.com/budtmo/docker-android.git
   cd docker-android
   ```
3. **启动模拟器**（使用 Docker Compose 示例）：
   ```
   docker-compose up -d
   ```
   这将启动一个默认 Android 模拟器（例如 API 28 版本）。
4. **自定义配置**：
   - 编辑 `docker-compose.yml` 文件，指定 Android 版本、设备型号等参数。
   - 示例：设置 API 29 设备：
     ```
     environment:
       - DEVICE="29"
       - RESOLUTION="1080x1920"
     ```
   - 重新启动：`docker-compose down && docker-compose up -d`。
5. **访问模拟器**：
   - VNC 访问：使用 VNC 客户端连接 `localhost:5900`（密码：secret）。
   - Web 访问：通过浏览器打开 `http://localhost:6080`（noVNC 接口）。
6. **ADB 交互**：
   - 连接 ADB：`adb connect localhost:5555`。
   - 安装 APK：`adb install app.apk`。
   - 运行测试：集成 Appium Server，启动测试脚本。
7. **停止与清理**：
   ```
   docker-compose down
   docker system prune -f  # 清理镜像（可选）
   ```

更多细节请参考仓库的 README.md 文件。