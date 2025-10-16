
---
title: judge0
---

# Judge0 项目

## 项目地址
[https://github.com/judge0/judge0](https://github.com/judge0/judge0)

## 主要特性
Judge0 是一个开源的在线代码执行引擎和 API，支持多种编程语言的代码编译、执行和评估。它设计用于构建代码评估系统、在线 IDE 或自动化测试平台。主要特性包括：
- **多语言支持**：内置 70+ 种编程语言和框架，如 C、C++、Java、Python、JavaScript、Ruby 等，可轻松扩展。
- **API 驱动**：提供 RESTful API 接口，便于集成到 Web 应用或服务中，支持 JSON 和 XML 格式。
- **隔离执行**：使用 Docker 容器化执行代码，确保安全隔离，防止恶意代码影响系统。
- **实时反馈**：返回执行结果、输出、错误信息、时间和内存使用统计，支持自定义超时和输入。
- **开源与可扩展**：基于 MIT 许可，完全开源，支持自托管部署，并可自定义语言支持。
- **高性能**：优化了执行效率，支持并行处理多个提交。

## 主要功能
- **代码提交与执行**：通过 API 提交源代码、语言 ID、输入数据，引擎自动编译并执行，返回结果。
- **结果检索**：使用提交的 token 查询执行状态和输出，支持轮询或 Webhook 通知。
- **错误处理**：详细报告编译错误、运行时异常和资源限制违规。
- **批量处理**：支持创建、批量执行和批量检索作业。
- **配置选项**：可设置输入/输出限制、额外参数（如优化级别），并集成认证机制。
- **Web 界面**：提供简单的 Web UI 用于测试 API，但核心是后端服务。

## 用法
### 部署
1. **前提**：安装 Docker 和 Docker Compose（推荐），或使用 Ruby on Rails 环境。
2. **克隆仓库**：
   ```
   git clone https://github.com/judge0/judge0.git
   cd judge0
   ```
3. **使用 Docker Compose 启动**（开发模式）：
   ```
   docker-compose up -d
   ```
   这将启动 API 服务（端口 3000）和 Web UI（端口 3001）。
4. **生产部署**：配置环境变量（如数据库、Redis），使用 Kubernetes 或云服务部署。详细见 [部署文档](https://ce.judge0.com)。

### API 用法示例
API 基地址：`http://localhost:3000`（默认）。

- **提交代码执行**（POST /submissions）：
  使用 curl 或 HTTP 客户端发送 JSON：
  ```
  curl -X POST "http://localhost:3000/submissions?base64_encoded=true&fields=*"
  -H "Content-Type: application/json"
  -d '{
    "source_code": "base64编码的源代码",
    "language_id": 71,  // Python 示例
    "stdin": "base64编码的输入",
    "expected_output": null
  }'
  ```
  返回 JSON 包含 `token` 用于检索结果。

- **检索结果**（GET /submissions/{token}）：
  ```
  curl "http://localhost:3000/submissions/{token}?base64_encoded=true&fields=*"
  ```
  返回执行输出、时间、内存等。

更多细节参考 [API 文档](https://ce.judge0.com)。项目适合教育、竞赛或 CI/CD 集成。