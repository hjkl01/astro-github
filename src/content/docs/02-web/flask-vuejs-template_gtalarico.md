---
title: flask-vuejs-template
---

# Flask-Vue.js 模板项目

## 项目地址
[GitHub 项目地址](https://github.com/gtalarico/flask-vuejs-template)

## 主要特性
- **前后端分离架构**：基于 Flask（后端 Python 框架）和 Vue.js（前端 JavaScript 框架），实现清晰的前后端分离，便于开发和维护。
- **现代化工具集成**：支持 Webpack 打包、热重载（Hot Reload）和代码拆分，提高开发效率和性能。
- **API 支持**：内置 RESTful API 接口示例，便于前后端数据交互。
- **模板结构**：提供标准化的项目模板，包括 Flask 后端路由、Vue.js 组件和静态资源管理，适合快速启动 Web 应用开发。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 环境，易于部署。

## 主要功能
- **后端功能**：Flask 处理服务器逻辑，包括路由定义、数据库集成（可扩展 SQLite 或其他 ORM）和 API 端点。
- **前端功能**：Vue.js 构建单页应用（SPA），支持组件化开发、状态管理和路由导航。
- **开发工具**：集成 Gulp 或类似任务运行器，用于自动化构建、测试和部署流程。
- **示例应用**：包含基本的用户认证、数据展示和表单交互演示，展示如何连接前后端。
- **扩展性**：易于添加第三方库，如 Vuex（状态管理）和 Axios（HTTP 请求）。

## 用法
1. **克隆项目**：使用 Git 克隆仓库：
   ```
   git clone https://github.com/gtalarico/flask-vuejs-template.git
   cd flask-vuejs-template
   ```

2. **安装依赖**：
   - 后端：创建虚拟环境并安装 Flask 依赖：
     ```
     python -m venv venv
     source venv/bin/activate  # Linux/macOS，或 venv\Scripts\activate (Windows)
     pip install -r requirements.txt
     ```
   - 前端：安装 Node.js 依赖：
     ```
     npm install
     ```

3. **运行项目**：
   - 启动后端服务器：
     ```
     flask run
     ```
   - 启动前端开发服务器（支持热重载）：
     ```
     npm run dev
     ```
   - 访问 `http://localhost:5000`（后端）或 `http://localhost:8080`（前端）查看应用。

4. **构建和部署**：
   - 生产构建：
     ```
     npm run build
     ```
   - 将构建后的静态文件集成到 Flask 的 `static` 目录中，然后部署到服务器（如 Heroku 或 VPS）。

5. **自定义开发**：修改 `app.py`（Flask 入口）、Vue 组件文件，并通过 API 实现业务逻辑。参考 README.md 获取更多细节和故障排除。