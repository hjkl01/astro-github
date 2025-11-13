---
title: skopeo
---

# skopeo

## 项目简介

`skopeo` 是一个命令行工具，用于对容器镜像和镜像仓库执行各种操作。它不需要用户以root身份运行，也不需要守护进程即可执行操作。`skopeo` 支持OCI镜像以及原始的Docker v2镜像。

## 主要功能

Work with remote images registries - retrieving information, images, signing content

`skopeo` 可以与以下类型的镜像和仓库一起工作：

- `containers-storage:docker-reference`：位于本地containers/storage镜像存储中的镜像。
- `dir:path`：现有本地目录路径，以单独文件形式存储清单、层tarball和签名。
- `docker://docker-reference`：实现"Docker Registry HTTP API V2"的注册表中的镜像。
- `docker-archive:path[:docker-reference]`：存储在`docker save`格式文件中的镜像。
- `docker-daemon:docker-reference`：存储在docker守护进程内部存储中的镜像。
- `oci:path:tag`：符合"Open Container Image Layout Specification"的目录中的镜像标签。

## 安装

请参考项目文档获取详细用法。
