
---
title: stremio-web
---

**项目地址**：<https://github.com/Stremio/stremio-web>

**主要特性与功能**  
1. **全平台 Web 客户端** – 通过浏览器即可访问 Stremio 内容，支持 PC、Mac、Linux 以及移动设备（iOS、Android）。  
2. **流式播放** – 与 Stremio 服务后端配合，直接在浏览器中流式播放电影与电视剧，支持多路音轨、字幕、画中画。  
3. **插件（Add‑ons）生态** – 通过官方或第三方插件检索并显示可用内容，支持下载、投屏等。  
4. **个人化内容池** – 书签、观看历史、收藏（Watchlist）等，可同步到账号。  
5. **离线使用** – 通过 Service Workers 缓存 UI 与部分离线内容，支持在无网络环境下查看已缓存信息。  
6. **同步与多设备** – 通过 Stremio 账号实现跨设备状态同步，包括播放进度、下载文件等。  
7. **投屏功能** – 支持 Chromecast、AirPlay 等协议，将内容投屏到电视或大屏。  
8. **易扩展的框架** – 基于 React + MobX，使用 TypeScript 编写，组件化结构便于开发和插件生态集成。  

**用法**  
1. **部署**  
   ```bash
   git clone https://github.com/Stremio/stremio-web.git
   cd stremio-web
   npm install
   npm run build   # 打包
   npm run serve   # 开发服务器
   ```
2. **访问**  
   通过 `http://localhost:3000`（默认）或配置 `PORT` 访问 UI。  
3. **登录** – 在主页右上角点击“登录”，输入 Stremio 账号或使用聚合 API 关键字。  
4. **使用插件** – 进入“Add‑ons”页面，搜索并启用所需插件；激活后可在搜索结果中看到插件提供的内容。  
5. **播放** – 选中影片 → 选择源 → 点击播放；使用右侧控制栏调节音量、字幕、画质。  
6. **投屏** – 右上角投屏图标，选择目标设备即可投射。  

**进一步扩展**  
- 在 `src/addons` 目录下开发自定义插件，可直接与 Stremio 后端交互。  
- 使用 `stremio-web` 的 API 接口，可与自己的后端或第三方服务集成。  

这就是 Stremio Web 客户端的核心特性、功能与基础使用方式。