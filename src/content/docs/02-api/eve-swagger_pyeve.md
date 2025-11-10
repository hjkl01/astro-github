---
title: eve-swagger
---

# EVE Swagger 项目

## 项目地址
[https://github.com/pyeve/eve-swagger](https://github.com/pyeve/eve-swagger)

## 主要特性
EVE Swagger 是一个基于 Python 的工具包，专为 EVE（Eve 框架）设计，用于生成和集成 Swagger（OpenAPI）规范文档。它支持自动生成 API 文档、验证和可视化接口，帮助开发者快速构建 RESTful API 的文档化系统。主要特性包括：
- **自动文档生成**：基于 Eve 框架的资源和端点，自动生成 Swagger JSON/YAML 规范。
- **集成 Swagger UI**：提供内置的 Swagger UI 接口，便于浏览器中查看和测试 API。
- **自定义扩展**：支持自定义 Swagger 配置，如添加认证、标签和描述。
- **兼容性强**：适用于 Python 3.x 环境，与 Eve 框架无缝集成。
- **轻量级**：无外部依赖过多，易于安装和部署。

## 主要功能
- **API 规范生成**：从 Eve 的域（domain）配置中提取端点、参数和响应，输出标准 Swagger 2.0 或 OpenAPI 3.0 格式。
- **文档可视化**：通过 Flask 或其他 Web 服务器托管 Swagger UI，实现交互式 API 探索。
- **验证与测试**：集成 Swagger 编辑器，支持 API 路径测试和 schema 验证。
- **认证支持**：内置 OAuth、API Key 等认证机制的 Swagger 配置。
- **扩展钩子**：允许开发者通过钩子函数自定义 Swagger 输出，如添加额外元数据。

## 用法
### 安装
```bash
pip install eve-swagger
```

### 基本配置
在 Eve 应用中初始化 Swagger：
```python
from eve import Eve
from eve_swagger import get_swagger_blueprint

app = Eve()

# 配置 Swagger
swagger_template = {
    'schemes': ['http', 'https'],
    'swagger': '2.0',
    'info': {
        'title': 'My API',
        'version': '1.0'
    }
}
swagger_url = '/swagger'  # Swagger JSON 端点
swaggerui_blueprint = get_swagger_blueprint(
    swagger_template,
    '/swagger.json',
    '/swagger/'
)

app.register_blueprint(swaggerui_blueprint)
```

### 运行示例
1. 定义 Eve 域（domain），如资源配置。
2. 启动应用：`python app.py`。
3. 访问 `http://localhost:5000/swagger/` 查看 Swagger UI。
4. 通过 UI 测试 API 端点。

更多细节请参考项目 README。