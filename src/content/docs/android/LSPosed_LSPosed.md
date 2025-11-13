---
title: LSPosed
---

# LSPosed Framework

## 项目介绍

LSPosed是一个Riru / Zygisk模块，旨在提供一个ART hooking框架，提供与OG Xposed一致的API，同时利用LSPlant hooking框架。

Xposed是一个模块化框架，允许用户在不修改任何APK的情况下改变系统和应用的行为。这表示模块可以在不同版本和ROM上正常工作，只要原始代码没有发生太大变化。Xposed的一个显著优点是易于撤销：所有的更改均在内存中进行，您只需停用模块并重启设备即可恢复到原始系统。此外，多个模块可以对同一部分系统或应用进行更改，而修改的APK则需要选择其中一个，不能轻易合并，除非作者构建多个包含不同组合的APK。

## 支持的版本

安卓版本：8.1 ~ 14

## 安装方法

1. 安装Magisk v24+
2. 访问项目地址以获取更多信息及下载：[LSPosed](https://github.com/LSPosed/LSPosed)

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL