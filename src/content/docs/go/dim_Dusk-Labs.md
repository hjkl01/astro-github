---
title: dim
---

# Dim

**GitHub 项目地址:** [https://github.com/Dusk-Labs/dim](https://github.com/Dusk-Labs/dim)

## 项目简介

Dim 是一个自托管的媒体管理器。只需最少的设置，Dim 就能组织和美化您的媒体收藏，让您随时随地访问和播放它们。

## 运行方式

### 从二进制文件运行

#### 依赖项

- libva2
- libva-drm2
- libharfbuzz
- libfontconfig
- libfribidi
- libtheora
- libvorbis
- libvorbisenc
- libtheora0

然后从 GitHub release 标签下载二进制文件：

1. 解压 `unzip ./release-linux.zip && tar -xvzf ./release.tar.gz`
2. 运行 `cd release && ./dim`
3. 然后可以通过浏览器访问 Dim Web UI `http://0.0.0.0:8000`（假设本地运行。）

### 使用 Docker 运行

以下命令在端口 8000 上运行 dim，将配置存储在 `$HOME/.config/dim` 中。您可以更改该路径以将配置存储在其他位置。您可以挂载任意数量的包含媒体的目录，重复 `-v HOST_PATH:CONTAINER_PATH` 选项。在此示例中，主机上的 `/media` 路径在 Docker 容器中以相同路径提供。这个名称 "media" 是任意的，您可以选择任何名称。

```
docker run -d -p 8000:8000/tcp -v $HOME/.config/dim:/opt/dim/config -v /media:/media:ro ghcr.io/dusk-labs/dim:dev
```

多架构镜像位于 `ghcr.io/dusk-labs/dim:master`

要使用硬件加速，挂载相关设备：

```
docker run -d -p 8000:8000/tcp -v $HOME/.config/dim:/opt/dim/config -v /media:/media:ro --device=/dev/dri/renderD128 ghcr.io/dusk-labs/dim:dev
```

请参阅 [docker-compose-template.yaml](https://github.com/Dusk-Labs/dim/blob/master/docker-compose-template.yml) 以使用 Docker Compose 运行 dim。

### 从源码运行

#### 依赖项

要从源码运行，您需要先在系统上安装以下依赖项：

- sqlite
- cargo
- rustc (nightly)
- yarn, npm
- libssl-dev
- libva2 (仅 Linux)
- libva-dev (仅 Linux)
- libva-drm2 (仅 Linux)
- ffmpeg

安装依赖项后，克隆仓库并构建项目：

```
git clone https://github.com/Dusk-Labs/dim
yarn --cwd ui/ && yarn --cwd ui/ build
mkdir utils && ln -nfs $(which ffmpeg) utils/ffmpeg && ln -nfs $(which ffprobe) utils/ffprobe
```

如果您在 Linux 上运行，使用：

```
cargo run --features vaapi --release
```

在其他不支持 libva 的平台上，使用：

```
cargo run --release
```

## 许可证

Dim 根据 AGPLv3 许可证获得许可（请参阅 [LICENSE.md](/Dusk-Labs/dim/blob/master/LICENSE.md) 或 [https://opensource.org/licenses/AGPL-3.0](https://opensource.org/licenses/AGPL-3.0)）
