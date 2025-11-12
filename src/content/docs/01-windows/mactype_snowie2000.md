---
title: mactype
---

# MacType [[中文文档]](https://github.com/snowie2000/mactype/blob/master/doc/README_CHS.md)

更好的 Windows 字体渲染。

## 最新 beta

[2018.1-beta5](https://github.com/snowie2000/mactype/releases/tag/2018.1-beta5)

请阅读发布说明以了解如何

## 官方站点

MacType 官方站点（下载是较旧的发布版本）：

http://www.mactype.net

## 有什么新功能？

- Win10 兼容
- 更新 FreeType（高达 git commit 0c4feb72cf976f63d4bf62436bc48f190d0e0c28）
- 支持颜色字体 :sunglasses:
- 新安装程序
- 大量错误修复
- 多显示器支持更新
- Tray 应用现在可以在 Service Mode 下拦截 explorer
- 变音符号调整
- EasyHook 更新
- Tray Mode 下较低 CPU
- 更好的 DirectWrite 支持感谢 しらいと[http://silight.hatenablog.jp]
- 单独 DirectWrite 参数调整
- 繁体中文本地化大大改进感谢 GT Wang
- 英文本地化改进
- 添加韩文本地化，感谢 조현희
- MultiLang 系统改进
- （不包括 Infinality，因为这仍然是实验性的）

## 捐赠

MacType 现在接受捐赠。

请访问 http://www.mactype.net 并留意右下角 :heart:

感谢您的支持！您的捐赠将保持服务器运行，保持我更新，并买更多咖啡 :coffee:

## 已知问题

- 请在升级前备份您的配置文件！

- 只有简体中文/繁体中文和英文是完全本地化的，一些选项由于语言文件中的字符串缺失而在 MacType Tuner 中可能缺失。您可以帮助翻译！

- 如果您想将 MacType-patch 与 MacType 官方发布一起使用，请记住将 DirectWrite=0 添加到您的配置文件中，否则您可能会遇到神秘问题

- 如果您运行 64 位 Windows，杀毒/反恶意软件软件可能会因为 MacType 试图修改运行软件而冲突。一个可能的解决方法是尝试在 Service Mode（推荐）下运行，或将 HookChildProcesses=0 添加到您的配置文件。有关解释，请参见 https://github.com/snowie2000/mactype/wiki/HookChildProcesses

- Office 2013 不使用 DirectWrite 或 GDI（它使用自己的自定义渲染），因此 Office 2013 不适用于 MacType。如果这困扰您，您可以使用 Office 2010，它使用 GDI 或 Office 2016，它使用 DirectWrite。

- WPS 2019 已知会过滤 MacType dll 以防止它加载到 WPS.exe 进程中。用户更喜欢降级 WPS 或要求金山修改他们对 WPS 的保护。

## 如何构建

检查如何构建 [文档](https://github.com/snowie2000/mactype/blob/master/doc/HOWTOBUILD.md)
