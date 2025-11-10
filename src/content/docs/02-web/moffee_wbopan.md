---
title: moffee
---

# Moffee 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/wbopan/moffee)

## 主要特性
Moffee 是一个基于 Python 的简单 Web 框架，专注于轻量级开发和快速原型构建。其核心特性包括：
- **简洁的路由系统**：支持 RESTful 路由定义，易于映射 URL 到处理函数。
- **内置模板引擎**：集成 Jinja2，支持动态 HTML 生成和变量渲染。
- **轻量级依赖**：最小化外部库依赖，便于部署和维护。
- **异步支持**：可选集成 asyncio，实现高并发处理。
- **内置调试工具**：提供开发模式下的错误追踪和日志记录。

## 主要功能
- **Web 服务器启动**：快速创建 HTTP 服务器，支持 GET、POST 等方法。
- **请求处理**：处理查询参数、表单数据和 JSON 输入。
- **静态文件服务**：自动托管 CSS、JS 和图像文件。
- **中间件支持**：允许自定义中间件处理认证、日志等。
- **API 开发**：简化 JSON API 的构建，适合微服务应用。

## 用法
1. **安装**：
   ```
   pip install moffee
   ```

2. **基本示例**：
   创建 `app.py` 文件：
   ```python
   from moffee import App

   app = App()

   @app.route('/')
   def home():
       return 'Hello, Moffee!'

   if __name__ == '__main__':
       app.run(port=8000)
   ```

3. **运行**：
   ```
   python app.py
   ```
   访问 `http://localhost:8000` 查看输出。

4. **高级用法**：
   - 添加路由：使用 `@app.route('/path', methods=['POST'])`。
   - 模板渲染：`return app.render('template.html', data={'key': 'value'})`。
   - 更多细节请参考项目 README 和示例代码。