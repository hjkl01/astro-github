---
title: ygege
---

# ygege

ygege 是一个用 Rust 编写的 YGG Torrent 高性能索引器。

## 功能特性

- 自动解析当前 YGG Torrent 域名
- 自动绕过 Cloudflare（无需手动解决挑战）
- 近乎瞬时的搜索
- 无缝重新连接到过期会话
- 会话缓存
- 绕过虚假 DNS
- 低内存使用（Linux 发布模式下 14.7MB）
- 模块化种子搜索（按名称、种子数、下载数、评论、发布日期等）
- 详细种子元数据检索（描述、大小、种子数、下载数等）
- 零外部依赖
- 无需浏览器驱动

## 用法

### 安装

#### Docker

提供现成的 Docker 镜像。有关 Docker 部署和配置，请参阅 [Docker 指南](https://github.com/UwUDev/ygege/blob/master/docs/docker-guide.md)。

要创建自定义 Docker 镜像，请参阅 [Docker 构建指南](https://github.com/UwUDev/ygege/blob/master/docs/docker-dev.md)。

#### 手动安装

从源码编译应用程序，请遵循 [手动安装指南](https://github.com/UwUDev/ygege/blob/master/docs/source-guide.md)。

### Prowlarr 集成

ygege 可以作为 Prowlarr 的自定义索引器使用。要设置它，找到您的 AppData 目录（位于 Prowlarr 的 `/system/status` 页面），并将仓库中的 `ygege.yml` 文件复制到 `{your prowlarr appdata path}/Definitions/Custom` 文件夹，您可能需要创建 `Custom` 文件夹。

完成后，重启 Prowlarr 并转到索引器设置，您应该在可用索引器列表中看到 ygege。

注意：Prowlarr 不允许自定义“Base URL”。默认 URL 为 `http://localhost:8715/`。对于 Docker Compose 设置，使用 `http://ygege:8715/`。或者，使用 ygege-dns-redirect.local 与自定义 DNS 或 hosts 文件重定向。

### Cloudflare 绕过

ygege 无需浏览器或第三方服务即可绕过 Cloudflare 挑战。

### API 文档

API 文档可在 [此处](https://github.com/UwUDev/ygege/blob/master/docs/api-documentation.md) 获取。

## 编译要求

- Rust 1.85.0+
- OpenSSL 3+
- 构建 [wreq](https://crates.io/crates/wreq) 所需的所有依赖
