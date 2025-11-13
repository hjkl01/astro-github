---
title: InvenTree
---

# InvenTree

## 项目简介

InvenTree 是一个开源的库存管理系统，提供强大的低级库存控制和零件跟踪功能。系统的核心是基于 Python/Django 的数据库后端，提供 Web 界面和 REST API，支持与外部接口和应用程序的交互。强大的插件系统允许自定义应用程序和扩展。

## 主要功能

- **库存管理**：低级库存控制和零件跟踪
- **Web 界面**：基于 Django 的管理界面
- **REST API**：支持外部集成
- **插件系统**：可扩展的插件接口，支持自定义功能
- **多语言支持**：通过 Crowdin 社区贡献翻译
- **移动应用**：配套的移动 App，支持 Android 和 iOS
- **集成选项**：
  - InvenTree API
  - Python 模块
  - 插件接口
  - 第三方工具集成

## 技术栈

### 后端

- Python
- Django
- Django REST Framework (DRF)
- Django Q
- Django-Allauth

### 数据库

- PostgreSQL
- MySQL
- SQLite
- Redis

### 前端

- React
- Lingui
- React Router
- TanStack Query
- Zustand
- Mantine
- Mantine Data Table
- CodeMirror

### DevOps

- Docker
- Crowdin
- Codecov
- SonarCloud
- Packager.io

## 部署和使用

### 部署选项

1. **Docker 部署**：

   ```bash
   # 使用 Docker 快速启动
   docker run -p 8000:8000 inventree/inventree
   ```

2. **单行安装脚本**（适用于支持的发行版）：

   ```bash
   wget -qO install.sh https://get.inventree.org && bash install.sh
   ```

3. **裸机安装**：参考[安装指南](https://docs.inventree.org/en/latest/start/install/)

### 快速开始

1. 访问 [Demo 站点](https://demo.inventree.org/) 体验功能
2. 阅读完整[文档](https://docs.inventree.org/en/latest/)
3. 选择合适的部署方式安装

### 移动应用

- [Android Play Store](https://play.google.com/store/apps/details?id=inventree.inventree_app)
- [Apple App Store](https://apps.apple.com/au/app/inventree/id1581731101)

## 社区和贡献

- **报告问题**：[GitHub Issues](https://github.com/inventree/InvenTree/issues)
- **功能请求**：[GitHub Issues](https://github.com/inventree/InvenTree/issues/new?template=feature_request.md)
- **贡献代码**：参考[贡献指南](https://docs.inventree.org/en/latest/develop/contributing/)
- **翻译**：通过 [Crowdin](https://crowdin.com/project/inventree) 贡献本地化

## 许可证

MIT License

## 相关链接

- [官方网站](https://inventree.org)
- [文档](https://docs.inventree.org)
- [Demo](https://demo.inventree.org)
- [GitHub 仓库](https://github.com/inventree/InvenTree)
