
---
title: cert-manager
---

# cert-manager

**GitHub 项目地址:** https://github.com/cert-manager/cert-manager

## 项目简介
cert-manager 是一个 Kubernetes 原生的证书管理工具，负责自动化部署、续期、吊销和管理 TLS 证书。它通过自定义资源（CRD）与 Kubernetes 集成，支持多种证书颁发机构（CA）和多种挑战类型（HTTP、DNS、TLS）。

## 主要特性
- **自动化证书颁发与续期**：支持 ACME（Let's Encrypt）、Venafi、HashiCorp Vault、Webhook 等 CA。
- **多种挑战方式**：HTTP-01、DNS-01、TLS-ALPN-01。
- **自定义资源（CRD）**：`Issuer`、`ClusterIssuer`、`Certificate`、`CertificateRequest` 等。
- **与 Ingress 集成**：可在 Ingress 资源中直接引用证书。
- **自动吊销与吊销监控**：支持吊销功能与监控。
- **可扩展的插件体系**：支持自定义证书颁发逻辑。
- **高可用与水平可扩展**：可与 Kubernetes 集群无缝扩容。

## 核心功能
| 功能 | 说明 |
|------|------|
| Issuer / ClusterIssuer | 定义证书颁发机构，支持多种 CA。|
| Certificate | 请求和管理单个证书，自动续期。|
| Challenge Solvers | 自动处理 HTTP/DNS/TLS-ALPN 挑战。|
| CertificateRequest | 低级别证书请求，可用于自定义场景。|
| Webhook Issuer | 通过 webhook 调用外部 CA。|
| Helm / Kustomize 安装 | 通过 Helm chart 或 Kustomize 部署。|
| 日志与监控 | 与 Prometheus、Grafana 集成。|

## 用法示例

### 1. 安装 cert-manager（Helm）
```bash
# 添加 Helm 仓库
helm repo add jetstack https://charts.jetstack.io
helm repo update

# 安装 cert-manager
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager --create-namespace \
  --version v1.12.2 \
  --set installCRDs=true
```

### 2. 创建 ClusterIssuer（Let's Encrypt）
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your_email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - dns01:
        route53:
          region: us-east-1
          hostedZoneID: Z1234567890
```

### 3. 请求证书并绑定到 Ingress
```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: myapp-tls
  namespace: default
spec:
  secretName: myapp-tls
  dnsNames:
  - myapp.example.com
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80
```

### 4. 查看证书状态
```bash
kubectl describe certificate myapp-tls
```

## 参考资料
- 官方文档: https://cert-manager.io/docs/
- Helm chart: https://github.com/cert-manager/cert-manager/tree/master/deploy/charts/cert-manager

---