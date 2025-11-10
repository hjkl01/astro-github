---
title: quick-SQL-cheatsheet
---

# Quick SQL Cheatsheet

**项目地址：** [https://github.com/enochtangg/quick-SQL-cheatsheet/blob/master/README_zh-hans.md](https://github.com/enochtangg/quick-SQL-cheatsheet/blob/master/README_zh-hans.md)

## 主要特性
- **简洁快速参考**：这是一个SQL快速备忘单，专注于核心SQL语法和常用操作，提供简明扼要的示例，便于开发者或学习者快速查阅。
- **多语言支持**：项目包含英文和中文版本（README_zh-hans.md），便于不同语言用户使用。
- **覆盖广泛主题**：包括SQL基础语法、查询操作、聚合函数、连接、子查询、窗口函数等常见SQL概念。
- **开源免费**：基于GitHub托管，用户可以fork、贡献或下载使用，无需额外费用。
- **易于扩展**：Markdown格式，便于本地保存、打印或集成到笔记工具中。

## 功能
- **SQL语法速查**：提供SELECT、INSERT、UPDATE、DELETE等基本DML语句的语法模板和示例。
- **高级查询支持**：涵盖JOIN（内连接、外连接）、GROUP BY、HAVING、子查询、CTE（公共表表达式）等功能。
- **函数参考**：列出常用内置函数，如聚合函数（COUNT、SUM、AVG）、字符串函数（CONCAT、SUBSTRING）、日期函数（NOW、DATE_ADD）等。
- **数据库兼容性**：主要针对标准SQL，但示例适用于MySQL、PostgreSQL等主流数据库。
- **学习辅助**：通过代码块和解释，帮助用户理解SQL执行逻辑，避免常见错误。

## 用法
1. **在线浏览**：直接访问GitHub项目页面，阅读README_zh-hans.md文件，复制所需SQL片段到你的查询工具中测试。
2. **本地下载**：克隆仓库（`git clone https://github.com/enochtangg/quick-SQL-cheatsheet.git`），打开README_zh-hans.md文件，使用Markdown查看器或编辑器阅读。
3. **日常开发**：在编写SQL时，作为参考手册快速查找语法，例如使用SELECT语句查询数据：  
   ```
   SELECT column1, column2 FROM table_name WHERE condition;
   ```
4. **学习练习**：结合示例练习，如JOIN操作：  
   ```
   SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;
   ```
5. **贡献与自定义**：如果需要添加特定数据库的语法，可fork项目并提交pull request，或本地修改Markdown文件以适应个人需求。