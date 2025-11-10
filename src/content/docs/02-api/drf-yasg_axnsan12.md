---
title: drf-yasg
---

# drf-yasg 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/axnsan12/drf-yasg)

## 主要特性
drf-yasg（Django REST Framework Yet Another Swagger Generator）是一个用于 Django REST Framework (DRF) 的 Swagger/OpenAPI 文档生成器。它基于 Python 的 PyYAML 和 uritemplate 库，提供了以下核心特性：
- **自动生成 Swagger/OpenAPI 文档**：支持 OpenAPI 2.0（Swagger）和 OpenAPI 3.0 规范，自动从 DRF 视图和序列化器中提取 API 信息。
- **ReDoc 支持**：除了 Swagger UI，还支持 ReDoc 作为文档渲染选项，提供更现代化的 API 文档界面。
- **高度可定制**：允许通过装饰器、设置和自定义 schema 类来调整生成的文档，包括添加描述、示例、认证信息等。
- **认证集成**：无缝支持 DRF 的认证后端，如 Token、JWT 等，并在 Swagger UI 中提供认证测试功能。
- **分页和过滤支持**：自动处理 DRF 的分页器和过滤器，并在文档中正确显示参数。
- **静态文件生成**：可以生成静态的 Swagger JSON/YAML 文件，便于部署和离线使用。
- **兼容性强**：与 Django 2.x+ 和 DRF 3.x+ 兼容，支持 Python 3.6+。

## 主要功能
- **Swagger UI 集成**：通过 Django URL 配置，提供交互式的 API 文档界面，用户可以直接在浏览器中测试 API 端点。
- **Schema 生成**：使用 `get_schema_view` 函数动态生成 OpenAPI schema，支持多种格式（JSON、YAML）。
- **自定义组件**：允许扩展 schema 类来添加自定义操作、参数、安全定义等。
- **文档增强**：支持 Markdown 格式的描述、示例代码片段，以及多语言支持。
- **错误处理**：在文档中正确表示 DRF 的错误响应和状态码。

## 用法
### 安装
使用 pip 安装：
```
pip install drf-yasg
```

### 配置
1. **添加应用**：在 `settings.py` 中添加 `'drf_yasg'` 到 `INSTALLED_APPS`：
   ```python
   INSTALLED_APPS = [
       ...
       'drf_yasg',
       ...
   ]
   ```

2. **URL 配置**：在 `urls.py` 中添加 schema 和 UI 路由：
   ```python
   from rest_framework import permissions
   from drf_yasg.views import get_schema_view
   from drf_yasg import openapi

   schema_view = get_schema_view(
       openapi.Info(
           title="Your API",
           default_version='v1',
           description="API 描述",
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

   urlpatterns = [
       ...
       url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]
   ```

3. **在视图中使用**：使用 `@swagger_auto_schema` 装饰器自定义文档：
   ```python
   from drf_yasg.utils import swagger_auto_schema
   from drf_yasg import openapi

   class MyView(APIView):
       @swagger_auto_schema(
           operation_summary="API 摘要",
           operation_description="详细描述",
           responses={200: openapi.Response('成功响应', MySerializer)},
           manual_parameters=[openapi.Parameter('param', openapi.IN_QUERY, description='参数描述', type=openapi.TYPE_STRING)]
       )
       def get(self, request):
           # 视图逻辑
           pass
   ```

4. **运行和访问**：启动 Django 服务器后，访问 `/swagger/` 或 `/redoc/` 查看生成的文档。可以通过自定义设置调整文档行为，如在 `settings.py` 中配置 `SWAGGER_SETTINGS`。