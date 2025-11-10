---
title: ExplorerPatcher
---


# ExplorerPatcher (valinet)

GitHub地址: https://github.com/valinet/ExplorerPatcher

## 主要特性

- **支持 Windows 10 及 Windows 11**  
- 将系统自带的 Windows Explorer 变成 **文件管理器**，而非文件夹查看器  
- 内置 **侧边栏**、**查看模式**、**多列** 等桌面文件管理器常见功能  
- 与系统主题、图标压缩方案完全兼容  
- 支持快捷键和触摸手势操作  
- 内置错误日志和自定义主题配置  
- 兼容大多数文件类和第三方文件类型

## 功能概览

| 功能 | 说明 |
|------|------|
| 侧边栏导航 | 可添加磁盘、网络位置、快捷方式等 |
| 视图切换 | 详细、列表、图标等常规视图及自定义排列方式 |
| 快捷栏 | 快速访问常用工具与剪贴板功能 |
| 列管理 | 自定义显示哪些字段（大小、修改日期、类型等） |
| 搜索栏 | 支持关键词、属性搜索，支持正则表达式 |
| 触摸/鼠标手势 | 自定义缩放、拖拽等操作 |
| 日志与调试 | 自动记录错误并允许手动导出日志 |
| 高级配置 | 支持自定义皮肤、图标集、启动缩略图等 |

## 安装与使用

1. 从 [GitHub Release](https://github.com/valinet/ExplorerPatcher/releases) 页面下载最新版本。  
2. 运行 `ExplorerPatcher.exe`（无安装包），程序会自动检测系统版本并提示是否更新 Explorer。  
3. 根据提示重启计算机或手动重启 Explorer。  
4. 打开文件资源管理器，即可看到完整文件管理器界面。  

**重置或卸载**  
- 在 **控制面板 > 程序和功能** 中选中 *ExplorerPatcher* 并选择卸载。  
- 也可以运行提供的 `uninstall.exe` 或 `restore.exe` 进行恢复。  

> 注：首次运行时可能需要开启 *管理员权限*。  

---
如需进一步配置或自定义，可查看项目 README 或直接编辑 `settings.json`（位于 `%LocalAppData%\ExplorerPatcher\`）。