---
title: copilot-cli
---


# GitHub Copilot CLI

**GitHub Copilot CLI** 是 GitHub 提供的一套命令行工具，能够让你在终端中使用 GitHub Copilot 生成代码、补全、参考文档等服务。它集成了 Copilot 的 API 能力，支持多语言和多操作系统。

## 项目地址
- GitHub: <https://github.com/github/copilot-cli>

## 主要特性

| 特性 | 说明 |
|------|------|
| **代码补全** | 输入命令行提示，CLI 会返回 AI 建议的代码片段。 |
| **多语言支持** | 目前已支持 JavaScript、Python、Go、Java、Rust 等主流语言。 |
| **自动提问** | 通过 `!ask` 或 `!review` 等命令，可以向 Copilot 提问或请求代码审阅。 |
| **上下文感知** | CLI 自动捕获当前工作目录和文件，将文件内容作为上下文发送。 |
| **简洁运行** | 可单独使用、也可与其他工具如 `snippets` 或 `fuzzy finder` 集成。 |
| **可扩展插件** | 通过 `copilot` 命令可以安装和管理插件，扩展功能。 |
| **跨平台** | 支持 macOS、Linux、Windows（WSL/PowerShell）等。 |

## 安装方式

> ⚠️ 目前需要 **GitHub 账户** 并关联 **Copilot 订阅**（或试用阶段）才能使用。

### macOS / Linux (Homebrew / apt / yum)

```bash
brew install github/copilot-cli/copilot
# 或者
curl -fsSL https://raw.githubusercontent.com/github/copilot-cli/main/install.sh | sh
```

### Windows (Scoop)

```powershell
scoop bucket add github https://github.com/github/copilot-cli.git
scoop install copilot
```

### 直接下载安装包

1. 前往 [Releases](https://github.com/github/copilot-cli/releases) 页面，下载适合你系统的 `copilot-linux-x64`、`copilot-darwin-x64` 或 `copilot-windows-x64.exe`。
2. 解压后将可执行文件放入 `PATH` 所在目录。

## 配置

```bash
# 登录 GitHub 并提供访问令牌
copilot login
# 设置默认语言（可选）
copilot config set default-language python
```

## 常用令

| 命令 | 作用 | 例子 |
|------|------|------|
| `copilot generate` | 根据提示生成代码 | `copilot generate -p "Create a REST API endpoint in Go"` |
| `copilot continue` | 接续上一条生成的代码 | `copilot continue` |
| `copilot ask` | 向 Copilot 提问 | `copilot ask -p "How to handle errors in Rust?"` |
| `copilot review` | 审核代码片段 | `copilot review <filename>` |
| `copilot plugins list` | 列出已安装插件 | `copilot plugins list` |
| `copilot plugins install <plugin_name>` | 安装插件 | `copilot plugins install my-plugin` |
| `copilot plugins uninstall <plugin_name>` | 卸载插件 | `copilot plugins uninstall my-plugin` |

> 通过 `--help` 可以查看更多选项：`copilot generate --help`

## 示例

```bash
# 在当前项目的某个文件中，继续写代码
copilot continue

# 生成一个爬虫脚本
copilot generate -p "Write a Python script using requests to fetch JSON data from https://api.github.com"

# 给定一段代码，向 Copilot 询问改进建议
echo "def foo(x): return x + 1" > foo.py
copilot review foo.py
```

## 常见问题

- **如何保证生成的代码不泄露敏感信息？**  
  Copilot 只使用提交到 GitHub 的公开代码以及你在命令行中给定的上下文，绝不会自动上传或共享你的本地文件。

- **如何在 Docker 容器中使用 Copilot CLI？**  
  只需在容器内安装 Copilot 并 `copilot login`，因为 Docker 共享的 `HOME` 目录中会存储令牌。

- **为什么命令执行很慢？**  
  网络延迟或 GitHub 访问限制导致 API 响应慢。可在配置中调节 `timeout` 或使用国内镜像 (如 `cdn.jsdelivr.net`) 替代。

## 相关资源

- 官方文档: <https://docs.github.com/en/copilot/overview>  
- Issues & Discussions: <https://github.com/github/copilot-cli/issues>  
- 贡献指南: <https://github.com/github/copilot-cli/blob/main/CONTRIBUTING.md>
```
