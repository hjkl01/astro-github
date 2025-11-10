---
title: Django-React-Redux-Boilerplate
---

# Django-React-Redux-Boilerplate 项目

**项目地址：** [https://github.com/faisalnazik/Django-React-Redux-Boilerplate](https://github.com/faisalnazik/Django-React-Redux-Boilerplate)

## 主要特性
- **前后端分离架构**：后端使用Django框架，前端采用React和Redux构建，实现高效的现代Web应用开发。
- **预配置环境**：集成了Django REST Framework（DRF）用于API开发，Webpack用于前端打包，支持热重载（Hot Reload）。
- **认证系统**：内置JWT（JSON Web Tokens）认证机制，便于用户登录、注册和权限管理。
- **数据库支持**：默认使用SQLite，便于开发；易于切换到PostgreSQL或其他数据库。
- **开发工具集成**：包括ESLint、Prettier代码格式化，Docker支持容器化部署。
- **响应式设计**：前端使用Bootstrap或类似框架，确保跨设备兼容性。

## 主要功能
- **API开发**：Django后端提供RESTful API接口，支持CRUD操作、序列化、过滤和分页。
- **状态管理**：Redux处理前端应用状态，确保数据流清晰和可预测。
- **用户管理**：支持用户注册、登录、登出，以及基于角色的访问控制（RBAC）。
- **文件上传与处理**：集成文件上传功能，适用于图像、文档等资源管理。
- **实时更新**：前端热重载和后端开发服务器，实现快速迭代开发。
- **测试框架**：预置Django测试工具和Jest用于前端测试。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/faisalnazik/Django-React-Redux-Boilerplate.git
   cd Django-React-Redux-Boilerplate
   ```

2. **安装依赖**：
   - 后端：进入`backend`目录，运行`pip install -r requirements.txt`。
   - 前端：进入`frontend`目录，运行`npm install`。

3. **环境配置**：
   - 创建`.env`文件，设置数据库、密钥等变量（参考`env.example`）。
   - 运行数据库迁移：`python manage.py migrate`。

4. **启动开发服务器**：
   - 后端：`python manage.py runserver`（默认端口8000）。
   - 前端：`npm start`（默认端口3000）。
   - 访问`http://localhost:3000`查看前端应用。

5. **构建与部署**：
   - 前端构建：`npm run build`，输出到`backend/staticfiles`。
   - 生产部署：使用Docker Compose运行`docker-compose up`，或部署到Heroku/AWS等平台。

6. **自定义开发**：
   - 在`backend`中添加Django模型和视图。
   - 在`frontend`中使用Redux Actions和Reducers扩展功能。
   - 测试：运行`python manage.py test`（后端）和`npm test`（前端）。