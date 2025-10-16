
---
title: RevokeMsgPatcher
---

# RevokeMsgPatcher 项目

**GitHub 项目地址**: [https://github.com/huiyadanli/RevokeMsgPatcher](https://github.com/huiyadanli/RevokeMsgPatcher)

## 主要特性
RevokeMsgPatcher 是一个针对微信（WeChat）客户端的开源补丁工具，主要用于修改微信的反撤回机制。该项目基于 Android 平台的微信 APK 进行逆向工程和注入，核心特性包括：
- **防撤回功能**：允许用户查看已被撤回的消息内容，而不受微信官方撤回限制。
- **消息备份**：自动备份撤回前的消息，支持文本、图片、文件等多种类型。
- **自定义注入**：通过 Xposed 框架或类似 hook 机制注入代码，实现无缝修改。
- **开源透明**：项目代码公开，用户可自行编译和验证安全性。
- **兼容性**：支持多个微信版本（具体取决于项目维护状态），适用于 rooted Android 设备。

## 主要功能
- **撤回消息拦截**：当对方撤回消息时，工具会拦截并保存原消息，避免信息丢失。
- **通知提醒**：在消息列表中显示撤回提示，并提供查看原内容的入口。
- **隐私保护**：仅修改本地行为，不影响服务器端数据或他人体验。
- **日志记录**：内置日志系统，便于调试和问题排查。
- **模块化设计**：支持扩展其他微信功能修改，如防删除或消息过滤（视项目更新而定）。

## 用法
1. **环境准备**：
   - 确保设备已 root，并安装 Xposed Installer 或 EdXposed 框架。
   - 下载微信 APK（从官网获取最新版），并使用工具如 APKTool 解包。

2. **安装与配置**：
   - 从 GitHub 仓库克隆或下载源代码：`git clone https://github.com/huiyadanli/RevokeMsgPatcher.git`。
   - 使用 Android Studio 或 Gradle 编译项目，生成 .apk 或 .dex 文件。
   - 将生成的模块安装到 Xposed 框架中，并启用 RevokeMsgPatcher 模块。

3. **应用补丁**：
   - 重启设备或微信应用。
   - 在 Xposed 管理器中勾选模块，重启微信。
   - 测试：发送消息后撤回，检查是否能查看原内容。

4. **注意事项**：
   - 项目可能因微信更新而失效，需定期检查仓库更新。
   - 使用前备份设备数据，root 操作有风险。
   - 仅限个人学习使用，遵守微信服务条款，避免商业或非法用途。

更多详情请参考仓库的 README.md 文件。