---
title: node
---
---

## 贡献

- Fork → Clone → `git checkout -b feat/your-feature` → 提交 Pull Request
- 代码遵循 `golang` 规范，使用 `golangci-lint` 进行静态检查。
- 详细贡献指南请查看项目根目录的 `CONTRIBUTING.md`。

---
### 备注
- 运行时请确保 `node_exporter` 有足够权限读取 `/proc`、`/sys` 等系统目录。
- 对于容器化部署，可使用 `--path.rootfs=/host` 指向宿主机根目录。
> **完成**  
> 以上即为 `node_exporter` 项目的主要特性、功能与使用方法。祝使用愉快！