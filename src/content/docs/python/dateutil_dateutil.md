
---
title: dateutil
---

# dateutil 项目描述

## 项目地址
[https://github.com/dateutil/dateutil](https://github.com/dateutil/dateutil)

## 主要特性
dateutil 是 Python 的一个强大扩展日期时间库，旨在简化日期和时间的处理。它是标准库 `datetime` 模块的扩展，提供更灵活和直观的 API。主要特性包括：
- **相对时间计算**：支持自然语言描述的日期偏移，如“下一个周一”或“上个月”。
- **模糊解析**：无需预定义格式即可解析各种日期字符串，支持多种语言和格式。
- **时区处理**：集成 tz 模块，提供时区转换和 DST（夏令时）支持。
- **周期性事件**：处理重复事件和日历计算，如复活节日期。
- **轻量级**：纯 Python 实现，无需外部依赖，兼容 Python 2 和 3。

## 主要功能
- **rrule**：生成日期序列，支持每周、每月、每年等规则。
- **parser**：解析非标准日期字符串，例如“2023年10月1日”或“next Friday”。
- **tz**：处理时区信息，包括固定偏移和 IANA 时区数据库。
- **relativedelta**：计算日期间的相对差异，支持年、月、周等单位。
- **easter**：计算复活节等宗教日期。

## 用法示例
### 安装
```bash
pip install python-dateutil
```

### 基本用法
```python
from dateutil import parser
from dateutil.relativedelta import relativedelta
from datetime import datetime

# 模糊解析日期字符串
date = parser.parse("2023-10-01")
print(date)  # 输出: 2023-10-01 00:00:00

# 相对时间计算
today = datetime.now()
next_month = today + relativedelta(months=1)
print(next_month)

# 日期序列 (rrule)
from dateutil.rrule import rrule, DAILY
for dt in rrule(DAILY, byweekday=1, dtstart=datetime(2023, 10, 1), count=3):
    print(dt)  # 输出每周一的日期
```

该库广泛用于数据处理、调度任务和时间序列分析，文档详见项目 README。