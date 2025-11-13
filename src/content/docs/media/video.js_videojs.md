---
title: video.js
---


# video.js（VideoJS）

> 项目地址：<https://github.com/videojs/video.js>

## 项目简介
video.js 是一个开源的 HTML5 视频播放器，提供了丰富的功能、可扩展的插件体系以及跨浏览器、跨设备的兼容性。它支持 HLS/DASH、字幕、广告、可自定义的控制条以及多种第三方集成（如 React、Angular、Vue 等）。

## 主要特性
- **HTML5 原生支持**：无需 Flash，完全基于 `<video>` 标签。
- **多码流支持**：HLS、DASH、Smooth Streaming 等流媒体协议。
- **字幕与多语言**：支持 WebVTT、SRT 等字幕文件，字幕选择器。
- **可自定义 UI**：自定义控制栏、按钮、进度条、音量、全屏等。
- **插件生态**：官方插件（广告、统计、截图等）及社区插件。
- **响应式布局**：自适应宽高、可设置最大/最小尺寸。
- **多平台兼容**：桌面浏览器、iOS、Android、电视盒子等。
- **无障碍支持**：ARIA、键盘导航、屏幕阅读器友好。

## 核心功能
| 功能 | 说明 |
|------|------|
| **视频播放** | 控制播放/暂停、快进/快退、音量、全屏 |
| **播放列表** | 自动播放下一集、播放顺序切换 |
| **广告插入** | VAST/VPAID、广告时长计时 |
| **统计与分析** | 事件回调、播放时长、错误日志 |
| **截图 & 截帧** | 截取当前帧生成图片 |
| **多屏幕投射** | Chromecast、AirPlay、DLNA |
| **广告后续** | 广告后跳转、广告播放完成事件 |
| **主题与皮肤** | 自定义 CSS、主题切换 |

## 用法

### 1. 安装

```bash
# npm
npm install video.js

# yarn
yarn add video.js
```

### 2. 引入

**CSS**

```html
<link href="https://unpkg.com/video.js/dist/video-js.css" rel="stylesheet">
```

**JS**

```html
<script src="https://unpkg.com/video.js/dist/video.js"></script>
```

> 或者使用打包工具 `import 'video.js/dist/video-js.css'; import videojs from 'video.js';`

### 3. HTML

```html
<video
  id="my-video"
  class="video-js vjs-default-skin"
  controls
  preload="auto"
  width="640"
  height="264"
  data-setup='{}'>
  <source src="https://example.com/video.mp4" type="video/mp4">
  <source src="https://example.com/video.webm" type="video/webm">
  <p class="vjs-no-js">
    为了观看此视频，请启用 JavaScript 或升级到现代浏览器
  </p>
</video>
```

### 4. JavaScript 初始化

```js
const player = videojs('my-video', {
  autoplay: false,
  controls: true,
  language: 'zh-CN',
  plugins: {
    // 示例：使用广告插件
    ads: { /* 配置 */ }
  }
});

// 监听事件
player.on('ended', function() {
  console.log('视频播放结束');
});
```

### 5. React 示例（`videojs-react`）

```bash
npm install videojs-react
```

```jsx
import { Video } from 'videojs-react';

<Video
  src="https://example.com/video.mp4"
  width={640}
  height={264}
  controls
  autoplay={false}
  options={{
    plugins: {
      ads: { /* 配置 */ }
    }
  }}
/>
```

## 常见插件

| 插件 | 说明 |
|------|------|
| **videojs-contrib-hls** | HLS 播放 |
| **videojs-contrib-dash** | DASH 播放 |
| **videojs-ads** | VAST/VPAID 广告 |
| **videojs-ima** | Google IMA 集成 |
| **videojs-subtitles** | 字幕管理 |
| **videojs-snapshots** | 截图功能 |

## 开发与贡献

- Fork 项目，提交 PR。
- 运行 `npm run dev` 进行本地开发。
- 文档与示例位于 `docs/` 目录。

---
> **提示**：视频资源最好使用 CDN 或自托管，避免跨域加载失败。  
> **注意**：确保 `video.js` 与 `video-js.css` 的版本保持一致。
