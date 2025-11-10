---
title: atrilabs-engine
---

# Atri-Labs Engine 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/Atri-Labs/atrilabs-engine)

## 主要特性
Atri-Labs Engine（简称 Atri Engine）是一个开源的 Web 应用开发框架，专注于简化交互式 Web 应用的构建。它基于 Python 和 React 技术栈，允许开发者使用 Python 代码来定义应用的状态和逻辑，而无需编写复杂的 JavaScript 前端代码。主要特性包括：
- **Python 优先开发**：使用纯 Python 编写应用逻辑，支持 Streamlit-like 的声明式编程风格。
- **实时交互**：内置事件驱动系统，支持用户交互（如点击、输入）实时更新 UI，无需页面刷新。
- **组件化 UI**：集成 React 组件库，提供丰富的预置组件（如按钮、图表、表单），并支持自定义组件。
- **跨平台兼容**：生成的 Web 应用可在浏览器中运行，支持部署到各种云平台。
- **热重载开发**：开发过程中支持代码热更新，加速迭代。
- **模块化架构**：易于扩展，支持插件系统和第三方集成。

## 主要功能
- **状态管理**：通过 Python 类定义应用状态，支持 reactive 更新机制，当状态变化时自动渲染 UI。
- **事件处理**：内置事件监听器，用于处理用户交互，如按钮点击、表单提交等。
- **数据可视化**：集成 Plotly 和其他库，支持动态图表和数据展示。
- **API 集成**：轻松连接后端 API 或数据库，实现数据驱动应用。
- **主题和样式自定义**：支持 CSS 主题切换和自定义样式。
- **部署支持**：一键构建为静态文件或 Docker 容器，便于部署到 Vercel、Netlify 等平台。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/Atri-Labs/atrilabs-engine.git`
   - 安装依赖：`pip install -r requirements.txt`（后端 Python 环境）和 `npm install`（前端 React 环境）。

2. **创建应用**：
   - 在 `src` 目录下创建一个 Python 文件，例如 `my_app.py`。
   - 使用 Atri 的 API 定义组件和状态：
     ```python
     from atri import Atri, event

     app = Atri()

     @app.page("首页")
     @app.state(var_names=["counter"])
     def index(ctrl):
         with ctr.Main:
             h1("Atri 应用")
             btn("点击", on_click=increment)
             p(f"计数: {ctrl.counter}")

     def increment(ctrl):
         ctrl.counter += 1
         ctrl.update()
     ```

3. **运行应用**：
   - 启动后端：`python main.py`（默认端口 8000）。
   - 启动前端：`npm start`（默认端口 3000）。
   - 在浏览器访问 `http://localhost:3000` 查看应用。

4. **构建和部署**：
   - 构建：`npm run build` 生成静态文件。
   - 部署：将 `build` 目录上传到托管平台，或使用 Docker 镜像部署。

更多细节请参考项目 README 和示例代码。该框架适合快速原型开发和交互式 Web 应用构建。