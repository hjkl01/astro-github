
---
title: register
---

# Register

**项目地址**: https://github.com/is-a-dev/register

## 主要特性

- **简洁的 RESTful API**：使用 Node.js + Express 快速搭建后端服务。  
- **用户注册与登录**：支持以邮箱/用户名注册、登录并返回 JWT。  
- **密码安全**：采用 bcrypt 对密码进行加密存储。  
- **JWT 认证**：生成、校验 JWT，支持访问受限接口。  
- **多数据库支持**：默认 SQLite，亦可通过配置使用 PostgreSQL / MySQL / MongoDB。  
- **Swagger 文档**：自动生成接口文档，访问 `/api-docs` 即可查看。  
- **Docker 化**：提供 Dockerfile，支持一键构建与部署。  
- **单元测试**：使用 Jest 对核心业务逻辑进行单元测试。  

## 功能列表

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/register` | 用户注册（邮箱/用户名、密码等） |
| POST | `/api/login` | 用户登录，返回 JWT |
| GET  | `/api/users/:id` | 获取指定用户信息（需 JWT） |
| PUT  | `/api/users/:id` | 更新用户信息（需 JWT） |
| DELETE | `/api/users/:id` | 删除用户（管理员权限） |
| POST | `/api/refresh` | 刷新 access token |

## 使用方法

1. **克隆项目**  
   ```bash
   git clone https://github.com/is-a-dev/register.git
   cd register
   ```

2. **安装依赖**  
   ```bash
   npm install
   ```

3. **配置环境变量**（复制 `.env.example` 为 `.env` 并修改）  
   ```dotenv
   PORT=3000
   DB_URL=sqlite://./db.sqlite3   # 或者 postgres://user:pass@host/db
   JWT_SECRET=your_jwt_secret
   ```

4. **启动服务**  
   ```bash
   npm run dev   # 监听文件变化
   # 或
   npm start     # 生产环境
   ```

5. **访问 Swagger 文档**  
   浏览器访问 `http://localhost:3000/api-docs` 查看接口文档。

6. **Docker 部署**（可选）  
   ```bash
   docker build -t register-app .
   docker run -p 3000:3000 --env-file .env register-app
   ```

7. **运行单元测试**  
   ```bash
   npm test
   ```

> **提示**：如果使用非 SQLite 数据库，请先在数据库中执行 `npm run migrate`（或对应迁移命令）完成表结构创建。