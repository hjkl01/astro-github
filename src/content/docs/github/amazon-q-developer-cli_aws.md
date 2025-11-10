---
title: amazon-q-developer-cli
---


# Amazon Q Developer CLI

**项目地址**  
<https://github.com/aws/amazon-q-developer-cli>

## 概述  
Amazon Q Developer CLI 是一套命令行工具，帮助开发者将 Amazon Q（基于 AI 的代码生成与完善助手）无缝集成到本地开发流程，支持代码生成、代码审查、查询历史记录及插件化扩展。

## 主要功能  
- **代码生成**：基于自然语言描述直接生成 Java、Python、TypeScript 等语言的完整代码段。  
- **代码完善**：对已有代码块进行补全、重构或优化。  
- **查询历史**：检索本地会话历史和已生成的代码片段。  
- **插件系统**：以插件形式加入自定义命令或与 IDE、CI/CD 集成。  
- **自定义提示**：通过配置文件设置默认提示词、上下文和编码风格。  
- **多语言支持**：内置多种编程语言模板，支持自动切换。  
- **安全与合规**：支持对生成代码进行自动安全扫描，符合 AWS 安全最佳实践。

## 用法

### 1. 安装  
```bash
# 从 Homebrew（macOS/Linux）安装
brew tap aws/tap
brew install amazon-q-developer-cli
```
或手动下载二进制文件后解压至 PATH。

### 2. 初始化项目  
```bash
qdev init
```
会检测当前目录的语言环境，并生成qdev-config.yaml` 配置文件。

### 3. 生成代码  
```bash
# 生成一个用户模型类
qdev generate "Create a User model with fields id, name, email in Java"

# 生成函数实现
qdev complete "Implement a REST endpoint to fetch user details"
```

### 4. 检索历史  
```bash
qdev history list
qdev history view <id>
```

### 5. 使用插件  
```bash
# 安装官方插件
qdev plugin install qdev-plugin-aws-lambda

# 使用插件命令
qdev lambda deploy --function myFunc
```

### 6. 自定义提示  
在 `qdev-config.yaml` 中添加：
```yaml
prompts:
  default:
    description: "Generate code following AWS best practices"
```
使用 `qdev generate --prompt default "..."` 即可调用。

### 7. 与 IDE 集成  
支持 VS Code 插件 `amazon.q-developer`，可在编辑器内直接触发命令。

## 常见命令速查  

| 命令 | 说明 |
|------|------|
| `qdev generate <prompt>` | 生成新代码 |
| `qdev complete <prompt>` | 完成/重构已有代码 |
| `qdev history list` | 列出已生成记录 |
| `qdev history view <id>` | 查看单条记录详情 |
| `qdev plugin list` | 列出已安装插件 |
| `qdev plugin install <name>` | 安装插件 |
| `qdev plugin remove <name>` | 移除插件 |

---  
> **提示**：使用 `qdev --help` 查看所有可用选项与示例。