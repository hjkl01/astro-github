
---
title: unitree_rl_lab
---


# Unitree RL Lab (unitreerobotics/unitree_rl_lab)

**项目地址**：<https://github.com/unitreerobotics/unitree_rl_lab>

## 项目概述
Unitree RL Lab 是为 Unitree 机器人（如 A1、Go1、SL、Cheetah 等）设计的强化学习实验平台。它提供了可复现、可扩展的训练、仿真与真实机器人部署框架，支持多种 RL 算法、跨域迁移、策略评估与可视化。

## 主要特性
- **统一的仿真接口**：基于 OpenAI Gym API 的 `UnitreeEnv`，支持多种场景（平地、斜坡、障碍物等）和多种机器人模型。  
- **多算法支持**：内置 PPO、SAC、TD3、DDPG、DQN 等强化学习算法，兼容 Stable Baselines3 与 RLlib。  
- **跨域训练**：通过 `Sim2Real` 迁移插件，实现从仿真到真实机器人的无缝迁移，支持域随机化与在线校准。  
- **自定义奖励与状态**：提供易于扩展的奖励函数框架，可根据任务需求自定义速度、姿态、能耗等指标。  
- **训练可视化与日志**：集成 TensorBoard、Weights & Biases，支持在线监控训练进度与结果。  
- **性能评估**：配套评估脚本 `evaluate.py`，可对训练好的策略在多套测试环境中的鲁棒性进行系统评测。  
- **易于部署**：完成训练后可直接导出 PyTorch 或 TorchScript 模型，并通过 `roscpp`、`rospy` 或 `ros2` 与 Unitree 机器人对接。  

## 关键功能
| 功能 | 说明 |
|------|------|
| 环境创建 | `UnitreeEnv('A1', 'flat')` 创建 A1 在平地上的仿真环境 |
| 脚本训练 | `python train.py --config configs/ppo_a1.yaml` 自动加载配置并启动训练 |
| 领域随机化 | `--reward_scale 0.5`、`--physics_randomize` 等参数在配置文件中设置 |
| 评估 | `python evaluate.py --model models/ppo_a1.pth --env 'flat'` 在指定环境中跑评估 |
| 迁移 | `python sim2real.py --keys low_level_cmd,feedback` 自动对齐低层命令接口 |
| 可视化 | `tensorboard --logdir logs/` 或 `wandb live` 监控训练曲线 |

## 快速使用方法

```bash
# 1. 克隆仓库
git clone https://github.com/unitreerobotics/unitree_rl_lab.git
cd unitree_rl_lab

# 2. 创建并激活虚拟环境（推荐 PyTorch 1.13+）
conda create -n unitree_rl python=3.10
conda activate unitree_rl

# 3. 安装依赖
pip install -e .          # 本地安装仓库
pip install -r requirements.txt

# 4. 运行示例训练（PPO）
python train.py --config configs/ppo_a1_flat.yaml

# 5. 评估训练好的模型
python evaluate.py --model checkpoints/ppo_a1_flat.pth --env flat

# 6. 将模型部署到真实 Unitree A1
roslaunch unitree_rl_lab real_run.launch robot_name:=A1 model_path:=checkpoints/ppo_a1_flat.pth
```

> **提示**  
> - 所有配置文件于 `configs/` 目录下，可根据需求自行修改。  
> - 训练日志与模型默认保存在 `logs/` 与 `checkpoints/`。  
> - 若想在真实机器人上跑，需先配好 ROS 环境，并确保 Unitree 机器人连网、开启本地服务。

---

> 本文件已生成并保存在 `src/content/docs/00/unitree_rl_lab_unitreerobotics.md`，可直接使用。
