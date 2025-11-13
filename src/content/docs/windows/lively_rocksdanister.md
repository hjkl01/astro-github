---
title: lively
---

# Lively - 动画壁纸系统

[![GitHub release](https://img.shields.io/github/release/rocksdanister/lively/all.svg)](https://github.com/rocksdanister/lively/releases)
[![Github all releases](https://img.shields.io/github/downloads/rocksdanister/lively/total.svg)](https://github.com/rocksdanister/lively/releases)

## 内容

- [关于](#about)
- [功能](#features)
- [下载](#download)
- [问题](#issues)
- [贡献](#contributing)
- [支持](#support)
- [许可证](#license)

## 关于

![demo-gif](/resources/preview.gif?raw=true 'demo')

将视频和 GIF 文件、仿真器、HTML、Web 地址和 Shaders、游戏转换为 Windows 桌面壁纸；**当全屏应用/游戏运行时，壁纸会完全暂停播放（0% CPU 和 GPU 使用）。**

![demo-gif2](/resources/dragdrop.gif?raw=true 'dragdrop')

只需拖拽文件、网页到设置壁纸。

#### 加入讨论：

- <a href="https://discord.gg/TwwtBCm">Discord 群组</a>
- <a href="https://www.reddit.com/r/LivelyWallpaper/">Reddit</a>

Lively 仍在开发中，如果您遇到错误，请在 GitHub Issue 中创建，并附上 <a href="https://github.com/rocksdanister/lively/wiki/Common-Problems">日志文件</a>

帮助将 Lively 翻译成其他语言：<a href="https://github.com/rocksdanister/lively-translations">翻译文件</a>

<a href="https://github.com/rocksdanister/lively/wiki">完整文档</a>

## 功能

_等待一秒，预览 gif 剪辑需要一些时间加载。_

#### 视频

![demo-gif2](/resources/vid.gif?raw=true 'video')

<a href="https://www.pexels.com/video/aerial-view-of-a-foggy-landscape-2547258/">雾景</a> 由 Tom Fisk

- 使用外部编解码器包或内部 Windows 编解码器。
- 播放 .mp4、mkv、webm、avi、mov 等
- 硬件加速支持。
- 当不在桌面上时，音频会静音。

#### YouTube 和流

![demo-gif3](/resources/yt-gif.gif?raw=true 'html')

- 只需拖拽 YouTube 链接到桌面壁纸设置。
- 视频质量可调整。
- 附加软件 <a href="https://github.com/rocksdanister/lively/wiki/Youtube-Wallpaper">必需</a>。

#### Web 页面和 HTML

![demo-gif7](/resources/html.gif?raw=true 'html')

<a href="http://louie.co.nz/25th_hour/">25 小时</a> 由 Loius Coyle

- 加载 HTML 文件或 Web 地址作为壁纸。
- 运行 webgl、javascript .. 基本上任何在 Chrome 上工作的东西。
- 音频响应壁纸支持，创建对 <a href="https://github.com/rocksdanister/lively/wiki/Web-Guide-II-:-System-Audio-Data">系统音频</a> 做出响应的壁纸
- 自定义支持，<a href="https://github.com/rocksdanister/lively/wiki/Web-Guide-IV-:-Interaction">文档</a>。

#### Shaders

![demo-gif7](/resources/shadertoy.gif?raw=true 'htmlshadertoy')

<a href="https://www.shadertoy.com/view/lscczl">宇宙之内</a>，<a href="https://www.shadertoy.com/view/MdfBRX">回家之路</a> 由 BigWIngs

- 在浏览器中运行 GLSL shaders。
- 支持 Shadertoy.com URLs 作为壁纸。

#### 复古游戏仿真器

![demo-gif4](/resources/emulator.gif?raw=true 'html')

- 即将推出

#### 游戏

![demo-gif5](/resources/unity.gif?raw=true 'unity')

- 可以将 Unity 和 Godot 游戏作为壁纸启动。
- 动态音频视觉化器、3D 场景..

#### GIFs

![demo-gif6](/resources/gif.gif?raw=true 'gif')

<a href="https://giphy.com/gifs/nyan-cat-sIIhZliB2McAo"> Nyan cat</a>

- 将模因/Cinemagraphs 作为壁纸...

#### 其他应用程序

- 实验性，对某些有效。

#### 更多：

- 易于使用，只需拖拽媒体文件和网页到 Lively 窗口设置壁纸。
- 实时可自定义 Web 壁纸支持。
- 易于分享 Lively-zip 格式，只需拖拽 zip 文件到库中导入，使用内置创建器制作它们（确保兼容性）。
- 硬件加速视频播放，支持您选择的外部 Directshow 编解码器。（推荐 LAV、K-Lite、Kawaii Codec..）
- 库浏览和预览壁纸。
- 您可以与 Rainmeter 一起使用。
- 高效，它是一个原生 C# WPF 应用程序，具有 C++ 调用。
- 完全开源和免费；没有黑魔法，没有付费功能。

#### 多显示器支持：

- 完整多显示器支持。
- 将单个壁纸跨越所有屏幕。
- 复制相同壁纸所有屏幕。
- 每屏幕不同壁纸。

#### 关于性能：

- 当全屏应用/游戏在机器上运行时，壁纸播放暂停（~0% CPU、GPU 使用）。
- 可选择仅在桌面上播放壁纸。
- 应用规则：根据运行的前台应用程序设置壁纸播放规则。（如 photoshop 打开时始终暂停等）
- 基于显示器（多显示器）：根据全屏应用/游戏运行的显示器暂停壁纸播放（取决于哪个显示器）或所有显示器。
- 当全屏应用/游戏运行时杀死壁纸（即将推出）。
- 当不在桌面上时静音音频（或可选始终静音）。

**_我没有正式与 Unity 技术、godot、shadertoy 相关联；_**

## 下载

##### 最新版本：v0.9.6.0 (Windows 10, 8.1)[有什么新功能？](https://github.com/rocksdanister/lively/releases/tag/v0.9.6.0)

- [`下载 Lively 安装器`][direct-full-win32]  
   _102MB，包含 Web 壁纸支持和一些示例壁纸。_
- [`下载 Lively 便携版`][direct-full-portable-win32]  
  _111MB，（无安装和更新程序）包含 Web 壁纸支持和一些示例壁纸。_

**便携版构建：需要最新的 Visual C++ Redistributable：[vc_redist.x86.exe](https://aka.ms/vs/16/release/vc_redist.x86.exe)**

[direct-full-win32]: https://github.com/rocksdanister/lively/releases/download/v0.9.6.0/lively_setup_x86_full_v0960.exe
[direct-full-portable-win32]: https://github.com/rocksdanister/lively/releases/download/v0.9.6.0/lively_portable_x86_full_v0960.zip

**安装器会给出 Smartscreen 警告，[讨论。](https://github.com/rocksdanister/lively/issues/9)**

某些杀毒软件的启发式算法会将 Lively 检测为病毒，这是误报
**Lively 完全 [开源](https://en.wikipedia.org/wiki/Free_and_open-source_software)，您可以自由检查代码。**

[遇到麻烦？ ](https://github.com/rocksdanister/lively/wiki/Common-Problems)

## 问题

~~[TODO 列表](https://trello.com/b/rdFFxuMF/lively-wallpaper-system)~~

请查看 GitHub [问题。](https://github.com/rocksdanister/lively/issues)

## 贡献

代码贡献欢迎，请查看 [指南](https://github.com/rocksdanister/lively/wiki) 以进行拉取请求。

一些 Lively 语言是机器翻译的，

帮助将 Lively 翻译成其他语言：<a href="https://github.com/rocksdanister/lively-translations">翻译文件</a>

##### 相关项目

https://github.com/rocksdanister/lively-cef

https://github.com/rocksdanister/lively-gallery

## 支持

您总是可以通过给我买杯咖啡来帮助开发（paypal）：
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/P5P1U8NQ)

## 许可证

Lively 根据 Microsoft 公共许可证 (Ms-PL) 许可。
