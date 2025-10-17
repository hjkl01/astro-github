
---
title: mitmproxy
---

# mitmproxy 项目

**GitHub 项目地址:** [https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

## 主要特性
mitmproxy 是一个开源的交互式 HTTPS 代理工具，支持 TCP、HTTP 和 WebSocket 协议。它以强大的脚本化能力和用户友好的界面著称，主要特性包括：
- **交互式控制台和 Web 界面**：提供 mitmconsole（命令行界面）和 mitmweb（Web 界面），允许实时查看和修改流量。
- **脚本化支持**：使用 Python 脚本扩展功能，支持拦截、修改和重放请求/响应。
- **流量捕获与分析**：捕获所有网络流量，支持过滤、搜索和导出数据。
- **SSL/TLS 支持**：自动处理 HTTPS 解密，无需手动安装证书（通过 CA 证书实现）。
- **跨平台兼容**：支持 Linux、macOS 和 Windows。
- **轻量级和高效**：基于 Python 开发，资源占用低，适合开发和测试环境。

## 主要功能
- **代理流量**：作为中间人代理，拦截客户端与服务器间的通信，支持 HTTP/1.1、HTTP/2 和 WebSocket。
- **请求/响应修改**：实时编辑 HTTP 头、体、查询参数等，支持自动化脚本处理。
- **流量重放和回放**：记录流量并重复发送，用于测试和调试。
- **插件系统**：内置插件如流量过滤、导出为 HAR/JSON 格式，以及自定义 Python 扩展。
- **安全测试**：用于渗透测试、API 调试和网络安全分析，支持检测漏洞和模拟攻击。
- **自动化集成**：可与 CI/CD 管道集成，用于自动化测试。

## 用法
### 安装
1. 通过 pip 安装：`pip install mitmproxy`（推荐 Python 3.8+）。
2. 或使用 Homebrew（macOS）：`brew install mitmproxy`。
3. 详细安装指南见官方文档：[docs.mitmproxy.org](https://docs.mitmproxy.org/stable/overview-installation/)。

### 基本用法
1. **启动代理**：
   - 命令行模式：`mitmproxy`（默认监听 8080 端口）。
   - Web 界面：`mitmweb`（Web UI 在 http://localhost:8081）。
   - 指定端口：`mitmproxy --listen-port 8888`。

2. **配置客户端**：
   - 将浏览器或应用的代理设置为 `127.0.0.1:8080`。
   - 对于 HTTPS，安装 mitmproxy 的 CA 证书（自动生成在 `~/.mitmproxy/mitmproxy-ca-cert.pem`）。

3. **交互操作**：
   - 在 mitmconsole 中，使用键如 `e` 编辑请求、`k` 杀死连接、`w` 保存流量。
   - 通过 Web 界面点击查看、编辑流量，支持过滤（如 `~u example.com` 过滤 URL）。

4. **脚本化示例**：
   创建 `example.py`：
   ```python
   from mitmproxy import http

   def request(flow: http.HTTPFlow) -> None:
       if "example.com" in flow.request.pretty_url:
           flow.request.headers["X-Custom"] = "modified"
   ```
   运行：`mitmproxy -s example.py`。

5. **高级用法**：
   - 流量导出：`mitmdump -w output.flow`（二进制格式，后续用 `mitmdump -r output.flow` 重放）。
   - 帮助：运行 `mitmproxy --help` 或查阅文档。

更多细节请参考官方文档：[docs.mitmproxy.org](https://docs.mitmproxy.org/stable/)。