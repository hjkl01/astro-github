---
title: nixopus
---

# nixopus

**项目作者**: raghavyuva  
**项目链接**: [https://github.com/raghavyuva/nixopus](https://github.com/raghavyuva/nixopus)  
**网站**: [https://nixopus.com](https://nixopus.com)  
**文档**: [https://docs.nixopus.com](https://docs.nixopus.com)

## 项目简介

Nixopus 是一个开源的部署平台，是 Vercel、Heroku 和 Netlify 的替代品。它提供了简化的工作流程，支持一键部署应用、自托管和终端集成。项目目前处于 alpha/pre-release 阶段，不建议用于生产环境。

## 主要功能

- **一键部署应用**：无需配置文件或 SSH 命令，直接部署应用。
- **浏览器文件管理**：在浏览器中拖拽、编辑文件，就像文件管理器一样。
- **内置终端**：无需离开页面即可访问服务器终端。
- **实时监控**：实时查看 CPU、RAM 和磁盘使用情况。
- **自动 SSL 证书**：域名自动获取 HTTPS 证书。
- **GitHub 集成**：推送代码后自动部署。
- **代理管理**：使用 Caddy 反向代理路由流量。
- **智能警报**：通过 Slack、Discord 或邮件通知异常情况。

## 安装和快速开始

### 安装 Nixopus

#### 基本安装（无域名，通过 IP:端口部署）

```bash
curl -sSL https://install.nixopus.com | bash
```

#### 自定义 IP 设置

```bash
curl -sSL https://install.nixopus.com | bash -s -- --host-ip 10.0.0.154
```

#### 仅安装 CLI 工具（不运行 `nixopus install`）

```bash
curl -sSL https://install.nixopus.com | bash -s -- --skip-nixopus-install
```

### 可选参数

- `--api-domain` 或 `-ad`：指定 Nixopus API 可访问的域名（例如：`nixopusapi.example.tld`）
- `--view-domain` 或 `-vd`：指定 Nixopus 应用可访问的域名（例如：`nixopus.example.tld`）
- `--host-ip` 或 `-ip`：指定服务器 IP 地址（例如：`10.0.0.154` 或 `192.168.1.100`）。如果不提供，将自动检测公网 IP。
- `--verbose` 或 `-v`：安装时显示更多详细信息
- `--timeout` 或 `-t`：设置每个步骤的超时时间（默认：300 秒）
- `--force` 或 `-f`：如果文件已存在则替换
- `--dry-run` 或 `-d`：查看会发生什么而不进行更改
- `--config-file` 或 `-c`：自定义配置文件路径（默认为内置的 `config.prod.yaml`）

#### 示例：使用可选参数安装

```bash
nixopus install \
  --api-domain nixopusapi.example.tld \
  --view-domain nixopus.example.tld \
  --verbose \
  --timeout 600
```

#### 示例：自定义 IP 设置

```bash
nixopus install \
  --host-ip 10.0.0.154 \
  --verbose
```

更多安装选项请参考[安装文档](https://docs.nixopus.com/install/#installation-options)。

## 注意事项

⚠️ **重要提示**：Nixopus 目前处于 alpha/pre-release 阶段，还未准备好用于生产环境。虽然欢迎试用，但建议等到 beta 或稳定版本发布后再用于生产环境。该平台仍在测试和开发中。

## 贡献者

项目由多个贡献者维护，包括主要开发者 raghavyuva 等。

## 许可证

查看[许可证](https://github.com/raghavyuva/nixopus/blob/master/LICENSE.md)了解更多信息。
