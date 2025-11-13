---
title: MagicMirror
---


# MagicMirror (MagicMirrorOrg)

**项目地址**: https://github.com/MagicMirrorOrg/MagicMirror

## 简介  
MagicMirror 是一款基于 Node.js 的智能镜面显示系统，采用模块化设计，可在任何显示屏（如 Raspberry Pi、PC 等）上运行。镜面显示内容可通过配置文件灵活定制，支持多种功能模块，满足日常信息展示与交互需求。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **模块化架构** | 通过 `modules/` 目录加载独立功能模块，支持自定义开发与第三方插件。 |
| **实时信息显示** | 天气、新闻、日历、时间、股票、交通、天气预报等信息随时更新。 |
| **多语言与时区** | 支持多语言配置，自动根据本地时区刷新时间与天气。 |
| **自定义布局** | 通过 `config/config.js` 设置模块位置、大小、样式与行为。 |
| **多显示屏支持** | 可在多台显示器上分别加载不同模块，实现多镜面协同。 |
| **可扩展** | 官方提供大量标准模块，社区也有丰富的第三方插件。 |
| **轻量、低功耗** | 适合 Raspberry Pi 等单板电脑，运行稳定且能耗低。 |
| **Web 控制** | 通过浏览器访问 `http://<mirror_ip>:<port>` 进行配置与调试。 |

## 核心功能模块（示例）  

| 模块 | 作用 | 关键配置项 |
|------|------|-----------|
| `MMM-Weather` | 显示天气预报 | `apikey`, `city`, `units` |
| `MMM-News` | 新闻头条 | `feeds`, `maxItems` |
| `MMM-Calendar` | 日历事件 | `calendars`, `maxEvents` |
| `MMM-Clock` | 时钟与日期 | `displayUnits`, `showDate` |
| `MMM-StockTicker` | 股票行情 | `symbols`, `refreshInterval` |
| `MMM-WeatherForecast` | 天气预报 | `days`, `temperatureUnit` |
| `MMM-WorldClock` | 世界时钟 | `cities`, `timeZone` |
| `MMM-Notifications` | 系统通知 | `displayTime`, `maxNotifications` |

## 安装与运行  

1. **克隆仓库**  
   ```bash
   git clone https://github.com/MagicMirrorOrg/MagicMirror.git
   cd MagicMirror
   ```

2. **安装依赖**  
   ```bash
   npm install
   ```

3. **配置文件**  
   - 复制示例配置：`cp config/config.js.sample config/config.js`
   - 编辑 `config/config.js`，根据需求修改模块列表、位置、颜色等。

4. **启动 MagicMirror**  
   ```bash
   npm start
   ```

   默认端口为 `8080`，可通过浏览器访问 `http://localhost:8080` 或镜面设备 IP 进行预览。

5. **自定义模块**  
   - 在 `modules/` 目录下添加或修改模块文件。
   - 在 `config.js` 中添加相应模块配置，位置使用 `position`（如 `top_left`, `bottom_center` 等）。

## 常用命令  

| 命令 | 说明 |
|------|------|
| `npm start` | 启动镜面显示 |
| `npm run build` | 打包前端资源 |
| `npm test` | 运行单元测试 |
| `npm install <module-name>` | 安装第三方模块 |

## 参考文档  

- [官方文档](https://magicmirror.builders/)  
- [模块开发指南](https://magicmirror.builders/docs/modules/)  
- [配置文件示例](https://github.com/MagicMirrorOrg/MagicMirror/blob/master/config/config.js.sample)

---  

> **提示**：本项目使用 MIT 许可证，欢迎 Fork、Pull Request 与社区交流。