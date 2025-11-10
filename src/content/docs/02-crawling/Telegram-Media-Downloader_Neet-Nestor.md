---
title: Telegram-Media-Downloader
---

# Telegram-Media-Downloader

## 功能介绍

Telegram-Media-Downloader 是一个用户脚本，允许用户从 Telegram Web 应用中下载图片、GIF、音频和视频，即使在聊天、故事或私人频道中下载被禁用或限制。

### 主要功能

- **解锁下载限制**：在 Telegram Web 上，即使群组或频道限制下载，该脚本也能恢复下载功能。
- **支持多种媒体类型**：包括图片、GIF、音频和视频。
- **进度显示**：对于视频下载，提供底部右角的进度条；图片和音频下载无进度条。
- **兼容性**：支持 Telegram Web 的两个版本（webk.telegram.org 和 webz.telegram.org），某些功能（如语音消息下载）仅在 /k/ 版本可用。

### 注意事项

- 该脚本仅在 Telegram Webapp 上工作。
- 对于允许保存内容的频道和聊天，该脚本无效，请使用官方下载按钮。
- 脚本基于用户脚本管理器运行，如 Tampermonkey 或 Violentmonkey。

## 用法

### 安装步骤

1. **安装用户脚本管理器**：
   - Chrome: [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) 或 [Violentmonkey](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag)
   - Firefox: [Greasemonkey](https://addons.mozilla.org/firefox/addon/greasemonkey/)、[Tampermonkey](https://addons.mozilla.org/firefox/addon/tampermonkey/) 或 [Violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/)
   - Safari: [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) 或 [Userscripts](https://apps.apple.com/app/userscripts/id1463298887)
   - Microsoft Edge: [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) 或 [Violentmonkey](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag)
   - Opera: [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) 或 [Violentmonkey](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag)
   - Maxthon: [Violentmonkey](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag)

   注意：如果使用 Chrome 浏览器中的 Tampermonkey，请按照[说明](https://www.tampermonkey.net/faq.php#Q209)启用开发者模式。

2. **安装脚本**：
   - **通过 Greasy Fork**：访问 [https://greasyfork.org/scripts/446342-telegram-media-downloader](https://greasyfork.org/scripts/446342-telegram-media-downloader) 并安装。
   - **手动安装**：打开 Tampermonkey 仪表板，将 `src/tel_download.js` 文件拖拽到其中并点击“安装”按钮。

### 使用方法

1. 打开 Telegram Webapp（推荐使用 [https://webk.telegram.org](https://webk.telegram.org) 或 [https://web.telegram.org/k/](https://web.telegram.org/k/)）。
2. 导航到限制下载的聊天、频道或故事。
3. 对于图片、GIF 和视频，脚本会自动添加下载按钮。
4. 点击下载按钮开始下载。
5. 检查下载进度：视频下载时，底部右角会显示进度条；也可以在浏览器开发者工具控制台中查看日志。

### 支持的 Webapp 版本

- **推荐版本**：[https://webk.telegram.org](https://webk.telegram.org) / [https://web.telegram.org/k/](https://web.telegram.org/k/)
- **备用版本**：[https://webz.telegram.org](https://webz.telegram.org) / [https://web.telegram.org/a/](https://web.telegram.org/a/)

如果某些功能不工作，建议切换到 /k/ 版本。

## 贡献

欢迎社区贡献！如果您想为 Telegram Media Downloader 做出贡献，请遵循以下步骤：

### 报告问题

- 检查 Issues 标签页是否已有类似问题。
- 如果没有，创建一个新问题，提供清晰的标题和描述，并附上截图或日志。

### 提交拉取请求

1. Fork 仓库。
2. 克隆您的 Fork：`git clone https://github.com/YOUR-USERNAME/Telegram-Media-Downloader.git`
3. 创建新分支：`git checkout -b feature-or-bugfix-name`
4. 进行更改并确保脚本在支持的 Telegram Webapp 上正常工作。
5. 提交更改：`git commit -m "Add feature/fix issue: Brief description"`
6. 推送到您的 Fork：`git push origin feature-or-bugfix-name`
7. 提交拉取请求到原仓库。

### 开发指南

- 保持代码清洁并有良好文档。
- 遵循现有编码风格。
- 在 Telegram WebK 和 WebZ 版本上测试更改。
- 确保与主要用户脚本管理器兼容，如 Tampermonkey 和 Violentmonkey。

### 翻译帮助

- 检查 `docs/greasyfork` 文件夹中的现有翻译。
- 添加新文件，如 `docs/fr-FR.md`，并翻译 `docs/greasyfork/en-US.md` 的内容。
- 提交拉取请求。

## 支持作者

如果您喜欢这个脚本，可以通过 [Venmo](https://venmo.com/u/NeetNestor) 或 [buy me a coffee](https://ko-fi.com/neetnestor) 支持作者。

## 许可证

该项目基于 GPL-3.0 许可证。
