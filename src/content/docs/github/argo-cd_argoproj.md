---
title: argo-cd
---


# Argo CD（GitOps 解决方案）

## 项目地址  
https://github.com/argoproj/argo-cd

## 项目概览  
Argo CD 是一款基于 Kubernetes 的持续交付（CD）工具，采用 GitOps 思维，通过管理 Git 仓库中定义的 Kubernetes 资源，自动将应用部署到集群。它支持 Git 仓库作为单一真理源，将 Git 状态自动同步到集群，实现 rollback、自动化监控与审计。

## 主要特性  

- **GitOps 原生**：所有资源声明存放在 Git，Argo CD 负责持续监控并将差异同步到集群。  
- **可视化 UI & CLI**：提供 Web UI、REST API 和 `argocd` 命令行，支持多语言团队统一操作。  
- **资源管理**：支持 Helm、Kustomize、Ksonnet、Bare YAML 等多种配置管理方式。  
- **自动同步**：可配置 PR 自评审后自动同步或手动同意。  
- **策略/权限控制**：配合 RBAC、SAML/OIDC、Kubernetes 的 Service Account 等实现细粒度访问控制。  
- **多集群支持**：一个 Argo CD 实例可管理多个 Kubernetes 集群。  
- **安全与审计**：事件日志记录与 RBAC 规则，满足合规需求。  
- **自定义 Workflows**：支持自定义资源定义（CRD）以及应用同步/验证钩子。  

## 用法概览  

1. **安装 Argo CD**  
   ```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```

2. **访问 UI**  
   ```bash
   # 端口转发（如果没有 Ingress）
   kubectl port-forward svc/argocd-server -n argocd 8080:443
   ```

3. **登录命令行**  
   ```bash
   argocd login <ARGOCD_FQDN> --username admin --password $(kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d)
   ```

4. **添加应用**  
   ```bash
   argocd app create my-app \
     --repo https://github.com/argoproj/argo-cd-example-apps.git \
     --path webapp \
     --dest-server https://kubernetes.default.svc \
     --dest-namespace default \
     --sync-policy automated
   ```

5. **同步 & 声明**  
   - 在 UI 里按 `Sync` 按钮手动同步。  
   - 通过设置 `--sync-policy automated` 让 Argo CD 自动监控 Git 更改并同步。  

6. **监控 & 回滚**  
   - UI 左侧可查看应用状态、历史提交、回滚版本。  
   - CLI 回滚：`argocd app rollback my-app 1234`（其中 1234 为历史 sync 号）。  

7. **RBAC 配置**  
   - 修改 `argocd-rbac-cm` ConfigMap：  
     ```yaml
     apiVersion: v1
     kind: ConfigMap
     metadata:
       name: argocd-rbac-cm
       namespace: argocd
     data:
       policy.csv: |
         g, developers, role:readonly
         p, role:readonly, applications, get, */*, allow
     ```
   - 重新加载：`kubectl -n argocd rollout restart deployment argocd-server`  

## 典型命令  
| 操作 | 命令 | 说明 |
|-----|-----|------|
| 查看应用列表 | `argocd app list` | 列出所有应用 |
| 查看应用状态 | `argocd app get <app-name>` | 显示不同资源的状态与差异 |
| 同步应用 | `argocd app sync <app-name>` | 手动触发同步 |
| 回滚 | `argocd app rollback <app-name> <revision>` | 回滚到指定历史版本 |
| 删除应用 | `argocd app delete <app-name>` | 在 Argo CD 中移除应用 |

## 进一步资源  
- 官方文档: https://argo-cd.readthedocs.io/en/stable/  
- GitHub 仓库: https://github.com/argoproj/argo-cd  
- 运行示例: https://github.com/argoproj/argo-cd-example-apps  

```markdown