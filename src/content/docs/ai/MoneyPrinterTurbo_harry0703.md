---
title: MoneyPrinterTurbo
---

## 项目简介

MoneyPrinterTurbo 是一个利用 AI 大模型一键生成高清短视频的工具。只需提供视频主题或关键词，即可全自动生成视频文案、视频素材、视频字幕、视频背景音乐，然后合成一个高清的短视频。

## 功能特性

- **完整的 MVC 架构**：代码结构清晰，易于维护，支持 API 和 Web 界面。
- **AI 自动生成视频文案**：支持自动生成文案，也可自定义文案。
- **多种高清视频尺寸**：
  - 竖屏 9:16，1080x1920
  - 横屏 16:9，1920x1080
- **批量视频生成**：一次生成多个视频，选择最满意的一个。
- **视频片段时长设置**：调节素材切换频率。
- **多语言支持**：中文和英文视频文案。
- **多种语音合成**：可实时试听效果。
- **字幕生成**：可调整字体、位置、颜色、大小，支持字幕描边。
- **背景音乐**：随机或指定音乐文件，可设置音量。
- **高清无版权素材**：支持使用本地素材。
- **多种 LLM 支持**：OpenAI、Moonshot、Azure、gpt4free、one-api、通义千问、Google Gemini、Ollama、DeepSeek、文心一言、Pollinations 等。

## 用法

### 快速开始

1. **克隆代码**：

   ```
   git clone https://github.com/harry0703/MoneyPrinterTurbo.git
   cd MoneyPrinterTurbo
   ```

2. **配置环境**：
   - 复制 `config.example.toml` 为 `config.toml`。
   - 配置 Pexels API keys 和 LLM provider 相关 API Key。

3. **安装依赖**：
   - 创建虚拟环境（推荐使用 conda）：
     ```
     conda create -n MoneyPrinterTurbo python=3.11
     conda activate MoneyPrinterTurbo
     pip install -r requirements.txt
     ```
   - 安装 ImageMagick（根据系统选择）。

4. **启动服务**：
   - **Web 界面**：运行 `webui.bat` (Windows) 或 `sh webui.sh` (MacOS/Linux)，访问浏览器。
   - **API 服务**：运行 `python main.py`，访问 API 文档。

### Docker 部署

```
cd MoneyPrinterTurbo
docker-compose up
```

访问 Web 界面：http://0.0.0.0:8501  
访问 API 文档：http://0.0.0.0:8080/docs

### 配置要求

- CPU：4核以上，内存：4G以上。
- 系统：Windows 10 或 MacOS 11.0 以上。

## 注意事项

- 路径避免中文、特殊字符、空格。
- 确保网络正常，VPN 需全局模式。
- 字幕生成支持 edge（快但质量不稳定）和 whisper（慢但质量可靠）模式。
- 背景音乐位于 `resource/songs` 目录。
- 字幕字体位于 `resource/fonts` 目录。
