
---
title: MusicGPT
---


# MusicGPT（gabotechs)

> 项目地址: https://github.com/gabotechs/MusicGPT

## 项目概述
MusicGPT 是一个基于 GPT-4 的乐曲生成框架，用户可以通过自然语言描述生成旋律、和弦进程、面向不同风格的音乐片段，并支持将生成结果导出为 MIDI 或 WAV 格式。项目中已经集成了多种第三方工具（如 Magenta、VaryMusic 等），并通过 Streamlit 搭建了可交互的 Web 界面。

## 主要特性
- **自然语言驱动**：用户只需输入如“写一段浪漫爵士钢琴独奏”，即可获得对应的旋律与伴奏。  
- **多种输出格式**：生成的音乐可直接导出为 `.mid`（MIDI）或 `.wav`（音频）文件。  
- **多风格模型**：支持 `Pop`、`Jazz`、`Classical`、`Rock` 等多种音乐风格，并可自定义音调与节奏。  
- **Web UI**：使用 Streamlit 提供交互式界面，支持实时预览和下载。  
- **后台服务**：通过 FastAPI 与 Web UI 解耦，支持多用户并发生成。  
- **可扩展**：通过插件化机制可以接入各类音频合成器（如 VST、JAMS## 安装与启动
```bash
# 1. 克隆仓库
git clone https://github.com/gabotechs/MusicGPT.git
cd MusicGPT

# 2. 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行 Streamlit 前端
streamlit run app/main.py
# 或者运行 FastAPI 后端
uvicorn api.server:app --reload
```

## 使用示例
1. 打开浏览器访问 `http://localhost:8501`（Streamlit 前端）或 `http://localhost:8000/docs`（FastAPI 文档）。  
2. 在文本框中输入 **“请为我写一段适合晚上听的抒情电子音乐”**，点击 **Generate**。  
3. 页面将显示生成的旋律图谱，并提供 **Play**、**Download MIDI**、**Download WAV** 按钮。

## 配置
- `config.yaml`：全局配置文件，支持设置 OpenAI API Key、最大 token 数、风格映射等。  
- `.env`：环境变量文件，存放 `OPENAI_API_KEY`、`MAGENTA_HOME` 等信息。

## 常见问题
- **OpenAI Key 不工作**  
  请确认你已经在 OpenAI 控制台启用 GPT-4 API，并把 Key 放在 `.env`。  
- **安装失败**  
  若出现 `protobuf` 版本冲突，可尝试升级 `pip` 并单独安装 `protobuf==3.20.*`。

## 贡献
欢迎 Issue 与 PR。请先阅读 `CONTRIBUTING.md` 了解贡献流程。

## 许可证
MIT License
```
This markdown 文件应保存为 `src/content/docs/00/MusicGPT_gabotechs.md`，即可完成需求。