
---
title: djangorestframework-simplejwt
---

# djangorestframework-simplejwt 项目

## 项目地址
https://github.com/jazzband/djangorestframework-simplejwt

## 主要特性
djangorestframework-simplejwt 是一个用于 Django REST Framework 的 JSON Web Token (JWT) 认证库。它基于 PyJWT 实现，提供简单、高效的 token-based 认证机制。主要特性包括：
- **无状态认证**：使用 JWT 进行认证，无需服务器端会话存储，支持分布式系统。
- **可配置的 token 类型**：支持 Access Token（短期访问）和 Refresh Token（长期刷新），默认 Access Token 有效期 5 分钟，Refresh Token 有效期 1 天。
- **自定义签名算法**：支持 HS256、RS256 等多种算法，默认使用 HMAC-SHA256。
- **黑名单支持**：可将已失效的 token 添加到黑名单中，防止重用。
- **易于扩展**：提供自定义 token 声明、过期时间和验证逻辑的钩子。
- **与 DRF 集成**：无缝集成 Django REST Framework 的认证和权限系统。

## 主要功能
- **Token 生成**：用户登录后生成 Access 和 Refresh Token，支持自定义 payload（如用户 ID、权限等）。
- **Token 验证**：在 API 视图中验证 token 的有效性、签名和过期时间。
- **Token 刷新**：使用 Refresh Token 获取新的 Access Token，而无需重新登录。
- **Token 撤销**：支持将 token 加入黑名单，实现注销功能。
- **多用户支持**：适用于用户认证、API 授权等场景，兼容 Django 的用户模型。

## 用法
### 安装
```bash
pip install djangorestframework-simplejwt
```

### 配置
在 `settings.py` 中添加：
```python
INSTALLED_APPS = [
    # ...
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# 可选：自定义 token 设置
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,  # 刷新时生成新 Refresh Token
    'BLACKLIST_AFTER_ROTATION': True,  # 旧 Refresh Token 加入黑名单
}
```

### URL 配置
在 `urls.py` 中包含默认视图：
```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 使用示例
- **获取 Token**：POST 到 `/api/token/`，body 为 `{"username": "user", "password": "pass"}`，响应包含 `access` 和 `refresh` token。
- **验证 Token**：在视图中使用 `@permission_classes([IsAuthenticated])` 或在 headers 中添加 `Authorization: Bearer <access_token>`。
- **刷新 Token**：POST 到 `/api/token/refresh/`，body 为 `{"refresh": "<refresh_token>"}`。
- **自定义视图**：继承 `TokenObtainPairView` 来添加额外逻辑，如自定义 serializer。

更多细节请参考项目文档。