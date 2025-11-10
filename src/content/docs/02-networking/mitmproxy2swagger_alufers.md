---
title: mitmproxy2swagger
---

# mitmproxy2swagger 项目

## 项目地址
[https://github.com/alufers/mitmproxy2swagger](https://github.com/alufers/mitmproxy2swagger)

## 主要特性
- **自动生成 OpenAPI/Swagger 规范**：通过拦截 HTTP/HTTPS 流量，自动捕获 API 请求和响应，生成符合 OpenAPI 2.0 (Swagger 2) 规范的 JSON 或 YAML 文件。
- **支持 mitmproxy 集成**：作为 mitmproxy 的插件运行，无缝集成到代理流程中，支持实时流量分析和规范生成。
- **智能推断 API 结构**：自动识别路径、方法（GET、POST 等）、参数、请求体、响应体和状态码，支持 JSON、XML 等常见格式的推断。
- **自定义配置**：允许用户配置过滤规则、忽略特定流量、自定义描述和标签，便于生成更精确的 API 文档。
- **轻量级和易扩展**：基于 Python 开发，易于修改和扩展，支持命令行和脚本化使用。

## 主要功能
- **流量捕获与规范生成**：在 mitmproxy 中运行插件，捕获 API 调用后，一键导出 Swagger 规范文件，用于 API 文档化或测试。
- **API 端点发现**：自动发现和组织 API 端点，支持分组和标签化，便于大型项目的文档管理。
- **响应验证**：生成规范时包括示例响应，帮助验证 API 行为和错误处理。
- **导出与集成**：支持直接导出到文件，或集成到 CI/CD 流程中自动化生成文档。
- **隐私与安全**：仅处理本地代理流量，不上传数据，确保敏感信息的安全。

## 用法
1. **安装**：
   - 确保已安装 mitmproxy（`pip install mitmproxy`）。
   - 克隆仓库：`git clone https://github.com/alufers/mitmproxy2swagger.git`。
   - 进入目录：`cd mitmproxy2swagger`。

2. **运行 mitmproxy 与插件**：
   - 使用命令启动 mitmproxy 并加载插件：`mitmproxy -s mitmproxy2swagger.py`。
   - 配置浏览器或应用使用 mitmproxy 作为代理（默认端口 8080），并安装 mitmproxy CA 证书以支持 HTTPS。

3. **捕获流量**：
   - 通过代理访问目标 API，插件会自动记录请求/响应。
   - 在 mitmproxy 界面（按 `?` 查看帮助）中，按 `w` 键写入生成的 Swagger 文件（默认输出到当前目录的 `swagger.json`）。

4. **自定义选项**：
   - 编辑 `mitmproxy2swagger.py` 中的配置，如 `output_file`（输出文件名）、`filter`（流量过滤规则，例如只捕获特定主机）。
   - 示例：运行时添加脚本选项 `mitmproxy -s mitmproxy2swagger.py -O swagger.yaml` 以输出 YAML 格式。

5. **高级用法**：
   - 集成到脚本：编写 Python 脚本来自动化运行，例如结合 `mitmdump` 用于批量测试。
   - 生成后，使用 Swagger UI 或 Editor 查看和编辑规范文件。

更多细节请参考仓库的 README.md 文件。