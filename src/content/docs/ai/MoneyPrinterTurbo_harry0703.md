---
title: MoneyPrinterTurbo
---

## 项目简介

MoneyPrinterTurbo 是一个利用 AI 大模型一键生成高清短视频的工具。只需提供视频主题或关键词，即可自动生成视频文案、视频素材、视频字幕、视频背景音乐，并合成高清短视频。

## 主要功能

- **自动生成内容**：支持 AI 自动生成视频文案，也可自定义文案。
- **多种视频尺寸**：支持竖屏 9:16 (1080x1920) 和横屏 16:9 (1920x1080) 高清视频。
- **批量生成**：可一次生成多个视频，选择最满意的一个。
- **语音合成**：支持多种语音合成，可实时试听效果，支持中文和英文。
- **字幕生成**：可调整字体、位置、颜色、大小，支持字幕描边。
- **背景音乐**：随机或指定音乐文件，可设置音量。
- **素材来源**：高清无版权素材，也可使用本地素材。
- **AI 模型支持**：支持 OpenAI、Moonshot、Azure、DeepSeek 等多种模型。

## 使用方法

### 快速开始

1. **克隆代码**：

   ```
   git clone https://github.com/harry0703/MoneyPrinterTurbo.git
   cd MoneyPrinterTurbo
   ```

2. **配置环境**：
   - 复制 `config.example.toml` 为 `config.toml`，配置 API 密钥和相关参数。
   - 安装依赖：`pip install -r requirements.txt`
   - 安装 ImageMagick（用于视频处理）。

3. **启动服务**：
   - Web 界面：运行 `webui.bat` (Windows) 或 `sh webui.sh` (Mac/Linux)，访问浏览器界面。
   - API 服务：运行 `python main.py`，访问 API 文档。

### Docker 部署

```
cd MoneyPrinterTurbo
docker-compose up
```

访问 Web 界面：http://0.0.0.0:8501

### Colab 体验

点击链接在 Google Colab 中快速体验：[Open in Colab](https://colab.research.google.com/github/harry0703/MoneyPrinterTurbo/blob/main/docs/MoneyPrinterTurbo.ipynb)

## 配置要求

- CPU：4核以上，内存：4G以上。
- 系统：Windows 10+ 或 MacOS 11.0+。
- 网络：需正常访问相关服务，VPN 建议全局模式。

## 注意事项

- 路径避免中文、特殊字符、空格。
- 字幕生成支持 edge（快但质量不稳定）和 whisper（慢但质量可靠）模式。
- 背景音乐位于 `resource/songs` 目录，可替换。
- 字幕字体位于 `resource/fonts` 目录，可自定义。

更多详情请查看 [GitHub 仓库](https://github.com/harry0703/MoneyPrinterTurbo)。
