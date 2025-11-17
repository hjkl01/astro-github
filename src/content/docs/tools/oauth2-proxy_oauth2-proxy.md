---
title: oauth2-proxy
---

## 功能介绍

OAuth2-Proxy 是一个灵活的开源工具，可以作为独立的反向代理或中间件组件集成到现有的反向代理或负载均衡器中。它提供了一种简单且安全的方式，使用 OAuth2 / OIDC 认证来保护您的 Web 应用程序。作为反向代理，它会拦截对应用程序的请求，并将用户重定向到 OAuth2 提供者进行认证。作为中间件，它可以无缝集成到现有基础设施中，为多个应用程序处理认证。

OAuth2-Proxy 支持许多 OAuth2 和 OIDC 提供者，包括 Google、Microsoft Entra ID、GitHub、login.gov 等。通过专门的提供者实现，OAuth2-Proxy 可以提取更多关于用户的详细信息，如首选用户名和组。这些详细信息可以作为 HTTP 头转发到上游应用程序。

## 用法

### 安装

OAuth2-Proxy 的[安装文档](https://oauth2-proxy.github.io/oauth2-proxy/installation) 涵盖了如何安装和配置您的设置。此外，您可以查看[示例设置文件](https://github.com/oauth2-proxy/oauth2-proxy/tree/master/contrib/local-environment)。

### 发布版本

#### 二进制文件

我们为所有主要架构以及更特殊的架构如 `ppc64le` 和 `s390x` 发布编译好的二进制文件。

查看[最新发布](https://github.com/oauth2-proxy/oauth2-proxy/releases/latest)。

#### 镜像

从 `v7.6.0` 开始，基础镜像已从 Alpine 更改为 [GoogleContainerTools/distroless](https://github.com/GoogleContainerTools/distroless)。此镜像安装的依赖更少，因此应提高安全性。镜像也因此略小。对于调试目的（以及那些真正需要它的人，例如 `armv6`），我们仍提供基于 Alpine 的镜像。这些镜像的标签以 `-alpine` 结尾。

自 2023-11-18 起，我们直接从 `master` 分支构建夜间镜像，并提供在 `quay.io/oauth2-proxy/oauth2-proxy-nightly`。这些镜像被视为不稳定，因此**不应**用于生产目的，除非您知道自己在做什么。

### 参与贡献

加入 #oauth2-proxy [Slack 频道](https://gophers.slack.com/archives/CM2RSS25N) 与其他用户聊天，或直接联系维护者。使用[公共邀请链接](https://invite.slack.golangbridge.org/) 获取 Gopher Slack 空间的邀请。

OAuth2-Proxy 是一个社区驱动的项目。我们依赖用户的贡献来不断改进它。虽然审查时间可能有所不同，但我们感谢您的耐心和理解。作为一个志愿者驱动的项目，我们努力保持这个项目的稳定性，可能需要更长时间来合并更改。

如果您想为项目贡献，请查看我们的[贡献指南](https://oauth2-proxy.github.io/oauth2-proxy/community/contribution)。

谁在使用 OAuth2-Proxy？请查看我们的新[采用者](/oauth2-proxy/oauth2-proxy/blob/master/ADOPTERS.md)文件，并随时打开 PR 添加您的组织。
