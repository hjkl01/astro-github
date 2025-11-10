---
title: chrome-extensions-samples
---


# chrome-extensions-samples

项目地址: https://github.com/GoogleChrome/chrome-extensions-samples

## 项目简介  
GoogleChrome 提供的一组 Chrome 扩展示例代码库，旨在帮助开发者快速了解并掌握 Chrome 扩展的各种 API 与最佳实践。

## 主要特性与功能  

| 类别 | 示例标题 | 关键点 | 说明 |
|------|----------|--------|------|
| **内容脚本** | `content-script` | 自动跑脚本、注入 CSS | 展示如何在页面中注入脚本与样式 |
| **背景脚本** | `background` | 长期运行、事件驱动 说明 Service Worker、事件驱动等背景脚本机制 |
| **弹出页/页面** | `popup`, `options_page` | 交互 UI、存储 | 通过 UI 与用户交互并使用 `chrome.storage` |
| **权限与 API** | `permissions`, `content_security_policy` | 动态权限、CSP | 动态请求权限，演示 CSP 配置方法 |
| **消息传递** | `communication`, `backgroundMessage` | 发送/接收消息 | 演示页面与背景脚本、内容脚本的双向通信 |
| **omniBox** | `omnibox` | 地址栏输入 | 通过地址栏实现自定义搜索或命令 |
| **主机权限** | `read_write` | 访问文件/存储 | 访问浏览器内存表或本地文件系统 |
| **跨域请求** | `webRequest` | 拦截/修改请求 | 示例如何拦截网络请求并修改响应 |
| **国际化** | `i18n` | 多语言支持 | 展示通过 `__MSG_...__` 进行国际化 |
| **打包与发布** | `packaging` | 打包工具 | 如何使用 `web-ext` 或 `chrome-cli` 打包扩展 |

## 典型用例

- **背景脚本**  
  ```js
  // 在 background.js 中监听事件
  chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
      if (msg.type === 'GET_TIME') {
          sendResponse({time: Date.now()});
      }
  });
  ```

- **内容脚本**  
  ```js
  // contentScript.js
  document.body.style.backgroundColor = '#ffeb3b';
  ```

- **权限请求**  
  ```json
  // manifest.json
  {
      "permissions": ["storage", "https://*/*"],
      "host_permissions": ["https://api.example.com/*"]
  }
  ```

## 如何使用

1. **克隆代码库**  
   ```bash
   git clone https://github.com/GoogleChrome/chrome-extensions-samples.git
   cd chrome-extensions-samples
   ```

2. **加载扩展**  
   - 打开 `chrome://extensions/`  
   - 开启“开发者模式”  
   - 选择“加载已解压的扩展程序”，并定位到任意子目录（如 `popup/`）

3. **运行示例**  
   - 每个子目录包含独立的 `manifest.json`，可单独运行。  
   - 对于需要多页面交互的示例，打开相应页面并观察控制台或 UI 交互。

4. **学习与改造**  
   - 阅读 `manifest.json` 与源码，了解各 API 的使用方式。  
   - 修改代码后，刷新扩展页面即可看到效果。

## 备注  

- 所有示例均遵循 Chrome 官方扩展开发规范，适合作为学习与参考。  
- 您可以根据自己的项目需求，将示例代码迁移或组合在自己的扩展项目中。  

祝开发愉快！  

```   ```

