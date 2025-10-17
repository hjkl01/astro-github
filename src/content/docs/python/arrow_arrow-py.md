
---
title: arrow
---

# Arrow 项目概述

**项目地址**: [https://github.com/arrow-py/arrow](https://github.com/arrow-py/arrow)

## 主要特性

Arrow 是一个 Python 库，提供了一个更人性化和直观的日期时间处理接口。它基于 Python 的标准 `datetime` 模块，但通过更简洁的 API 和额外的功能来简化日期时间操作。主要特性包括：

- **人性化时间表示**：允许以自然语言方式创建、操作和格式化日期时间，例如“今天”、“明天”或“上周一”。
- **时区支持**：内置时区处理，支持 IANA 时区数据库，无需额外依赖。
- **不可变对象**：Arrow 对象是不可变的，确保线程安全和函数式编程友好。
- **国际化**：支持多种语言的本地化格式化和解析。
- **偏移量计算**：轻松计算相对日期，如“3 个月后”或“2 周前”。
- **与标准库兼容**：可以无缝转换为 `datetime` 对象，并支持大多数标准操作。
- **轻量级**：无外部依赖，易于集成到现有项目中。

Arrow 解决了 Python 标准库中日期时间处理的痛点，如复杂的时区转换和冗长的代码。

## 主要功能

- **创建日期时间**：从字符串、时间戳或现有 `datetime` 对象创建 Arrow 对象。
- **格式化和解析**：使用自定义格式字符串或 ISO 8601 标准解析和输出日期。
- **时间计算**：支持加减时间单位（如天、月、年），并处理闰年和时区偏移。
- **比较和排序**：提供直观的比较方法，如 `arrow1 < arrow2`。
- **时区转换**：轻松切换时区，例如从 UTC 到本地时间。
- **人类可读输出**：生成如“2 天前”或“明年 3 月”的描述性字符串。
- **周期和范围**：处理日期范围、迭代周/月/年等周期。

## 用法示例

### 安装
```bash
pip install arrow
```

### 基本用法

1. **创建 Arrow 对象**：
   ```python
   import arrow

   # 从当前时间创建
   now = arrow.now()
   print(now)  # 输出类似: 2023-10-01T12:00:00.123456+00:00

   # 从字符串创建（指定时区）
   dt = arrow.get('2023-10-01', 'YYYY-MM-DD')
   utc_dt = arrow.get('2023-10-01T12:00:00', 'YYYY-MM-DDTHH:mm:ss', tzinfo='UTC')
   ```

2. **时间计算**：
   ```python
   tomorrow = now.shift(days=1)
   next_month = now.shift(months=1)
   print(tomorrow.humanize())  # 输出: "tomorrow"（或本地化版本）
   ```

3. **格式化和时区**：
   ```python
   # 格式化输出
   formatted = now.format('YYYY-MM-DD HH:mm:ss')
   print(formatted)  # 输出: 2023-10-01 12:00:00

   # 时区转换
   local = now.to('Asia/Shanghai')
   print(local)  # 转换为上海时区
   ```

4. **解析和比较**：
   ```python
   # 解析自然语言
   parsed = arrow.get('today')
   print(parsed == now)  # True，如果是今天

   # 比较
   if dt < now:
       print("过去的时间")
   ```

更多高级用法，请参考官方文档：[Arrow Documentation](https://arrow.readthedocs.io/en/latest/)。Arrow 适用于 Web 开发、数据分析和任何需要日期处理的 Python 项目。