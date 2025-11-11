---
title: PythonRobotics
---

# PythonRobotics

PythonRobotics 是一个 Python 代码集合和机器人算法的教科书，提供易于理解的机器人算法实现。

## 功能

- **易读性**：代码设计易于阅读，帮助理解每个算法的基本思想。
- **实用性**：选择广泛使用和实用的机器人算法。
- **最小依赖**：使用最少的外部库依赖。
- **全面覆盖**：包括定位（Localization）、映射（Mapping）、SLAM、路径规划（Path Planning）、路径跟踪（Path Tracking）、手臂导航（Arm Navigation）、空中导航（Aerial Navigation）和双足行走（Bipedal）等模块。

主要算法示例：

- 定位：扩展卡尔曼滤波（EKF）、粒子滤波、柱状图滤波。
- 映射：高斯网格映射、射线投射网格映射、激光雷达到网格映射。
- SLAM：迭代最近点（ICP）匹配、FastSLAM 1.0。
- 路径规划：动态窗口方法、网格搜索（Dijkstra、A\*、D\*、D\* Lite）、势场算法、状态格子规划、PRM、RRT、LQR 等。
- 路径跟踪：Stanley 控制、后轮反馈控制、LQR 控制、模型预测控制。
- 其他：手臂控制、无人机轨迹跟随、火箭着陆、二足规划。

## 用法

1. **克隆仓库**：

   ```
   git clone https://github.com/AtsushiSakai/PythonRobotics.git
   ```

2. **安装依赖**：
   - 使用 conda：
     ```
     conda env create -f requirements/environment.yml
     ```
   - 使用 pip：
     ```
     pip install -r requirements/requirements.txt
     ```

3. **运行示例**：
   - 进入相应目录（如 `PathPlanning/AStar/`）。
   - 执行 Python 脚本，例如 `python a_star.py`。
   - 查看动画和结果。

4. **文档**：完整文档和教科书可在 [https://atsushisakai.github.io/PythonRobotics/](https://atsushisakai.github.io/PythonRobotics/) 查看。

如果喜欢这个项目，请给仓库加星！
