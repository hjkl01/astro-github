
---
title: Magisk
---

# Magisk 项目

**GitHub 项目地址:** [https://github.com/topjohnwu/Magisk](https://github.com/topjohnwu/Magisk)

## 主要特性
Magisk 是一个开源的 Android root 解决方案，专注于系统无痕化（systemless）root。它允许用户在不修改系统分区的情况下获得 root 权限，从而避免触发某些应用的 root 检测（如银行应用）。主要特性包括：
- **无痕 root**：所有修改均发生在 boot 分区，避免直接更改系统文件。
- **模块系统**：支持模块化扩展，用户可以安装各种模块来修改系统行为，而不影响 OTA 更新。
- **MagiskHide**：隐藏 root 状态，绕过应用的 root 检测，支持列表式隐藏特定应用。
- **Magisk Manager**：内置管理应用，用于安装、卸载模块、管理 root 权限和监控系统。
- **支持广泛设备**：兼容大多数 Android 设备，包括 A/B 分区和动态分区。
- **安全与兼容**：提供 SELinux 政策增强、 Zygisk（Zygote 注入）用于模块运行时注入，以及 DenyList 功能替代 MagiskHide。
- **开源与社区驱动**：完全开源，社区活跃，支持自定义内核和 ROM。

## 主要功能
- **Root 管理**：授予/撤销应用 root 权限，支持超级用户（su）命令。
- **模块安装**：从仓库或本地安装模块，如 AdAway（广告屏蔽）、Viper4Android（音频修改）等。
- **系统修改**：支持主题、字体、性能优化等无痕修改。
- **备份与恢复**：Magisk Manager 可备份 root 环境和模块。
- **OTA 更新兼容**：在 root 状态下安全应用系统更新。
- **高级功能**：支持 Magisk Modules API、Riru/EdXposed 集成（用于 Xposed 框架）、以及核心-only 模式用于调试。

## 用法
1. **下载与安装**：
   - 从 GitHub Releases 下载最新 Magisk APK 和 boot.img（或使用 Magisk Manager 下载）。
   - 使用 TWRP 或其他自定义恢复模式刷入 Magisk ZIP 文件，或修补 boot.img 并通过 fastboot 刷入。
   - 重启设备后，安装 Magisk Manager APK 进行管理。

2. **获取 root**：
   - 安装后，Magisk Manager 会显示 root 状态。首次使用需完成设置向导。

3. **安装模块**：
   - 在 Magisk Manager 的“模块”标签中搜索或下载 ZIP 文件，安装后重启生效。

4. **隐藏 root**：
   - 使用“设置”中的 DenyList 添加应用，隐藏 root 痕迹。启用 Zygisk 以增强兼容性。

5. **卸载**：
   - 在 Magisk Manager 中选择“卸载”选项，恢复原始 boot.img。

**注意**：Root 操作有风险，可能导致设备变砖或保修失效。请备份数据，并在兼容设备上操作。详细安装指南见 GitHub Wiki。