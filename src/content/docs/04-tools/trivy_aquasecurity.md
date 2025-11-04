
---
title: trivy
---


# Trivy – 开源容器与依赖安全扫描工具

> GitHub 项目地址: https://github.com/aquasecurity/trivy

---

## 主要特性

- **多平台扫描**：支持 Docker、OCI、Aqua Registry、Git、Helm Charts、Kubernetes 原生资源等。
- **全栈依赖检测**：扫描操作系统包（Debian、Ubuntu、Alpine、Rocky、CentOS 等）、语言包管理器（Go、Python、Ruby、Java、NodeJS、.NET 等）以及容器镜像里的应用层依赖。
- **漏洞数据库**：
  - OS 指纹 & CVE
  - 语言包漏洞
  - 合规性检查（CIS、DISA STIG 等）
- **Secrets 检测**：自动发现硬编码的密码、API Key、证书等敏感信息。
- **快速定位**：只扫描影响层，几秒至数分钟内完成，支持多进程并行。
- **格式化输出**：支持 `table`、`json`、`template`、`junit`、`sarif` 等多种输出格式，方便集成 CI/CD。
- **插件化与自定义**：可通过 Trivy plugin 或自定义 `Vulnerability-Input`/`Configuration-Input` 进行扩展。

---

## 基本功能

| 功能 | 描述 |
|------|------|
| 镜像扫描 | `trivy image <镜像名>` |
| 本地文件系统扫描 | `trivy fs <路径>` |
| Git 仓库扫描 | `trivy repo <仓库地址>` |
| Helm Chart 扫描 | `trivy chart <chart-name>` |
| Kubernetes 资源扫描 | `trivy k8s`（通过 K8s API 或 `kubeconffile`配置） |
| 攻击面低耗资源扫描 | `trivy config`（扫描配置文件的安全错误） |
| Terraform 资源扫描 | `trivy tf`（扫描 AWS 资源配置） |

---

## 安装方式

1. **Docker**（推荐）  
   ```bash   docker pull aquasec/trivy:latest
   docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest trivy image alpine:latest
   ```

2. **包管理器**  
   - **Homebrew**（macOS / Linux）  
     ```bash
     brew install aquasecurity/trivy/trivy
     ```  
   - **APT (Debian、Ubuntu)**  
     ```bash
     sudo apt-get install -y libssl-dev libffi-dev cargo
     cargo install trivy
     ```
   - **YUM / DNF (CentOS / Rocky)**  
     ```bash
     sudo yum install -y git golang
     go install github.com/aquasecurity/trivy/cmd/trivy@latest
     ```

3. **Go**  
   ```bash
   go install github.com/aquasecurity/trivy/cmd/trivy@latest
   ```

---

## 用法示例

```bash
# 1. 镜像扫描（默认输出表格）
trivy image alpine:latest

# 2. 镜像扫描（JSON 输出，写文件）
trivy image alpine:latest --format json --output alpine_scan.json

# 3. 阻止低危（=MEDIUM, HIGH, CRITICAL）漏洞
trivy image alpine:latest --severity HIGH,CRITICAL

# 4. 本地文件系统扫描
trivy fs ./myproject

# 5. Git 仓库扫描（带分支）
trivy repo https://github.com/aquasecurity/trivy --branch main

# 6. Helm Chart 扫描（从 registry）
trivy chart library/redis:6.0

# 7. Kubernetes 资源扫描（集成到 CI）
trivy k8s --server https://my-k8s-api:6443 --kubeconfig $HOME/.kube/config

# 8. 只列出所有已知包（不做漏洞扫描）
trivy image alpine:latest --list-all-pkgs

# 9. 使用自定义模板生成 HTML 报告
trivy image alpine:latest --format template --template "@/path/to/template.tmpl" --output report.html
```

---

## 与 CI/CD 集成

```yaml
# GitHub Actions 示例
name: Scan Docker Image
on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Trivy
      uses: aquasecurity/trivy-action@v0.1.0
    - name: Scan Docker image
      run: trivy image --format template --template "@trivy.tmpl" --output trivy_report.html ghcr.io/myorg/myapp:latest
```

---

## 相关文档

- 官方使用手册: https://aquasecurity.github.io/trivy/latest/docs/quick-start/
- 详细配置与插件: https://aquasecurity.github.io/trivy/latest/docs/configuration/
- 改进与贡献: https://github.com/aquasecurity/trivy/blob/master/CONTRIBUTING.md

---```
