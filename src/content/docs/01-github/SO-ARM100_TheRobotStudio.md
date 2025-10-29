
---
title: SO-ARM100
---


# SO-ARM100 - TheRobotStudio

**仓库地址**: https://github.com/TheRobotStudio/SO-ARM100

---

## 项目简介

SO-ARM100 是一套面向工业级机械臂的软硬件一体化平台，专为快速原型开发、算法研究和小批量生产而设计。它包含完整的机械结构、驱动电路、软件包与演示案例，支持 **C++** 与 **Python** 双语言调用，兼容 Raspberry Pi、Arduino 与 Jetson Nano 等常见单板计算机。

---

## 核心特性

- **模块化机械结构**：采用可拆卸铝型材与 3D 打印零件组合，方便现场快速组装与维护。  
- **多轴高精度控制**：支持 6 轴伺服驱动，分辨率可达 0.1°，可通过 UART/USB 进行低延迟控制。  
- **低功耗电源管理**：内置 12V/24V 双路电源模块，支持单板电流监测与过载保护。  
- **跨平台 SDK**：提供 C++/Python API，支持 ROS、WebSocket 与 MQTT 等通讯协议。  
- **任务调度与路径规划**：附带 `TrajectoryPlanner` 库，可实现直线、圆弧、时间基轨迹生成。  
- **视觉感知集成**：内置摄像头接口，配合 OpenCV/ROS 进行目标检测与姿态估计。  
- **安全与冗余**：硬件限位开关、软件异常检测，支持硬件重置与安全停机。  
- **实时监控与调试**：通过 Web UI 或命令行工具实时查看关节角度、电流与温度等状态。  

---

## 功能概述

| 功能模块 | 主要接口 | 关键参数 |
|----------|----------|----------|
| 关节动力学 | `Arm::setJointAngle(joint, angle)` | 关节编号(1‑6)、角度(°) |
| 末端执行器 | `Gripper::open/close()` | 开/闭 |
| 轨迹跟踪 | `TrajectoryPlanner::planPath(start, end, speed)` | 起点/终点坐标, 速度 |
| 视觉外参 | `Camera::setExtrinsic(T,R)` | 位移 T(3×1), 旋转矩阵 R(3×3) |
| 状态监测 | `SystemInfo::getAll()` | 角度、速度、电流、温度等 |
| 故障处理 | `ErrorHandler::reset()` | 回档到安全状态 |

---

## 使用方法

### 1. 环境准备

1. **硬件**：SO-ARM100 机械臂 + 计算节点（Raspberry Pi 4/Jetson Nano/Arduino Nano）  
2. **驱动电路**：按手册焊接 MCU 与伺服驱动。  
3. **软件依赖**  
   ```
   sudo apt-get install git cmake build-essential python3-venv
   pip3 install -r requirements.txt
   ```

### 2. 下载源码

```bash
git clone https://github.com/TheRobotStudio/SO-ARM100.git
cd SO-ARM100
```

### 3. 编译库

```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install
```

### 4. 运行演示程序

```bash
cd ../demo
python3 demo.py
```

> 典型演示：`demo.py` 会让机械臂从坐标 A 运动到 B，然后打开/关闭抓手。

### 5. 自定义命令

```cpp
#include <so_arm100/arm.h>

int main() {
    Arm arm;
    arm.connect("COM3");          // 或 "/dev/ttyUSB0"
    arm.setJointAngle(1, 90.0);   // 第 1 轴 +90°
    arm.moveTo({0.3, 0.2, 0.5});  // 末端坐标
    arm.gripper.open();
    return 0;
}
```

### 6. 通过 Web 监控

```bash
cd server
python3 app.py
```

访问 `http://<raspberrypi_ip>:5000` 可实时查看关节状态与录制轨迹。

---

## 代码结构

```
SO-ARM100/
├── src/                 # 源代码
│   ├── arm.cpp          # 机械臂核心实现
│   ├── gripper.cpp
│   ├── trajectory.cpp
│   └── ...
├── include/             # 头文件
│   ├── arm.h
│   ├── gripper.h
│   └── ...
├── demo/                # 本地演示脚本
├── server/              # Web 与 WebSocket 服务
├── config/              # 配置文件（如 CAN 速率、加速度等）
├── CMakeLists.txt
├── requirements.txt
└── README.md
```

---

## 依赖

| 库 | 版本 | 说明 |
|----|------|------|
| C++ STL | 11+ | - |
| Eigen | 3.3+ | 线性代数 |
| ROS Noetic | - | 仅限需要 ROS 的用户 |
| OpenCV | 4.5+ | 图像处理 |
| Flask | 1.1+ | Web UI |
| pyserial | 3.5+ | 串口通信 |

---

## 参与贡献

1. Fork 本仓库  
2. 新建 Feature 分支  
3. 提交合并请求（Merge Request）  
4. 请务必通过 CI 检查并更新文档

---

感谢使用 SO-ARM100，祝你实验愉快 🚀
