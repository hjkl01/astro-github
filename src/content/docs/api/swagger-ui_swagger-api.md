---
title: swagger-ui
---


# Swagger UI（swagger-api/swagger-ui）

> GitHub 项目地址: <https://github.com/swagger-api/swagger-ui>

## 项目概览
Swagger UI 是一套基于浏览器的前端工具，能够根据 OpenAPI（Swagger）规范生成交互式 API 文档。开发者可以通过它快速查看 API 接口、发送请求、查看响应结果，极大地提升文档可读性与测试效率。

## 主要特性
- **自动化渲染**：直接读取 `swagger.json` / `swagger.yaml`，无需手动编写文档页面。
- **交互式 API 调用**：内置请求发送器（XHR/Fetch），可实时测试接口。
- **丰富 UI**：支持主题切换、响应预览、参数验证、请求头/查询参数/路径参数/请求体可视化。
- **可嵌入**：可通过 CDN、NPM 或直接下载源码嵌入任意 Web 项目。
- **多语言支持**：默认支持多种语言，易于国际化。
- **自定义扩展**：通过配置 `swagger-ui` 提供的插件机制，可扩展功能（如 OAuth2、Auth0 等身份验证）。

## 功能与使用方式

### 1. 安装方式
```bash
# 通过 npm
npm install swagger-ui-dist

# 通过 CDN
<link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css">
<script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
<script src="https://unpkg.com/swagger-ui-dist/swagger-ui-standalone-preset.js"></script>
```

### 2. 基础配置示例
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>API 文档</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css">
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
  <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-standalone-preset.js"></script>
  <script>
    window.onload = () => {
      const ui = SwaggerUIBundle({
        url: 'https://petstore.swagger.io/v2/swagger.json', // 你的 OpenAPI 文档地址
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout"
      });
      window.ui = ui;
    };
  </script>
</body>
</html>
```

### 3. 开发环境集成
- **Vue / React / Angular**：使用官方提供的组件包 `swagger-ui-express` 与 `swagger-ui-react` 等进行集成。
- **后端框架**：在 Node.js Express 中可以使用 `swagger-ui-express`，在 Spring Boot 中可使用 `springdoc-openapi-ui`。

### 4. 常见配置
- `docExpansion`（`none` | `list` | `full`）：控制 API 列表展开状态。
- `defaultModelsExpandDepth`：模型展开深度。
- `supportedSubmitMethods`：支持的请求方法。
- `requestInterceptor` / `responseInterceptor`：请求/响应拦截器，用于身份验证、日志等。

## 如何贡献
- Fork 本仓库 → 新建分支 → 提交代码 → Pull Request。
- 查看 `CONTRIBUTING.md`，遵循编码规范与测试要求。

---
> 本文档旨在快速了解 Swagger UI 的核心特性与基本使用方法，详情请参阅官方文档及源代码。