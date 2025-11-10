---
title: localstack
---

# LocalStack

## 功能

LocalStack 是一个云软件开发框架，用于在本地开发和测试您的 AWS 应用程序。它是一个云服务仿真器，在单个容器中运行在您的笔记本电脑或 CI 环境中。使用 LocalStack，您可以在本地机器上完全运行 AWS 应用程序或 Lambdas，而无需连接到远程云提供商！

LocalStack 支持越来越多的 AWS 服务，包括：

- AWS Lambda
- S3
- DynamoDB
- Kinesis
- SQS
- SNS
- 以及更多！

无论是测试复杂的 CDK 应用程序或 Terraform 配置，还是刚刚开始学习 AWS 服务，LocalStack 都能帮助加速和简化您的测试和开发工作流程。

LocalStack 还提供额外功能，使云开发者的生活更轻松！查看 LocalStack 的用户指南以获取更多信息。

## 用法

### 安装

最快的方式是通过 LocalStack CLI 开始。它使您能够通过命令行直接启动和管理 LocalStack Docker 容器。在继续之前，请确保您的机器安装了功能正常的 Docker 环境。

#### Brew (macOS 或带有 Homebrew 的 Linux)

通过我们的官方 LocalStack Brew Tap 安装 LocalStack CLI：

```
brew install localstack/tap/localstack-cli
```

#### 二进制下载 (macOS, Linux, Windows)

如果您的机器上未安装 Brew，您可以直接下载预构建的 LocalStack CLI 二进制文件：

- 访问 [localstack/localstack-cli](https://github.com/localstack/localstack-cli/releases/latest) 并下载适用于您的平台的最新版本。
- 将下载的存档提取到 PATH 变量中包含的目录：
  - 对于 macOS/Linux，使用命令：`sudo tar xvzf ~/Downloads/localstack-cli-*-darwin-*-onefile.tar.gz -C /usr/local/bin`

#### PyPI (macOS, Linux, Windows)

LocalStack 使用 Python 开发。要使用 pip 安装 LocalStack CLI，请运行以下命令：

```
python3 -m pip install localstack
```

`localstack-cli` 安装使您能够运行包含 LocalStack 运行时的 Docker 镜像。要与本地 AWS 服务交互，您需要单独安装 `awslocal` CLI。有关安装指南，请参考 [`awslocal` 文档](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal)。

> **重要**：不要使用 `sudo` 或以 `root` 用户运行。LocalStack 必须完全在本地非 root 用户下安装和启动。如果您在 macOS High Sierra 上遇到权限问题，请使用 `pip install --user localstack` 安装。

### 快速开始

在 Docker 容器中启动 LocalStack，运行：

```
localstack start -d
```

您可以通过运行以下命令查询 LocalStack 上相应服务的状态：

```
localstack status services
```

要在 LocalStack 上使用 SQS（完全托管的分布式消息队列服务），运行：

```
awslocal sqs create-queue --queue-name sample-queue
```

了解更多关于 [LocalStack AWS 服务](https://docs.localstack.cloud/references/coverage/) 以及如何使用 LocalStack 的 `awslocal` CLI。

### 运行

您可以通过以下选项运行 LocalStack：

- [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)
- [Docker](https://docs.localstack.cloud/getting-started/installation/#docker)
- [Docker Compose](https://docs.localstack.cloud/getting-started/installation/#docker-compose)
- [Helm](https://docs.localstack.cloud/getting-started/installation/#helm)

### 配置和使用

要开始使用 LocalStack，请查看我们的 [文档](https://docs.localstack.cloud)。

- [LocalStack 配置](https://docs.localstack.cloud/references/configuration/)
- [LocalStack 在 CI 中](https://docs.localstack.cloud/user-guide/ci/)
- [LocalStack 集成](https://docs.localstack.cloud/user-guide/integrations/)
- [LocalStack 工具](https://docs.localstack.cloud/user-guide/tools/)
- [理解 LocalStack](https://docs.localstack.cloud/references/)
- [常见问题](https://docs.localstack.cloud/getting-started/faq/)

要使用图形用户界面与 LocalStack 交互，您可以使用以下 UI 客户端：

- [LocalStack Web 应用程序](https://app.localstack.cloud)
- [LocalStack Desktop](https://docs.localstack.cloud/user-guide/tools/localstack-desktop/)
- [LocalStack Docker Extension](https://docs.localstack.cloud/user-guide/tools/localstack-docker-extension/)

### 版本

请参考 [GitHub 版本](https://github.com/localstack/localstack/releases) 查看每个版本的完整更改列表。有关扩展版本说明，请参考 [变更日志](https://docs.localstack.cloud/references/changelog/)。

### 贡献

如果您有兴趣为 LocalStack 贡献：

- 从阅读我们的 [贡献指南](/localstack/localstack/blob/main/docs/CONTRIBUTING.md) 开始。
- 查看我们的 [开发环境设置指南](/localstack/localstack/blob/main/docs/development-environment-setup/README.md)。
- 浏览我们的代码库并 [打开问题](https://github.com/localstack/localstack/issues)。

我们感谢所有贡献和反馈。

### 联系我们

与 LocalStack 团队联系，报告 🐞 [问题](https://github.com/localstack/localstack/issues/new/choose)，为 👍 [功能请求](https://github.com/localstack/localstack/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+) 投票，🙋🏽 询问 [支持问题](https://docs.localstack.cloud/getting-started/help-and-support/)，或 🗣️ 讨论本地云开发：

- [LocalStack Slack 社区](https://localstack.cloud/slack/)
- [LocalStack GitHub 问题跟踪器](https://github.com/localstack/localstack/issues)
