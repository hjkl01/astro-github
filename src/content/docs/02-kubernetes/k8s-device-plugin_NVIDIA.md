---
title: k8s-device-plugin
---
---

## 常见问题

- **GPU 驱动未安装**  
  插件会在启动时失败，请确认节点上已安装匹配的驱动版本。

- **CPU 与 GPU 资源不匹配**  
  Kubernetes 规划时可能出现错误，建议检查节点可用 CPU 与 GPU 的对应关系。

- **多租户隔离问题**  
  使用 `nodeSelector` 或 `affinity` 进一步限制 Pod 调度范围。

---
> 以上内容为 NVIDIA k8s-device-plugin 的核心特性、功能与使用方式。请根据自身集群环境进行相应调整。