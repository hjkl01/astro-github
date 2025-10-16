
---
title: wsgidav
---

# WsgiDAV 项目概述

**项目地址：** [https://github.com/mar10/wsgidav](https://github.com/mar10/wsgidav)

## 主要特性
WsgiDAV 是一个基于 WebDAV 协议的 Python 库，主要特性包括：
- **轻量级实现**：纯 Python 实现，支持 WSGI 接口，易于集成到现有 Web 应用中。
- **协议兼容性**：完整支持 WebDAV/1 和部分 WebDAV/2 特性，包括锁定（Locks）、版本控制（Versioning）和属性管理（Properties）。
- **存储抽象**：提供灵活的存储后端抽象，支持文件系统、本地数据库或自定义存储（如虚拟文件系统），便于扩展。
- **安全性支持**：集成认证机制，如 Basic Auth、Digest Auth 和自定义认证后端，支持 HTTPS。
- **跨平台兼容**：适用于 Windows、Linux 和 macOS，支持 Python 2.7 及 Python 3.x 版本。
- **性能优化**：高效处理大文件传输和并发请求，适合作为文件共享服务器使用。

## 主要功能
WsgiDAV 的核心功能聚焦于 WebDAV 服务器的构建和托管：
- **文件管理**：允许远程客户端通过 HTTP/HTTPS 进行文件上传、下载、删除、复制和移动操作。
- **目录浏览**：支持 Web 界面或客户端（如 Windows Explorer、macOS Finder）浏览和导航目录结构。
- **属性与元数据**：管理文件/目录的自定义属性，支持 XML-based 属性存储和检索。
- **锁定机制**：防止并发修改，提供共享锁和独占锁以避免数据冲突。
- **扩展性**：内置钩子（hooks）和中间件系统，便于添加日志、缓存或自定义行为。
- **集成工具**：包含命令行工具，用于快速启动服务器或测试 WebDAV 功能。

## 用法指南
### 安装
使用 pip 安装：
```
pip install wsgidav
```

### 基本用法
1. **简单服务器启动**（命令行模式）：
   ```
   wsgidav --host=0.0.0.0 --port=80 --root=/path/to/your/files --auth=anonymous
   ```
   这将启动一个 WebDAV 服务器，根目录映射到指定路径，支持匿名访问。

2. **Python 代码集成**（作为 WSGI 应用）：
   ```python
   from wsgidav.wsgidav_app import WsgiDAVApp
   import os

   config = {
       "host": "0.0.0.0",
       "port": 80,
       "root": os.path.abspath("/path/to/files"),
       "user_mapping": {"user": "password"},  # 简单认证
   }

   app = WsgiDAVApp(config)
   # 在 WSGI 服务器（如 Gunicorn）中运行：gunicorn your_app:app
   ```

3. **自定义存储**：
   继承 `wsgidav.dav_provider.DAVProvider` 类实现自定义存储逻辑，例如：
   ```python
   from wsgidav.dav_provider import DAVProvider

   class MyProvider(DAVProvider):
       def get_directory_info(self, path, environ):
           # 自定义目录信息逻辑
           pass

   # 在 config 中指定 provider
   config["provider_mapping"] = {"/": MyProvider}
   ```

4. **客户端连接**：
   - Windows：将服务器地址映射为网络驱动器（`net use Z: http://server:port/`）。
   - macOS：使用 Finder 的“连接服务器”（`http://server:port`）。
   - 命令行工具：如 `cadaver` 或 `curl` 测试上传/下载。

更多高级用法详见项目文档和示例代码。建议在生产环境中结合认证和 HTTPS 使用，以确保安全。