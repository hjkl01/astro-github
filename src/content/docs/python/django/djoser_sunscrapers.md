---
title: djoser
---

# Djoser 项目

## 项目地址
[https://github.com/sunscrapers/djoser](https://github.com/sunscrapers/djoser)

## 主要特性
Djoser 是一个 Django REST Framework (DRF) 的用户认证库，旨在简化 Django 项目的用户注册、登录和认证流程。它基于 JWT（JSON Web Token）或其他认证后端，提供 RESTful API 接口，支持用户管理功能。核心特性包括：
- **用户注册与激活**：支持邮箱验证和账户激活。
- **登录与注销**：提供 token-based 认证，支持 JWT 或会话认证。
- **密码管理**：包括密码重置、更改和验证功能。
- **用户资料管理**：允许用户查看、更新个人信息。
- **社交登录集成**：可扩展支持 OAuth 等第三方登录。
- **自定义性强**：高度可配置，支持自定义视图、序列化器和模板。
- **安全性**：集成 Django 的内置安全机制，如密码哈希和 CSRF 保护。

## 主要功能
- **认证端点**：提供 `/auth/users/` 等 API，用于用户创建、登录、token 获取。
- **用户操作**：支持密码重置流程（通过邮箱发送链接）、用户详情获取和更新。
- **视图集集成**：无缝集成 DRF 的 ViewSet 和 Serializer，便于扩展。
- **多语言支持**：内置 i18n 支持，可翻译错误消息和界面。
- **测试友好**：包含测试客户端和示例，便于单元测试。

## 用法
1. **安装**：
   ```
   pip install djoser
   ```

2. **Django 配置**：
   在 `settings.py` 中添加：
   ```python
   INSTALLED_APPS = [
       # ...
       'rest_framework',
       'rest_framework_simplejwt',  # 或其他认证后端
       'djoser',
   ]

   DJOSER = {
       'SERIALIZERS': {
           'user_create': 'djoser.serializers.UserCreateSerializer',
           'user': 'djoser.serializers.UserSerializer',
           'current_user': 'djoser.serializers.UserSerializer',
       },
       'PERMISSIONS': {
           'user_create': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],
       },
   }

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ],
   }
   ```

3. **URL 配置**：
   在 `urls.py` 中包含：
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('auth/', include('djoser.urls')),
       path('auth/', include('djoser.urls.authtoken')),  # 如果使用 token 认证
   ]
   ```

4. **自定义用户模型**（可选）：
   如果使用自定义 User 模型，确保在 `settings.py` 中设置 `AUTH_USER_MODEL`，并相应调整序列化器。

5. **运行与测试**：
   - 迁移数据库：`python manage.py migrate`。
   - 创建超级用户：`python manage.py createsuperuser`。
   - 访问 API，例如 POST `/auth/users/` 创建用户，GET `/auth/users/me/` 获取当前用户。

详细文档参考 GitHub 仓库的 README 和官方文档。