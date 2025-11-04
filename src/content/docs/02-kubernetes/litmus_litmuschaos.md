
---
title: litmus
---


# Litmus — Kubernetes 级的混沌工程平台

**项目地址**：[https://github.com/litmuschaos/litmus](https://github.com/litmuschaos/litmus)

## 一、概述  
Litmus 是一个开源的混沌工程框架，旨在帮助 DevOps 和 SRE 团队在 Kubernetes 环境中主动识别、诊断并修复系统脆弱点。它提供了可重用的实验模板、可视化仪表盘、自动化支持以及与 CI/CD 流水线深度集成的能力。

---

## 二、主要特性

| 特性 | 说明 |
|------|------|
| **实验模板化** | 通过 `chaos-experiments` CRD 定义成熟的混沌实验（如 PodKill、NetworkLatency 等），可复用、可自定义。 |
| **工程化流程** | `chaos-engine` CRD 描述一次完整的混沌实验生命周期（目标、实验、恢复），实现实验的 Declarative 管理。 |
| **可视化仪表盘** | 开箱即用的 Grafana Dashboard，实时展示实验状态、资源指标与恢复效果。 |
| **CI/CD 集成** | 提供基于 GitOps 的实验调度与监控，支持 Argo CD、Tekton 等主流 CI/CD。 |
| **SLO/SLI 验证** | 在实验前后对业务 SLO 进行验证，输出失败率、延时等安全指标。 |
| **安全与权限** | 通过 RBAC 控制实验权限，支持最小化特权原则。 |
| **多框架支持** | 除了 ChaosEngine，还兼容 `chaos-runner`、`litmusctl` 等工具，灵活使用。 |
| **插件化扩展** | 支持自定义实验插件，轻松扩展新实验。 |

---

## 三、安装与配置

> **前置**：已搭建 `k8s` 集群，并安装 `kubectl`。

```bash
# 1. 安装 Litmus Operator
helm repo add litmuschaos https://litmuschaos.github.io/litmus-helm/
helm repo update
helm install litmus litmuschaos/litmus \
  --namespace litmus-system \
  --create-namespace

# 2. 安装 Chaos-Experiment CRDs
kubectl apply -f https://github.com/litmuschaos/litmus/blob/master/chaos-platform/helm/litmus/values.yaml --recursive
```

---

## 四、使用示例

### 1. 创建混沌实验

```yaml
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosEngine
metadata:
  name: pod-kill
  namespace: default
spec:
  appinfo:
    appid: "nginx"
  experiments:
  - name: pod-kill
    spec:
      components:
        env:
        - name: CHAOS_DURATION
          value: "30"  # 运行时长
        - name: TARGET_POD_LABEL
          value: "app=nginx"
```

```bash
kubectl apply -f pod-kill.yaml
```

### 2. 监控实验状态

```bash
kubectl get chaosengine -n default
# 或使用 litmusctl
litmusctl get experiment pod-kill -n default
```

### 3. 验证 SLO

在实验 YAML 中添加 `slos` 字段，Litmus 将自动把实验进度与 SLO 对比，并生成报告。

```yaml
slos:
  - name: latency
    params:
      target: 200ms
      matcher: ">=200"
```

---

## 五、最佳实践

1. **实验前后对比**：使用 `litmusctl diff` 或 Grafana 仪表盘对比指标变化。  
2. **版本管理**：将实验 YAML 存入 Git，使用 GitOps 自动触发。  
3. **权限控制**：仅给信任的团队成员 `create` 和 `delete` `ChaosEngine` 的权限。  
4. **链式实验**：通过 Blueprint 或 `workflow` 组合多实验，实现从网络延迟到磁盘故障的完整路径测试。  

---

## 六、进一步阅读

- 官方文档：[https://litmuschaos.githubmus/](https://litmuschaos.github.io/litmus/)  
- 实验案例集（GitHub Repo）：`examples` 文件夹  
- 社区交流：Slack、GitHub Discussions

> **提示**：本节为简版参考文档，更多高级用法可查看官方官方文档与社区演示。  
