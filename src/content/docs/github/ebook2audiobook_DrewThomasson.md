
---
title: ebook2audiobook
---


# ebook2audiobook

**项目地址:** https://github.com/DrewThomasson/ebook2audiobook

## 主要特性
- ✔ 支持多种电子书格式（EPUB、PDF、MOBI、AZW3 等）  
- ✔ 自动提取文本并按章节或段落拆分  
- ✔ 多语音引擎：Google TTS、Amazon Polly、Microsoft Azure TTS、pyttsx3  
- ✔ 语言、语速、音量自定义  
- ✔ 输出 MP3 / WAV，可设置声道和比特率  
- ✔ 命令行工具，CLI 与 Python API 双接口  
- ✔ 配置文件（JSON/YAML）支持批量转换  
- ✔ 进度条、日志记录、异常处理  

## 快速使用
### 安装
### CLI
```bash
# 单文件转换
ebook2audiobook input.epub \
    --voice google \
    --lang en \
    --rate 200 \
    --output book.mp3

# 批量转换
ebook2audiobook --config config.yaml
```

### Python API
```python
from ebook2audiobook import Ebook2AudioBook

converter = Ebook2AudioBook('my_book.epub')
converter.convert(
    output='my_book.mp3',
    voice='aws',
    language='fr',
    rate=180,
)
```

## 配置示例（config.yaml）
```yaml
files:
  - path: books/book1.epub
    output: output/book1.mp3
  - path: books/book2.pdf
    output: output/book2.mp3
voice: google
language: en
rate: 210
volume: 1.0
```

## 依赖
- ebooklib、pdfminer.six、pydub、gTTS、boto3、requests、pyttsx3  

## 许可证
MIT © DrewThomasson
