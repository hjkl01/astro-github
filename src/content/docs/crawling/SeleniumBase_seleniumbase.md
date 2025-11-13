---
title: SeleniumBase
---

# SeleniumBase 项目

## 项目地址
[GitHub 项目地址](https://github.com/seleniumbase/SeleniumBase)

## 主要特性
SeleniumBase 是一个开源的 Python 框架，基于 Selenium WebDriver 构建，旨在简化浏览器自动化测试和网络爬虫任务。它提供了丰富的内置功能，使测试编写更高效、更可靠。主要特性包括：

- **内置浏览器驱动管理**：自动下载和管理 Chrome、Firefox 等浏览器的驱动程序，无需手动配置。
- **页面对象模型 (POM) 支持**：简化页面元素定位和交互，提供 SB (SeleniumBase) 语法来编写更简洁的测试代码。
- **内置测试报告和截图**：自动生成 HTML 测试报告，支持失败时截图和视频录制，便于调试。
- **跨浏览器和跨平台支持**：兼容多种浏览器（如 Chrome、Firefox、Edge）和操作系统（Windows、macOS、Linux）。
- **集成 pytest**：无缝集成 pytest 测试框架，支持并行测试、参数化测试和插件扩展。
- **网络爬虫和数据提取**：内置工具用于处理 JavaScript 渲染页面、API 调用和数据验证。
- **安全性与合规**：支持隐身模式、代理配置和无头浏览器模式，适用于 CI/CD 管道。
- **额外功能**：包括 PDF 处理、邮件发送、数据库集成和视觉测试（使用 OCR 和图像比较）。

## 主要功能
SeleniumBase 的核心功能聚焦于自动化测试和浏览器交互，涵盖以下方面：

- **自动化测试**：编写端到端 (E2E) 测试脚本，模拟用户行为如点击、输入、导航和表单提交。
- **网络自动化**：处理动态网页、AJAX 请求和单页应用 (SPA)，支持等待元素加载和断言验证。
- **数据驱动测试**：从 CSV、JSON 或数据库加载测试数据，支持参数化执行。
- **移动端模拟**：通过 Chrome DevTools 模拟移动设备浏览器。
- **API 测试集成**：结合 Requests 库进行后端 API 测试，与前端自动化结合。
- **性能监控**：内置 PageSpeed Insights 集成，用于页面加载性能测试。
- **多语言支持**：核心基于 Python，但提供 JS 示例和多语言文档。

## 用法
SeleniumBase 的使用非常简单，首先通过 pip 安装：

```bash
pip install seleniumbase
```

### 基本用法示例
1. **编写测试脚本**（保存为 `test_example.py`）：
   ```python
   from seleniumbase import BaseCase

   class MyTestClass(BaseCase):
       def test_google_search(self):
           self.open("https://www.google.com")
           self.type("#AP1", "SeleniumBase\n")  # 输入搜索关键词
           self.assert_text("SeleniumBase", "#search")  # 验证结果
           self.save_screenshot("search_result.png")  # 保存截图
   ```

2. **运行测试**：
   ```bash
   pytest test_example.py --browser=chrome
   ```
   - `--browser=chrome` 指定浏览器。
   - `--headless` 运行无头模式。
   - `--demo` 启用演示模式（慢速执行，便于观察）。

3. **高级用法**：
   - **页面对象**：创建自定义页面类继承 `BaseCase`，封装元素和方法。
   - **命令行选项**：使用 `sb manage` 命令管理驱动，或 `pytest` 与插件如 `html-report` 生成报告。
   - **集成 CI/CD**：在 Jenkins 或 GitHub Actions 中运行，支持 Docker 容器化。

更多详情请参考项目文档：https://github.com/seleniumbase/SeleniumBase/wiki