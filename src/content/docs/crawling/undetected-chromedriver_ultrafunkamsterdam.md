
---
title: undetected-chromedriver
---

# undetected-chromedriver 项目

## 项目地址
[GitHub 项目地址](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

## 主要特性
- **反检测机制**：该项目是一个修改版的 Selenium WebDriver，专为 Chrome 浏览器设计，能够有效规避网站的反自动化检测（如 Cloudflare、Akamai 等），让自动化脚本看起来像真实用户操作。
- **隐秘性强**：通过修改 Chrome 的 DevTools 协议、WebDriver 属性和浏览器指纹，隐藏自动化痕迹，避免被网站识别为机器人。
- **兼容性好**：支持多种 Python 环境和 Chrome 版本，易于集成到现有的 Selenium 项目中。
- **轻量级**：无需额外安装 Chrome 扩展或复杂配置，保持原生 Selenium 的简洁性。
- **开源免费**：基于 MIT 许可，社区活跃，支持自定义修改。

## 主要功能
- **自动化浏览器控制**：像标准 Selenium 一样，支持网页导航、元素交互、表单提交等自动化任务，但更注重隐蔽性。
- **自动更新驱动**：内置机制可自动下载匹配当前 Chrome 版本的 WebDriver，避免手动更新。
- **浏览器指纹伪装**：修改 navigator、screen 等属性，使浏览器行为更接近真实用户。
- **异常处理**：提供更好的错误处理，针对检测失败时的重试和调试支持。
- **多平台支持**：兼容 Windows、macOS 和 Linux 系统。

## 用法
1. **安装**：
   - 通过 pip 安装：`pip install undetected-chromedriver`
   - 确保已安装 Selenium：`pip install selenium`

2. **基本用法示例**（Python 代码）：
   ```python
   import undetected_chromedriver as uc
   from selenium.webdriver.common.by import By

   # 创建隐秘的 Chrome 驱动
   driver = uc.Chrome(use_subprocess=True)  # use_subprocess=True 可进一步增强隐秘性

   # 导航到目标网页
   driver.get("https://example.com")

   # 进行自动化操作，例如查找元素
   element = driver.find_element(By.ID, "some-id")
   element.click()

   # 关闭驱动
   driver.quit()
   ```

3. **高级配置**：
   - 指定 Chrome 路径：`driver = uc.Chrome(executable_path='/path/to/chrome')`
   - 使用 headless 模式：`options = uc.ChromeOptions(); options.add_argument('--headless'); driver = uc.Chrome(options=options)`
   - 更多选项参考官方文档，适用于爬虫、测试自动化等场景。

注意：使用时遵守网站服务条款，避免滥用。