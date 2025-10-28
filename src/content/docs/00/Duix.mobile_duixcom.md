
---
title: Duix.mobile
---

# Duix.mobile

**GitHub 项目地址**  
<https://github.com/duixcom/Duix.mobile>

---

## 项目简介

Duix.mobile 是 Duix 平台的官方移动端客户端，采用 Flutter 开发，支持 iOS 与 Android。主要为设备管理、实时监控、固件升级等场景提供一站式解决方案。

---

## 核心特性

| 领域 | 说明 |
|------|------|
| **多平台支持** | 一份代码覆盖 iOS 与 Android，保持 UI 与体验一致 |
| **设备管理** | 新增、编辑、删除设备，批量操作与分组管理 |
| **实时监控** | 通过 MQTT/WebSocket 实时获取设备状态、告警与日志 |
| **OTA 固件升级** | 支持版本回滚、升级进度显示、失败重试 |
| **安全与权限** | Token 登录、权限校验、双因素验证 |
| **离线缓存** | 设备信息、历史数据离线可查看 |
| **主题自适应** | 暗黑/亮色主题，随系统模式自动切换 |
| **状态管理** | Riverpod 统一管理应用状态 |
| **网络请求** | Dio + Json Serializable，支持拦截与错误统一处理 |
| **CI/CD** | GitHub Actions 自动构建、单元测试、App Store / Play Store 发布 |

---

## 快速上手

```bash
# 克隆仓库
git clone https://github.com/duixcom/Duix.mobile.git
cd Duix.mobile

# 安装依赖
flutter pub get

# 运行
flutter run
```

> 需要先在 Duix 平台上创建应用并获取 App ID 与 Secret，放置到 `lib/config/duix_config.dart` 配置文件中。

---

## 使用流程

1. **登录**  
   - 登录。  
   - 登录状态会在 `SharedPreferences` 中持久化。

2. **设备列表**  
   - 主页面显示已绑定的设备列表，支持搜索、筛选与分组。  
   - 通过 `Add Device` 按钮添加新设备或手动扫描二维码绑定。

3. **设备详情**  
   - 点击设备进入详情页，实时显示状态、告警级别及历史日志。  
   - 支持配置参数编辑与重置。

4. **OTA 升级**  
   - 在设备详情页的 OTA 选项卡中选择固件版本。  
   - 单击 `Start Upgrade` 后出现进度条，升级完成后显示结果。  
   - 支持断点续传与多设备批量升级。

5. **设置**  
   - 切换主题、语言、账号管理、查看版本信息与日志导出。  

---

## 发展路线（示例）

- **蓝牙低能耗 (BLE) 监控**：实时获取离线设备状态。  
- **多语言支持**：实现国际化（简体中文、英文）。  
- **日志可视化**：使用 FlChart 展示历史数据趋势。  
- **插件化架构**：支持模块化扩展，自定义功能插件。  

---

## 许可证

本项目采用 MIT 许可证，详见根目录 `LICENSE` 文件。