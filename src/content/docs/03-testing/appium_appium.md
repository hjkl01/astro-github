
---
title: appium
---

# Appium – 开源移动自动化框架

**项目地址**: <https://github.com/appium/appium>

---

## 1. 项目简介
Appium 是一款完全开放源代码、无侵入性的移动自动化框架，支持 iOS、Android、Windows 和 macOS 应用的自动化测试。它遵循 WebDriver（Selenium）协议，允许使用多种编程语言编写测试脚本，真正实现“一套测试脚本，多端可用”。

---

## 2. 主要特性
| 特色 | 说明 |
| --- | --- |
| **跨平台** | 同一套测试脚本即可在 iOS、Android、Windows、macOS 上运行。 |
| **无侵入性** | 通过 native 框架（XCUITest、UIAutomator、Espresso 等）驱动设备，不需要修改或签名应用。 |
| **多语言客户端** | 官方支持 Java、Python、JavaScript、Ruby、C#, Kotlin 等多种语言。 |
| **WebDriver 兼容** | 使用标准 HTTP 接口，兼容 Selenium/WebDriver 官方 API。 |
| **可扩展插件** | 支持多种插件，例如 Appium Desktop、Appium Doctor、Appium Inspector 等。 |
| **多种驱动** | iOS (XCUITest, UIAutomation), Android (UIAutomator, Espresso, Selendroid, Appium automation), Windows (WinAppDriver), macOS (XCUITest). |

---

## 3. 核心功能

### 3.1 自动化测试服务器  
- 监听 HTTP 请求，解析 `DesiredCapabilities` 并启动对应设备会话。  
- 支持多线程并发会话。  

### 3.2 元素定位与交互  
- 支持传统 WebDriver 定位：id、xpath、cssSelector、className、tag name、linkText。  
- 通过 `accessibility id`、`uiautomator`、`xpath` 等定位 iOS/Android 元素。  
- 支持多种动作：tap、swipe、drag、pinch、键盘输入、滚动。  

### 3.3 日志与截图  
- 可在测试过程中获取设备日志、性能度量。  
- 支持随时截屏、录屏。  

### 3.4 集成与 CI/CD  
- 通过 Node, Python 或 Java 直接与 Jenkins、GitHub Actions 等 CI 系统集成。  
- 提供 `appium-doctor` 用于检查环境完整性。  

---

## 4. 支持平台

| 平台 | 驱动 | 关键技术 |
| --- | --- | --- |
| iOS | XCUITest（iOS 9+）, UIAutomation（iOS 7-8） | Xcode, Instruments |
| Android | UIAutomator2, Espresso, Selendroid (legacy) | Android SDK |
| Windows | WinAppDriver | UI Automation |
| macOS | XCUITest | Xcode |

---

## 5. 开始使用

### 5.1 安装 Appium（Node 版）
```bash
# 全局安装
npm install -g appium

# 检查环境完整性
appium-doctor
```

### 5.2 启动 Appium 服务器
```bash
# 默认端口 4723
appium
# 或自定义端口
appium --port 5555
```

### 5.3 配置 `DesiredCapabilities`
```json
{
  "platformName": "iOS",
  "platformVersion": "14.4",
  "deviceName": "iPhone 13",
  "app": "/path/to/YourApp.app",
  "automationName": "XCUITest",
  "udid": "00008030-001C497E0040002E"
}
```

### 5.4 运行测试脚本（Java 例子）
```java
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.remote.MobileCapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.URL;

public class ExampleTest {
  public static void main(String[] args) throws Exception {
    DesiredCapabilities caps = new DesiredCapabilities();
    caps.setCapability(MobileCapabilityType.PLATFORM_NAME, "iOS");
    caps.setCapability(MobileCapabilityType.PLATFORM_VERSION, "14.4");
    caps.setCapability(MobileCapabilityType.DEVICE_NAME, "iPhone 13");
    caps.setCapability(MobileCapabilityType.APP, "/path/to/App.app");

    AppiumDriver<MobileElement> driver = new AppiumDriver<>(
        new URL("http://127.0.0.1:4723/wd/hub"), caps);

    // 简单交互
    MobileElement button = driver.findElementByAccessibilityId("loginButton");
    button.click();

    driver.quit();
  }
}
```

---

## 6. 示例代码（Python 版）

```python
from appium import webdriver

caps = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "Android Emulator",
    "appPackage": "com.example.myapp",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 操作
driver.find_element_by_accessibility_id("login").click()

driver.quit()
```

---

## 7. 相关工具与资源

- **Appium Desktop** – 图形化界面，查看网络流、元素、截图。  
- **Appium Inspector** – 通过 Chrome DevTools / Safari 进行元素检查。  
- **Appium Doctor** – 快速检测本地环境是否满足运行需求。  
- **社区插件** – e.g. `appium-webdriverio`, `react-native-testing-library` 等。

---