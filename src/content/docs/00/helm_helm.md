
---
title: helm
---


# Helm

- **项目地址**: [https://github.com/helm/helm](https://github.com/helm/helm)

## 项目简介
Helm 是 Kubernetes 的软件包管理器，类似于 Linux 的 `apt` 或 `yum`。它通过 **Charts**（Chart 是预先打包好的 Kubernetes 资源模板集）来简化应用的安装、升级、版本回滚、依赖管理和环境隔离等工作。

## 主要特性

| # | 特性 | 说明 |
|---|------|------|
| 1 | **Chart 结构** | 统一的包结构，包含 `templates/`、`values.yaml`、`charts/` 等目录。 |
| 2 | **模板化** | 使用 Go 模板（`{{ }}`）实现参数化部署，支持条件、循环、函数等。 |
| 3 | **值文件** | 默认 `values.yaml` 可覆盖，支持多层 `.yaml` 文件。 |
| 4 | **依赖管理** | `Chart.yaml` 的 `dependencies` 字段可声明子 chart，`helm dependency update` 自动下载。 |
| 5 | **Release 版本化** | 通过 `helm install` 创建 Release，`helm upgrade` & `helm rollback` 管理历史版本。 |
| 6 | **钩子（Hooks）** | 在安装、升级、卸载流程中插入自定义预/post 步骤，如数据库迁移。 |
| 7 | **Chart 仓库** | 支持本地/远程镜像仓库，`helm repo add/delete` 配置；`helm search repo` 查询。 |
| 8 | **Lint & Test** | `helm lint` 检查 chart 合规性，`helm test` 运行测试用例。 |
| 9 | **升级与回滚** | `helm upgrade` 采用零停机升级，`helm rollback` 快速恢复。 |
| 10 | **版本兼容** | Helm 3 采用 client‑side 模式，无 Tiller，使用 Kubernetes API 直接操作。 |

## 基本使用流程

```bash
# 1. 安装 Helm（根据平台官方文档）
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 2. 添加官方仓库
helm repo add stable https://charts.helm.sh/stable
helm repo update

# 3. 搜索 Chart
helm search repo nginx

# 4. 安装 Chart
helm install my-nginx stable/nginx-ingress     # default values
helm install my-nginx stable/nginx-ingress -f custom-values.yaml

# 5. 查看 Release
helm list -n <namespace>

# 6. 升级 Chart
helm upgrade my-nginx stable/nginx-ingress -f upgrade-values.yaml

# 7. 回滚 Release
helm rollback my-nginx <revision-number>

# 8. 卸载 Release
helm uninstall my-nginx

# 9. 本地开发 Chart
helm create mychart              # 自动生成骨架
cd mychart
# 编辑 templates/ 与 values.yaml
 template .                  # 预览渲染结果
helm lint .                      # 检查
helm install local-release .     # 本地安装
```

## Helm 命令快速参考

| 命令 | 功能 |
|------|------|
| `helm install` | 创建 Release |
| `helm upgrade` | 升级 Release |
| `helm rollback` | 回滚到旧版 |
| `helm uninstall` | 删除 Release |
| `helm search repo` | 搜索仓库 |
| `helm repo add` | 添加仓库 |
| `helm repo update` | 更新仓库 |
| `helm template` | 渲染模板到 stdout |
| `helm lint` | 检查 Chart |
| `helm package` | 打包成 .tgz |
| `helm repo index` | 生成索引文件 |
| `helm dependency update` | 更新子 chart 依赖 |

## 常用语法与函数

- `{{ .Values.foo }}` → 从 `values.yaml` 读取 `foo`。
- `{{ if .Values.enabled }}` → 条件渲染。
- `{{ include "mychart.fullname" . }}` → 递归渲染子模板。
- `{{ .Release.Name }}` → 当前 Release 名。
- `{{ .Chart.Version }}` → Chart 版本。

## Tips

1. **多环境部署**  
   - 采用不同 `values-<env>.yaml`，在 `install/upgrade` 时使用 `-f` 叠加覆盖。
2. **CI/CD 集成**  
   - 通过 GitHub Actions / GitLab CI 自动执行 `helm lint`、`helm test`、`helm upgrade`。
3. **自建仓库**  
   - 使用 `chartmuseum` 或 `artifacthub/charts` 部署私有 chart 仓库。

> 🚀 Helm 让 Kubernetes 应用管理变得像安装普通软件包一样简单。通过模板化、参数化与版本化，团队可以快速原型、持续交付并保障可回溯性。