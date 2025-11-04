
---
title: podkop
---


# podkop

**项目地址**: https://github.com/itdoginfo/podkop

## 主要特性
- **Pod 删除工具**：快速删除符合条件的 Kubernetes Pod。
- **多维过滤**：支持按命名空间、标签、字段选择器等多种条件过滤。
- **安全模式**：支持 `--dry-run` 预览将要删除的 Pod，避免误删。
- **强制删除**：`--force` 选项可立即强制删除即使 Pod 正在终止。
- **批量处理**：一次性删除所有命名空间或所有 Pod。
- **交互式确认**：默认交互模式在删除前进行确认，`--yes` 可跳过确认。
- **日志与输出**：支持自定义日志级别，`--verbose` 打印详细信息。
- **可配置**：支持通过环境变量或配置文件指定 kubeconfig 路径。
- **跨平台**：已预编译 Windows、Linux、macOS 版本，亦可自行编译。

## 安装方式
```bash
# 通过 Go 安装
go install github.com/itdoginfo/podkop@latest

# 或使用预编译二进制
# 下载对应系统的 tar.gz 或 zip 包，解压后直接使用
```

## 基本用法

```bash
# 查看帮助
podkop -h

# 删除指定命名空间下的 Pod（按标签过滤）
podkop delete -n frontend -l app=web

# 删除所有命名空间下的 Pod
podkop delete --all-namespaces

# 预览将要删除的 Pod
podkop delete -n backend -l app=api --dry-run

# 强制删除 Pod，跳过确认
podkop delete -n kube-system --force --yes

# 监视并删除满足条件的 Pod（实时模式）
podkop watch -n default -l app=worker
```

## 命令说明

| 命令 | 说明 |
|------|------|
| `podkop delete` | 删除 Pod。可配合 `-n`, `-l`, `--field-selector`, `--all-namespaces`, `--dry-run`, `--force`, `--yes` 等选项。 |
| `podkop watch` | 监视符合条件的 Pod 并自动删除，支持实时日志输出。 |
| `podkop version` | 查询工具版本信息。 |

## 配置

- **kubeconfig**：默认读取 `$HOME/.kube/config`。可通过 `--kubeconfig` 指定路径或设置 `KUBECONFIG` 环境变量。  
- **日志级别**：`--log-level=debug|info|warn|error`。默认 `info`。  

---

> **提示**：在生产环境中使用时，建议先执行 `--dry-run` 以确认删除范围，避免误删重要 Pod。