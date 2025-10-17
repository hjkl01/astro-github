
---
title: smarGate
---

# smarGate 项目

## 项目地址
[GitHub 项目地址](https://github.com/lazy-luo/smarGate)

## 主要特性
- **智能网关功能**：smarGate 是一个开源的智能家居网关项目，支持多种物联网协议集成，如 Zigbee、Z-Wave 和 Wi-Fi，实现设备间的无缝连接和控制。
- **模块化设计**：采用模块化架构，便于扩展和自定义，支持插件系统，用户可以轻松添加新设备或协议支持。
- **安全机制**：内置加密通信、用户认证和访问控制，确保数据传输安全，支持 HTTPS 和 MQTT 安全协议。
- **跨平台支持**：兼容 Linux、Windows 和 Raspberry Pi 等平台，适合家庭或企业级部署。
- **开源与社区驱动**：基于 MIT 许可，鼓励社区贡献，提供 API 接口和 Web 管理界面。

## 主要功能
- **设备管理**：自动发现和配对智能设备，支持实时监控设备状态、固件更新和批量配置。
- **自动化规则**：内置规则引擎，用户可以设置触发器和动作，实现场景自动化，例如“当门铃响起时，打开客厅灯”。
- **数据可视化**：提供仪表盘和图表功能，展示传感器数据、能耗统计和历史日志，便于分析和优化。
- **集成支持**：兼容 Home Assistant、OpenHAB 等主流智能家居平台，还支持语音控制集成（如 Alexa 或 Google Assistant）。
- **API 和 SDK**：暴露 RESTful API 和 SDK，允许开发者构建自定义应用或第三方集成。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/lazy-luo/smarGate.git`
   - 进入目录：`cd smarGate`
   - 安装依赖：使用 `pip install -r requirements.txt`（Python 环境）或跟随 README 中的 Docker 部署指南。

2. **配置**：
   - 编辑 `config.yaml` 文件，设置数据库连接、设备协议和网络参数。
   - 通过 Web 界面（默认端口 8080）登录并添加设备：访问 `http://localhost:8080`，创建管理员账户。

3. **运行**：
   - 启动服务：`python main.py` 或使用 Docker：`docker-compose up -d`。
   - 配对设备：使用 Web 界面扫描并添加支持的智能设备。

4. **使用示例**：
   - 创建自动化规则：在 Web 界面导航到“规则”部分，选择触发事件（如时间或传感器输入），定义动作（如发送通知或控制设备）。
   - API 调用：使用 curl 测试，例如 `curl -X POST http://localhost:8080/api/devices/on -d '{"device_id": "lamp1"}'` 来打开灯具。
   - 监控：通过移动 App 或 Web 仪表盘查看实时数据。

详细用法请参考项目 README 和文档。