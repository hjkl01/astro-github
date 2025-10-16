
---
title: mimesis
---

# Mimesis 项目

## 项目地址
[GitHub 项目地址](https://github.com/lk-geimfari/mimesis)

## 主要特性
Mimesis 是一个开源的 Python 库，用于生成模拟数据。它基于提供的数据提供者（providers）来创建各种类型的伪造数据，如姓名、地址、电子邮件、日期等。核心特性包括：
- **多语言支持**：支持多种语言和区域设置的数据生成，例如英文、中文、俄文等。
- **高度可定制**：通过不同的提供者（Provider）和区域（Locale）来生成特定类型的数据。
- **数据类型丰富**：涵盖个人信息、互联网数据、金融数据、文本内容等多个类别。
- **无依赖性强**：核心功能无需外部依赖，轻量级且高效。
- **开源与活跃维护**：MIT 许可，社区驱动，定期更新。

## 主要功能
Mimesis 的功能主要围绕数据生成展开，分为多个提供者模块：
- **个人信息**：生成姓名、性别、年龄、地址、电话号码等。
- **互联网数据**：创建电子邮件、URL、IP 地址、用户名等。
- **金融数据**：模拟信用卡号、银行账户、货币金额等。
- **文本与内容**：产生句子、段落、书籍标题、公司名称等。
- **时间与日期**：生成日期、时间、时区等。
- **其他**：包括开发相关数据（如代码、UUID）、结构化数据（如 JSON 示例）等。
它支持随机种子设置以确保可重现性，并可通过组合提供者创建复杂数据集。

## 用法
### 安装
使用 pip 安装：
```
pip install mimesis
```

### 基本用法示例
1. **导入和初始化**：
   ```python
   from mimesis import Person, Address
   from mimesis.locales import Locale

   # 使用英文区域
   person = Person('en')
   address = Address('en')
   ```

2. **生成数据**：
   ```python
   # 生成姓名
   name = person.full_name()  # 示例输出: "John Doe"

   # 生成地址
   street = address.street()  # 示例输出: "123 Main St"

   # 使用中文区域
   person_zh = Person(Locale.ZH)
   name_zh = person_zh.full_name()  # 示例输出: "李伟"
   ```

3. **高级用法**：
   - 设置种子：`person = Person('en', seed=42)` 以确保结果一致。
   - 生成列表：`names = person.full_names(quantity=5)` 生成 5 个姓名。
   - 自定义提供者：通过 `mimesis.Generic` 类组合多个提供者。

更多细节请参考项目文档和示例代码。