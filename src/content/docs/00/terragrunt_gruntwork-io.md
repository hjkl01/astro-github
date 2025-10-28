
---
title: terragrunt
---


# Terragrunt（gruntwork-io/terragrunt）

> 项目地址: <https://github.com/gruntwork-io/terragrunt>

## 项目简介
Terragrunt 是一个为 Terraform 设计的“幽灵工具”，它通过在 Terraform 的基础上提供多层封装，帮助团队实现：

- **DRY（Don't Repeat Yourself）**：共享配置、模块依赖和命令。
- **可维护的状态管理**：统一远程状态、加锁、防止并发冲突。
- **多环境、层级化部署**：支持父子层级目录结构，逐级继承变量与模块。
- **更安全、更易审计**：集成 Terraform Enterprise、Atlantis 等工具。

## 主要特性
| 特性 | 说明 |
|------|------|
| **多层次配置继承** | 通过 `terragrunt.hcl` 文件，子模块可继承父模块的 `remote_state`、变量、依赖等。 |
| **自动化远程状态配置** | 自动配置 S3、Azure Storage、Google Cloud Storage 等后端，无需手动书写 Terraform backend。 |
| **Terraform 依赖管理** | `dependencies` 阶段可自动完成 `terraform init`、`plan`、`apply` 时的依赖模块同步。 |
| **锁定机制** | 集成 DynamoDB 等 backend，保证同一时间只有一个执行实例。 |
| **命令别名与批量执行** | 支持自定义别名、`terragrunt run-all` 等执行多模块命令。 |
| **敏感变量自动加密** | 支持 `sensitive` 变量，避免日志泄露。 |
| **模块多环境支持** | 通过子文件夹（dev、prod 等）统一管理不同环境配置，避免手工切换变量。 |

## 核心功能
1. **`terragrunt init`**  
   自动完成 Terraform 初始化，配置后端、拉取模块。

2. **`terragrunt plan`**  
   自动解析依赖图，按正确顺序执行 `plan`，支持增量计划。

3. **`terragrunt apply`**  
   同依赖管理，执行资源创建/更新。

4. **`terragrunt destroy`**  
   在已指定的目录层级安全销毁资源。

5. **`terragrunt run-all [cmd]`**  
   在当前目录及其子目录递归执行 `cmd`（如 `apply`、`plan`）。  

## 简易使用示例

```hcl
// root/terragrunt.hcl
locals {
  region = "us-east-1"
}

remote_state {
  backend = "s3"
  config = {
    bucket         = "my-terragrunt-state"
    key            = "${path_relative_to_include()}/terraform.tfstate"
    region         = local.region
    encrypt        = true
    dynamodb_table = "my-terragrunt-lock"
  }
}
```

```hcl
// dev/terragrunt.hcl
include {
  path = find_in_parent_folders()
}

terraform {
  source = "git::https://github.com/gruntwork-io/terragrunt-examples.git//modules/vpc"
}
```

```bash
# 初始化所有子模块
terragrunt run-all init

# 生成计划
terragrunt run-all plan

# 应用更改
terragrunt run-all apply
```

## 快速上手流程
1. **安装 Terragrunt**  
   ```bash
   brew install terragrunt  # macOS
   curl -L https://github.com/gruntwork-io/terragrunt/releases/download/vX.Y.Z/terragrunt_linux_amd64 -o /usr/local/bin/terragrunt
   chmod +x /usr/local/bin/terragrunt
   ```

2. **创建仓库结构**  
   ```
   ├── terragrunt.hcl              # 根配置
   ├── dev
   │   └── terragrunt.hcl          # 环境模块
   └── prod
       └── terragrunt.hcl
   ```

3. **添加模块依赖**  
   在子模块 `terragrunt.hcl` 里使用 `include {}` 引入父级配置，并通过 `terraform { source = ... }` 指定模块。

4. **执行**  
   ```bash
   terragrunt run-all apply
   ```

## 结语
Terragrunt 通过让 Terraform “按部就班”运行，显著提升团队协作效率、降低配置漂移和错误率。无论是单一项目还是多环境的长期运维，皆可获得标准化、可审计的基础设施即代码实践。
```
