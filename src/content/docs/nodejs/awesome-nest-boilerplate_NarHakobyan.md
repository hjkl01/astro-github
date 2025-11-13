---
title: awesome-nest-boilerplate
---

# Awesome Nest Boilerplate

**项目地址:** [https://github.com/NarHakobyan/awesome-nest-boilerplate](https://github.com/NarHakobyan/awesome-nest-boilerplate)

## 主要特性

- **基于NestJS框架**：采用模块化架构，支持依赖注入、装饰器和TypeScript，提供企业级后端开发体验。
- **集成ORM工具**：内置TypeORM，支持PostgreSQL、MySQL等数据库，简化实体管理和迁移操作。
- **认证与授权**：集成JWT和Passport.js，支持用户注册、登录和角色-based访问控制（RBAC）。
- **API文档化**：使用Swagger/OpenAPI自动生成API文档，便于前端开发和测试。
- **测试支持**：预配置Jest和Supertest，支持单元测试和端到端（E2E）测试。
- **环境配置**：使用dotenv管理开发、生产环境变量，支持多环境切换。
- **错误处理与日志**：内置全局异常过滤器和Winston日志系统，提高应用鲁棒性。
- **模块化结构**：清晰的项目目录结构，包括控制器、服务、模块和共享组件，便于扩展和维护。
- **多运行时支持**：支持 Node.js、Bun 和 Deno 运行时，可以使用任意一种运行、构建和测试应用。

## 主要功能

- **用户管理**：提供CRUD操作，支持用户创建、更新、删除和查询。
- **认证系统**：实现安全的登录、令牌验证和刷新机制。
- **数据库交互**：通过Repository模式处理数据持久化，支持事务和关系查询。
- **API路由**：RESTful API设计，支持GET、POST、PUT、DELETE等HTTP方法。
- **文件上传**：集成Multer，支持图片和文件上传处理。
- **邮件服务**：可选集成Nodemailer，用于发送验证邮件或通知。
- **实时功能**：支持WebSocket（通过Socket.io）实现聊天或通知推送。
- **性能优化**：内置缓存（如Redis）和速率限制（throttler），提升应用性能。

## 用法

1. **克隆项目**：

   ```
   git clone https://github.com/NarHakobyan/awesome-nest-boilerplate.git
   cd awesome-nest-boilerplate
   ```

2. **安装依赖**：

   ```
   npm install
   ```

3. **配置环境**：
   - 复制`.env.example`为`.env`，并填写数据库连接、JWT密钥等配置（如DB_HOST、JWT_SECRET）。

4. **运行迁移**（如果使用TypeORM）：

   ```
   npm run typeorm:migration:run
   ```

5. **启动开发服务器**：

   ```
   npm run start:dev
   ```

   - 应用默认运行在`http://localhost:3000`。
   - 访问Swagger文档：`http://localhost:3000/api`。

6. **构建和生产运行**：

   ```
   npm run build
   npm run start:prod
   ```

7. **运行测试**：
   ```
   npm run test
   # 或端到端测试
   npm run test:e2e
   ```

此boilerplate适合快速构建NestJS应用，可根据需求扩展模块。建议阅读项目README以获取更多细节。
