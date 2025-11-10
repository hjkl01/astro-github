---
title: external-dns
---


# External DNS - Kubernetes 集成

**项目地址**: <https://github.com/kubernetes-sigs/external-dns>

## 项目概述

External DNS 是一个开源工具，旨在自动将 Kubernetes Service 和 Ingress 的 DNS 记录同步到外部 DNS 提供商（如 AWS Route53、Google Cloud DNS、Azure DNS、Cloudflare、Digital、NS1 等）。它使得在 Kubernetes 集群内部创建的服务能够无缝映射到生产环境的域名，实现完全自动化的 DNS 管理。

## 主要特性

1. **多供应商支持**  
   - 与常见 DNS 提供商（AWS、GCP、Azure、Cloudflare、DigitalOcean、NS1、Route53 等）无缝集成。  
   - 通过插件化架构，支持自定义 DNS 后端。

2. **资源类型支持**  
   - Service、Ingress、Deployment、Endpoints、EndpointsSlice 等。  
   - 通过注解或标签选择需要同步的 DNS 记录。

3. **自动化 DNS 记录管理**  
   - 根据 Kubernetes 资源的变化，自动创建、更新和删除 DNS A/AAAA/CNAME/NS/LOC/Other 记录。  
   - 支持多种 Kubernetes API 资源及其字段映射。

4. **自定义记录规则**  
   - 使用注解（`external-dns.alpha.kubernetes.io/hostname`、`external-dns.alpha.kubernetes.io/target` 等）自定义主机名、TTL、记录类型。  
   - 支持“mesh”模式（多集群多区域）与“shared”模式（单集群使用多域名）。

5. **安全 & 细粒度访问控制**  
   - 通过 RBAC 与 Pod Security Policies 结合使用，最小权限原则。  
   - 支持使用 ServiceAccount 与外部 DNS 供应商的凭证管理。

6. **可观测性与监控**  
   - 通过 Prometheus 导出 metrics（记录同步状态、失败次数、延迟等）。  
   - 日志可与 Fluentd 等日志聚合工具集成。

## 功能与使用

1. **安装（示例: Helm）**

   ```bash
   helm repo add external-dns https://kubernetes-sigs.github.io/external-dns/
   helm repo update
   helm install external-dns external-dns/external-dns \
     --namespace kube-system \
     --set provider.aws=true \          # 若使用 AWS Route53
     --set aws.zoneType=public \        # 区域类型
     --set policy=sync \                # 同步策略
     --set txtOwnerId=my-cluster \      # TXT 记录唯一标识
     --set domainFilters=mydomain.com   # 仅同步指定域名
   ```

2. **注解与标签**

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx
     labels:
       external-dns.alpha.kubernetes.io/hostname: "nginx.example.com"
   spec:
     ...
   ```

   或者

   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: my-ingress
     annotations:
       external-dns.alpha.kubernetes.io/hostname: "app.example.com"
   spec:
     ingressClassName: nginx
     rules:
       - host: app.example.com
         http:
           paths:
             - path: /
               backend:
                 service:
                   name: my-service
                   port:
                     number: 80
   ```

3. **同步策略**

   - `none`: 不同步任何记录（仅供测试）。  
   - `upsert-only`: 仅插入或更新记录，删除旧记录需手动操作。  
   - `sync`: 脚本阶段同步，删除后自动清理。

4. **多集群与多域名**

   ```yaml
   # 在同一 YAML 中使用不同注解实现多域名
   metadata:
     annotations:
       external-dns.alpha.kubernetes.io/hostname: "app1.example.com,app2.example.com"
   ```

5. **监控与日志**

   - Prometheus 自动挂载 `/metrics`。  
   - 通过 `kubectl logs -n kube-system deployment/external-dns` 查看日志。

## 开发与贡献

- 采用 Go 语言实现，遵循 Kubernetes 代码规范。  
- 项目使用 `Makefile` 进行构建、测试与发布。  
- 欢迎提交 PR、Issue，或参与 `providers` 目录下的插件开发。

## 参考

- 官方文档: <https://github.com/kubernetes-sigs/external-dns/blob/master/docs/README.md>  
- 常见问题: <https://github.com/kubernetes-sigs/external-dns/issues>  

---
> **注**：上述示例仅供参考，实际使用请根据目标 DNS 공급商和集群环境进行适配。