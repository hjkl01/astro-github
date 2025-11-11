---
title: mactype
---

# MacType 项目

## 项目地址

[https://github.com/snowie2000/mactype](https://github.com/snowie2000/mactype)

## 主要特性

MacType 是一个开源的字体渲染引擎，为 Windows 提供更好的字体渲染。它模拟 macOS 和 Linux 的抗锯齿渲染方式，使字体更平滑清晰。主要特性包括：

- **多种渲染模式**：支持 MacType 专有、GDI+、DirectWrite 等。
- **Win10 兼容**：支持 Windows 10，多显示器。
- **颜色字体支持**：支持颜色字体。
- **全局与应用特定**：为系统或特定应用自定义。
- **开源免费**：GPL 许可，支持捐赠。

## 主要功能

- **字体优化**：改善锯齿感，接近 Retina 效果。
- **配置文件**：INI 文件自定义参数。
- **排除列表**：为特定软件排除。
- **热键切换**：实时切换模式。
- **多语言**：支持中文、英文、韩文等。

## 用法

1. **下载**：
   - 从 Releases 下载最新 beta，如 2018.1-beta5。
   - 或官方站点（较旧版本）。

2. **安装**：
   - 运行安装器，重启。

3. **配置**：
   - 编辑 `%APPDATA%\MacType\MacType.ini` 设置模式。
   - 使用热键切换。

4. **高级**：
   - 为应用添加规则，如 `[App.Chrome.exe] Mode=Default`。
   - 备份配置文件升级前。

注意：备份配置；64位 Windows 可能与杀毒冲突，使用 Service Mode；Office 2013 不支持。更多见 Wiki。
