---
title: litmus
---
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
