
---
title: drf-spectacular
---

# drf-spectacular 项目

## 项目地址
[GitHub 项目地址](https://github.com/tfranzel/drf-spectacular)

## 主要特性
drf-spectacular 是一个用于 Django REST Framework (DRF) 的 OpenAPI 3 规范生成器。它提供自动化的 API 文档生成，支持 OpenAPI 3 和 Swagger UI 的集成。主要特性包括：
- **自动 schema 生成**：基于 DRF 的视图、序列化器和路由自动生成 OpenAPI 3 规范，无需手动编写 YAML 或 JSON。
- **类型注解支持**：充分利用 Python 类型提示（typing）和 DRF 的序列化器来推断 API 结构，提高文档准确性。
- **扩展性强**：支持自定义 schema 生成器、组件和操作扩展，便于处理复杂 API 场景。
- **集成 Swagger UI 和 ReDoc**：内置浏览器端文档渲染，支持交互式 API 测试。
- **兼容性好**：与 DRF 的核心功能无缝集成，支持分页、认证、过滤等高级特性。
- **性能优化**：生成 schema 的过程高效，适合大型项目。

## 主要功能
- **OpenAPI Schema 生成**：从 DRF 代码中提取路径、方法、参数、请求/响应模型等信息，形成完整的 API 规范。
- **组件管理**：自动处理 schemas、parameters、responses 等 OpenAPI 组件，支持复用和继承。
- **认证与安全**：集成 DRF 的认证机制，如 Token、JWT 等，并在 schema 中正确表示。
- **错误处理**：支持自定义错误响应 schema，提高 API 文档的完整性。
- **版本控制**：通过命名空间或路径前缀支持 API 版本化。
- **插件系统**：提供扩展点，如支持第三方包（drf-yasg 的替代）或自定义渲染。

## 用法
### 安装
使用 pip 安装：
```
pip install drf-spectacular
```

### 配置
在 Django 的 `settings.py` 中添加：
```python
INSTALLED_APPS = [
    # ...
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your API Title',
    'DESCRIPTION': 'Your API Description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # 如果需要动态生成
}
```

在 `urls.py` 中添加 schema 视图：
```python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

### 基本用法
1. **在视图中使用**：DRF 视图无需额外修改，schema 会自动从序列化器和视图方法推断。
   示例序列化器：
   ```python
   from rest_framework import serializers

   class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model = User
           fields = ['id', 'name', 'email']
   ```

2. **自定义 schema**：使用 `@extend_schema` 装饰器细化文档：
   ```python
   from drf_spectacular.utils import extend_schema, OpenApiExample

   @extend_schema(
       description='Create a new user',
       examples=[
           OpenApiExample('Example 1', value={'name': 'John', 'email': 'john@example.com'})
       ]
   )
   def create(self, request):
       # view logic
   ```

3. **访问文档**：运行 Django 服务器后，访问 `/api/docs/` 查看 Swagger UI，或 `/api/redoc/` 查看 ReDoc。

### 高级用法
- **组件扩展**：通过 `SPECTACULAR_SETTINGS` 配置全局组件，或使用 `extend_schema_component` 添加自定义 schemas。
- **侧边栏生成**：启用 `SERVE_PERMISSIONS` 来控制 schema 访问权限。
- **导出 schema**：通过 `/api/schema/` 端点获取 JSON/YAML 格式的 OpenAPI 文件，用于外部工具集成。

更多细节请参考项目文档。