
---
title: glance
---


# glanceapp/glance

**项目地址**: https://github.com/glanceapp/glance

## 项目概述
glance 是一款基于 Docker 的开源仪表盘，旨在为开发团队提供实时、可视化的 GitHub 仓库状态监控。通过调用 GitHub API 与 Webhook，glance 自动收集代码提交、Issue、Pull Request、CI/CD 状态、代码覆盖率等指标，并以简洁的图表和表格呈现。

## 主要特性
- **实时数据刷新**：支持 GitHub Webhook，数据可在几秒内同步更新。
- **多维度指标展示**：提交量、作者贡献、PR 成功率、分支合并速率、CI 构建成功率等。
- **自定义仪表盘**：用户可根据需要添加、删除或重新排列组件。
- **多仓库管理**：一次部署可监控多仓库，支持团队级别的视图聚合。
- **权限细粒度**：通过 GitHub OAuth 认证，权限控制细致到用户/团队层级。
- **轻量级部署**：单个 Docker Compose 文件即可快速启动，零 CDN/代理需求。

## 功能一览
| 功能 | 说明 |
|------|------|
| **Dashboard** | 传统的柱状、折线图显示 Commit/PR/Issue 趋势。 |
| **Repo Overview** | 单仓库实时概览，包括最新提交、PR、Issue、Star 数量。 |
| **CI/CD Status** | 显示最近 30 条构建结果，支持多种 CI 提供商（GitHub Actions, Travis, Jenkins 等）。 |
| **Code Coverage** | 可与覆盖率服务（Codecov, Coveralls 等）集成，展示覆盖率变化。 |
| **Auth & Permission** | 基于 OAuth 授权，限制只能查看自己访问权限范围内的仓库。 |
| **Webhook Agent** | 自动注册 GitHub Webhook，在事件发生时立刻抓取最新信息。 |

## 使用方法

### 1. 获取项目

```bash
git clone https://github.com/glanceapp/glance.git
cd glance
```

### 2. 配置环境变量  
在 `docker-compose.yml` 或 `.env` 内配置：

```dotenv
# OAuth Application
GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret

# Repository to monitor (comma separated if multiple)
GITHUB_REPOSITORIES=org1/repo1,org2/repo2

# Optional: CI provider configuration
CI_PROVIDER=github_actions
```

> **Tip**：在 GitHub 上注册 OAuth App，授权回调地址为 `https://<YOUR_HOST>/oauth/callback`。

### 3. 启动服务

```bash
docker-compose up -d
```

### 4. 访问仪表盘  
打开浏览器访问：

```
https://<YOUR_HOST>/dashboard
```

首次访问会跳转到 GitHub 登录，完成授权后即可查看各仓库的实时指标。

### 5. 高级配置（可选）

- **自定义组件**：修改 `templates/` 内的 Vue/Jade 文件，重新部署。
- **邮件/Slack 通知**：在 `config/email.yml`、`config/slack.yml` 中填写接收者信息。
- **多语言**：编辑 `locales/zh_CN.yml` 等文件。

### 6. 生产部署

```bash
# 生产环境
docker-compose -f docker-compose.prod.yml up -d
```

> 使用 `docker-compose.prod.yml` 预设了更高的并发、日志滚动与 HTTPS。

---

> 以上即为 glanceapp/glance 的主要特性、功能及使用流程。祝使用愉快！   
