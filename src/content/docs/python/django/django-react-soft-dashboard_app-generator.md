---
title: django-react-soft-dashboard
---

# Django React Soft Dashboard 项目

## 项目地址
[GitHub 项目地址](https://github.com/app-generator/django-react-soft-dashboard)

## 主要特性
- **全栈架构**：基于 Django（后端框架）和 React（前端框架）构建，提供现代化的全栈 Web 应用开发模板。
- **软仪表盘设计**：采用 Soft UI Dashboard 主题，界面优雅、响应式，支持暗黑模式和多种 UI 组件（如图表、表格、表单）。
- **认证系统**：内置用户注册、登录、登出功能，支持 JWT 或会话认证。
- **模块化结构**：后端使用 Django 的 MVT 模式，前端使用 React 的组件化开发，便于扩展和维护。
- **集成工具**：支持 PostgreSQL/MySQL 等数据库、Redis 缓存，以及 Docker 部署。
- **开源免费**：MIT 许可，适合开发者快速启动仪表盘项目。

## 主要功能
- **用户管理**：管理员面板，支持用户角色管理、权限控制。
- **仪表盘页面**：实时数据可视化，包括图表（Chart.js）、进度条和统计卡片。
- **CRUD 操作**：后端 API 支持创建、读取、更新、删除数据，前端通过 Axios 调用 API。
- **路由与导航**：React Router 处理前端路由，Django URLs 处理后端路由。
- **主题与自定义**：内置 Tailwind CSS 和 Bootstrap，支持自定义样式和组件。
- **安全特性**：CSRF 保护、输入验证、HTTPS 支持。

## 用法
1. **克隆仓库**：  
   ```
   git clone https://github.com/app-generator/django-react-soft-dashboard.git
   cd django-react-soft-dashboard
   ```

2. **环境设置**：  
   - 安装 Python 依赖：`pip install -r requirements.txt`（后端）。  
   - 安装 Node.js 依赖：`npm install`（前端）。  
   - 配置数据库：在 `settings.py` 中设置数据库连接。

3. **运行后端**：  
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. **运行前端**：  
   ```
   npm start
   ```

5. **访问应用**：  
   - 后端 API：`http://localhost:8000`。  
   - 前端仪表盘：`http://localhost:3000`。  
   - 创建超级用户：`python manage.py createsuperuser`，然后登录 `/admin`。

6. **部署**：使用 Docker Compose 或 Heroku 等平台部署，支持生产环境配置。  
   参考仓库的 README.md 获取详细步骤和故障排除。