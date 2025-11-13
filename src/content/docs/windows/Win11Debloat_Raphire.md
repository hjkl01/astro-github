---
title: Win11Debloat
---

<div align="center" markdown="1">
   <sup>特别感谢：</sup>
   <br>
   <br>
   <a href="https://www.warp.dev/windebloat">
      <img alt="Warp sponsorship" width="400" src="https://github.com/user-attachments/assets/c21102f7-bab9-4344-a731-0cf6b341cab2">
   </a>

### [Warp, the intelligent terminal for developers](https://www.warp.dev/windebloat)

[Available for MacOS, Linux, & Windows](https://www.warp.dev/windebloat)<br>

</div>
<hr>

# Win11Debloat

[![GitHub Release](https://img.shields.io/github/v/release/Raphire/Win11Debloat?style=for-the-badge&label=Latest%20release)](https://github.com/Raphire/Win11Debloat/releases/latest)
[![Join the Discussion](https://img.shields.io/badge/Join-the%20Discussion-2D9F2D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Raphire/Win11Debloat/discussions)
[![Static Badge](https://img.shields.io/badge/Documentation-_?style=for-the-badge&logo=bookstack&color=grey)](https://github.com/Raphire/Win11Debloat/wiki/)

Win11Debloat 是一个简单、易用且轻量的 PowerShell 脚本，允许您快速清理和改善您的 Windows 体验。它可以移除预装的 bloatware 应用、禁用遥测、移除侵入性界面元素等等。没有必要手动逐一设置所有内容。Win11Debloat 使过程快速而简单！

脚本还包括许多系统管理员会欣赏的功能，例如支持 Windows Audit 模式、将更改应用于其他 Windows 用户的能力，以及在运行时无需用户输入即可运行脚本的能力。请参考我们的 [wiki](https://github.com/Raphire/Win11Debloat/wiki/) 以获取更多详细信息。

![Win11Debloat Menu](/Assets/menu.png)

#### 这个脚本帮到您了吗？请考虑通过给我买杯咖啡来支持我的工作

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M5C6UPC)

## 用法

> [!Warning]
> 非常小心地制作了这个脚本，以确保它不会意外破坏任何操作系统功能，但请自行承担风险！如果您遇到任何问题，请 [这里](https://github.com/Raphire/Win11Debloat/issues) 报告。

### 快速方法

下载并自动运行脚本通过 PowerShell。

1. 打开 PowerShell 或 Terminal，最好作为管理员。
2. 将下面的命令复制并粘贴到 PowerShell 中：

```powershell
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
```

3. 等待脚本自动下载 Win11Debloat。
4. 仔细阅读并遵循屏幕上的说明。

此方法支持自定义脚本行为的命令行参数。请点击 [这里](https://github.com/Raphire/Win11Debloat/wiki/How-To-Use#parameters) 以获取更多信息。

### 传统方法

<details>
  <summary>手动下载并运行脚本。</summary><br/>

1. [下载最新版本的脚本](https://github.com/Raphire/Win11Debloat/releases/latest)，并将 .ZIP 文件解压到您想要的位置。
2. 导航到 Win11Debloat 文件夹
3. 双击 `Run.bat` 文件启动脚本。注意：如果控制台窗口立即关闭且没有任何反应，请尝试下面的高级方法。
4. 接受 Windows UAC 提示以管理员身份运行脚本，这是必需的。
5. 仔细阅读并遵循屏幕上的说明。
</details>

### 高级方法

<details>
  <summary>手动下载脚本并通过 PowerShell 运行脚本。推荐用于高级用户。</summary><br/>

1. [下载最新版本的脚本](https://github.com/Raphire/Win11Debloat/releases/latest)，并将 .ZIP 文件解压到您想要的位置。
2. 以管理员身份打开 PowerShell 或 Terminal。
3. 临时启用 PowerShell 执行通过输入以下命令：

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process -Force
```

4. 在 PowerShell 中，导航到文件解压的目录。示例：`cd c:\Win11Debloat`
5. 现在通过输入以下命令运行脚本：

```powershell
.\Win11Debloat.ps1
```

6. 仔细阅读并遵循屏幕上的说明。

此方法支持自定义脚本行为的命令行参数。请点击 [这里](https://github.com/Raphire/Win11Debloat/wiki/How-To-Use#parameters) 以获取更多信息。

</details>

## 功能

下面是 Win11Debloat 提供的关键功能和功能的概述。对于默认模式中包含的功能的更多信息，请参考下面的 [默认设置](#default-settings) 部分。

> [!Tip]
> Win11Debloat 所做的所有更改都可以轻松恢复，几乎所有应用都可以通过 Microsoft Store 重新安装。完整的恢复更改指南可以在 [这里](https://github.com/Raphire/Win11Debloat/wiki/Reverting-Changes) 找到。

#### 应用移除

- 移除各种预装应用。点击 [这里](https://github.com/Raphire/Win11Debloat/wiki/App-Removal) 以获取更多信息。
- 移除或替换所有固定应用从开始，为当前用户，或为所有现有和新用户。（仅限 W11）

#### 遥测、跟踪和建议内容

- 禁用遥测、诊断数据、活动历史、应用启动跟踪和定向广告。
- 禁用提示、技巧、建议和 Windows 中的广告。
- 禁用 Microsoft Edge 中的广告、建议和 MSN 新闻馈送。
- 禁用 'Windows Spotlight' 桌面背景选项。

#### Bing Web 搜索、Copilot 和 AI 功能

- 禁用并移除 Bing web 搜索、Bing AI 和 Cortana 从 Windows 搜索。
- 禁用并移除 Microsoft Copilot。
- 禁用 Windows Recall。（仅限 W11）
- 禁用 Click to Do、AI 文本和图像分析工具。（仅限 W11）
- 禁用 Edge 中的 AI 功能。（仅限 W11）
- 禁用 Paint 中的 AI 功能。（仅限 W11）
- 禁用 Notepad 中的 AI 功能。（仅限 W11）

#### 个性化

- 启用暗模式用于系统和应用。
- 禁用透明度、动画和视觉效果。
- 关闭增强指针精度，也称为鼠标加速。
- 禁用粘滞键键盘快捷键。（仅限 W11）
- 恢复旧的 Windows 10 样式上下文菜单。（仅限 W11）
- 隐藏上下文菜单中的 'Include in library'、'Give access to' 和 'Share' 选项。（仅限 W10）

#### 文件资源管理器

- 更改文件资源管理器打开的默认位置。
- 显示隐藏的文件、文件夹和驱动器。
- 显示已知文件类型的文件扩展名。
- 隐藏文件资源管理器导航窗格中的 Home 或 Gallery 部分。（仅限 W11）
- 隐藏文件资源管理器导航窗格中的 3D 对象、音乐或 OneDrive 文件夹。（仅限 W10）
- 隐藏文件资源管理器导航窗格中的重复可移动驱动器条目，只保留 'This PC' 下的条目。

#### 任务栏

- 将任务栏图标对齐到左侧。（仅限 W11）
- 选择任务栏按钮的组合模式和标签。（仅限 W11）
- 选择在多显示器使用时任务栏上显示应用图标的方式。（仅限 W11）
- 隐藏或更改任务栏上的搜索图标/框。（仅限 W11）
- 隐藏任务栏上的任务视图按钮。（仅限 W11）
- 禁用任务栏和锁屏上的小部件。
- 隐藏任务栏上的聊天（meet now）图标。（仅限 W10）
- 启用任务栏右键菜单中的 'End Task' 选项。（仅限 W11）
- 启用任务栏应用区域中的 'Last Active Click' 行为。这允许您重复点击任务栏中的应用程序图标，在该应用程序的打开窗口之间切换焦点。

#### 开始

- 禁用开始菜单中的推荐部分。（仅限 W11）
- 禁用开始菜单中的 Phone Link 移动设备集成。（仅限 W11）

#### 其他

- 禁用 Xbox 游戏/屏幕录制，这也会停止游戏覆盖弹出。
- 禁用快速启动以确保完全关闭。
- 禁用现代待机期间的网络连接以减少电池消耗。（仅限 W11）
- 选项 [将更改应用于不同的用户](https://github.com/Raphire/Win11Debloat/wiki/Advanced-Features#running-as-another-user)，而不是当前登录的用户。
- [Sysprep 模式](https://github.com/Raphire/Win11Debloat/wiki/Advanced-Features#sysprep-mode) 将更改应用于 Windows 默认用户配置文件。之后，所有新用户将自动应用更改。

### 默认设置

Win11Debloat 的默认模式允许您快速轻松地应用大多数人推荐的更改。这包括移除许多烦人的干扰、禁用遥测和跟踪，并可选地卸载默认或您的自定义应用选择。要应用默认设置，正常启动脚本，并在脚本菜单中选择选项 `1`。

或者，您可以使用 `-RunDefaults` 或 `-RunDefaultsLite` 参数立即运行默认设置，而无需通过菜单或应用移除选项。使用 `-RunDefaults` 参数将运行脚本在默认模式并移除默认应用选择。而使用 `-RunDefaultsLite` 参数将运行脚本在默认模式而不移除任何应用。示例：

```powershell
& ([scriptblock]::Create((irm "https://debloat.raphi.re/"))) -RunDefaults
```

#### 默认模式中包含的更改

- 移除默认或您的自定义应用选择。（见下面的默认应用选择）
- 禁用遥测、诊断数据、活动历史、应用启动跟踪和定向广告。
- 禁用 Windows 中的提示、技巧、建议和广告。
- 禁用 Microsoft Edge 中的广告、建议和 MSN 新闻馈送。
- 禁用并移除 Bing web 搜索、Bing AI 和 Cortana 从 Windows 搜索。
- 禁用并移除 Microsoft Copilot。
- 禁用 Windows Recall。（仅限 W11）
- 禁用 Click to Do、AI 文本和图像分析工具。（仅限 W11）
- 禁用快速启动以确保完全关闭。
- 禁用现代待机期间的网络连接以减少电池消耗。（仅限 W11）
- 显示已知文件类型的文件扩展名。
- 隐藏 'This pc' 下文件资源管理器中的 3D 对象文件夹。（仅限 W10）
- 禁用任务栏和锁屏上的小部件。
- 隐藏任务栏上的 Chat (meet now) 图标。（仅限 W10）

#### 默认移除的应用

当您选择移除默认应用选择时，会卸载这些应用。

<details>
  <summary>点击展开</summary>
  <blockquote>
    
    Microsoft 应用：
    - Clipchamp.Clipchamp (Microsoft 的视频编辑器)
    - Microsoft.3DBuilder (基本 3D 建模软件)
    - Microsoft.549981C3F5F10 (Cortana 应用，已停产)
    - Microsoft.BingFinance (通过 Bing 的财经新闻和跟踪，已停产)
    - Microsoft.BingFoodAndDrink (通过 Bing 的食谱和食物新闻，已停产)
    - Microsoft.BingHealthAndFitness (通过 Bing 的健康和健身跟踪/新闻，已停产)
    - Microsoft.BingNews (通过 Bing 的新闻聚合，已停产)
    - Microsoft.BingSports (通过 Bing 的体育新闻和分数，已停产)
    - Microsoft.BingTranslator (通过 Bing 的翻译服务)
    - Microsoft.BingTravel (通过 Bing 的旅行规划和新闻，已停产)
    - Microsoft.BingWeather (通过 Bing 的天气预报)
    - Microsoft.Copilot (集成到 Windows 中的 AI 助手)
    - Microsoft.Getstarted (Windows 的提示和介绍指南，无法在 Windows 11 中卸载)
    - Microsoft.Messaging (消息应用，通常与 Skype 集成，大部分已弃用)
    - Microsoft.Microsoft3DViewer (3D 模型查看器)
    - Microsoft.MicrosoftJournal (针对笔输入优化的数字笔记应用)
    - Microsoft.MicrosoftOfficeHub (访问 Microsoft Office 应用和文档的中心，Microsoft 365 应用的先驱)
    - Microsoft.MicrosoftPowerBIForWindows (商业分析服务客户端)
    - Microsoft.MicrosoftSolitaireCollection (纸牌游戏集合)
    - Microsoft.MicrosoftStickyNotes (数字便签应用，已弃用并被 OneNote 取代)
    - Microsoft.MixedReality.Portal (Windows Mixed Reality 头显的门户)
    - Microsoft.NetworkSpeedTest (互联网连接速度测试实用工具)
    - Microsoft.News (新闻聚合。取代 Bing News，现在是 Microsoft Start 的一部分)
    - Microsoft.Office.OneNote (数字笔记应用，通用 Windows 平台版本)
    - Microsoft.Office.Sway (演示和故事讲述应用)
    - Microsoft.OneConnect (移动运营商管理应用，被 Mobile Plans 取代)
    - Microsoft.PowerAutomateDesktop (桌面自动化工具)
    - Microsoft.Print3D (3D 打印准备软件)
    - Microsoft.SkypeApp (Skype 通信应用，通用 Windows 平台版本)
    - Microsoft.Todos (待办事项和任务管理应用)
    - Microsoft.Windows.DevHome (开发者仪表板和工具配置实用工具，不再受支持)
    - Microsoft.WindowsAlarms (闹钟和时钟应用)
    - Microsoft.WindowsFeedbackHub (向 Microsoft 提供 Windows 反馈的应用)
    - Microsoft.WindowsMaps (地图和导航应用)
    - Microsoft.WindowsSoundRecorder (基本音频录制应用)
    - Microsoft.WindowsTerminal (Windows 11 中的新默认终端应用)
    - Microsoft.XboxApp (旧 Xbox Console Companion App，不再受支持)
    - Microsoft.ZuneVideo (租用/购买/播放视频内容的电影和电视应用。重新命名为 "Films & TV")
    - MicrosoftCorporationII.MicrosoftFamily (管理家庭账户和设置的家庭安全应用)
    - MicrosoftCorporationII.QuickAssist (远程协助工具)
    - MSTeams (新 MS Teams 应用。工作/学校或个人)

    第三方应用：
    - ACGMediaPlayer
    - ActiproSoftwareLLC
    - AdobeSystemsIncorporated.AdobePhotoshopExpress
    - Amazon.com.Amazon
    - AmazonVideo.PrimeVideo
    - Asphalt8Airborne
    - AutodeskSketchBook
    - CaesarsSlotsFreeCasino
    - COOKINGFEVER
    - CyberLinkMediaSuiteEssentials
    - DisneyMagicKingdoms
    - Disney
    - DrawboardPDF
    - Duolingo-LearnLanguagesforFree
    - EclipseManager
    - Facebook
    - FarmVille2CountryEscape
    - fitbit
    - Flipboard
    - HiddenCity
    - HULULLC.HULUPLUS
    - iHeartRadio
    - Instagram
    - king.com.BubbleWitch3Saga
    - king.com.CandyCrushSaga
    - king.com.CandyCrushSodaSaga
    - LinkedInforWindows
    - MarchofEmpires
    - Netflix
    - NYTCrossword
    - OneCalendar
    - PandoraMediaInc
    - PhototasticCollage
    - PicsArt-PhotoStudio
    - Plex
    - PolarrPhotoEditorAcademicEdition
    - Royal Revolt
    - Shazam
    - Sidia.LiveWallpaper
    - SlingTV
    - Spotify
    - TikTok
    - TuneInRadio
    - Twitter
    - Viber
    - WinZipUniversal
    - Wunderlist
    - XING

</blockquote>
</details>

#### 默认不移除的应用

这些应用不会被 Win11Debloat 移除，除非用户明确选择。

<details>
  <summary>点击展开</summary>
  <blockquote>

    杂项应用：
    - Microsoft.Edge (Edge 浏览器，仅在 EEA 中可移除)
    - Microsoft.GetHelp (某些 Windows 11 故障排除程序所需)
    - Microsoft.M365Companions (Microsoft 365 商业日历、文件和人员迷你应用，这些应用如果由您的 Microsoft 365 管理员启用可能会重新安装)
    - Microsoft.MSPaint (Paint 3D)
    - Microsoft.OutlookForWindows (新的邮件应用)
    - Microsoft.OneDrive (OneDrive 消费者)
    - Microsoft.Paint (经典 Paint)
    - Microsoft.People (邮件和日历所需并包含在内)
    - Microsoft.RemoteDesktop
    - Microsoft.ScreenSketch (Snipping Tool)
    - Microsoft.Whiteboard (仅在具有触摸屏和/或笔支持的设备上预装)
    - Microsoft.Windows.Photos
    - Microsoft.WindowsCalculator
    - Microsoft.WindowsCamera
    - Microsoft.WindowsNotepad
    - Microsoft.windowscommunicationsapps (邮件和日历)
    - Microsoft.WindowsStore (Microsoft Store，注意：此应用无法重新安装！)
    - Microsoft.WindowsTerminal (Windows 11 中的新默认终端应用)
    - Microsoft.YourPhone (Phone Link)
    - Microsoft.Xbox.TCUI (UI 框架，移除此可能破坏 MS store、照片和某些游戏)
    - Microsoft.ZuneMusic (现代媒体播放器)
    - MicrosoftWindows.CrossDevice (文件资源管理器、相机和更多中的手机集成)

    游戏相关应用：
    - Microsoft.GamingApp (现代 Xbox 游戏应用，安装某些游戏所需)
    - Microsoft.XboxGameOverlay (游戏覆盖，某些游戏所需)
    - Microsoft.XboxGamingOverlay (游戏覆盖，某些游戏所需)
    - Microsoft.XboxIdentityProvider (Xbox 登录框架，某些游戏所需)
    - Microsoft.XboxSpeechToTextOverlay (某些游戏可能需要，注意：此应用无法重新安装！)

    HP 应用：
    - AD2F1837.HPAIExperienceCenter
    - AD2F1837.HPConnectedMusic
    - AD2F1837.HPConnectedPhotopoweredbySnapfish
    - AD2F1837.HPDesktopSupportUtilities
    - AD2F1837.HPEasyClean
    - AD2F1837.HPFileViewer
    - AD2F1837.HPJumpStarts
    - AD2F1837.HPPCHardwareDiagnosticsWindows
    - AD2F1837.HPPowerManager
    - AD2F1837.HPPrinterControl
    - AD2F1837.HPPrivacySettings
    - AD2F1837.HPQuickDrop
    - AD2F1837.HPQuickTouch
    - AD2F1837.HPRegistration
    - AD2F1837.HPSupportAssistant
    - AD2F1837.HPSureShieldAI
    - AD2F1837.HPSystemInformation
    - AD2F1837.HPWelcome
    - AD2F1837.HPWorkWell
    - AD2F1837.myHP

</blockquote>
</details>

## 许可证

Win11Debloat 根据 MIT 许可证授权。有关更多信息，请参阅 LICENSE 文件。
