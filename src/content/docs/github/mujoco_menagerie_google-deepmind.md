---
title: mujoco_menagerie
---

# MuJoCo Menagerie

MuJoCo Menagerie 是由 Google DeepMind 维护的一个高质量模型集合，用于 MuJoCo 物理引擎。该项目旨在为社区提供经过精心设计的模型，这些模型在 MuJoCo 中能够直接良好运行，避免了创建不良模型的问题。

## 功能

- **模型集合**：包含多种类型的机器人模型，包括：
  - 机械臂（Arms）：如 Franka Panda、KUKA iiwa14、Universal Robots UR5e 等。
  - 双足机器人（Bipeds）：如 Agility Cassie。
  - 四足机器人（Quadrupeds）：如 Unitree Go2、ANYmal B、Boston Dynamics Spot 等。
  - 人形机器人（Humanoids）：如 Unitree H1、PAL TALOS 等。
  - 无人机（Drones）：如 Bitcraze Crazyflie 2、Skydio X2。
  - 末端执行器（End-effectors）：如 Shadow Hand、Robotiq 2F-85 等。
  - 移动操纵器（Mobile Manipulators）：如 Google Robot、Stanford TidyBot 等。
  - 其他：如生物力学模型（flybody）、传感器（Intel Realsense D435i）等。

- **模型质量**：每个模型都经过精心设计，确保在 MuJoCo 中稳定运行。项目引入了质量等级系统（A+ 到 C），以帮助用户了解模型的真实性和稳定性。

- **兼容性**：支持 MJX（MuJoCo XLA）变体，一些模型提供 MJX 兼容版本。

- **开源**：所有模型都基于开源许可证，每个模型目录下有独立的 LICENSE 文件。

## 用法

### 前提条件

需要安装 MuJoCo。可以从 GitHub releases 下载预构建二进制文件，或通过 PyPI 安装 Python 绑定：`pip install mujoco`。

### 加载模型

#### 通过 robot-descriptions 包

安装 `robot_descriptions` 包：`pip install robot_descriptions`。

然后加载模型：

```python
import mujoco

# 加载特定模型描述
from robot_descriptions import panda_mj_description
model = mujoco.MjModel.from_xml_path(panda_mj_description.MJCF_PATH)

# 直接加载 MjModel 实例
from robot_descriptions.loaders.mujoco import load_robot_description
model = load_robot_description("panda_mj_description")

# 加载模型变体，如无夹持器的 Panda
model = load_robot_description("panda_mj_description", variant="panda_nohand")
```

#### 通过 git clone

克隆仓库：

```bash
git clone https://github.com/google-deepmind/mujoco_menagerie.git
```

使用 Python 查看器交互式探索模型：

```bash
python -m mujoco.viewer --mjcf mujoco_menagerie/unitree_go2/scene.xml
```

### 模型结构

每个模型目录包含：

- `assets/`：3D 网格文件（.stl 或 .obj）。
- `<model>.xml`：MJCF 模型定义。
- `scene.xml`：包含模型的场景文件（带平面、光源等）。
- `README.md`：模型生成详细说明。
- `LICENSE`：许可证信息。
- 可选的 MJX 变体文件。

## 贡献

项目欢迎社区贡献，如添加新模型或改进现有模型。请参考 CONTRIBUTING.md 获取详细信息。

## 引用

如果在工作中使用 Menagerie，请使用以下引用：

```
@software{menagerie2022github,
  author = {Zakka, Kevin and Tassa, Yuval and {MuJoCo Menagerie Contributors}},
  title = {{MuJoCo Menagerie: A collection of high-quality simulation models for MuJoCo}},
  url = {http://github.com/google-deepmind/mujoco_menagerie},
  year = {2022},
}
```
