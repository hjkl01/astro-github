---
title: skopeo
---

# skopeo

## 项目简介

`skopeo` 是一个命令行工具，用于对容器镜像和镜像仓库执行各种操作。它不需要用户以root身份运行，也不需要守护进程即可执行操作。`skopeo` 支持OCI镜像以及原始的Docker v2镜像。

## 主要功能

- **复制镜像**：在各种存储机制之间复制容器镜像，包括容器注册表、容器存储后端、本地目录和本地OCI布局目录。
- **检查镜像**：检查远程镜像的属性，包括其层，而无需将镜像拉取到主机。
- **删除镜像**：从镜像仓库中删除镜像。
- **同步注册表**：将外部镜像仓库同步到内部注册表，用于离线部署。
- **认证**：支持向注册表传递适当的凭据和证书进行认证。

`skopeo` 可以与以下类型的镜像和仓库一起工作：

- `containers-storage:docker-reference`：位于本地containers/storage镜像存储中的镜像。
- `dir:path`：现有本地目录路径，以单独文件形式存储清单、层tarball和签名。
- `docker://docker-reference`：实现"Docker Registry HTTP API V2"的注册表中的镜像。
- `docker-archive:path[:docker-reference]`：存储在`docker save`格式文件中的镜像。
- `docker-daemon:docker-reference`：存储在docker守护进程内部存储中的镜像。
- `oci:path:tag`：符合"Open Container Image Layout Specification"的目录中的镜像标签。

## 安装

有关详细的安装或构建说明，请参见[install.md](https://github.com/containers/skopeo/blob/main/install.md)。

`skopeo` 也可以作为容器镜像在[quay.io](https://quay.io/skopeo/stable)上获得。更多信息，请参见[Skopeo Image](https://github.com/containers/image_build/blob/main/skopeo/README.md)页面。

## 常用用法

### 检查仓库

`skopeo inspect` 命令可以检查注册表上的仓库，并获取镜像层。`inspect` 命令获取仓库的清单，并能够显示类似`docker inspect`的JSON输出，关于整个仓库或标签的信息。这有助于在拉取镜像（占用磁盘空间）之前收集有关仓库或标签的有用信息。

#### 示例：显示fedora:latest的属性

```bash
skopeo inspect docker://registry.fedoraproject.org/fedora:latest
```

输出示例：

```json
{
    "Name": "registry.fedoraproject.org/fedora",
    "Digest": "sha256:0f65bee641e821f8118acafb44c2f8fe30c2fc6b9a2b3729c0660376391aa117",
    "RepoTags": [
        "34-aarch64",
        "34",
        "latest",
        ...
    ],
    "Created": "2022-11-24T13:54:18Z",
    "DockerVersion": "1.10.1",
    "Labels": {
        "license": "MIT",
        "name": "fedora",
        "vendor": "Fedora Project",
        "version": "37"
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Layers": [
        "sha256:2a0fc6bf62e155737f0ace6142ee686f3c471c1aab4241dc3128904db46288f0"
    ],
    ...
}
```

#### 显示容器配置

```bash
skopeo inspect --config docker://registry.fedoraproject.org/fedora:latest | jq
```

### 复制镜像

`skopeo copy` 可以复制容器镜像，包括清单、文件系统层和签名。

#### 示例：从一个注册表复制到另一个

```bash
skopeo copy docker://quay.io/buildah/stable docker://registry.internal.company.com/buildah
```

#### 示例：复制到本地目录

```bash
skopeo copy oci:busybox_ocilayout:latest dir:existingemptydirectory
```

### 删除镜像

```bash
skopeo delete docker://localhost:5000/imagename:latest
```

### 同步注册表

```bash
skopeo sync --src docker --dest dir registry.example.com/busybox /media/usb
```

### 认证到注册表

`skopeo` 使用`--creds`（用于`inspect`或`delete`）或`--src-creds`/`--dest-creds`（用于`copy`）标志的凭据；否则，它使用由`skopeo login`、`podman login`、`buildah login`或`docker login`设置的配置。

#### 示例：登录

```bash
skopeo login --username USER myregistrydomain.com:5000
```

#### 示例：使用--creds直接认证

```bash
skopeo inspect --creds=testuser:testpassword docker://myregistrydomain.com:5000/busybox
```

```bash
skopeo copy --src-creds=testuser:testpassword docker://myregistrydomain.com:5000/private oci:local_oci_image
```

## 许可证

`skopeo` 根据Apache License, Version 2.0许可。有关完整许可证文本，请参见[LICENSE](https://github.com/containers/skopeo/blob/main/LICENSE)。
