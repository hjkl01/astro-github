
---
title: gitleaks
---

# Gitleaks 项目描述

## 项目地址
[https://github.com/zricethezav/gitleaks](https://github.com/zricethezav/gitleaks)

## 主要特性
Gitleaks 是一个开源工具，用于检测 Git 仓库中意外提交的敏感信息，如 API 密钥、密码、令牌等。它通过扫描 Git 历史记录和文件内容来识别潜在的安全风险。主要特性包括：
- **快速扫描**：高效扫描大型 Git 仓库，支持并行处理。
- **自定义规则**：内置预定义规则集，可通过 JSON 配置自定义检测规则，支持正则表达式匹配。
- **报告生成**：输出详细的扫描报告，包括发现的泄露位置、上下文和严重性。
- **多平台支持**：跨 Windows、macOS 和 Linux 平台运行。
- **集成友好**：易于集成到 CI/CD 管道中，如 GitHub Actions、Jenkins 等。
- **无状态扫描**：不修改仓库内容，仅进行只读分析。

## 主要功能
- **Git 历史扫描**：分析所有提交、分支和标签，检测历史中的敏感数据泄露。
- **文件内容检查**：扫描工作目录和未提交的文件。
- **规则管理**：使用默认规则检测常见凭证（如 AWS 密钥、JWT 令牌），并允许扩展规则以覆盖特定需求。
- **输出格式**：支持 JSON、CSV 和纯文本格式的报告，便于自动化处理。
- **性能优化**：支持排除路径、限制扫描深度，以减少扫描时间。

## 用法
Gitleaks 使用 Go 语言编写，通过二进制文件或 Docker 运行。基本用法如下：

### 安装
- 从 GitHub Releases 下载预编译二进制文件，或使用 Go 安装：`go install github.com/zricethezav/gitleaks/v8@latest`。
- Docker 方式：`docker run --rm -v "$PWD:/path" zricethezav/gitleaks detect -v`。

### 基本命令
- **扫描仓库**：在仓库根目录运行 `gitleaks detect`，扫描整个 Git 历史。
  示例：`gitleaks detect --source .`
- **自定义配置**：使用配置文件 `gitleaks.toml` 或 `--config` 参数指定规则。
  示例：`gitleaks detect --config myrules.toml`
- **报告输出**：指定输出文件和格式。
  示例：`gitleaks detect --report-format json --report-path results.json`
- **选项**：
  - `--verbose` 或 `-v`：启用详细日志。
  - `--redact`：在报告中隐藏敏感信息。
  - `--no-git`：仅扫描当前文件，不检查 Git 历史。
  - `--exit-code`：设置非零退出码以便 CI 集成。

更多高级用法和选项，请参考项目 README。