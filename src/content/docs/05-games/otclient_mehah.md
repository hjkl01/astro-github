---
title: otclient
---

# OTClient - Redemption

## 项目简介

OTClient 是一个用于 OTServ 的 Tibia 客户端替代品，用 C++20 和 Lua 编写。它采用模块化系统，使用 Lua 脚本处理游戏界面和功能，使其灵活且易于定制。

## 主要功能

### 核心特性

- **LUA 脚本化**：所有游戏界面功能均通过 LUA 脚本实现
- **CSS-like UI 语法**：用于界面设计
- **模块化系统**：每个功能都是独立的模块，便于定制和扩展
- **多线程优化**：包括异步纹理加载、垃圾回收等性能优化
- **着色器支持**：图形效果和着色器系统
- **动画纹理**：支持动态纹理效果
- **透明度和多语言支持**

### 界面与用户体验

- **UIWidgets 改进**：更好的性能和响应
- **自动重载模块**：开发时自动更新
- **附加效果系统**：支持光环、翅膀等特效（兼容 APNG）
- **模块控制器系统**：更安全的模块创建和管理
- **反锯齿模式选项**：平滑渲染
- **生物信息显示**：通过 UIWidget 显示
- **HTML/CSS 语法支持**
- **延迟自适应相机**：根据服务器延迟调整相机速度

### 兼容性与协议

- 支持客户端版本 12.85 ~ 12.92、13.00 ~ 13.40（包括 protobuf）
- 支持序列化包和压缩
- 兼容 TFS、Canary 等服务器

### 社区模块与集成

- Discord RPC 集成
- 加密系统
- 客户端更新器
- 彩色文本支持
- QR 码支持
- 打字图标
- 平滑走路高度
- Tibia 13 布局
- 浏览器客户端
- 移动设备支持
- 3D 声音效果
- 机器人支持（Bot V8）
- 着色器帧缓冲
- 完整百科全书

## 安装与使用

### 编译

访问 [Wiki](https://github.com/mehah/otclient/wiki) 获取编译指南。

### Docker

```bash
# 构建镜像
docker build -t mehah/otclient .

# 运行容器
xhost +
docker run -it --rm \
  --env DISPLAY \
  --volume /tmp/.X11-unix:/tmp/.X11-unix \
  --device /dev/dri \
  --device /dev/snd mehah/otclient /bin/bash
xhost -
```

### 移动项目

支持 Android 和 iOS 编译，详情见 [Android 编译指南](https://github.com/mehah/otclient/wiki/Compiling-on-Android)。

## 协议支持

| 协议/版本                      | 描述                           | 兼容性 |
| ------------------------------ | ------------------------------ | ------ |
| TFS (7.72)                     | Downgrade nekiro / Nostalrius  | ✅     |
| TFS 0.4 (8.6)                  | Fir3element                    | ✅     |
| TFS 1.5 (8.0 / 8.60)           | Downgrade nekiro / MillhioreBT | ✅     |
| TFS 1.4.2 (10.98)              | Release Otland                 | ✅     |
| TFS 1.6 (13.10)                | Main repo otland (2024)        | ✅     |
| Canary (13.21 / 13.32 / 13.40) | OpenTibiaBr                    | ✅     |
| Canary (14.00 ~ 14.12)         | OpenTibiaBr                    | ✅     |

## 许可证

MIT License - 可用于商业、非商业、封闭或开放项目。

## 贡献者

项目由 mehah 维护，有 72 位贡献者。欢迎捐赠支持：[PayPal](https://www.paypal.com/donate/?business=CV9D5JF8E46LY&no_recurring=0&item_name=Thank+you+very+much+for+your+donation.&currency_code=BRL)

## 链接

- GitHub: https://github.com/mehah/otclient
- Discord: https://discord.gg/tUjTBZzMCy
