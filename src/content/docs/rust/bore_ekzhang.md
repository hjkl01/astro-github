---
title: bore
---

# bore

**项目地址**: https://github.com/ekzhang/bore

## 主要特性

- **简单 TCP 隧道**：现代、简单的 Rust TCP 隧道，将本地端口暴露到远程服务器，绕过标准 NAT 连接防火墙。
- **高效**：仅约 400 行安全异步 Rust 代码，易于安装和自托管，无额外功能。
- **跨平台**：支持多种安装方式，包括 Cargo、二进制、Docker 等。
- **无意见化**：专注于转发 TCP 流量，简单高效。

## 功能概览

- **本地转发**：使用 `bore local` 命令将本地端口转发到远程服务器。
- **自托管服务器**：运行 `bore server` 启动服务器，支持自定义端口范围和认证。
- **认证支持**：可选的秘密认证，防止未经授权使用。

## 用法

### 安装

- **Cargo**：`cargo install bore-cli`
- **Homebrew (macOS)**：`brew install bore-cli`
- **Arch Linux**：`yay -S bore`
- **二进制**：从 [Releases](https://github.com/ekzhang/bore/releases) 下载。
- **Docker**：`docker run -it --init --rm --network host ekzhang/bore <ARGS>`

### 本地转发

```shell
bore local 8000 --to bore.pub
```

这将本地 `localhost:8000` 暴露到公共互联网 `bore.pub:<PORT>`。

选项：

- `--port <PORT>`：指定远程端口。
- `--local-host <HOST>`：指定本地主机。
- `--secret <SECRET>`：认证秘密。

### 自托管服务器

```shell
bore server
```

选项：

- `--min-port <MIN>`：最小端口。
- `--max-port <MAX>`：最大端口。
- `--secret <SECRET>`：认证秘密。

## 示例

将本地 HTTP 服务器暴露：

```shell
bore local 3000 --to bore.pub
```

然后访问分配的 URL。
