---
title: nexus-cli
---

# Nexus CLI 项目

## 项目地址

[https://github.com/nexus-xyz/nexus-cli](https://github.com/nexus-xyz/nexus-cli)

## 主要特性

Nexus CLI 是一个高性能命令行界面，用于向 Nexus 网络贡献证明。Nexus 网络是一个全球分布式证明网络，旨在实现可验证计算，推动"可验证互联网"的发展。

## 主要功能

- **自适应任务难度系统**：根据节点性能自动调整任务难度，从小难度开始，根据完成时间自动提升。
- **多种安装方式**：支持预编译二进制（推荐）、非交互式安装和 Docker 容器化部署。
- **用户和节点注册**：支持注册钱包地址和节点 ID，保存凭据到配置文件。
- **证明贡献**：运行证明任务，支持无头模式和自定义难度覆盖。
- **许可证**：采用 Apache-2.0 和 MIT 双许可证。

## 用法

1. **安装**：
   - 推荐方式：`curl https://cli.nexus.xyz/ | sh`（下载最新二进制并启动交互模式）。
   - 非交互式：`curl -sSf https://cli.nexus.xyz/ -o install.sh && chmod +x install.sh && NONINTERACTIVE=1 ./install.sh`。

2. **注册**：
   - 注册用户：`nexus-cli register-user --wallet-address <钱包地址>`。
   - 注册节点：`nexus-cli register-node --node-id <节点ID>`。

3. **启动证明**：
   - 基本启动：`nexus-cli start`（使用现有节点 ID）。
   - 指定节点 ID：`nexus-cli start --node-id <节点ID>`。
   - 无头模式：`nexus-cli start --headless`。
   - 自定义难度：`nexus-cli start --max-difficulty <难度>`（如 small、medium、large 等）。

4. **其他命令**：
   - 注销：`nexus-cli logout`（清除凭据）。
   - 帮助：`nexus-cli --help`。

5. **Docker 部署**：
   - 更新 `docker-compose.yaml` 中的节点 ID。
   - 构建和运行：`docker compose build --no-cache && docker compose up -d`。
   - 查看日志：`docker compose logs`。
   - 停止：`docker compose down`。

使用前需接受[使用条款](https://nexus.xyz/terms-of-use)。更多详情请参考[官方文档](https://docs.nexus.xyz)
