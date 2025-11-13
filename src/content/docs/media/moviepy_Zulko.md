---
title: moviepy
---

# MoviePy 项目

**GitHub 项目地址:** [https://github.com/Zulko/moviepy](https://github.com/Zulko/moviepy)

## 主要特性
MoviePy 是一个开源的 Python 视频编辑库，专注于简单、高效的视频处理。它基于 FFmpeg 和 ImageMagick 等工具，支持纯 Python 实现，无需复杂的依赖。主要特性包括：
- **视频编辑功能**：支持剪切、拼接、叠加视频和图像，实现转场效果。
- **文本和特效**：添加标题、字幕、动画文本，以及颜色调整、滤镜和变换。
- **音频处理**：提取、混合音频轨道，添加背景音乐或音效。
- **格式支持**：处理多种视频格式（如 MP4、AVI、GIF），并支持帧级操作。
- **无外部依赖**：核心功能纯 Python 编写，便于集成到脚本或应用中。
- **跨平台**：兼容 Windows、macOS 和 Linux，支持 Jupyter Notebook 预览。

## 主要功能
- **视频剪辑**：裁剪视频片段、合并多个视频。
- **效果应用**：旋转、缩放、淡入淡出、速度调整。
- **图像与视频合成**：将图像序列转换为视频，或在视频上叠加图像/文本。
- **GIF 和动画**：创建 GIF 或简单动画。
- **音频同步**：与视频音频分离或重新同步。
- **批量处理**：支持脚本自动化编辑多个文件。

## 用法
安装 MoviePy 后（使用 `pip install moviepy`），可以通过简单代码实现编辑。以下是基本用法示例：

### 1. 导入和基本剪切
```python
from moviepy.editor import VideoFileClip

# 加载视频
clip = VideoFileClip("input.mp4")

# 剪切前 10 秒
subclip = clip.subclip(0, 10)

# 保存结果
subclip.write_videofile("output.mp4")
```

### 2. 添加文本叠加
```python
from moviepy.editor import TextClip, CompositeVideoClip

# 创建文本剪辑
txt_clip = TextClip("Hello World", fontsize=70, color='white').set_position('center').set_duration(5)

# 叠加到视频
video = CompositeVideoClip([clip, txt_clip])
video.write_videofile("output_with_text.mp4")
```

### 3. 音频处理
```python
# 提取音频
audio = clip.audio
audio.write_audiofile("audio.wav")

# 添加背景音乐
background = AudioFileClip("music.mp3").volumex(0.5)  # 音量减半
final_audio = CompositeAudioClip([audio, background])
clip_with_music = clip.set_audio(final_audio)
```

更多高级用法请参考官方文档。MoviePy 适合初学者和自动化脚本，学习曲线平缓。