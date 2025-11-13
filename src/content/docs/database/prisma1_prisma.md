---
title: prisma1
---

# Prisma 1 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/prisma/prisma1)

## 主要特性
Prisma 1 是一个开源的现代数据库工具包和 ORM（对象关系映射）框架，主要用于 Node.js 和 TypeScript 环境。它强调声明式数据建模、类型安全和高效的数据库交互。核心特性包括：
- **声明式数据建模**：使用 Prisma Schema 定义数据库结构，支持关系型数据库如 PostgreSQL、MySQL 和 SQLite。
- **类型安全的查询**：生成类型安全的客户端，支持自动代码生成，确保查询与数据库模式一致。
- **实时订阅**：支持 GraphQL 订阅，实现数据库变化的实时通知。
- **迁移管理**：内置迁移工具，帮助管理数据库 schema 的演变。
- **GraphQL 支持**：无缝集成 GraphQL，提供自动生成的 API 端点。
- **性能优化**：高效的查询执行和批量操作，减少 N+1 查询问题。

## 主要功能
- **数据库客户端生成**：基于 schema 自动生成 Prisma Client，用于执行 CRUD 操作、查询和事务。
- **查询构建器**：提供链式 API（如 `prisma.user.findMany({ where: { name: 'Alice' } })`）来构建复杂查询。
- **关系处理**：支持一对多、多对多关系，自动处理联接查询。
- **中间件和插件**：允许自定义查询逻辑，如日志记录或认证。
- **部署友好**：支持 Docker 和云环境部署，便于 CI/CD 集成。

## 用法
1. **安装**：在 Node.js 项目中运行 `npm install prisma --save-dev` 和 `npm install @prisma/client`。
2. **初始化**：使用 `npx prisma init` 创建 `prisma/schema.prisma` 文件，配置数据库连接（如 `datasource db { provider = "postgresql" url = env("DATABASE_URL") }`）。
3. **定义模型**：在 schema 中定义数据模型，例如：
   ```
   model User {
     id    Int    @id @default(autoincrement())
     name  String
     posts Post[]
   }

   model Post {
     id        Int      @id @default(autoincrement())
     title     String
     user      User     @relation(fields: [userId], references: [id])
     userId    Int
   }
   ```
4. **生成客户端**：运行 `npx prisma generate` 生成 Prisma Client。
5. **数据库迁移**：使用 `npx prisma migrate dev` 创建和应用迁移。
6. **使用客户端**：在代码中导入并使用，例如：
   ```javascript
   const { PrismaClient } = require('@prisma/client');
   const prisma = new PrismaClient();

   async function main() {
     const allUsers = await prisma.user.findMany();
     console.log(allUsers);
   }

   main().finally(() => prisma.$disconnect());
   ```
7. **部署**：在生产环境中设置环境变量，并运行生成和迁移命令。

注意：Prisma 1 已归档，推荐迁移到 Prisma 2+ 以获得最新功能和支持。