---
title: openpilot
---


# OpenPilot (comma.ai)

## 项目地址
- https://github.com/commaai/openpilot

## 概览  
OpenPilot 是开源自动驾驶系统，支持多款车型，能够实现自适应巡航、车道保持、盲点监测等功能。项目核心基于 C++/Python，使用深度学习模型处理摄像头、雷达、雷达等传感器输入。

## 主要特性  
- **车道保持与巡航**：主动相机+前雷达+后雷达相结合，保持车道并控制速度。  
- **行驶评估**：实时评估路况，给出安全距离、适用转向等信息。  
- **车辆兼容性**：支持 Tesla、Fiat/Chrysler、Ford、General Motors 等多厂商车型。  
- **模块化设计**：`car`, `selfdrive`, `tools` 等目录分离硬件抽象、核心算法与工具。  
- **远程更新**：使用 `openpilot` 套件通过 OTA 下载模型/算法更新。  
- **安全性**：实现硬件安全层（HSL）、安全检查、监控遥测数据。  
- **社区驱动**：通过 CI、issue、PR 维持高质量代码和贡献。

## 用法  
1. **克隆仓库**  
   ```bash
   git clone https://github.com/commaai/openpilot.git
   cd openpilot
   ```

2. **安装依赖**（示例在 Ubuntu 22.04）  
   ```bash
   sudo apt update
   sudo apt install -y python3-pip python3-venv
   pip3 install -r requirements/requirements.txt
   ```

3. **准备硬件**  
   - 安装兼容的 OBDII 插口或 `comma two` 设备。  
   - 通过 SD 卡或 USB 将固件镜像烧写到车载存储。

4. **构建与运行**  
   ```bash
   make -j$(nproc)  # 编译所有模块
   make subsys      # 只编译子系统
   # 启动仿真（可选）
   make emulate
   ```

5. **日常使用**  
   - 在车内使用 `comma two` 或 `dashcam` 按键进入 `openpilot`。  
   - 通过汽车仪表盘监控驾驶状态。  
   - 如需更新，请使用
     ```bash
     tools/pr/subprocess/check_for_updates.sh
     ```

## 贡献指南  
- 先执行 `tools/pr/pr_tool.py` 检查本地更改。  
- 提交 PR 时注明 `#[issue #]`。  
- 按照代码规范编写文档、单元测试。  

## 许可证  
MIT 许可证。查看 `LICENSE` 文件了解更多细节。  
