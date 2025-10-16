
---
title: alive-progress
---

# alive-progress 项目

## 项目地址
[GitHub 项目地址](https://github.com/rsalmei/alive-progress)

## 主要特性
- **生动动画效果**：提供多种动态进度条样式，如心跳、旋转、计数器等，模拟生命般的动画，使进度显示更具吸引力。
- **自定义灵活**：支持自定义动画、颜色、长度和更新频率，易于适应不同终端环境。
- **兼容性强**：适用于 Python 3.6+，支持 Jupyter Notebook 和各种终端（包括 Windows、macOS 和 Linux）。
- **轻量高效**：无外部依赖，仅需标准库，性能开销低。
- **多语言支持**：内置英文提示，可轻松扩展到其他语言。

## 主要功能
- **实时进度跟踪**：显示任务进度百分比、已完成项数和预计剩余时间。
- **动画渲染**：使用 ASCII 艺术和 Unicode 字符创建流畅的动画效果，避免静态进度条的单调。
- **错误处理**：自动处理异常情况，如进度超限或中断，确保输出优雅。
- **集成简单**：可无缝集成到循环或迭代任务中，支持手动或自动更新。

## 用法示例
### 安装
```bash
pip install alive-progress
```

### 基本用法
```python
from alive_progress import alive_bar
import time

# 模拟一个循环任务
with alive_bar(100) as bar:  # total=100 表示总项数
    for i in range(100):
        time.sleep(0.05)  # 模拟工作
        bar()  # 更新进度

# 输出示例：动态动画进度条，如 "▋▋▋▋▋ 50/100 [50%] in 2s"
```

### 自定义样式
```python
from alive_progress import alive_bar

with alive_bar(10, bar='classic', spinner='dots') as bar:
    for i in range(10):
        # 你的代码
        bar()
```

更多细节请参考 [GitHub 项目文档](https://github.com/rsalmei/alive-progress)。