---
title: flask-react-spa
---

# Flask-React-SPA 项目

## 项目地址
[https://github.com/briancappello/flask-react-spa](https://github.com/briancappello/flask-react-spa)

## 主要特性
- **前后端分离架构**：使用 Flask 作为后端 API 服务，React 作为前端单页应用（SPA），实现高效的现代 Web 开发模式。
- **API 驱动**：Flask 提供 RESTful API 接口，支持 JSON 数据交互，便于前后端独立开发和部署。
- **热重载支持**：开发模式下，Flask 和 React 均支持热重载，加速开发迭代。
- **生产优化**：集成构建工具，支持将 React 应用打包为静态文件，由 Flask 直接服务，实现无缝部署。
- **认证与安全**：内置用户认证机制（如 JWT），支持安全的会话管理。
- **模块化设计**：代码结构清晰，后端使用 Flask 的蓝图（Blueprints），前端采用 React 的组件化开发。

## 主要功能
- **用户管理**：支持用户注册、登录、登出，以及个人资料管理。
- **API 端点**：提供示例 API，如获取用户列表、帖子等，易于扩展自定义功能。
- **前端界面**：React 构建的响应式 UI，包括导航栏、表单和动态内容渲染。
- **数据交互**：前端通过 Axios 或 Fetch 调用后端 API，实现实时数据更新。
- **错误处理**：内置全局错误处理和日志记录，提升应用鲁棒性。
- **测试支持**：包含单元测试框架，便于测试 API 和组件。

## 用法
1. **环境准备**：
   - 安装 Python 3.x 和 Node.js。
   - 克隆仓库：`git clone https://github.com/briancappello/flask-react-spa.git`。
   - 进入项目目录：`cd flask-react-spa`。

2. **后端设置**：
   - 安装依赖：`pip install -r requirements.txt`。
   - 设置环境变量（如数据库配置），运行 Flask：`flask run`（默认端口 5000）。

3. **前端设置**：
   - 进入前端目录：`cd client`。
   - 安装依赖：`npm install`。
   - 开发模式运行：`npm start`（默认端口 3000，前端代理到后端）。

4. **生产部署**：
   - 构建 React：`npm run build`（生成静态文件到 `build` 目录）。
   - 配置 Flask 服务静态文件：更新 `app.py` 以服务 `build` 目录。
   - 运行：`python app.py` 或使用 Gunicorn 等部署到服务器。

5. **扩展**：
   - 添加新 API：在 Flask 的 `api` 模块中定义路由。
   - 修改前端：在 React 的 `src` 目录编辑组件和页面。
   - 测试：运行 `pytest` 测试后端，`npm test` 测试前端。

此项目适合学习 Flask 与 React 集成，或作为快速启动单页应用的模板。