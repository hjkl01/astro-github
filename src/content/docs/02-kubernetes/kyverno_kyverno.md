
---
title: kyverno
---

# Kyverno - Kubernetes 策略引擎

## 项目地址
[kyverno/kyverno](https://github.com/kyverno/kyverno)

## 主要特性
- **Policy/规则引擎**：在 Kubernetes 集群中根据示例、规范或安全需求自动强制执行策略。
- **运行时自动化**：支持 `Admit`、`Validate`、`Mutate`、`Generate` 四大操作，实时处理入站请求。
- **策略声明式配置**：使用 YAML 书写策略，轻松管理和版本化。
- **多租户与命名空间隔离**：通过 NamespaceSelector 或 ClusterPolicy 控制适用范围。
- **兼容 Kubernetes 生态**：与OPA、Gatekeeper、OPA‑Bridge 等工具协同使用。
- **灵活的策略写法**：支持 `rego` 样式表达式或 Kyverno 自己的- **日志与审计**：完整的审计日志，可通过指标（Prometheus）观察执行情况。

## 主要功能
| 功能 | 说明 |
|------|------|
| **Admit** | 拒绝不符合策略的 Pod/Service 等资源创建请求。 |
| **Validate** | 仅验证资源，允许创建但记录失败。 |
| **Mutate** | 自动修改资源的字段（如标签、注解、容器镜像版本等）。 |
| **Generate** | 根据现有资源生成补充资源（如自动创建 ConfigMap）。 |
| **ClusterPolicy** | 集群级策略，影响整个集群。 |
| **ResourcePolicy** | 仅作用于特定资源或命名空间。 |
| **PolicyException** | 指定例外情况，临时绕过策略。 |
| **Dry-Run** | 模拟执行，检查策略是否符合预期。 |

## 快速使用方法
1. **安装 Kyverno**  
   ```bash
   kubectl create -f https://github.com/kyverno/kyverno/releases/download/v3.1.0-1/kyverno.yaml
   ```

2. **验证已安装**  
   ```bash
   kubectl get pods -n kyverno
   ```

3. **编写策略**  
   创建 `policy.yaml`  
   ```yaml
   apiVersion: kyverno.io/v1
   kind: ClusterPolicy
   metadata:
     name: restrict-privileged
   spec:
     validationFailureAction: Enforce
     rules:
     - name: deny-privileged
       match:
         resources:
           kinds: [Pod]
       validate:
         message: "Pods with privileged containers are not allowed."
         pattern:
           spec:
             containers:
             - securityContext:
                 privileged: false
   ```

4. **部署策略**  
   ```bash
   kubectl apply -f policy.yaml
   ```

5. **测试**  
   创建一个包含 `privileged: true` 的 Pod，Kyverno 将拒绝创建并返回明确信息。

6. **监控 & 日志**  
   - 日志：`kubectl logs -n kyverno $POD_NAME`  
   - 监控指标：将 `prometheus` 端点添加到 Prometheus 中即可。

## 进一步阅读
- 官方文档：https://kyverno.sigs.k8s.io/docs/  
- 示例与模板：https://github.com/kyverno/kyverno/tree/main/config/samples
