---
title: strix
---

# Strix

Strix 是一个开源的 AI 黑客工具，用于保护您的应用程序。它由自主 AI 代理组成，这些代理像真实黑客一样运行您的代码，发现漏洞，并通过实际的证明概念（PoC）验证它们。适用于需要快速、准确的安全测试的开发者和安全团队，无需手动渗透测试或静态分析工具的误报。

## 主要功能

- **完整黑客工具包**：包括 HTTP 代理、浏览器自动化、终端环境、Python 运行时、侦察、代码分析和知识管理。
- **代理团队协作**：分布式工作流，专门化的代理针对不同攻击和资产，并行执行以实现快速全面覆盖。
- **真实验证**：通过 PoC 验证漏洞，而不是误报。
- **开发者友好**：CLI 工具，提供可操作的报告。
- **自动修复和报告**：加速补救过程。

## 支持的漏洞检测

- 访问控制：IDOR、权限提升、认证绕过
- 注入攻击：SQL、NoSQL、命令注入
- 服务端：SSRF、XXE、反序列化漏洞
- 客户端：XSS、原型污染、DOM 漏洞
- 业务逻辑：竞态条件、工作流操纵
- 认证：JWT 漏洞、会话管理
- 基础设施：配置错误、暴露服务

## 安装和使用

### 先决条件

- Docker（运行中）
- Python 3.12+
- LLM 提供商密钥（或本地 LLM）

### 安装

```bash
pipx install strix-agent
```

### 配置

设置 AI 提供商：

```bash
export STRIX_LLM="openai/gpt-4"
export LLM_API_KEY="your-api-key"
```

可选配置：

```bash
export LLM_API_BASE="your-api-base-url"  # 如果使用本地模型，如 Ollama、LMStudio
export PERPLEXITY_API_KEY="your-api-key"  # 用于搜索功能
```

### 基本用法

运行安全评估：

```bash
strix --target ./app-directory
```

首次运行会拉取沙箱 Docker 镜像。结果保存在 `agent_runs/<run-name>` 下。

### 用法示例

- 本地代码库分析：

  ```bash
  strix --target ./app-directory
  ```

- 仓库安全审查：

  ```bash
  strix --target https://github.com/org/repo
  ```

- Web 应用评估：

  ```bash
  strix --target https://your-app.com
  ```

- 多目标白盒测试（源代码 + 部署应用）：

  ```bash
  strix -t https://github.com/org/app -t https://your-app.com
  ```

- 测试多个环境：

  ```bash
  strix -t https://dev.your-app.com -t https://staging.your-app.com -t https://prod.your-app.com
  ```

- 聚焦测试：

  ```bash
  strix --target api.your-app.com --instruction "优先测试认证和授权"
  ```

- 使用凭据测试：
  ```bash
  strix --target https://your-app.com --instruction "使用凭据测试：testuser/testpass。聚焦权限提升和访问控制绕过。"
  ```

### 无头模式

使用 `-n/--non-interactive` 标志以编程方式运行 Strix，无交互 UI。CLI 打印实时漏洞发现，并在退出前提供最终报告。当发现漏洞时以非零代码退出。

```bash
strix -n --target https://your-app.com --instruction "聚焦认证和授权漏洞"
```

### CI/CD 集成（GitHub Actions）

将 Strix 添加到管道中，在拉取请求上运行安全测试：

```yaml
name: strix-penetration-test

on:
  pull_request:

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Strix
        run: pipx install strix-agent

      - name: Run Strix
        env:
          STRIX_LLM: ${{ secrets.STRIX_LLM }}
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
        run: strix -n -t ./
```

## 企业平台

托管平台提供：

- 执行仪表板
- 自定义微调模型
- CI/CD 集成
- 大规模扫描
- 第三方集成
- 企业支持

访问 [usestrix.com](https://usestrix.com) 获取演示。

## 安全架构

- **容器隔离**：所有测试在沙箱 Docker 环境中运行。
- **本地处理**：测试在本地运行，无数据发送到外部服务。

**警告**：仅测试您拥有或有权限测试的系统。您负责以道德和合法的方式使用 Strix。

## 贡献

欢迎社区贡献！请参阅 [贡献指南](https://github.com/usestrix/strix/blob/main/CONTRIBUTING.md)。

## 支持项目

喜欢 Strix？在 GitHub 上给我们 ⭐！

加入我们的社区：[Discord](https://discord.gg/YjKFvEZSdZ)
