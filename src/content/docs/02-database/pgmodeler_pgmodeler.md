---
title: pgmodeler
---

# pgModeler 项目描述

## 项目地址
[https://github.com/pgmodeler/pgmodeler](https://github.com/pgmodeler/pgmodeler)

## 主要特性
pgModeler 是一个开源的 PostgreSQL 数据库建模工具，专为设计和管理 PostgreSQL 数据库而开发。它提供了一个图形化的用户界面，支持从概念设计到物理实现的完整数据库建模流程。主要特性包括：

- **图形化建模界面**：直观的拖拽式界面，支持实体关系图 (ERD) 的创建和编辑。
- **PostgreSQL 原生支持**：完全兼容 PostgreSQL 的所有功能，包括扩展、触发器、序列和自定义类型。
- **反向工程**：从现有数据库导入结构，自动生成模型图。
- **前向工程**：从模型生成 SQL 脚本，支持创建、更新和迁移数据库。
- **模型验证**：内置验证工具检查模型的完整性和一致性。
- **多平台支持**：兼容 Windows、Linux 和 macOS。
- **开源与社区驱动**：基于 GPL 许可，允许用户自定义和扩展。
- **高级功能**：支持关系继承、视图设计、权限管理以及数据导入/导出。

## 主要功能
pgModeler 的核心功能围绕 PostgreSQL 数据库生命周期展开：

- **数据库设计**：创建表、列、约束（主键、外键、唯一、检查）、索引和视图。
- **关系管理**：可视化定义表间关系，支持一对多、多对多等。
- **脚本生成**：自动产生 DDL（数据定义语言）脚本，支持版本控制和差异比较。
- **模型导入/导出**：导入 SQL 文件或数据库连接导出模型，支持 XML 和 PNG 等格式。
- **数据建模**：虽然主要聚焦结构，但可集成数据生成器模拟数据。
- **集成工具**：与 pgAdmin 等工具结合使用，支持直接连接 PostgreSQL 服务器测试模型。

## 用法
pgModeler 的使用简单直观，适合数据库管理员、开发者和设计师。基本步骤如下：

1. **安装**：
   - 从 GitHub Releases 下载预编译二进制文件，或通过包管理器安装（例如，Ubuntu: `sudo apt install pgmodeler`）。
   - 确保 PostgreSQL 已安装并运行。

2. **启动与创建模型**：
   - 运行 `pgmodeler` 命令或打开 GUI。
   - 新建项目：File > New Model，选择 PostgreSQL 版本。

3. **设计数据库**：
   - 使用工具栏拖拽表、视图等元素到画布。
   - 编辑属性：在右侧面板定义列类型、约束和关系。
   - 连接关系：拖动线条从一个表到另一个，设置外键。

4. **验证与生成**：
   - Tools > Validate Model 检查错误。
   - File > Export > SQL Dump 生成脚本。
   - 连接数据库：Database > Connect，执行脚本创建实际数据库。

5. **反向工程**：
   - Database > Import > Database，选择连接参数，从现有数据库生成模型。

6. **高级用法**：
   - 使用插件扩展功能。
   - 通过命令行模式批量处理：`pgmodeler --input model.pgmodeler --output script.sql`。

更多细节请参考项目文档或示例文件。