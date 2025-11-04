
---
title: atlantis
---


# Atlantis（runatlantis/atlantis）

**项目地址**  
[https://github.com/runatlantis/atlantis](https://github.com/runatlantis/atlantis)

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **GitHub PR 驱动的 Terraform 流程** | 在 Pull Request 触发时自动执行 `terraform plan`，并在 PR 评论中展示结果。 |
| **多仓库 & 多环境支持** | 通过 `atlantis.yaml` 配置文件可为不同仓库、分支或目录设置独立的 Terraform 环境。 |
| **安全的 Terraform `apply`** | 需要手动批准后才执行 `terraform apply`，可防止未经授权的变更。 |
| **与 CI/CD 集成** | 与 GitHub Actions、GitLab、Bitbucket 等无缝集成，支持自定义工作流。 |
| **Slack / Teams 通知** | 在指定渠道推送 `plan` 与 `apply` 结果，提升团队协作效率。 |
| **自托管与云托管** | 可自行部署在 Kubernetes、Docker 或云服务器，也可以使用官方托管服务。 |
| **权限细粒度** | 支持基于 GitHub 组织/团队、用户或 IP 白名单的访问控制。 |
| **插件化架构** | 可以通过编写自定义插件扩展功能，例如支持 Terraform Cloud、Terragrunt 等。 |

---

## 核心功能

1. **自动化 Terraform 计划**  
   - 在 PR 创建或更新时自动运行 `terraform init` + `terraform plan`。  
   - 结果以评论形式返回，包含执行摘要与差异对比。

2. **安全的 Terraform 应用**  
   - 需要在 PR 里添加 `atlantis apply` 评论才能触发 `terraform apply`。  
   - 通过 `atlantis.yaml` 指定哪些用户可以执行 apply。

3. **多环境 & 多仓库管理**  
   - `atlantis.yaml` 里可定义 `project`，每个项目映射到特定目录、工作空间与 Terraform 版本。  
   - 支持 `allow_apply = true/false`，`apply_requirements` 等细粒度配置。

4. **集成与通知**  
   - 支持 Slack/Teams 机器人，自动推送计划与应用结果。  
   - 与 GitHub Actions、GitLab CI 等兼容，可做进一步的工作流自定义。

5. **安全与权限**  
   - 基于 OAuth、IP 白名单或自定义 webhook 验证请求身份。  
   - 对 `apply` 操作可设置只允许特定团队或用户执行。

---

## 快速上手

### 1. 安装

```bash
# Docker 方式
docker run -d \
  -p 4141:4141 \
  -v /path/to/atlantis:/etc/atlantis \
  -v /path/to/terraform-state:/var/atlantis/state \
  runatlantis/atlantis
```

> **Tip**：在本地开发时可使用 `docker-compose.yml` 进行快速部署。

### 2. 配置

在项目根目录放置 `atlantis.yaml`（示例）：

```yaml
version: 3
projects:
  - dir: ./infra
    workspace: default
    terraform_version: 1.8
    autoplan:
      when_modified: ["*.tf", "*.tfvars"]
      enabled: true
    apply_requirements: [approved, mergeable]
```

> - `dir`：Terraform 代码所在目录。  
> - `workspace`：Terraform 工作空间。  
> - `autoplan.when_modified`：触发自动计划的文件模式。  
> - `apply_requirements`：apply 前必须满足的条件。

### 3. GitHub 集成

1. **创建 GitHub App**  
   - 进入 Settings → Developer settings → GitHub Apps → New GitHub App。  
   - 选中 **Repository permissions** → **Pull requests** → `Read & Write`。  
   - 生成私钥并记录 `App ID` 与 `Private Key`。

2. **在 Atlantis 服务器中配置**  
   ```bash
   atlantis server --app-id=YOUR_APP_ID --private-key=/path/to/key.pem \
     --github-token=/path/to/token | atlantis server
   ```

3. **安装 App 至仓库**  
   - 访问 `https://github.com/settings/apps/YOUR_APP_NAME/installations/new`。  
   - 选中需要的仓库。

### 4. 使用流程

1. **提交 PR**  
   - 在 PR 中修改 Terraform 代码，提交 PR。  
   - Atlantis 自动执行 `plan`，并在 PR 评论中显示结果。

2. **批准 & Apply**  
   - 需要 `apply_requirements` 中指定的条件满足。  
   - 在 PR 评论中添加 `atlantis apply`，Atlantis 触发 `apply` 并更新状态。

3. **监控 & 通知**  
   - 配置 Slack Webhook，Atlantis 会将计划和应用结果推送至指定频道。

---

## 参考文档

- 官方文档：<https://www.runatlantis.io/docs/>
- 配置示例：<https://github.com/runatlantis/atlantis/tree/main/examples>
- 常见问题：<https://github.com/runatlantis/atlantis/issues>
- 社区讨论：<https://github.com/runatlantis/atlantis/discussions>

---

> **注**：上述示例仅为快速入门，实际部署请根据团队安全策略、网络环境与 Terraform 版本进行细化调整。

```

*此文件可直接保存为 `src/content/docs/00/atlantis_runatlantis.md`。*