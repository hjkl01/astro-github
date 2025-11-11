---
title: filebrowser
---

# filebrowser

## 功能

filebrowser 是一个简单、现代的Web文件管理器，允许用户通过浏览器界面浏览、上传、下载、删除和重命名文件。它支持多用户、权限管理、搜索功能，并提供RESTful API。

## 用法

### 安装

可以通过Docker、预编译二进制文件或从源码构建安装。

#### 使用Docker

```bash
docker run -v /path/to/files:/srv -p 80:80 filebrowser/filebrowser
```

#### 下载二进制文件

从GitHub releases页面下载适合你系统的二进制文件，然后运行：

```bash
./filebrowser
```

### 基本使用

1. 启动filebrowser后，访问浏览器中的地址（默认 http://localhost:8080）。
2. 使用默认凭据登录（用户名：admin，密码：admin）。
3. 浏览文件系统，上传文件，创建文件夹等。
4. 配置用户和权限以实现多用户支持。

更多详细信息请参考项目的GitHub页面。
