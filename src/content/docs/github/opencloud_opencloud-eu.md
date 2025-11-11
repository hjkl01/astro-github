---
title: opencloud
---

# OpenCloud

OpenCloud 是一个开源的云存储服务器项目，由 OpenCloud GmbH 开发。该项目的主要仓库包含了后端服务的 Go 语言代码库，用于提供文件存储、共享和协作功能。

## 功能

- **文件存储和共享**：提供安全的文件存储和共享服务，支持用户和团队协作。
- **身份验证**：使用 OpenID Connect 进行用户认证，支持外部 IdP（如 Keycloak）或嵌入式 LibreGraph Connect 身份提供者。
- **无数据库设计**：所有数据存储在文件系统中，默认根目录为 `$HOME/.opencloud/`。
- **模块化架构**：包含多个服务，如用户管理、文件处理等。
- **开源许可证**：采用 Apache 2.0 许可证。

## 用法

### 构建 OpenCloud

1. 生成必要的资产（如 Web UI 和内置 IdP）：

   ```
   make generate
   ```

2. 编译 `opencloud` 二进制文件：

   ```
   make -C opencloud build
   ```

   这将生成 `opencloud/bin/opencloud` 二进制文件。

### 运行服务器

1. 初始化服务器配置（默认配置存储在 `$HOME/.opencloud`）：

   ```
   opencloud/bin/opencloud init
   ```

2. 启动服务器：
   ```
   opencloud/bin/opencloud server
   ```

### 更多设置选项

有关详细的设置和安装选项，请参考 [OpenCloud 开发文档](https://docs.opencloud.eu/)。

## 贡献

OpenCloud 欢迎各种形式的贡献，包括报告问题、请求功能、编写文档、代码贡献和审查。更多信息请参见 [贡献指南](https://github.com/opencloud-eu/opencloud/blob/main/CONTRIBUTING.md)。

## 安全

如果发现安全相关问题，请立即联系 [security@opencloud.eu](mailto:security@opencloud.eu)。
