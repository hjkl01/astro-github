---
title: cai
---


# cai (Alias Robotics C++ AI Library)

**项目地址**: https://github.com/aliasrobotics/cai

## 简介  
cai 是 Alias Robotics 为机器人开发的 C++ AI 库，提供从感知、建图、路径规划到运动控制的完整栈。该库基于 ROS 2、OpenCV、Eigen 等开源工具实现，旨在帮助快速构建自研机器人平台的 AI 能力。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **感知模块** | 支持 LIDAR、相机、IMU 等传感器数据的采集与预处理；实现点云滤波、特征提取、目标检测（基于 OpenCV + YOLOv5）等功能。 |
| **建图** | 提供 2D/3D SLAM（基于 GMapping / Cartographer）以及稀疏点云地图生成。 |
| **路径规划** | 实现 A*、Dijkstra、RRT* 等离散规划算法；支持全局与局部规划。 |
| **运动控制** | 速度指令发布、PID 控制器、轨迹跟踪（Pure Pursuit、Dynamic Window Approach）。 |
| **模块化** | 各功能分为独立的 CMake 子模块，易于扩展与单元测试。 |
| **ROS 2 兼容** | 所有节点均为 ROS 2 节点，支持 rclcpp、rclpy；可通过 launch 文件一键启动。 |
| **跨平台** | 支持 Ubuntu 20.04/22.04、Windows 10/11；编译环境为 C++17。 |

## 功能概览  

1. **SensorInterface** – 统一的传感器装配与数据同步接口。  
2. **Perception** – 点云滤波、语义分割、目标检测与跟踪。  
3. **Mapping** – SLAM 模块、地图保存与加载。  
4. **Planner** – 全局与局部路径规划器，支持动态障碍物更新。  
5. **Controller** – 速度命令生成与执行，支持多传感器融合。  
6. **Visualization** – 通过 RViz2 可视化感知结果、地图与轨迹。  

## 用法  

### 1. 克隆仓库  

```bash
git clone https://github.com/aliasrobotics/cai.git
cd cai
```

### 2. 安装依赖  

```bash
# ROS 2 Humble 或 Iron
sudo apt update
sudo apt install -y ros-${ROS_DISTRO}-desktop-full \
                    ros-${ROS_DISTRO}-nav2-bringup \
                    ros-${ROS_DISTRO}-nav2-common \
                    ros-${ROS_DISTRO}-nav2-msgs \
                    ros-${ROS_DISTRO}-rviz2 \
                    ros-${ROS_DISTRO}-image-transport \
                    libopencv-dev libeigen3-dev libpcl-dev \
                    libyaml-cpp-dev

# 若使用 YOLOv5 目标检测
pip install torch torchvision
```

### 3. 编译

```bash
colcon build --symlink-install
source install/setup.bash
```

### 4. 运行示例

```bash
# 启动感知节点
ros2 launch cai perception.launch.py

# 启动地图构建节点
ros2 launch cai mapping.launch.py

# 启动导航节点
ros2 launch cai navigation.launch.py
```

> **说明**  
> - `perception.launch.py` 负责加载传感器接口、YOLOv5 检测器以及点云滤波器。  
> - `mapping.launch.py` 运行 SLAM（Cartographer）并将地图发布到 `/map` 话题。  
> - `navigation.launch.py` 订阅 `/map` 与 `/goal`，使用 RRT* 规划路径，并通过 `controller` 节点发布 `cmd_vel`。

### 5. 自定义使用

```cpp
#include <cai/perception/Perception.hpp>
#include <cai/mapping/SLAM.hpp>
#include <cai/planner/Planner.hpp>
#include <cai/controller/Controller.hpp>

int main(int argc, char** argv)
{
    // 初始化 ROS2
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("cai_demo");

    // 1. 传感器 & 感知
    cai::SensorInterface sensor(node);
    cai::Perception perception(sensor);

    // 2. SLAM
    cai::SLAM slam(node, perception);
    slam.start();

    // 3. 路径规划
    cai::Planner planner(node, slam);
    std::vector<cai::Pose2D> path = planner.plan(start, goal);

    // 4. 控制
    cai::Controller controller(node);
    controller.follow(path);

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
```

### 6. 参数配置

所有节点均可通过 ROS 2 参数服务器或 YAML 文件配置，例如：

```yaml
# config/perception.yaml
camera:
  frame_id: "camera_color_optical_frame"
lidar:
  frame_id: "lidar_link"
yolo:
  model_path: "/home/user/models/yolov5s.pt"
  iou_threshold: 0.45
  conf_threshold: 0.5
```

使用 `ros2 param load` 或在 launch 文件中使用 `-p` 选项加载。

## 贡献

- Fork 本仓库 → 新建分支 → 提交 PR  
- 所有提交需通过 CI（GitHub Actions）自动编译与测试  
- 请保持代码风格与 `clang-format` 兼容，提交前执行 `clang-format -i .`

## 许可证

本项目采用 **Apache License 2.0**。详见 `LICENSE` 文件。  

---  
**作者**: Alias Robotics  
**维护者**: aliasrobotics-devs  
**发布时间**: 2024-03
