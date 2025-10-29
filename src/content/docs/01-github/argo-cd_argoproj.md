
---
title: argo-cd
---

# Argo CD 简介

> 项目地址: <https://github.com/argoproj/argo-cd>

## 一、项目概述  
Argo CD 是一个基于 GitOps 思想的 Kubernetes 持续交付（CD）工具。它通过 Git 作为单一真相源，自动将 Kubernetes 集群与 Git 仓库中声明的资源保持同步，实现快速、可审计、可回滚的应用部署。

## 二、主要特性  

| 特性 | 说明 |
|------|------|
| **GitOps 原则** | 所有资源定义均存放在 Git 仓库，Argo CD 通过监控 Git 变更并同步到集群。 |
| **声明式应用管理** | 通过 YAML/Helm/ Kustomize 等声明式方式描述应用，支持多集群、多环境。 |
| **自动同步** | 配置 Auto‑Sync 后，Git 变更会自动触发同步。手动同步亦可通过 UI/CLI 触发。 |
| **健康与状态监控** | 内置资源健康检查，显示应用状态（Healthy/Degraded/Unknown）。 |
| **多集群与多命名空间** | 同一 UI 可管理多个 Kubernetes 集群和命名空间。 |
| **RBAC & SSO** | 支持基于角色的访问控制、OpenID Connect、SAML、Azure AD 等单点登录。 |
| **通知与 Webhook** | 通过 Slack、Email、Webhook 等渠道发送同步/健康告警。 |
| **CLI (argocd)** | 命令行工具支持应用创建、同步、查询等操作。 |
| **自定义资源支持** | 可通过自定义资源（CRDs）扩展 Argo CD 功能。 |
| **插件化** | 支持自定义插件（Argo CD Exec、Helm、Kustomize 等）以满足特定需求。 |

## 三、核心功能  

1. **应用定义**  
   - `Application` 资源描述应用：来源、目标集群、命名空间、同步策略等。  
2. **同步**  
   - **自动同步**：配置 `spec.syncPolicy.automated` 开启后，Git 变更会触发同步。  
   - **手动同步**：UI 或 `argocd app sync <name>` 手动触发。  
3. **差异化查看**  
   - UI/CLI 显示 Git 与集群资源的差异，支持逐资源级别查看。  
4. **回滚**  
   - 通过 `argocd app rollback <name> <revision>` 或 UI 回滚到指定 Git 版本。  
5. **健康检查**  
   - 支持自定义健康检查脚本或使用内置 K8s 资源状态。  
6. **权限管理**  
   - 通过 `argocd cluster add` 与 `argocd cluster delete` 管理访问的集群。  
   - 使用 `argocd auth` 配置 RBAC。  

## 四、使用指南  

### 1. 安装 Argo CD  
```bash
# 安装到 kube-system 命名空间
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### 2. 访问 UI  
```bash
# 暴露服务
kubectl port-forward svc/argocd-server -n argocd 8080:443
# 打开浏览器访问 https://localhost:8080
```

### 3. 登录  
```bash
# 通过 CLI 登录
argocd login localhost:8080 --username admin --password $(kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d)
```

### 4. 添加应用  
```bash
argocd app create my-app \
  --repo https://github.com/your-org/your-repo.git \
  --path path/to/chart \
  --dest-namespace default \
  --dest-server https://kubernetes.default.svc
```

### 5. 同步与管理  
```bash
# 同步
argocd app sync my-app

# 查看状态
argocd app get my-app

# 回滚
argocd app rollback my-app 123456
```

### 6. 设置 Auto‑Sync  
在 `Application` YAML 里添加：
```yaml
spec:
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### 7. 配置 RBAC  
创建 `argocd-rbac-cm` ConfigMap：
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-rbac-cm
  namespace: argocd
data:
  policy.csv: |
    p, role:admin, applications, *, */*, allow
    g, alice, role:admin
```

### 8. 通知与 Webhook  
在 `argocd-notifications-cm` ConfigMap 配置：
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-notifications-cm
  namespace: argocd
data:
  config.yaml: |
    trigger:
      on-sync-succeeded: &on-sync-succeeded
        when: "success"
        send: email
    template:
      email: |
        Subject: ArgoCD {{ .app.name }} sync succeeded
        Body: |
          {{ .app.name }} has been successfully synced.
```

## 五、扩展与自定义  

- **插件**：通过 `argocd exec` 插件执行自定义脚本。  
- **自定义资源**：通过 CRDs 结合 Argo CD 进行业务级治理。  

## 六、常见命令速查  

| 命令 | 说明 |
|------|------|
| `argocd app list` | 列出所有应用 |
| `argocd app diff <name>` | 查看差异 |
| `argocd app health <name>` | 检查健康 |
| `argocd cluster add <context>` | 绑定集群 |
| `argocd repo add <url> --username <u> --password <p>` | 添加 Git 仓库 |

> 详细使用请参阅官方文档: <https://argo-cd.readthedocs.io/>
