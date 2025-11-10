# Strix by usestrix

## 功能

Strix 是一个开源的 AI 黑客工具，用于安全测试应用程序。它使用自主 AI 代理模拟真实黑客的行为，动态运行代码、发现漏洞并通过实际的 PoC（Proof of Concept）验证漏洞。与静态分析工具不同，Strix 提供真实的验证，避免误报。

### 主要特性

- **完整的黑客工具包**：包括 HTTP 代理、浏览器自动化、终端环境、Python 运行时、侦察、代码分析和知识管理。
- **全面的漏洞检测**：覆盖访问控制、注入攻击、服务端漏洞、客户端漏洞、业务逻辑、认证和基础设施漏洞。
- **代理图**：分布式工作流，代理协作并扩展测试。
- **开发者友好**：CLI 工具，提供可操作的报告，支持自动修复和报告。
- **CI/CD 集成**：与 GitHub Actions 集成，在拉取请求中自动扫描漏洞。

### 用例

- 检测和验证应用程序中的关键漏洞。
- 在数小时内完成渗透测试，并生成合规报告。
- 自动化漏洞赏金研究并生成 PoC。
- 在 CI/CD 中运行测试，阻止漏洞进入生产环境。

## 用法

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
export LLM_API_BASE="your-api-base-url"  # 用于本地模型，如 Ollama 或 LMStudio
export PERPLEXITY_API_KEY="your-api-key"  # 用于搜索功能
```

### 运行安全评估

```bash
strix --target ./app-directory
```

首次运行会拉取沙箱 Docker 镜像。结果保存在 `agent_runs/<run-name>` 下。

### 示例用法

- 本地代码库分析：`strix --target ./app-directory`
- 仓库安全审查：`strix --target https://github.com/org/repo`
- Web 应用程序评估：`strix --target https://your-app.com`
- 多目标白盒测试：`strix -t https://github.com/org/app -t https://your-app.com`
- 带指令的聚焦测试：`strix --target api.your-app.com --instruction "优先测试认证和授权"`
- 带凭据的测试：`strix --target https://your-app.com --instruction "使用凭据测试：testuser/testpass。重点关注权限提升和访问控制绕过"`

### 无头模式

使用 `-n/--non-interactive` 标志以编程方式运行，无交互 UI。适用于服务器和自动化作业。

```bash
strix -n --target https://your-app.com --instruction "重点关注认证和授权漏洞"
```

### CI/CD 集成（GitHub Actions）

在拉取请求中运行安全测试：

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

### 云托管版本

如果不想设置本地环境，可以使用云托管版本：[usestrix.com](https://usestrix.com)

### 安全架构

- **容器隔离**：所有测试在沙箱 Docker 环境中运行。
- **本地处理**：测试在本地运行，不发送数据到外部服务。

**警告**：仅测试您拥有或有权限测试的系统。您负责以道德和合法的方式使用 Strix。
