---
title: GDA-android-reversing-Tool
---

# GDA Android Reversing Tool

## 项目地址
[GitHub 项目地址](https://github.com/charles2gan/GDA-android-reversing-Tool)

## 主要特性
- **基于GDA框架**：这是一个Android逆向工程工具，构建在GDA（Ghidra Decompiler for Android）基础上，提供高效的反编译和分析功能。
- **支持APK分析**：专为Android应用逆向设计，支持直接加载和解析APK文件，提取DEX、Smali代码等。
- **集成反混淆**：内置反混淆模块，帮助处理混淆后的Android应用代码，提高逆向效率。
- **可视化界面**：提供图形化界面，便于导航类结构、方法调用和资源文件。
- **插件扩展**：支持自定义插件，允许用户扩展功能，如集成Frida动态分析或自定义脚本。

## 主要功能
- **反编译APK**：自动反编译Android APK文件，生成Java-like伪代码和Smali代码。
- **代码分析**：支持静态代码分析，包括数据流图、控制流图和调用图的生成，用于漏洞挖掘和恶意代码检测。
- **资源提取**：提取APK中的资源文件，如图片、XML配置和字符串资源。
- **调试支持**：结合Ghidra的调试器，实现对反汇编代码的交互式调试。
- **批量处理**：支持批量分析多个APK文件，适用于大规模逆向任务。

## 用法
1. **安装**：从GitHub仓库克隆项目，安装依赖（如Java 8+和Ghidra）。运行`./gradlew build`构建项目。
2. **启动工具**：执行`java -jar GDA.jar`启动图形界面。
3. **加载APK**：在界面中选择“File > Open”导入APK文件，工具将自动解析并显示项目结构。
4. **分析代码**：浏览类树，点击方法查看反编译代码；使用“Analyze”菜单运行静态分析。
5. **导出结果**：通过“Export”功能保存反编译代码、报告或图表到本地文件。
6. **高级用法**：编辑配置文件`config.properties`自定义反混淆规则，或加载插件扩展功能。适用于安全研究、应用审计等场景。