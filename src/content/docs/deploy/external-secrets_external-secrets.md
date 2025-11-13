---
title: external-secrets
---

# External Secrets Operator

External Secrets Operator 是一个 Kubernetes operator，用于从第三方秘密管理系统（如 AWS Secrets Manager、HashiCorp Vault、Google Secrets Manager、Azure Key Vault 等）读取信息，并自动将这些值注入到 Kubernetes Secret 中。

## 功能

- **集成多种秘密存储**：支持 AWS Secrets Manager、HashiCorp Vault、Google Secrets Manager、Azure Key Vault、IBM Cloud Secrets Manager、Akeyless、CyberArk Secrets Manager、Pulumi ESC 等。
- **自动同步**：从外部 API 读取秘密并自动注入到 Kubernetes Secret 中。
- **安全管理**：避免在 Kubernetes 集群中明文存储敏感信息。
- **多租户支持**：支持多个命名空间和集群级别的秘密管理。
- **可扩展**：支持自定义提供商和生成器。

## 用法

### 安装

使用 Helm 安装：

```bash
helm repo add external-secrets https://charts.external-secrets.io
helm install external-secrets external-secrets/external-secrets
```

或者使用 kubectl 应用 YAML：

```bash
kubectl apply -f https://raw.githubusercontent.com/external-secrets/external-secrets/main/deploy/charts/external-secrets/crds
kubectl apply -f https://raw.githubusercontent.com/external-secrets/external-secrets/main/deploy/charts/external-secrets/templates
```

### 创建 SecretStore

定义一个 SecretStore 来连接到外部秘密存储，例如 AWS Secrets Manager：

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secretsmanager
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa
```

### 创建 ExternalSecret

定义一个 ExternalSecret 来从 SecretStore 同步秘密：

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: example-secret
spec:
  refreshInterval: 15s
  secretStoreRef:
    name: aws-secretsmanager
    kind: SecretStore
  target:
    name: example-secret
    creationPolicy: Owner
  data:
    - secretKey: username
      remoteRef:
        key: prod/myapp
        property: username
    - secretKey: password
      remoteRef:
        key: prod/myapp
        property: password
```

这将创建一个名为 `example-secret` 的 Kubernetes Secret，其中包含从 AWS Secrets Manager 同步的 `username` 和 `password`。

更多详细信息请参考 [官方文档](https://external-secrets.io)。
