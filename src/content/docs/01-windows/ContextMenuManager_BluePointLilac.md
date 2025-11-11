---
title: ContextMenuManager
---

# ContextMenuManager 项目

**项目地址:** [https://github.com/BluePointLilac/ContextMenuManager](https://github.com/BluePointLilac/ContextMenuManager)

## 主要特性

ContextMenuManager 是一个纯粹的 Windows 右键菜单管理程序，用于管理文件、文件夹、新建、发送到、打开方式等右键菜单项目。它具有以下核心特性：

- **启用/禁用菜单项**：支持启用或禁用各种右键菜单项目，包括系统默认和第三方添加的项。
- **修改菜单项**：允许修改菜单项的名称、图标、导航注册表位置、导航文件位置，或永久删除。
- **自定义添加**：支持自定义添加右键菜单项目，自定义菜单命令。
- **兼容性强**：适用于 Windows 10、8.1、8、7、Vista，支持 64bit 和 32bit 系统，高分屏显示。
- **多语言支持**：支持国际化多语言显示，包括中文。
- **安全提示**：修改前提示潜在风险，支持撤销操作；可能被误报为病毒，需添加白名单。

## 主要功能

- **菜单管理**：启用、禁用、修改或删除右键菜单项，包括文件、文件夹、新建、发送到、打开方式、自定义文件格式、IE浏览器、WinX等。
- **自定义添加**：添加自定义菜单命令。
- **导航功能**：导航到注册表位置或文件位置，便于手动操作。
- **兼容提示**：处理与其他右键管理程序的冲突，建议单独使用。

## 用法

1. **下载与安装**：
   - 从 [GitHub Releases](https://github.com/BluePointLilac/ContextMenuManager/releases) 或 [Gitee Releases](https://gitee.com/BluePointLilac/ContextMenuManager/releases) 下载最新版本的 zip 或 exe 文件。
   - 程序分为 .NET 3.5 版和 .NET 4.0 版，根据系统选择（Vista 需要安装 [.NET Framework](https://dotnet.microsoft.com/download/dotnet-framework)）。
   - 解压或安装后运行，无需管理员权限查看，但修改需提升权限。

2. **启动程序**：
   - 运行 ContextMenuManager.exe，程序会扫描当前系统的右键菜单。

3. **管理菜单**：
   - 在界面中选择菜单类型（如文件、文件夹等）。
   - 查看列表中的菜单项，启用/禁用、修改名称/图标，或删除。
   - 添加新项：选择添加选项，输入命令和参数。

4. **应用更改**：
   - 修改后应用更改，可能需重启资源管理器生效。
   - 注意：与其他程序冲突时，先用对应程序还原。

5. **注意事项**：
   - 程序读写注册表和文件，可能被 Windows Defender 误报，添加白名单。
   - 不用于清理未卸载程序，但可定位相关位置。
   - 适合电脑小白使用启用/禁用功能。

此工具适合 Windows 用户优化右键菜单，提升效率。更多细节请参考项目 README。
