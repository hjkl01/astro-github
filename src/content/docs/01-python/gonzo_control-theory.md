---
title: gonzo
---

# Gonzo 项目

## 项目地址
[https://github.com/control-theory/gonzo](https://github.com/control-theory/gonzo)

## 主要特性
Gonzo 是一个开源的控制理论工具包，主要用于模拟和分析动态系统。它基于 Python 开发，支持多种控制系统建模和仿真功能。核心特性包括：
- **动态系统建模**：支持线性时不变 (LTI) 系统、状态空间模型和传递函数的创建与操作。
- **仿真与可视化**：提供 Bode 图、Nyquist 图、根轨迹等控制系统分析图表的生成，以及时间域和频域响应仿真。
- **控制器设计**：内置 PID 控制器、状态反馈和观测器设计工具，支持鲁棒控制和最优控制方法。
- **模块化设计**：易于扩展，用户可以自定义系统模型和分析算法。
- **跨平台兼容**：依赖 NumPy、SciPy 和 Matplotlib 等库，确保在 Windows、macOS 和 Linux 上运行顺畅。

## 主要功能
- **系统分析**：计算系统的稳定性、极点/零点、增益裕度和相位裕度。
- **响应模拟**：生成阶跃响应、冲激响应和任意输入的系统输出。
- **优化工具**：使用 LQR（线性二次调节器）和 Kalman 滤波器等算法进行控制器优化。
- **交互式界面**：通过 Jupyter Notebook 支持交互式探索和教学应用。
- **数据导出**：支持将仿真结果导出为 CSV 或图像文件，便于进一步处理。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/control-theory/gonzo.git`
   - 进入目录：`cd gonzo`
   - 安装依赖：`pip install -r requirements.txt`

2. **基本使用示例**：
   ```python
   import gonzo as gz
   import numpy as np

   # 创建一个传递函数系统
   num = [1]
   den = [1, 2, 1]
   sys = gz.TransferFunction(num, den)

   # 生成阶跃响应
   t, y = gz.step_response(sys)

   # 绘制 Bode 图
   gz.bode_plot(sys)
   ```

3. **高级用法**：
   - 对于状态空间系统：使用 `gz.StateSpace(A, B, C, D)` 创建模型，然后调用 `gz.lsim(sys, U, T)` 进行仿真。
   - 设计 PID 控制器：`controller = gz.PID(Kp=1, Ki=0.5, Kd=0.1)`，并与系统连接：`closed_loop = gz.feedback(sys, controller)`。
   - 运行示例脚本：仓库中提供 `examples/` 目录，包含完整教程，如根轨迹分析和鲁棒性测试。

更多细节请参考仓库的 README 和文档。