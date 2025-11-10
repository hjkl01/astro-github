---
title: pendulum
---

# Pendulum 项目

## 项目地址
[GitHub 项目地址](https://github.com/sdispater/pendulum)

## 主要特性
Pendulum 是一个 Python 库，旨在提供比 Python 标准库 `datetime` 更易用和功能丰富的日期时间处理工具。它基于 `dateutil` 和 `pytz` 库，专注于简化日期时间操作，同时保持高性能和准确性。主要特性包括：
- **直观 API**：语法简洁，支持链式调用，便于处理复杂日期时间逻辑。
- **时区支持**：内置全面的时区处理，支持 IANA 时区数据库，避免常见时区错误。
- **相对日期计算**：轻松添加/减去时间单位，如天、周、月、年，支持智能的月末处理。
- **格式化和解析**：高级字符串格式化、解析功能，支持多种 locale。
- **周期和间隔**：处理日期范围、周期性事件和时间间隔。
- **不可变性**：返回新实例，避免修改原对象，提高代码安全性。
- **兼容性**：与标准库 `datetime` 高度兼容，便于迁移。

## 主要功能
- **日期时间创建**：从字符串、时间戳或现有 `datetime` 对象创建 Pendulum 实例。
- **时间计算**：支持加减操作，如 `add(days=5)` 或 `subtract(months=1)`。
- **时区转换**：使用 `in_timezone()` 方法切换时区。
- **格式化**：使用 `format()` 方法输出自定义格式字符串，支持 i18n。
- **解析**：从自然语言字符串解析日期，如 `parse('tomorrow')`。
- **比较和排序**：支持日期时间对象的比较操作。
- **周期处理**：创建日期范围（如 `range('2023-01-01', '2023-12-31')`）并迭代。
- **本地化**：支持多种语言的月份和星期名称。

## 用法示例
安装 Pendulum：
```bash
pip install pendulum
```

基本用法：
```python
import pendulum

# 创建当前时间（UTC）
now = pendulum.now('UTC')
print(now)  # 2023-10-01T12:00:00+00:00

# 从字符串创建
dt = pendulum.parse('2023-10-01')
print(dt.format('YYYY-MM-DD'))  # 2023-10-01

# 添加时间
future = dt.add(days=7, hours=3)
print(future)  # 2023-10-08T03:00:00+00:00

# 时区转换
local = future.in_timezone('Asia/Shanghai')
print(local)  # 2023-10-08T11:00:00+08:00

# 相对日期
yesterday = pendulum.yesterday('locale=en')
print(yesterday.format('dddd, MMMM Do YYYY'))  # Sunday, September 30th 2023
```

更多细节请参考官方文档。