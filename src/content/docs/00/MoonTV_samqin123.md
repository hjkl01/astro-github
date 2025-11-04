
---
title: MoonTV
---

# MoonTV

项目地址: https://github.com/samqin123/MoonTV

## 主要特性

- 支持多路高清直播频道
- 自动抓取并更新频道播放链接
- 提供 RESTful API 供前端或第三方调用
- 轻量级 Node.js 服务器，易于部署
- 支持 M3U 播放列表导出

## 功能

1. **频道管理**：可在 `config/channels.json` 中自定义频道名称与 URL  
2. **自动更新**：内置定时任务，每小时检查频道源是否可用  
3. **API 接口**  
   - `GET /api/channels` 返回频道列表  
   - `GET /api/stream/:id` 直接获取指定频道的播放地址  
4. **前端演示**：简单的 HTML 页面，使用 `<video>` 标签播放

## 用法

1. 克隆项目  
   ```bash
   git clone https://github.com/samqin123/MoonTV.git
   cd MoonTV
   ```

2. 安装依赖  
   ```bash
   npm install
   ```

3. 配置频道（可选）  
   修改 `config/channels.json`，添加或删除频道。

4. 启动服务器  
   ```bash
   npm start
   ```

5. 访问浏览器  
   打开 `http://localhost:3000` 查看频道列表，点击即可观看。

## 部署

- 直接使用 Node.js 运行  
- 或者使用 Docker：  
  ```bash
  docker build -t moon-tv .
  docker run -p 3000:3000 moon-tv
  ```

## 贡献

欢迎提交 Issues 与 Pull Requests。请遵循项目的贡献指南。