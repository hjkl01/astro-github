---
title: openvas-scanner
---

# OpenVAS Scanner

OpenVAS Scanner 是 Greenbone Community Edition 的扫描器组件。它是一个功能完整的漏洞扫描引擎，用于执行持续更新和扩展的漏洞测试（VTs）馈送。

## 功能

- **漏洞检测**：扫描网络、主机和应用程序中的安全漏洞。
- **持续更新**：使用最新的漏洞测试馈送，确保检测最新的威胁。
- **多语言实现**：包含 C 语言和 Rust 语言的实现版本。
- **集成支持**：与 Greenbone Vulnerability Management (GVM) 系统集成。
- **Docker 支持**：提供 Docker 镜像，便于容器化部署。

## 用法

### 安装

从源代码安装：

```bash
cmake .
make install
```

详细的安装要求和说明请参考 [INSTALL.md](https://github.com/greenbone/openvas-scanner/blob/main/INSTALL.md) 文件。该文件还包含设置 `openvas` 和使扫描器可用于其他 GVM 模块的说明。

### Docker 使用

拉取官方镜像：

```bash
docker pull greenbone/openvas-scanner:stable
```

或本地构建：

```bash
docker build -t <image-name> -f .docker/prod.Dockerfile .
```

更多关于 Greenbone Community Containers 的信息，请参考 [官方文档](https://greenbone.github.io/docs/latest/22.4/container/)。

### Rust 实现

该仓库还包含一个 Rust 项目，旨在替换当前的扫描器堆栈（openvas-scanner, ospd-openvas, notus-scanner）。它简化了扫描器的使用，并集中了扫描所需的一切。目前它使用 openvas-scanner 作为扫描引擎。

更多信息请参考 [rust/README.md](https://github.com/greenbone/openvas-scanner/blob/main/rust/README.md)。

## 支持

如果您对 `openvas` 的使用有任何问题，请使用 [Greenbone Community Portal](https://community.greenbone.net/)。如果您发现软件问题，请在 GitHub 上 [创建问题](https://github.com/greenbone/openvas-scanner/issues)。

## 许可证

该模块（除 rust/ 目录下的 Rust 实现外）根据 GNU General Public License v2.0 仅授权。单个文件可能根据 GNU General Public License v2.0 仅或 GNU General Public License v2.0 或更高版本授权，请查看 [license-details.md](https://github.com/greenbone/openvas-scanner/blob/main/license-details.md) 文件以获取详细信息。

rust/ 目录下的 Rust 实现根据 GNU General Public License v2.0 或更高版本与 OpenSSL 异常授权。单个文件还根据 MIT 授权。
