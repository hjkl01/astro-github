
---
title: dashboard
---


# Kubernetes Dashboard

**项目地址**: https://github.com/kubernetes/dashboard

---

## 项目概述
Kubernetes Dashboard 是一个基于 Web 的用户界面，帮助用户直观地管理 Kubernetes 集群。它提供了对集群资源（如 Deployments、Pods、Services 等）的可视化管理、监控以及错误排查能力。

## 主要特性
- **资源可视化**  
  - 直观展示集群、命名空间、工作负载、服务、持久卷等资源状态。  
- **日志与事件查看**  
  - 直接查看 Pod 日志和事件，快速定位问题。  
- **资源操作**  
  - 支持创建、更新、删除资源，编辑 YAML/JSON。  
- **权限管理**  
  - 支持基于 RBAC 的访问控制，安全性高。  
- **监控与指标**  
  - 集成 Metrics Server，展示 CPU、内存使用情况。  
- **多语言支持**  
  - 支持多语言界面，默认中文。  

## 功能细节
1. **集群概览**  
   - 查看节点、工作负载、服务、Ingress、PVC 等总体信息。  
2. **命名空间管理**  
   - 按命名空间切分资源视图，便于多项目管理。  
3. **资源编辑**  
   - 通过 YAML/JSON 编辑器直接修改资源定义。  
4. **安全与认证**  
   - 支持 Token、证书、OIDC 等多种鉴权方式。  
5. **日志与事件**  
   - 实时流式日志、历史日志；显示事件列表。  
6. **监控**  
   - CPU、内存、网络等实时指标；支持自定义阈值。  

## 安装与使用

```bash
# 1. 安装 Dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc.0/aio/deploy/recommended.yaml

# 2. 创建 ServiceAccount 和 ClusterRoleBinding（示例）
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
EOF

# 3. 获取访问 Token
kubectl -n kubernetes-dashboard create token admin-user

# 4. 通过端口转发访问
kubectl proxy
# 访问地址: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

### 访问方式
- **本地访问**：`kubectl proxy` + 访问上述 URL。  
- **服务端口转发**：`kubectl port-forward svc/kubernetes-dashboard 8443:443 -n kubernetes-dashboard`，然后访问 `https://localhost:8443`.  

### 注意事项
- 默认启用 HTTPS，访问时须忽略自签名证书错误。  
- 若需外部访问，建议使用 Ingress 或 LoadBalancer 并配置 TLS。  

## 参考链接
- 官方文档: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
- GitHub 仓库: https://github.com/kubernetes/dashboard

--- 
