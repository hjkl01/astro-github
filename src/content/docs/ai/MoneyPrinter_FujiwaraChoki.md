---
title: MoneyPrinter
---

# MoneyPrinter

MoneyPrinter 是一个自动化工具，用于创建 YouTube Shorts。只需提供一个视频主题，它就能自动生成视频脚本、语音、字幕，并使用 MoviePy 合成视频。

## 功能

- 自动化生成 YouTube Shorts 视频
- 使用 AI 生成视频脚本和内容
- 支持语音合成和字幕添加
- 基于 MoviePy 进行视频编辑和合成
- 支持本地运行和 Docker 部署

## 用法

1. 克隆仓库：

   ```
   git clone https://github.com/FujiwaraChoki/MoneyPrinter.git
   cd MoneyPrinter
   ```

2. 安装依赖：

   ```
   pip install -r requirements.txt
   ```

3. 设置环境变量：复制 `.env.example` 到 `.env`，并填写必要的 API 密钥和其他配置（如 OpenAI API、TikTok session ID 等）。

4. 运行脚本：
   - 本地运行：参考 `Local.md` 文件中的说明。
   - Docker 运行：使用 `docker-compose.yml` 启动。

5. 提供视频主题，工具将自动生成完整的视频。

## 注意事项

- 确保安装 ImageMagick，并正确设置路径。
- 获取 TikTok session ID 需要登录 TikTok 浏览器并复制 cookie 中的 `sessionid` 值。
- 如果遇到 `playsound` 安装问题，可以尝试 `pip install -U wheel` 和 `pip install -U playsound`。

更多详细信息请参考项目的 [GitHub 页面](https://github.com/FujiwaraChoki/MoneyPrinter) 和本地说明文件。
