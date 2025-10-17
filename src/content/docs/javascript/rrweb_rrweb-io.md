
---
title: rrweb
---

# rrweb 项目

**GitHub 项目地址**: [https://github.com/rrweb-io/rrweb](https://github.com/rrweb-io/rrweb/blob/master/README.zh_CN.md)

## 主要特性

rrweb 是一个开源的会话重放（Session Replay）框架，主要用于前端页面的录制和回放。它具有以下核心特性：

- **无侵入式录制**：无需修改现有代码，通过简单的脚本注入即可捕获页面交互、DOM 变化和用户行为。
- **高保真回放**：支持精确重放鼠标移动、点击、滚动、输入等事件，实现像素级别的页面还原。
- **性能优化**：采用增量快照（incremental snapshots）机制，仅记录变化部分，减少数据量和存储开销。
- **跨浏览器支持**：兼容主流浏览器，包括 Chrome、Firefox、Safari 等。
- **隐私保护**：内置敏感数据屏蔽功能，可配置忽略密码字段、个人隐私信息等。
- **轻量级**：核心库大小小巧，易于集成到各种前端框架中，如 React、Vue、Angular。
- **扩展性强**：支持插件系统，可自定义录制规则、数据加密和回放自定义。

## 主要功能

rrweb 的功能聚焦于会话录制与重放，帮助开发者调试用户体验问题、监控应用性能和分析用户行为：

- **事件录制**：捕获用户交互事件（如点击、输入、滚动、视口变化）和 DOM 修改事件。
- **会话回放**：基于录制数据实时或离线重放整个用户会话，支持时间轴控制、暂停/快进。
- **数据采样**：可选的采样模式，仅录制部分会话以降低负载。
- **集成工具**：提供 CLI 工具用于打包和部署，支持与 Sentry、Datadog 等监控平台的集成。
- **自定义 API**：暴露录制器（Recorder）和回放器（Replayer）的 API，便于高级定制。
- **移动端支持**：扩展到移动浏览器和小程序的录制功能。

## 用法

### 安装

通过 npm 安装：

```bash
npm install rrweb
```

### 基本用法

1. **录制页面**：
   在 HTML 中引入 rrweb 并启动录制器：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/rrweb@latest/dist/rrweb.min.js"></script>
   <script>
     rrweb.record({
       emit(event) {
         // 发送事件到服务器，例如通过 WebSocket 或 AJAX
         console.log(event);
       },
     });
   </script>
   ```

   这将开始捕获页面事件，并通过 `emit` 回调发送数据。

2. **回放会话**：
   使用录制的数据重放：

   ```html
   <script>
     const events = [/* 从服务器获取的事件数组 */];
     const replayer = new rrweb.Replayer(events);
     replayer.play();
   </script>
   ```

3. **高级配置**：
   - 配置采样率：`{ sampleRate: 100 }`（百分比）。
   - 屏蔽元素：使用 `blockClass` 或 `maskAllInputs` 选项。
   - 集成到 React/Vue：通过 hooks 或插件直接调用录制 API。

更多详细用法和示例，请参考项目 README 中的文档。rrweb 适用于 Web 应用监控、A/B 测试和用户反馈收集场景。