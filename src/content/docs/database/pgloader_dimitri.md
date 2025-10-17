
---
title: pgloader
---

# pgloader 项目

**GitHub 项目地址:** [https://github.com/dimitri/pgloader](https://github.com/dimitri/pgloader)

## 主要特性
pgloader 是一个开源工具，用于将数据从各种来源高效迁移到 PostgreSQL 数据库。它支持多种数据格式的导入和转换，强调数据完整性和性能优化。主要特性包括：
- **多源数据支持**：从 CSV、TSV、固定宽度文件、MySQL、SQLite、SQL Server、MS Access 等多种来源导入数据。
- **数据转换**：自动处理数据类型转换、编码转换、日期格式调整，以及自定义转换规则。
- **错误处理**：内置数据验证和错误报告机制，支持跳过无效行或中止导入。
- **并行处理**：利用多线程加速大规模数据加载，提高效率。
- **配置驱动**：通过配置文件定义迁移规则，支持复杂场景如表结构映射和索引创建。
- **安全性**：支持 SSL 连接和密码加密，确保数据传输安全。

## 主要功能
- **数据加载**：快速将外部数据文件或数据库内容加载到 PostgreSQL 中，支持增量更新。
- **模式转换**：自动或手动映射源数据库的表结构到 PostgreSQL 的 schema，包括主键、外键和约束。
- **数据清洗**：内置函数处理常见问题，如 NULL 值填充、字符串修剪和数值格式标准化。
- **报告生成**：加载完成后提供详细报告，包括加载行数、错误统计和性能指标。
- **扩展性**：可通过 Lisp 脚本自定义加载逻辑，适用于高级用户。

## 用法
pgloader 的用法主要基于命令行或配置文件。安装后（通过源代码编译或包管理器），基本步骤如下：

1. **安装**：
   - 从 GitHub 克隆仓库：`git clone https://github.com/dimitri/pgloader.git`
   - 构建并安装：使用 SBCL（Common Lisp）编译，运行 `make` 和 `make install`。

2. **基本命令**：
   - 加载 CSV 文件：`pgloader csv://file.csv postgresql://user:pass@host/dbname`
   - 从 MySQL 迁移：`pgloader mysql://user:pass@host/dbname postgresql://user:pass@host/targetdb`

3. **使用配置文件**（推荐复杂任务）：
   - 创建一个 `.load` 文件，例如：
     ```
     LOAD CSV
         FROM 'data.csv'
         INTO postgresql://user:pass@host/dbname

     WITH truncate,
          skip header = 1,
          fields optionally enclosed by '"',
          fields escaped by double-quote,
          fields terminated by ','
          SET work_mem to '256MB', maintenance_work_mem to '1GB';
     ```
   - 运行：`pgloader config.load`

更多细节请参考项目文档中的 `man pgloader` 或在线手册。pgloader 适用于数据迁移、ETL 流程和数据库升级场景。