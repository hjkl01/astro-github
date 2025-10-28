
---
title: automatic-api
---

# Automatic API 项目

## 项目地址
[GitHub 项目地址](https://github.com/dbohdan/automatic-api)

## 主要特性
- **自动化API生成**：基于Python脚本自动生成RESTful API，支持从简单函数快速构建API端点。
- **框架无关**：不依赖特定Web框架，可与Flask、FastAPI等集成，灵活性高。
- **简单配置**：通过装饰器或配置字典定义API路由、参数和响应，支持JSON数据处理。
- **内置测试支持**：提供示例和测试用例，便于验证API功能。
- **轻量级设计**：代码简洁，易于扩展和自定义，适合小型项目或原型开发。

## 主要功能
- **路由定义**：自动将Python函数映射为HTTP端点，支持GET、POST等方法。
- **参数处理**：自动解析查询参数、路径参数和请求体，支持类型验证。
- **响应格式化**：统一返回JSON格式，支持错误处理和自定义响应。
- **文档生成**：内置简单文档生成，帮助开发者快速了解API接口。
- **扩展性**：支持添加中间件、认证和缓存机制。

## 用法
1. **安装**：克隆仓库后，使用`pip install -r requirements.txt`安装依赖。
2. **基本使用**：
   - 导入模块：`from automatic_api import create_app`。
   - 定义函数：例如`def hello(name): return {'message': f'Hello, {name}!'}`
   - 创建应用：`app = create_app([hello])`。
   - 运行：使用Flask运行`app.run()`，访问`/hello?name=World`测试。
3. **高级配置**：通过`ApiConfig`类自定义路由前缀、默认响应等。
4. **示例**：仓库中提供`examples/`目录，运行`python example.py`查看演示。
5. **扩展**：修改源代码添加自定义功能，或集成到现有项目中。