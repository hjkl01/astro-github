
---
title: aws-devops-zero-to-hero
---

# AWS DevOps Zero to Hero by iam-veeramalla

> 项目地址：<https://github.com/iam-veeramalla/aws-devops-zero-to-hero>

本项目提供一套完整的 AWS DevOps 实示例，涵盖基础设施即代码（IaC）、持续集成与持续交付（CI/CD）以及运维最佳实践。目标读者是希望从零开始学习 AWS DevOps 的开发者或运维工程师。

## 主要特性

| 特性 | 说明 |
|------|------|
| **多层级 IaC** | 使用 Terraform + CloudFormation + CDK 统一管理资源。Terraform 负责网络与安全配置，CloudFormation 负责服务部署，CDK 用于构建复杂的应用。 |
| **多环境支持** | `dev`、`test` 与 `prod` 三个独立环境，通过 `terraform.tfvars` 与 CDK context 区分。 |
| **CI/CD 自动化** | 通过 GitHub Actions + AWS CodeBuild/CodePipeline 实现代码提交 → 自动部署。|
| **基础设施蓝图** | 预置 VPC、子网、NAT、Route53、S3 归档桶、RDS 与 ECS。|
| **安全 & 合规** | IAM 角色细粒度控制、KMS 加密、Security Groups 最小权限原则。|
| **成本监控** | 配置 Cost Explorer、Budgets 与 CloudWatch Logs 进行实时成本与性能监控。|

## 目录结构

```
└─ aws-devops-zero-to-hero
   ├─ infra/          # 纯 Terraform 资源
   ├─ cdk/            # CDK 应用与组件
   ├─ cicd/           # GitHub Actions 与 CodePipeline 定义
   ├─ scripts/        # 便捷脚本（初始化、销毁等）
   ├─ docs/           # 本文件
   └─ README.md
```

## 快速开始

### 先决条件

| 组件 | 说明 | 版本 |
|------|------|------|
| **AWS CLI** | 用于与 AWS 交互 | ≥ 2.0 |
| **Terraform** | IaC 脚本执行 | ≥ 0.15 |
| **Node.js & npm** | CDK 与脚本运行 | ≥ 16 |
| **GitHub 账户** | CI 工作流触发 | 任意 |

> 确保已配置 `AWS_PROFILE` 或通过环境变量 `AWS_ACCESS_KEY_ID/SECRET_ACCESS_KEY` 赋予 IAM 权限。

### 克隆仓库

```bash
git clone https://github.com/iam-veeramalla/aws-devops-zero-to-hero.git
cd aws-devops-zero-to-hero
```

### Terraform 部署

```bash
# 进入 Terraform 目录
cd infra

# 初始化
terraform init

# 预览计划
terraform plan -var-file=vars/dev.tfvars       # 选 dev / test / prod

# 应用
terraform apply -var-file=vars/dev.tfvars
```

> Terraform 会创建 VPC、子网、RDS、S3、IAM 角色等资源，完成后按提示确认。

### CDK 部署（可选）

```bash
# 进入 CDK 目录
cd ../cdk

# 安装依赖
npm install

# 在 config/ 目录设置环境参数（dev / prod）
cp config/dev.json config/current.json

# 预览
cdk diff

# 部署
cdk deploy
```

### CI/CD 启用

1. 将 `infra/` 与 `cdk/` 目录推送至 GitHub 主分支。
2. 在 GitHub Repo Settings → Actions → Frameworks，确保已启用 GitHub Actions。
3. 每次 `push` 或 `pull request`，GitHub Actions 将自动执行 `terraform apply` + `cdk deploy`。

> 若需自定义流水线，请参阅 `cicd/` 目录下的 `workflow.yml`。

### 验证

- 访问 CodeBuild 控制台检查构建日志。
- 进入 AWS Management Console 的服务列表，确认资源已按预期创建。
- 可通过 S3 `deployment-logs` 桶查看部署日志。

### 清理

```bash
# 先销毁 CDK
cd ../cdk
cdk destroy --force

# 再销毁 Terraform
cd ../infra
terraform destroy -var-file=vars/dev.tfvars
```

## 参与贡献

- Fork → Pull Request 的方式提交更改。
- 代码审查遵循 `PEP8`（Python）、`prettier`（TS/JS）以及 Terraform Lint。
- 任何 bug、功能建议或 doc 更新，欢迎 issue 提交。

> 详细贡献指南请参阅 `CONTRIBUTING.md`。

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| Terraform 失败，提示 “No matching IPAM pool” | 更新 `vars/dev.tfvars` 中的 CIDR 与 IPv4 分配池 |
| CDK 执行时报错 “Forbidden” | 检查 IAM 角色是否有 `cloudformation:CreateStack` 权限 |
| 部署后环境无法访问 | 确认安全组允许必要的入口端口（如 80, 443） |

--- 

> 如需进一步了解每个资源的细节，请查看各自目录下的 README 与 `schema` 文档。祝你玩得愉快 🚀

---