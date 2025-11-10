---
title: AI-Vtuber
---

# Luna AI 项目

## 项目地址

https://github.com/Ikaros-521/AI-Vtuber

## 主要特性

Luna AI 是一款结合了最先进技术的虚拟AI主播。它的核心是一系列高效的人工智能模型和平台，包括 `ChatterBot、GPT、Claude、langchain、chatglm、text-generation-webui、讯飞星火、智谱AI、谷歌Bard、通义星尘、阿里云百炼（通义千问、百川、月之暗面、零一万物、MiniMax）、千帆大模型（文心一言）、Gemini、Kimi Chat、koboldcpp、FastGPT、Ollama、One-API、AnythingLLM、LLM_TPU、Dify、火山引擎（豆包）`。这些模型既可以在本地运行，也可以通过云端服务提供支持。当然，为了让对话照进现实，还结合了多模态模型，包括 `Gemini、glm-4v` 的图像识别能力，获取电脑画面进行分析讲解。

`Luna AI` 的外观由 `Live2D、Vtube Studio、xuniren、UE5 结合 Audio2Face、EasyAIVtuber、数字人视频播放器（Easy-Wav2Lip、Sadtalker、GeneFace++、MuseTalk、AniTalker、本地视频）、metahuman-stream（ernerf、musetalk、wav2lip）、DH_live、live2d-TTS-LLM-GPT-SoVITS-Vtuber` 技术打造，为用户提供了一个生动、互动的虚拟形象。这使得 `Luna AI` 能够在各大直播平台，如 `Bilibili、抖音、快手、微信视频号、拼多多、1688、斗鱼、淘宝、让弹幕飞、YouTube、Twitch 和 TikTok`，进行实时互动直播。当然，它也可以在本地环境中与您进行个性化对话。

为了使交流更加自然， `Luna AI` 使用了先进的自然语言处理技术，结合文本转语音系统，如 `Edge-TTS、VITS-Fast、elevenlabs、VALL-E-X、睿声AI、OpenVoice、GPT_SoVITS、clone-voice、Azure TTS、fish-speech、ChatTTS、CosyVoice、F5-TTS、MultiTTS、MeloTTS`。这不仅让它能够生成流畅的回答，还可以通过 `so-vits-svc 和 DDSP-SVC` 实现声音的变化，以适应不同的场景和角色。

此外， `Luna AI` 还能够通过特定指令与 `Stable Diffusion` 协作，展示画作。用户还可以自定义文案，让 Luna AI 循环播放，以满足不同场合的需求。

本项目个人使用完全免费，商用抽成10%，如需商用请联系作者授权。  
如有发现一模一样的套壳售卖程序，皆为盗版，请及时止损。

## 主要功能

- **虚拟形象自定义**：用户可以上传或生成Vtuber的外观，包括服装、发型和配件，通过AI工具进行风格迁移。
- **对话AI集成**：内置聊天机器人（如基于ChatGPT或开源LLM），让Vtuber能智能回复观众问题、讲故事或进行角色扮演。
- **直播与录制**：一键启动直播模式，支持OBS集成；同时提供本地录制功能，用于内容创作。
- **表情与动作控制**：使用计算机视觉（如OpenCV）捕获用户面部表情，并映射到虚拟形象上，实现"镜像"互动。
- **多语言支持**：语音和文本处理支持中文、英语等多种语言，便于全球用户使用。
- **多模态支持**：结合图像识别能力，获取电脑画面进行分析讲解。
- **声音变化**：通过so-vits-svc 和 DDSP-SVC实现声音的变化。
- **画作展示**：通过特定指令与Stable Diffusion协作，展示画作。

## 用法

1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/Ikaros-521/AI-Vtuber.git`
   - 安装依赖：运行 `pip install -r requirements.txt`（需Python 3.8+和CUDA支持的GPU）。
   - 配置API密钥：如需外部AI服务（如OpenAI），在 `config.json` 中设置密钥。

2. **启动项目**：
   - 运行主脚本：`python main.py`
   - 通过GUI界面（基于Tkinter或类似）选择虚拟形象模板并自定义参数。

3. **创建Vtuber**：
   - 导入图像或使用内置生成器创建形象。
   - 设置对话脚本或启用AI模式。
   - 测试唇同步：输入文本，观察虚拟形象响应。

4. **直播模式**：
   - 连接直播平台API，启动流媒体输出。
   - 在聊天窗口监控互动，AI自动处理响应。

5. **高级用法**：
   - 自定义模型：替换AI模块（如用本地LLM替换云服务）。
   - 调试：查看日志文件 `logs/app.log` 以排查问题。

项目适合AI爱好者和内容创作者使用，文档详见仓库的README.md。
