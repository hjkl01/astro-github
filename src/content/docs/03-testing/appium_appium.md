---
title: appium
---

# Appium 项目

**GitHub 项目地址:** [https://github.com/appium/appium](https://github.com/appium/appium)

## 主要特性

Appium 是一个开源的跨平台自动化测试框架，专为原生、混合、移动 web 和桌面应用设计。它基于 W3C WebDriver 协议构建，提供模块化和可扩展的架构，支持多种编程语言，并拥有庞大的生态系统。主要特性包括：

- **跨平台支持**：兼容 iOS、Android、macOS、Windows 和其他平台
- **无需重新编译**：使用标准自动化 API，无需修改应用代码
- **多语言客户端**：支持 Java、Python、Ruby、.NET C# 等编程语言
- **WebDriver 协议**：基于 W3C 标准，确保测试的稳定性和兼容性
- **模块化设计**：通过驱动和插件扩展功能，支持特定平台自动化
- **云端集成**：支持本地和云端测试环境

## 主要功能

Appium 的核心功能聚焦于跨平台应用的自动化测试：

- **原生应用测试**：直接测试原生移动和桌面应用
- **混合应用测试**：支持混合应用的自动化
- **移动 web 测试**：在移动浏览器中进行 web 应用测试
- **桌面应用测试**：自动化桌面应用测试
- **API 测试**：通过客户端库进行 API 级别的测试
- **并行测试**：支持多个会话和并行执行

## 用法

### 安装

1. 确保 Node.js 版本 ≥ 14，并安装 npm。
2. 全局安装 Appium：
   ```
   npm install -g appium
   ```
   注意：这仅安装核心服务器，需要安装驱动来自动化特定平台。

### 驱动安装

Appium 通过驱动支持不同平台，使用扩展 CLI 管理驱动：

```bash
# 安装官方驱动（如 UiAutomator2 for Android）
appium driver install uiautomator2

# 安装 XCUITest 驱动 for iOS
appium driver install xcuitest

# 查看已安装驱动
appium driver list --installed
```

### 客户端库

选择编程语言的客户端库（如 Java）：

```xml
<!-- Maven -->
<dependency>
    <groupId>io.appium</groupId>
    <artifactId>java-client</artifactId>
    <version>9.0.0</version>
</dependency>
```

### 启动服务器

```bash
# 启动 Appium 服务器
appium server

# 指定主机和端口
appium --address 127.0.0.1 --port 4723
```

### 编写测试

```java
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

public class AppiumTest {
    public static void main(String[] args) {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("platformName", "Android");
        caps.setCapability("deviceName", "emulator-5554");
        caps.setCapability("app", "/path/to/app.apk");

        AppiumDriver<MobileElement> driver = new AndroidDriver<>(new URL("http://127.0.0.1:4723/wd/hub"), caps);

        // 测试代码
        MobileElement element = driver.findElementById("elementId");
        element.click();

        driver.quit();
    }
}
```

更多详情请参考官方文档：https://appium.io/docs/en/latest/
