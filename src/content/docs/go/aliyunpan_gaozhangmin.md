---
title: aliyunpan
---

# 小白羊网盘

小白羊网盘是一个基于阿里云盘Open平台API开发的网盘客户端，支持Windows、macOS和Linux操作系统。它提供了丰富的功能，帮助用户高效管理阿里云盘中的文件。

## 功能特性

- **多账号管理**：支持同时登录多个阿里云盘账号进行管理。
- **文件夹树操作**：提供特有的文件夹树结构，方便快速导航和操作。
- **在线视频播放**：支持播放网盘中各种格式的高清原画视频，可外挂字幕、音轨，并调整播放速度，支持播放列表。
- **文件排序与显示**：显示文件夹体积，支持按文件名、体积、时间等混合排序。
- **远程下载**：通过远程Aria2功能将文件直接下载到VPS或NAS。
- **批量操作**：支持批量重命名大量文件和多层嵌套的文件夹。
- **快速操作**：快速复制文件、预览视频雪碧图、直接删除文件。
- **大规模管理**：能够管理数万文件夹和数万文件，一次性列出文件夹中的全部文件。
- **批量传输**：支持一次性上传/下载百万级的文件/文件夹。

## 安装方法

### Windows

1. 访问 [Latest Release](https://github.com/gaozhangmin/aliyunpan/releases/latest) 页面下载 `XBYDriver-Setup-*.exe` 安装包。
2. 下载完成后双击安装包进行安装。
3. 如果提示不安全，点击 `更多信息` -> `仍要运行` 继续安装。
4. 安装完成后即可开始使用。

### macOS

1. 访问 [Latest Release](https://github.com/gaozhangmin/aliyunpan/releases/latest) 页面下载对应芯片的 `.dmg` 安装包（Apple Silicon机器使用arm64版本）。
2. 下载完成后双击安装包，将 `小白羊` 拖动到 `Applications` 文件夹。
3. 如果遇到开发者验证问题，参考故障排除部分。

### Linux

#### deb安装包

1. 访问 [Latest Release](https://github.com/gaozhangmin/aliyunpan/releases/latest) 页面下载以 `.deb` 结尾的安装包。
2. 执行 `sudo dpkg -i XBYDriver-*.deb` 进行安装。

#### AppImage安装包

1. 访问 [Latest Release](https://github.com/gaozhangmin/aliyunpan/releases/latest) 页面下载以 `.AppImage` 结尾的安装包。
2. 执行 `chmod +x XBYDriver-*.AppImage` 赋予执行权限。
3. 双击运行或命令行执行启动。

## 使用方法

1. 启动应用后，登录您的阿里云盘账号。
2. 使用左侧文件夹树导航到所需目录。
3. 右键文件/文件夹进行上传、下载、复制、删除等操作。
4. 对于视频文件，双击即可在线播放，支持字幕和播放控制。
5. 在设置中配置远程Aria2等高级功能。

## 故障排除

- **macOS开发者验证**：如果提示无法打开，前往 `设置` -> `隐私与安全性`，点击 `仍要打开`。对于Apple Silicon版本，可能需要执行 `sudo xattr -d com.apple.quarantine /Applications/小白羊云盘.app`。

## 社区与支持

- **公众号**：关注小白羊公众号获取最新信息。
- **Telegram群组**：[加入讨论](https://t.me/+wjdFeQ7ZNNE1NmM1)。

## 免责声明

本程序为免费开源项目，仅用于分享网盘文件、方便下载及学习。请遵守相关法律法规，使用时请了解并承担相应风险，包括账号被ban、下载限速等。本程序通过官方SDK/接口实现，不破坏官方接口，不拦截或篡改用户数据。如有侵权，请联系作者处理。

项目基于 [liupan1890/aliyunpan](https://github.com/liupan1890/aliyunpan) 继续开发。
