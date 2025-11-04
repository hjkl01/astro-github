
---
title: gitleaks
---


# Gitleaks

**项目地址:** https://github.com/gitleaks/gitleaks

---

## 主要特性

| 特色 | 说明 |
|------|------|
| **全局扫描** | 可以递归扫描整个 Git 仓库，识别所有提交历史中的敏感信息。 |
| **正则表达式规则** | 内置数百条规则（如密码、API Key、证书等）并支持自定义正则表达式。 |
| **多平台** | 提供 Windows、macOS、Linux 二进制或可直接通过 `go build` 生成。 |
| **多语言** | 目录结构、配置文件、源代码兼容多语言项目。 |
| **智能忽略** | 支持 `.gitleaks.toml` 配置文件，可指定忽略的路径、文件、规则等。 |
| **CI 集成** | 一行命令即可在 CI Pipeline 中检测泄露，返回 JSON、SARIF 等格式的报告。 |
| **高性能** | 所有扫描在单次运行中完成，线性时间复杂度，兼顾速度与准确率。 |
| **可扩展** | 通过 `-i <file>` 方式批量注入自定义规则，或者利用 API 进行远程扫描。 |

---

## 功能介绍

1. **扫描模式**  
   - `--repo`: 指定要扫描的 Git 仓库。  
   - `--commit`: 指定扫描的提交范围（快照式）。  
   - `--glob`: 仅扫描符合 glob 模式的文件。  

2. **报告输出**  
   - `--report-file <path>`: 输出默认 JSON。  
   - `--report-format sarif`: 输出 SARIF 格式，方便 SAST 工具链集成。  
   - `--report-format txt`: 简易纯文本报告。  

3. **自定义规则**  
   - `--test-pattern "<regex>"`: 直接传递正则进行一次性扫描，适合测试。  
   - 配置文件 `.gitleaks.toml` 内可定义 `description`, `regex`, `entropy`, `captcha` 等属性。  

4. **忽略规则**  
   - `--exclude-path <path>` 与 `.gitleaks.toml` 中 `exclude-paths` 同样生效。  
   - 通过 `--exclude-rules <rule>` 或 `.gitleaks.toml` 中的 `exclude-rules` 排除特定规则。  

5. **CI/CD 集成**  
   ```bash
   gitleaks detect --repo . --report-format sarif --report-file gitleaks.sarif
   ```  

---

## 用法示例

```bash
# 基本扫描
gitleaks detect

# 指定 Git 仓库位置
gitleaks detect --repo /path/to/repo

# 仅扫描特定提交
gitleaks detect --repo . --commit HEAD~5..HEAD

# 输出 SARIF 格式报告
gitleaks detect --repo . --report-format sarif --report-file gitleaks.sarif

# 通过配置文件加载自定义规则与忽略
gitleaks detect --repo . --config .gitleaks.toml
```

> **Tip**: 在 CI Pipeline 中可直接使用 `gitleaks detect --report-format sarif`，随后将生成的 `sarif` 文件上传到安全审核工具。

---

> **常见命令行选项**  
> - `-h, --help`：显示帮助信息  
> - `-v, --version`：显示版本  
> - `-c, --config`：自定义配置文件路径  
> - `-i, --include-rule`：仅使用指定规则  
> - `-e, --exclude-rule`：排除指定规则  
> - `-p, --path`：指定扫描目录（默认目录为仓库根）  

--- 
**GitHub 仓库**: [https://github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)
