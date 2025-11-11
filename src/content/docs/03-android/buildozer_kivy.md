---
title: buildozer
---

# Buildozer

Buildozer 是一个开发工具，用于将 [Python](https://www.python.org/) 应用程序转换为可安装的二进制包，支持多个平台，包括移动设备。

应用开发者提供一个单独的 "buildozer.spec" 文件，该文件描述了应用程序的需求和设置，如标题和图标。然后，Buildozer 可以为 Android、iOS、Windows、macOS 和/或 Linux 创建可安装的包。

Buildozer 由 [Kivy Team](https://kivy.org/about.html) 管理，依赖于其兄弟项目：[python-for-android](https://github.com/kivy/python-for-android/) 和 [Kivy for iOS](https://github.com/kivy/kivy-ios/)。它提供了使使用 [Kivy 框架](https://github.com/kivy/kivy) 构建应用程序更轻松的功能，但也可以独立使用，甚至与其他 GUI 框架一起使用。

对于 Android，Buildozer 会自动下载并准备构建依赖项。有关更多信息，请参阅 [Android SDK NDK 信息](https://github.com/kivy/kivy/wiki/Android-SDK-NDK-Information)。

> [!NOTE]  
> 此工具与在线构建服务 `buildozer.io` 无关。

## 主要特性
- 单一的配置文件 (`buildozer.spec`) 来管理应用程序的打包设置。
- 支持多平台 (Android, iOS, Windows, macOS, Linux)。
- 自动处理 Android 的构建依赖项。

## 项目地址
[Buildozer GitHub Repository](https://github.com/kivy/buildozer)

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL