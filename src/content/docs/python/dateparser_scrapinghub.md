---
title: dateparser
---

# dateparser 项目

**项目地址：** [https://github.com/scrapinghub/dateparser](https://github.com/scrapinghub/dateparser)

## 主要特性
dateparser 是一个 Python 库，用于解析人类可读的日期字符串。它支持多种语言和日期格式，能够智能处理模糊或非标准日期表达。核心特性包括：
- **多语言支持**：支持 200 多种语言的日期解析，包括中文、日文、阿拉伯文等。
- **灵活的日期格式**：自动识别各种日期格式，如 "2023年10月1日"、"October 1st, 2023"、"1/10/23" 等。
- **相对日期处理**：理解相对时间表达，如 "昨天"、"下周三"、"3天前"。
- **时区支持**：可指定时区，并处理带时区的日期字符串。
- **容错性强**：即使日期字符串不完整或有拼写错误，也能尝试解析。
- **轻量级**：依赖少，易于集成到其他项目中。

## 主要功能
- **日期解析**：将自然语言日期字符串转换为 Python 的 `datetime` 对象。
- **语言检测**：自动检测输入字符串的语言。
- **自定义设置**：允许用户指定日期顺序（如 DD/MM/YYYY 或 MM/DD/YYYY）、默认时区等。
- **批量处理**：支持解析多个日期字符串。
- **验证与提取**：检查字符串是否包含日期，并提取有效日期部分。

## 用法
安装：使用 pip 安装 `pip install dateparser`。

### 基本用法示例
```python
from dateparser import parse

# 解析简单日期
date = parse('2023年10月1日')
print(date)  # 输出: 2023-10-01 00:00:00

# 相对日期
date = parse('昨天')
print(date)  # 输出: 昨天的日期

# 指定语言
date = parse('1 Oct 2023', languages=['en'])
print(date)

# 指定时区
from dateutil.tz import gettz
date = parse('2023-10-01 12:00', settings={'TIMEZONE': gettz('Asia/Shanghai')})
print(date)

# 自定义日期顺序
date = parse('10/01/2023', settings={'DATE_ORDER': 'DMY'})
print(date)  # 解释为 10月1日
```

更多细节请参考项目 README 和文档。