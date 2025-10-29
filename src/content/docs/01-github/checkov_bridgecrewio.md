
---
title: checkov
---

# Checkov (BridgeCrew)

**项目地址**: https://github.com/bridgecrewio/checkov

## 项目概述
Checkov 是一款开源的 IaC (基础设施即代码) 安全扫描与合规检查工具。它通过基于策略的规范，对 Terraform、CloudFormation、Kubernetes、Dockerfile 等多种 IaC 配置文件进行静态分析，帮助团队及时识别安全与合规风险。

## 主要特性

| # | 特性 | 说明 |
|---|------|------|
| 1 | **支持多种 IaC 语言** | Terraform、CloudFormation、Kubernetes (YAML/Helm)、Dockerfile、Serverless Framework、OpenAPI、ARM Templates 等 |
| 2 | **策略即代码 (Policy-as-Code)** | 1000+ 内置安全检查，支持自定义策略（Python/JSON/YAML） |
| 3 | **完整的命令行界面** | `checkov -d .`、`checkov -d ./terraform -o json` 等命令 |
| 4 | **CI/CD 集成** | GitHub Actions、GitLab CI、Azure DevOps、Bitbucket Pipelines、Jenkins、GitHub App 等官方集成 |
| 5 | **GitHub Action** | `actions/checkout` + `bridgecrewio/checkov-action`，按 PR 或 Commit 触发扫描 |
| 6 | **结果导出** | 支持Unit、JSON、SARIF、HTML、PNG 视图 |
| 7 | **忽略规则** | 通过 `# checkov:skip=CKV_AWS_123` 注解，或者 `.checkovignore`、`config.json` 配置 |
| 8 | **命名空间与组织管理** | 可在 GitHub Organization/仓库层级配置自定义检查参数 |

## 基本用法

```bash
# 安装
pip install checkov

# 在当前目录扫描所有 IaC 目录
checkov -d .

# 只扫描 Terraform 目录并输出 JSON
checkov -d ./terraform -o json
```

### GitHub Actions 示例

```yaml
name: IaC Security Scan

on:
  pull_request:
    branches: [main]

jobs:
  checkov:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Checkov
        run: pip install checkov
      - name: Run Checkov
        run: checkov -d .
```

### 配置自定义检查

```yaml
# .checkov.yaml
line_length: 100
skip_checks:
  - CKV_AWS_200
  - CKV_K8S_1
```

### 忽略单个资源

```hcl
resource "aws_security_group" "sg" {
  name = "sg"

  # checkov:skip=CKV_AWS_64
  tags = { Team = "infra" }
}
```

## 高级特性

| # | 功能 | 说明 |
|---|------|------|
| 1 | **SARIF 输出** | 与 GitHub Security tab 对接 |
| 2 | **可视化结果** | 生成 PNG 或 HTML 报告，支持嵌入 CI 管道 |
| 3 | **分支级安全策略** | 结合 GitHub Policy Sets 自动审核 |
| 4 | **多语言支持** | 保持 API 一致，可在 Python/Go 场景中嵌入 |
| 5 | **插件架构** | 通过 `checkov --plugin install <URL>` 引入新的检测插件 |

## 进一步资源

- 官方文档: https://www.checkov.io/
- 代码示例与社区插件: https://github.com/bridgecrewio/checkov/tree/master/ci
- GitHub Actions 集成: https://github.com/bridgecrewio/checkov-action

> **Tip:** 在 CI 之前先在本地 `checkov -d .` 运行，确保无警告后再提交代码。