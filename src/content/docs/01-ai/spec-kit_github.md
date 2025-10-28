
---
title: spec-kit
---

# GitHub 项目：spec-kit

## 项目地址
[https://github.com/github/spec-kit](https://github.com/github/spec-kit)

## 主要特性
- **规范工具集**：spec-kit 是一个由 GitHub 维护的开源工具包，主要用于生成和处理 OpenAPI（Swagger）规范文档，支持 YAML 和 JSON 格式的转换与验证。
- **轻量级设计**：基于 Ruby 语言开发，依赖最小化，便于集成到 CI/CD 管道中。
- **跨平台支持**：兼容多种操作系统，包括 macOS、Linux 和 Windows（通过 Ruby 环境）。
- **扩展性强**：提供插件机制，允许用户自定义规范生成和验证规则。

## 主要功能
- **规范生成**：从源代码或模板自动生成 OpenAPI 规范文件，支持 API 端点、参数和响应的标准化描述。
- **验证与 linting**：检查规范文件的语法错误、一致性和最佳实践，确保符合 OpenAPI 3.x 标准。
- **格式转换**：在 YAML 和 JSON 之间无缝转换规范文件，便于不同工具链的使用。
- **集成测试**：内置测试框架，用于验证 API 规范的完整性和准确性，支持与 RSpec 等测试工具结合。

## 用法
1. **安装**：
   - 确保已安装 Ruby（版本 2.5+）。
   - 通过 RubyGems 安装：`gem install spec-kit`。

2. **基本命令**：
   - 生成规范：`spec-kit generate --input api_source.rb --output spec.yaml`（从 Ruby 源生成 YAML 规范）。
   - 验证规范：`spec-kit validate spec.yaml`（检查 YAML 文件的合规性）。
   - 转换格式：`spec-kit convert spec.yaml --to json`（转换为 JSON）。

3. **高级用法**：
   - 配置插件：在 `~/.spec-kit/config.rb` 中添加自定义规则。
   - CI 集成：将命令集成到 GitHub Actions 或其他 CI 工具中，例如在 workflow 中运行 `spec-kit validate` 以自动化检查。
   - 示例：克隆仓库后，运行 `bundle install` 安装依赖，然后使用 `bin/spec-kit` 执行命令。

更多细节请参考仓库的 README 文件。