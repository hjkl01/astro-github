---
title: selenium-wire
---

# Selenium Wire 项目

## 项目地址
[GitHub 项目地址](https://github.com/wkeeling/selenium-wire)

## 主要特性
Selenium Wire 是一个基于 Selenium 的 Python 库扩展，它允许用户在运行 Selenium WebDriver 时拦截和修改 HTTP 请求和响应。主要特性包括：
- **请求拦截**：捕获和修改浏览器发出的所有 HTTP/HTTPS 请求。
- **响应修改**：拦截并更改服务器返回的响应内容。
- **代理集成**：内置代理服务器，支持 MITM（中间人）攻击以解密 HTTPS 流量。
- **认证支持**：处理 HTTP 基本认证和自定义认证。
- **无痕模式**：支持 headless 浏览器模式下的网络捕获。
- **兼容性**：与 Selenium 4 及以上版本兼容，支持多种浏览器如 Chrome、Firefox 等。

## 主要功能
- **网络流量监控**：实时查看和记录所有网络请求，包括 headers、body 和元数据。
- **请求/响应编辑**：在请求发送前或响应接收后动态修改内容，例如注入脚本或更改数据。
- **HTTPS 解密**：自动处理 SSL/TLS 证书以捕获加密流量。
- **自定义规则**：基于 URL 或其他条件应用过滤和修改规则。
- **调试工具**：提供详细的日志和调试信息，便于 web 应用测试和自动化脚本开发。

## 用法
### 安装
```bash
pip install selenium-wire
```

### 基本用法
1. **导入和初始化**：
   ```python
   from seleniumwire import webdriver

   # 创建 WebDriver 实例（使用 Chrome 示例）
   driver = webdriver.Chrome()
   ```

2. **访问页面并捕获请求**：
   ```python
   driver.get("https://example.com")

   # 访问所有捕获的请求
   for request in driver.requests:
       print(f"URL: {request.url}")
       print(f"Method: {request.method}")
       print(f"Response: {request.response.body.decode() if request.response else 'No response'}")
   ```

3. **修改请求**：
   ```python
   def interceptor(request):
       if 'example.com' in request.url:
           del request.headers['User-Agent']  # 修改 headers

   driver.request_interceptor = interceptor
   driver.get("https://example.com")
   ```

4. **修改响应**：
   ```python
   def response_interceptor(request, response):
       if 'example.com' in request.url:
           response.body = b"Modified response body"

   driver.response_interceptor = response_interceptor
   ```

### 注意事项
- 需要安装浏览器驱动（如 chromedriver）。
- 对于 HTTPS，首次运行可能需要安装 Selenium Wire 的 CA 证书。
- 适用于自动化测试、爬虫和 web 调试场景。更多细节请参考项目文档。