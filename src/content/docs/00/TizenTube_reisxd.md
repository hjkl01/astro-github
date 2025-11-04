
---
title: TizenTube
---


# TizenTube
> GitHub: <https://github.com/reisxd/TizenTube>

## 项目概述
TizenTube 是一个基于 Tizen OS 的轻量化 YouTube 客户端，专为 Smart TV/PlayStation 4/Device 使用。该项目将原生的 YouTube Web 体验移植到 Tizen 平台，支持字幕、搜索、播放控制、列表管理等核心功能，并且使用 UI Kit 进行 UI 设计，保持与官方视屏浏览器一致的体验。

## 主要特性
- **完整的 YouTube 播放功能**：点播视频、离线缓存、播放列表管理、广告跳过（若未被屏蔽）。
- **搜索与浏览**：支持文本搜索、排行榜、推荐、频道订阅等多种浏览模式。
- **界面布局**  
  - TV 侧：采用 10 分屏布局，支持遥控器操作。  
  - PS/ Set‑top 侧：采用典型的 3+1 小窗口布局，支持键盘/鼠标/游戏手柄。
- **语音/手势控制**：兼容 Tizen VoiceKit 与手势交互（如果设备支持）。
- **多语言字幕**：自动从 YouTube 获取可用字幕并切换。
- **图像缓存与优化**：使用本地缓存减少网络负担，支持低带宽环境。

## 关键功能
| 功能 | 说明 |
|------|------|
| **播放列表管理** | 轻松添加/移除、重排序视频。 |
| **自动续播** | 观看完一集后自动切换到下一集（若在播放列表中）。 |
| **离线缓存** | 通过“下载”按钮将视频缓存到本地，支持离线观看。 |
| **截屏与分享** | 在播放时截屏，并生成分享链接（需联网）。 |
| **用户反馈** | 集成 YouTube 的“喜欢/不喜欢”与评论功能。 |
| **主题切换** | 支持多种主题，颜色与背景可自定义。 |

## 使用方法
1. **准备环境**  
   * Tizen Studio ≥ 4.0（推荐 4.2+）。  
   * 生成 Tizen SDK 并完成 Play Store 账号验证。  
   * 通过 `npm` 或 `yarn` 安装项目依赖（如`tizen-sdk`）。

2. **获取源码**  
   ```bash
   git clone https://github.com/reisxd/TizenTube.git
   cd TizenTube
   ```

3. **构建与安装**  
   ```bash
   tizen package --type wasm --src ./tizen-wasm
   tizen install -p TizenTube.wgt
   ```
   对于 PS4/其它设备，只需更换 `device` 标签即可。

4. **运行**  
   * 在 Tizen 设备上启动应用，使用遥控器/键盘导航。  
   * 右上角 “搜索” 图标启动文字搜索。  
   * 通过 “菜单” 进入偏好设置、主题、下载管理。

5. **编译调试**（可选）  
   ```bash
   tizen watch --src ./tizen-wasm # 代码变更自动热更新
   ```

## 贡献方式
项目采用 MIT 许可证，欢迎 issue 与 pull request。请遵循下面的流程：

1. Fork 本仓库  
2. 新建 feature 分支 (`git checkout -b feature/<name>`)  
3. 编写代码并更新 README  
4. 提交 PR 并说明实现逻辑

> 项目地址已在文件顶部给出，欢迎探索与使用！  
