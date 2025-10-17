
---
title: flasgger
---

# Flasgger 项目概述

## 项目地址
[https://github.com/flasgger/flasgger](https://github.com/flasgger/flasgger)

## 主要特性
Flasgger 是一个基于 Flask 的 API 文档生成工具，它利用 Swagger UI 和 YAML/OpenAPI 规范来自动生成交互式 API 文档。主要特性包括：
- **Swagger 集成**：无缝集成 Swagger UI，支持实时浏览和测试 API 接口。
- **YAML/OpenAPI 支持**：使用 YAML 文件定义 API 规范，支持 OpenAPI 2.0 和 3.0 版本。
- **Flask 扩展**：作为 Flask 的轻量级扩展，便于在现有 Flask 项目中集成。
- **交互式文档**：提供可视化界面，用户可以直接在浏览器中测试 API 调用。
- **自动生成**：从代码注解或 YAML 文件自动生成文档，减少手动维护工作。
- **自定义主题**：支持自定义 Swagger UI 的外观和行为。

## 主要功能
- **API 文档生成**：通过装饰器（如 `@swag_from`）或 YAML 文件为 Flask 路由生成 Swagger 文档。
- **参数和响应定义**：支持定义查询参数、路径参数、请求体和响应模型，包括数据验证。
- **安全性支持**：集成 API 密钥、OAuth 等认证机制。
- **多端点管理**：处理多个 API 端点，支持分组和标签组织文档。
- **导出功能**：可导出 YAML 或 JSON 格式的 API 规范，便于与其他工具集成。

## 用法
### 安装
使用 pip 安装：
```
pip install flasgger
```

### 基本用法
1. **初始化**：
   在 Flask 应用中导入并初始化：
   ```python
   from flask import Flask
   from flasgger import Swagger

   app = Flask(__name__)
   swagger = Swagger(app)
   ```

2. **定义 API 端点**：
   使用装饰器添加 Swagger 注解：
   ```python
   from flasgger import swag_from

   @app.route('/hello')
   @swag_from('hello.yml')  # 引用 YAML 文件
   def hello():
       return "Hello, World!"
   ```

3. **YAML 文件示例**（hello.yml）：
   ```yaml
   ---
   definition:
     path: /hello
     method: get
     summary: Hello World 示例
     responses:
       200:
         description: 成功响应
   ```

4. **启动应用**：
   运行 Flask 应用后，访问 `/apidocs/` 路径即可查看 Swagger UI 文档。

### 高级用法
- **内联注解**：直接在 Python 代码中使用字典定义 Swagger 规范，而非外部 YAML 文件。
- **模板自定义**：通过 `template` 参数自定义 Swagger 配置。
- **Bower 支持**：可选使用 Bower 管理 Swagger UI 资源。

更多细节请参考项目文档。