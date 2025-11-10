---
title: docker-slim
---

# docker-slim 项目概述

**项目地址：** [https://github.com/docker-slim/docker-slim](https://github.com/docker-slim/docker-slim)

## 主要特性
docker-slim 是一个开源工具，用于优化 Docker 镜像的大小和安全性。它通过分析容器运行时行为，自动移除不必要的文件、依赖和层，从而生成更小的镜像。主要特性包括：
- **镜像最小化**：自动检测并移除镜像中的未使用组件，显著减少镜像体积（通常可达 30%-90% 的压缩率）。
- **安全性增强**：生成最小化镜像，减少攻击面；支持漏洞扫描和安全最佳实践。
- **无损优化**：确保优化后的镜像功能与原镜像一致，不影响应用程序运行。
- **多平台支持**：兼容 x86_64 和 ARM 架构，支持多种容器化环境。
- **自动化流程**：集成 CI/CD，支持 Docker Compose 和 Kubernetes。

## 主要功能
- **最小化镜像**：使用 `docker-slim min` 命令分析并构建优化后的镜像。
- **容器探针**：运行容器时动态监控文件系统和进程，识别必需组件。
- **多阶段构建**：支持从 Dockerfile 生成的镜像进行优化。
- **报告生成**：输出优化报告，包括移除的文件列表和大小变化。
- **自定义配置**：允许用户指定 HTTP 端点或命令来模拟真实运行场景。

## 用法
1. **安装**：
   - 通过 Homebrew：`brew install dslim/tap/docker-slim`
   - 或下载二进制文件并添加到 PATH。

2. **基本优化**：
   ```
   docker-slim min --target <原镜像名称> [选项]
   ```
   示例：`docker-slim min --target nginx:latest --http-probe --exec "nginx -g 'daemon off;'"`
   - `--target`：指定要优化的镜像。
   - `--http-probe`：启用 HTTP 探针以验证服务。
   - 输出：生成新镜像标签，如 `nginx:latest-slim`。

3. **高级用法**：
   - 构建 Dockerfile：`docker-slim build --target Dockerfile .`
   - X-Ray 模式：`docker-slim xray --target <镜像> --exec <命令>` 用于静态分析。
   - 配置选项：使用 `--continue-after` 或 `--dry-run` 自定义行为。

更多详情请参考项目文档。