
---
title: lerobot
---


# leRobot - Hugging Face 机器学习与机器人技术的整合框架

**项目地址**: [https://github.com/huggingface/lerobot](https://github.com/huggingface/lerobot)

## 主要特性

| 特性 | 说明 |
|------|------|
| **多环境支持** | 集成了 IsaacGym、MuJoCo、PyBullet、Robosuite 等主流物理仿真器，支持 60+ 机器人任务与情景。 |
| **统一数据接口** | 提供 `lerobot.dataset` 包，支持从多种数据源（视频、传感器、强化学习日志）构建、加载、预处理与增强。 |
| **强化学习算法** | 内置多种 RL 算法（PPO、DQN、SAC、TD3 等）以及自定义策略网络，支持分布式训练与多 GPU 并行。 |
| **模型与数据共享** | 与 Hugging Face Hub 无缝对接，支持上传/下载模型、数据集、实验结果；可在 Hub 上共享并复现实验。 |
| **实验管理** | 通过 `lerobot.trainers` 提供实验配置、日志、监控（WandB、TensorBoard）等完整训练管线。 |
| **可扩展性** | 通过插件式设计，用户可轻松添加自定义环境、算法、奖励函数等；支持自定义任务脚本。 |
| **文档与示例** | 详细的教程、API 文档与可直接运行的 Jupyter/脚本示例，降低入门门槛。 |

## 核心功能

- **环境封装**：`lerobot.envs` 提供统一的 Gym 接口，可直接使用 `gym.make("LegoRobot-v0")` 等方式创建环境。  
- **数据集管理**：`lerobot.datasets` 支持从视频、机器人传感器日志等生成 `Trajectory` 或 `Image` 数据集，支持在线增量训练。  
- **训练器**：`lerobot.trainers` 提供 `PPOTrainer`, `SACTrainer`, `DQNTrainer` 等，支持多种学习率调度、奖励归一化、经验回放。  
- **评估与部署**：`lerobot.eval` 可在仿真或真实机器人上跑评估脚本；支持导出 ONNX / TensorRT、ROS 包等。  
- **实验可视化**：内置 TensorBoard、WandB、Neptune 等日志工具，方便跟踪训练进度与超参调优。  

## 快速上手

```bash
# 1. 安装 leRobot
pip install le-robot

# 2. 运行官方示例（PPO + IsaacGym）
python -m lerobot.trainers.ppo \
  --env IsaacGym-PointGoal-v0 \
  --config configs/ppo.yaml \
  --output_dir ./results/ppo_pointgoal
```

### 代码示例（自定义环境 + PPO）

```python
from lerobot.envs import make
from lerobot.trainers import PPOTrainer
from lerobot.trainers.configs import get_config

# 创建自定义环境
env = make("LegoRobot-v0")

# 读取配置
config = get_config("ppo.yaml")
config.env_name = "LegoRobot-v0"

# 初始化训练器
trainer = PPOTrainer(env, config)

# 开始训练
trainer.train()
```

### 在 Hugging Face Hub 上分享模型

```bash
# 登录 Hugging Face
huggingface-cli login

# 上传模型
python -m lerobot.trainers.export \
  --model_path ./results/ppo_pointgoal/checkpoint-1000 \
  --repo_id username/lerobot-ppo-pointgoal \
  --push_to_hub
```

## 文档与资源

- **官方文档**: https://huggingface.co/docs/lerobot  
- **教程**: https://github.com/huggingface/lerobot/tree/main/tutorials  
- **示例代码**: https://github.com/huggingface/lerobot/tree/main/examples  
- **讨论社区**: https://discuss.huggingface.co/t/lerobot

---

> **提示**：在使用 leRobot 之前，请确保已安装相应的仿真器（如 IsaacGym、MuJoCo）并配置好环境变量。  
> 
> 更多信息请参考项目的 README 与 Wiki。