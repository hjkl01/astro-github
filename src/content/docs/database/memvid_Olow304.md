---
title: memvid
---

# memvid

memvid 是一个基于视频的 AI 内存库，能够将数百万个文本块存储在 MP4 文件中，并提供闪电般的语义搜索，无需数据库。

## 功能特性

- **高效存储**：将文本编码为 QR 码并压缩到视频帧中，利用视频编解码器实现 50-100 倍的存储压缩。
- **快速检索**：通过索引实现亚秒级语义搜索，直接帧寻址和 QR 解码。
- **零基础设施**：仅需 Python 和 MP4 文件，无需数据库集群或 Docker。
- **便携性**：MP4 文件可在任何支持视频播放的环境中工作，支持离线使用。
- **可扩展**：支持数百万文本块的索引和搜索。

## 安装

```bash
pip install memvid
# 支持 PDF
pip install memvid PyPDF2
```

## 基本用法

### 创建视频内存

```python
from memvid import MemvidEncoder

# 从文本块创建视频内存
chunks = ["NASA 成立于 1958 年", "阿波罗 11 号于 1969 年登月", "国际空间站于 1998 年发射"]
encoder = MemvidEncoder()
encoder.add_chunks(chunks)
encoder.build_video("space.mp4", "space_index.json")
```

### 与内存聊天

```python
from memvid import MemvidChat

# 与内存交互
chat = MemvidChat("space.mp4", "space_index.json")
response = chat.chat("人类何时登上月球？")
print(response)  # 引用阿波罗 11 号于 1969 年
```

## 高级用法

### 文档助手

```python
from memvid import MemvidEncoder
import os

encoder = MemvidEncoder(chunk_size=512)

# 索引所有 Markdown 文件
for file in os.listdir("docs"):
    if file.endswith(".md"):
        with open(f"docs/{file}") as f:
            encoder.add_text(f.read(), metadata={"file": file})

encoder.build_video("docs.mp4", "docs_index.json")
```

### PDF 库搜索

```python
# 索引多个 PDF
encoder = MemvidEncoder()
encoder.add_pdf("deep_learning.pdf")
encoder.add_pdf("machine_learning.pdf")
encoder.build_video("ml_library.mp4", "ml_index.json")

# 跨书籍语义搜索
from memvid import MemvidRetriever
retriever = MemvidRetriever("ml_library.mp4", "ml_index.json")
results = retriever.search("反向传播", top_k=5)
```

### 交互式 Web UI

```python
from memvid import MemvidInteractive

# 在 http://localhost:7860 启动
interactive = MemvidInteractive("knowledge.mp4", "index.json")
interactive.run()
```

### 规模优化

```python
# 大数据集最大压缩
encoder.build_video(
    "compressed.mp4",
    "index.json",
    fps=60,              # 每秒更多帧
    frame_size=256,      # 更小的 QR 码
    video_codec='h265',  # 更好的压缩
    crf=28              # 质量权衡
)
```

### 自定义嵌入

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')
encoder = MemvidEncoder(embedding_model=model)
```

### 并行处理

```python
encoder = MemvidEncoder(n_workers=8)
encoder.add_chunks_parallel(million_chunks)
```

## CLI 用法

```bash
# 处理文档
python examples/file_chat.py --input-dir /docs --provider openai

# 高级编解码器
python examples/file_chat.py --files doc.pdf --codec h265

# 加载现有
python examples/file_chat.py --load-existing output/memory
```

## 性能

- **索引**：现代 CPU 上约 10K 块/秒
- **搜索**：1M 块 <100ms（包括解码）
- **存储**：100MB 文本 → 1-2MB 视频
- **内存**：无论大小，恒定 500MB RAM

## 未来版本

v2 将包括：

- **增量编码**：通过知识版本进行时间旅行
- **流式摄取**：实时添加到视频
- **云仪表板**：带 API 管理的 Web UI
- **智能编解码器**：根据内容自动选择 AV1/HEVC
- **GPU 加速**：批量编码 100 倍更快
