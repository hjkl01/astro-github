
---
title: SafeLine
---

# SafeLine 项目

## 项目地址
[GitHub 项目地址](https://github.com/chaitin/SafeLine)

## 主要特性
SafeLine 是由 Chaitin 团队开发的一款开源 Web 安全防护工具，主要用于检测和防御 Web 应用的安全漏洞。它基于 OWASP 标准，采用轻量级设计，支持实时监控和自动化防护。核心特性包括：
- **漏洞扫描**：自动识别常见 Web 漏洞，如 SQL 注入、XSS、CSRF 等。
- **WAF 防护**：内置 Web 应用防火墙（WAF），拦截恶意请求。
- **日志分析**：实时记录攻击事件，提供详细的日志和报告。
- **规则自定义**：支持用户自定义安全规则，适应不同应用场景。
- **高性能**：低资源占用，支持高并发环境部署。
- **开源免费**：基于 Apache 2.0 许可，社区驱动开发。

## 主要功能
- **防护功能**：实时过滤 HTTP/HTTPS 请求，阻挡 SQL 注入、路径遍历、命令注入等攻击。
- **扫描功能**：集成漏洞扫描器，可对 Web 应用进行全面安全评估。
- **监控与告警**：监控应用流量，异常时发送告警通知（如邮件或 Webhook）。
- **集成支持**：易于集成到 Nginx、Apache 等 Web 服务器，或作为独立代理使用。
- **报告生成**：生成安全报告，包括漏洞详情和修复建议。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/chaitin/SafeLine.git`
   - 进入目录：`cd SafeLine`
   - 安装依赖（假设使用 Python 环境）：`pip install -r requirements.txt`

2. **配置**：
   - 编辑 `config.yaml` 文件，设置防护规则、监听端口（如 80/443）和后端应用地址。
   - 示例配置：
     ```
     server:
       port: 8080
     backend:
       host: localhost
       port: 3000
     rules:
       enable_sql_injection: true
       enable_xss: true
     ```

3. **运行**：
   - 启动服务：`python main.py` 或使用 Docker：`docker build -t safeline . && docker run -p 8080:8080 safeline`
   - 配置 Web 服务器将流量代理到 SafeLine 端口。

4. **使用**：
   - 访问应用时，SafeLine 会自动拦截可疑请求。
   - 查看日志：`tail -f logs/safeline.log`
   - 自定义规则：通过 Web 界面（默认 http://localhost:8080/admin）或配置文件添加规则。
   - 停止服务：Ctrl+C 或 `docker stop <container_id>`。

详细文档请参考仓库的 README.md 文件。