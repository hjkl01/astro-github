---
title: Gitleaks
---

# Gitleaks

## 项目介绍

Gitleaks 是一个用于检测代码库中秘密信息的工具。它可以扫描 Git 仓库、目录、文件以及通过 stdin 输入的内容，查找诸如密码、API 密钥、令牌等敏感信息。Gitleaks 使用正则表达式和熵分析来识别潜在的秘密泄露，帮助开发者在代码提交前或 CI/CD 流程中防止敏感信息被意外提交。

项目地址：[https://github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

## 主要功能

- **多扫描模式**：支持扫描 Git 仓库（`git`）、目录和文件（`dir`）、以及 stdin 输入（`stdin`）。
- **灵活配置**：支持自定义规则、正则表达式、熵阈值、路径过滤等。
- **多种输出格式**：支持 JSON、CSV、JUnit、SARIF 等报告格式，以及自定义模板。
- **基线支持**：可以创建基线报告，忽略已知的历史问题。
- **解码支持**：自动检测和解码 base64、hex、percent 编码的秘密。
- **归档扫描**：支持扫描压缩文件和归档文件中的内容。
- **集成友好**：支持 GitHub Action、Pre-commit Hook 等 CI/CD 集成。
- **性能优化**：支持并发扫描、超时设置、文件大小限制等。

## 安装方式

### MacOS

```bash
brew install gitleaks
```

### Docker

```bash
# Docker Hub
docker pull zricethezav/gitleaks:latest
docker run -v ${path_to_host_folder_to_scan}:/path zricethezav/gitleaks:latest [COMMAND] [OPTIONS] [SOURCE_PATH]

# GitHub Container Registry
docker pull ghcr.io/gitleaks/gitleaks:latest
docker run -v ${path_to_host_folder_to_scan}:/path ghcr.io/gitleaks/gitleaks:latest [COMMAND] [OPTIONS] [SOURCE_PATH]
```

### 从源码安装

```bash
git clone https://github.com/gitleaks/gitleaks.git
cd gitleaks
make build
```

### 二进制文件

从 [Releases 页面](https://github.com/gitleaks/gitleaks/releases) 下载适用于不同平台的二进制文件。

## 基本用法

### 扫描 Git 仓库

```bash
gitleaks git [OPTIONS] [PATH]
```

- 如果不指定 PATH，则扫描当前目录的 Git 仓库。
- 示例：扫描当前仓库并显示详细信息
  ```bash
  gitleaks git -v
  ```

### 扫描目录或文件

```bash
gitleaks dir [OPTIONS] [PATH]
```

- 如果不指定 PATH，则扫描当前目录。
- 示例：扫描指定目录
  ```bash
  gitleaks dir -v /path/to/directory
  ```

### 扫描 stdin 输入

```bash
cat file.txt | gitleaks stdin [OPTIONS]
```

## 高级用法

### 创建基线报告

```bash
# 生成基线报告
gitleaks git --report-path baseline.json

# 使用基线扫描，仅报告新问题
gitleaks git --baseline-path baseline.json --report-path findings.json
```

### 自定义配置

创建 `.gitleaks.toml` 文件来自定义规则：

```toml
title = "Custom Gitleaks configuration"

[[rules]]
id = "custom-api-key"
description = "Custom API key pattern"
regex = '''api[_-]?key[\\s]*[=:][\\s]*["']?([a-zA-Z0-9]{32,})["']?'''
secretGroup = 1
entropy = 3.0
```

### GitHub Action 集成

在 `.github/workflows/gitleaks.yml` 中添加：

```yaml
name: gitleaks
on: [pull_request, push, workflow_dispatch]
jobs:
  scan:
    name: gitleaks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Pre-commit Hook

1. 安装 pre-commit：
   ```bash
   pip install pre-commit
   ```
2. 创建 `.pre-commit-config.yaml`：
   ```yaml
   repos:
     - repo: https://github.com/gitleaks/gitleaks
       rev: v8.24.2
       hooks:
         - id: gitleaks
   ```
3. 安装 hook：
   ```bash
   pre-commit install
   ```

## 配置选项

- `--config`: 指定配置文件路径
- `--baseline-path`: 指定基线文件路径
- `--report-path`: 指定报告输出路径
- `--report-format`: 输出格式 (json, csv, junit, sarif, template)
- `--verbose`: 显示详细输出
- `--redact`: 部分或完全隐藏秘密 (默认 100%)
- `--max-decode-depth`: 最大解码深度 (默认 0)
- `--max-archive-depth`: 最大归档扫描深度 (默认 0)

## 示例输出

```
Finding:     "export BUNDLE_ENTERPRISE__CONTRIBSYS__COM=cafebabe:deadbeef",
Secret:      cafebabe:deadbeef
RuleID:      sidekiq-secret
Entropy:     2.609850
File:        cmd/generate/config/rules/sidekiq.go
Line:        23
Commit:      cd5226711335c68be1e720b318b7bc3135a30eb2
Author:      John
Email:       john@users.noreply.github.com
Date:        2022-08-03T12:31:40Z
Fingerprint: cd5226711335c68be1e720b318b7bc3135a30eb2:cmd/generate/config/rules/sidekiq.go:sidekiq-secret:23
```

## 注意事项

- Gitleaks 使用正则表达式检测秘密，可能会有误报。
- 建议结合 `.gitleaksignore` 文件忽略已知的安全测试用例。
- 对于已知秘密，可以在代码中添加 `#gitleaks:allow` 注释来忽略。
- 扫描大型仓库时，建议使用基线功能以减少重复报告。
