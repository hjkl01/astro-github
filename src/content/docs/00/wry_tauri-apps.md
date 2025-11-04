
---
title: wry
---


# wry - Tauri 的 WebView 引擎**项目地址**: https://github.com/tauri-apps/wry

## 主要特性

- **跨平台 WebView**：支持 Windows、macOS、Linux（X11/Wayland）等主流桌面操作系统。
- **安全性**：利用 Chromium 作为渲染引擎，提供 sandbox 与 CSP 相关功能，允许细粒度权限控制。
- **性能优越**：内置权重与资源管理，能够在内存与 CPU 使用上保持最优表现。
- **可定制化**：支持脚本注入、事件监听、API 绑定等多种可扩展方式。
- **无依赖可嵌入**：可直接在 Rust 项目中 `cargo` 引用，API 纯 Rust，无 C/C++ 绑定。

## 关键功能

| 功能 | 说明 |
|------|------|
| 创建浏览器窗口 | `Browser::new` 生成一个可配置的窗口实例 |
| 注入 JavaScript | `execute_script` 方法可在页面中执行脚本 |
| 事件监听 | `on_event` 绑定浏览器事件，如 `Loaded`, `LoadFailed` |
| 网络访问 | 支持自定义协议、拦截请求与响应 |
| 资源管理 | `BrowserHandle` 提供线程安全句柄 |
| 与 Rust 交互 | 通过 `use_eval` 与 `evaluate` 执行 Rust 与 JS 的双向通信 |
| 自定义 User Agent | 可设置 `UserAgent` 与 `Referrer` 等请求头 |
| 退出策略 | `run_on_main_thread` 与 `execute_on_main_thread` 处理跨线程调用 |

## 快速上手

```rust
use wry::webview::{WebViewBuilder, WebView};

fn main() -> wry::Result<()> {
    // 创建浏览器窗口
    let webview = WebViewBuilder::new()
        .with_url("https://www.rust-lang.org")?
        .with_title("Wry Demo")
        .build()?;

    // 监听加载完成
    webview.add_subscriber(|event| match event {
        wry::webview::WebViewEvent::Loaded => {
            println!("页面已加载");
        },
        _ => {}
    });

    // 注入脚本
    webview.execute_script("console.log('Hello from Wry');")?;

    // 运行事件循环
    webview.run()
}
```

> ⚡️ 运行前请在 Cargo.toml 添加依赖：  
> `wry = { version = "0.18", features = ["full"] }`

## 文档与社区

- 官方 GitHub Wiki: https://github.com/tauri-apps/wry/wiki  
- 示例项目: https://github.com/tauri-apps/wry/tree/main/examples  
- 讨论组: https://github.com/tauri-apps/wry/discussions  

--- 

> 以上内容已保存至 `src/content/docs/00/wry_tauri-apps.md`。👍