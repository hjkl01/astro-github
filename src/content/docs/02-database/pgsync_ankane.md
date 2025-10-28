
---
title: pgsync
---

# PGSync 项目描述

## 项目地址
[https://github.com/ankane/pgsync](https://github.com/ankane/pgsync)

## 主要特性
PGSync 是一个 Ruby gem，用于将 PostgreSQL 数据库同步到 Elasticsearch。它支持实时数据同步、复杂查询优化和自动索引管理。主要特性包括：
- **实时同步**：使用 PostgreSQL 的逻辑复制或触发器机制，实现数据变更的即时推送。
- **复杂查询支持**：自动生成 Elasticsearch 索引，处理关联关系（如 JOIN 操作），允许在 Elasticsearch 中执行类似 SQL 的复杂查询。
- **性能优化**：支持批量同步、增量更新和缓存机制，减少数据库负载。
- **易集成**：与 Ruby on Rails 无缝集成，支持自定义映射和过滤规则。
- **监控与错误处理**：内置日志记录和重试机制，确保同步可靠性。

## 主要功能
- **数据同步**：从 PostgreSQL 表或视图同步数据到 Elasticsearch，支持全量和增量同步。
- **关系处理**：自动处理多表关联，生成嵌套的 Elasticsearch 文档。
- **搜索与查询**：在 Elasticsearch 中执行全文搜索、过滤和聚合，模拟数据库查询。
- **配置灵活**：通过 YAML 或 Ruby 配置定义同步规则、索引结构和同步频率。
- **扩展性**：支持插件扩展，如自定义数据转换或集成其他工具。

## 用法
1. **安装**：
   - 确保已安装 PostgreSQL 和 Elasticsearch。
   - 使用 Bundler：在 Gemfile 中添加 `gem 'pgsync'`，然后运行 `bundle install`。

2. **配置**：
   - 创建 `config/pgsync.yml` 文件，定义数据库连接、Elasticsearch 索引和同步规则。例如：
     ```
     database:
       adapter: postgresql
       host: localhost
       database: mydb
     elasticsearch:
       hosts: ["localhost:9200"]
     syncs:
       - table: users
         elasticsearch_index: users
         relationships:
           - posts
     ```

3. **运行同步**：
   - 初始同步：`bundle exec pgsync`（同步所有配置的表）。
   - 实时同步：`bundle exec pgsync --daemon`（后台运行，监听变更）。
   - 特定表同步：`bundle exec pgsync users`。

4. **高级用法**：
   - 添加触发器：运行 `bundle exec pgsync triggers` 在 PostgreSQL 中安装同步触发器。
   - 查询示例：在 Rails 控制中使用 `Pgsync.search('query', index: 'users')` 执行搜索。
   - 更多细节参考项目 README 和文档。