---
title: proxy-list
---

# GitHub 项目：Proxy List

**项目地址：** [https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt](https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt)

## 主要特性
- **代理列表收集**：该项目维护了一个免费的代理服务器列表，包含来自全球各种来源的HTTP、HTTPS、SOCKS4和SOCKS5代理。
- **实时更新**：列表通过自动化脚本定期更新，确保代理的时效性和可用性。
- **原始格式**：提供纯文本格式（raw.txt），易于解析和集成到其他工具中。
- **开源免费**：基于GitHub托管，完全开源，用户可自由下载和使用。

## 主要功能
- **代理发现**：帮助用户快速获取大量代理IP地址，用于网络匿名、爬虫、绕过地域限制等场景。
- **列表过滤**：虽然原始列表未过滤，但用户可根据IP、端口、类型等自行筛选可用代理。
- **集成支持**：适用于开发脚本、浏览器扩展或自动化工具，直接读取txt文件作为代理源。

## 用法
1. **下载列表**：访问项目地址，直接下载 `proxy-list-raw.txt` 文件，文件内容为每行一个代理格式（如 `IP:端口 类型`）。
2. **解析使用**：使用编程语言（如Python）读取文件，例如：
   ```python
   with open('proxy-list-raw.txt', 'r') as f:
       proxies = [line.strip() for line in f if line.strip()]
   ```
3. **测试代理**：结合工具（如curl或自定义脚本）测试代理可用性，例如 `curl -x http://IP:端口 http://example.com`。
4. **集成应用**：在浏览器或软件中导入代理列表，实现轮换使用以提高稳定性。注意：代理可能不稳定，建议定期更新列表。