---
title: unitree
---

# unitree_rl_lab

## 功能介绍

unitree_rl_lab 是 Unitree Robotics 开发的强化学习实验室仓库，基于 IsaacLab 构建。该项目提供了一套用于 Unitree 机器人的强化学习环境，支持 Go2、H1 和 G1-29dof 机器人。项目旨在通过强化学习算法训练机器人执行各种任务，如运动控制和导航。

主要功能包括：

- 提供多种机器人模型的强化学习环境
- 支持 Isaac Sim、Mujoco 和物理机器人部署
- 包含训练、推理和部署脚本
- 基于开源框架 IsaacLab 和 Mujoco

## 用法

### 安装

1. 安装 IsaacLab：按照 [IsaacLab 安装指南](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html) 安装。

2. 克隆仓库：

   ```
   git clone https://github.com/unitreerobotics/unitree_rl_lab.git
   ```

3. 安装库：

   ```
   conda activate env_isaaclab
   ./unitree_rl_lab.sh -i
   ```

4. 下载机器人描述文件：
   - 方法1：使用 USD 文件，从 [unitree_model](https://huggingface.co/datasets/unitreerobotics/unitree_model) 下载。
   - 方法2：使用 URDF 文件，从 [unitree_ros](https://github.com/unitreerobotics/unitree_ros) 下载（推荐）。

5. 配置路径：在 `source/unitree_rl_lab/unitree_rl_lab/assets/robots/unitree.py` 中设置 `UNITREE_ROS_DIR` 或 `UNITREE_MODEL_DIR`。

### 运行

- 列出可用任务：

  ```
  ./unitree_rl_lab.sh -l
  ```

- 训练任务：

  ```
  ./unitree_rl_lab.sh -t --task Unitree-G1-29dof-Velocity
  ```

- 推理：
  ```
  ./unitree_rl_lab.sh -p --task Unitree-G1-29dof-Velocity
  ```

### 部署

- Sim2Sim：在 Mujoco 中测试模型。
- Sim2Real：部署到物理机器人，使用提供的控制器程序。

更多详情请参考项目 [README](https://github.com/unitreerobotics/unitree_rl_lab/blob/main/README.md)。
