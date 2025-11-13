---
title: python-user-agents
---

# python-user-agents 项目

**项目地址:** [https://github.com/selwin/python-user-agents](https://github.com/selwin/python-user-agents)

## 主要特性
- **轻量级用户代理解析器**：基于纯Python实现，无需外部依赖，支持快速解析User-Agent字符串。
- **浏览器和设备检测**：准确识别浏览器类型（如Chrome、Firefox）、操作系统（如Windows、iOS）和设备类型（如移动设备、桌面）。
- **高性能**：使用正则表达式和高效算法，适合高并发场景。
- **开源免费**：MIT许可，易于集成到Web应用中。

## 主要功能
- **解析User-Agent**：从HTTP请求头中提取浏览器、OS、设备等信息。
- **多平台支持**：兼容主流浏览器和操作系统，包括移动端和智能设备。
- **版本检测**：支持浏览器和OS版本号的提取。
- **自定义扩展**：允许开发者添加自定义规则以支持新兴User-Agent。

## 用法
1. **安装**：
   ```
   pip install user-agents
   ```

2. **基本用法**（Python代码示例）：
   ```python
   from user_agents import parse

   user_agent_string = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

   ua = parse(user_agent_string)

   # 检查是否为移动设备
   print(ua.is_mobile)  # False

   # 获取浏览器信息
   print(ua.browser.family)  # 'Chrome'
   print(ua.browser.version_string)  # '91.0.4472.124'

   # 获取操作系统信息
   print(ua.os.family)  # 'Windows'
   print(ua.os.version_string)  # '10'

   # 获取设备类型
   print(ua.device.family)  # 'Other'
   ```

3. **高级用法**：
   - 在Django/Flask等框架中集成：直接从request.headers['User-Agent']解析。
   - 示例：在Django视图中：
     ```python
     from user_agents import parse

     def my_view(request):
         ua = parse(request.META.get('HTTP_USER_AGENT', ''))
         if ua.is_mobile:
             return render(request, 'mobile.html')
         else:
             return render(request, 'desktop.html')
     ```

更多细节请参考项目README文档。