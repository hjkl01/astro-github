
---
title: strapi-docker
---

# Strapi Docker 示例项目

**项目地址：** [https://github.com/strapi/strapi-docker/tree/master/examples](https://github.com/strapi/strapi-docker/tree/master/examples)

## 主要特性
- **基于 Docker 的 Strapi 部署**：该项目提供 Strapi CMS（内容管理系统）的 Docker 容器化示例，支持快速部署和扩展。
- **多环境支持**：包括开发、生产和自定义配置的 Docker 环境，兼容 Docker Compose 和 Kubernetes。
- **数据库集成**：内置支持 SQLite、PostgreSQL、MySQL 等数据库的 Docker 配置，便于数据持久化和迁移。
- **插件和扩展**：展示如何集成 Strapi 的插件系统，并通过 Docker 卷挂载自定义内容。
- **安全性与优化**：示例包含环境变量管理、SSL 支持和性能调优的最佳实践。

## 主要功能
- **快速启动 Strapi**：使用 Docker 运行 Strapi 实例，实现 headless CMS 的内容管理、API 生成和用户认证。
- **示例配置**：提供多种 Docker Compose 文件，如基本部署、带数据库的完整栈，以及自定义构建的变体。
- **内容管理**：支持创建、编辑和管理内容类型、媒体文件和角色权限。
- **API 开发**：自动生成 RESTful 和 GraphQL API，支持实时预览和 webhook 集成。
- **可扩展性**：易于添加自定义插件、主题和第三方服务集成。

## 用法
1. **克隆仓库**：  
   ```
   git clone https://github.com/strapi/strapi-docker.git
   cd strapi-docker/examples
   ```

2. **选择示例**：  
   浏览 `examples` 目录，选择如 `docker-compose` 或 `custom` 文件夹。

3. **启动服务**（以 docker-compose 示例为例）：  
   - 编辑 `.env` 文件配置数据库和 Strapi 设置。  
   - 运行命令：  
     ```
     docker-compose up -d
     ```  
   Strapi 将在 `http://localhost:1337/admin` 可用。

4. **自定义配置**：  
   修改 `Dockerfile` 或 `docker-compose.yml` 以添加插件或调整端口。  
   对于生产环境，使用 `docker-compose.prod.yml` 并设置环境变量如 `NODE_ENV=production`。

5. **停止和清理**：  
   ```
   docker-compose down -v
   ```  
   参考仓库 README 以获取更多高级用法和故障排除。