---
title: Tinker Cookbook
---

## 功能介绍

Tinker Cookbook 是由 Thinking Machines Lab 开发的开源项目，旨在帮助研究者和开发者自定义语言模型。它提供了两个主要库：

- **tinker**：一个训练 SDK，用于微调语言模型。用户通过 API 请求发送数据，平台处理分布式训练的复杂性。
- **tinker-cookbook**：基于 Tinker API 的实用示例库，提供常见的抽象和真实场景的微调示例，帮助用户快速上手语言模型的定制化训练。

该项目支持多种训练场景，包括监督学习、强化学习、偏好学习、工具使用、多代理系统等。通过提供的 recipes，用户可以轻松实现聊天模型的微调、数学推理能力的提升、偏好对齐等任务。

## 用法

### 安装步骤

1. 通过 [waitlist](https://thinkingmachines.ai/tinker) 注册 Tinker 服务。
2. 在 [console](https://tinker-console.thinkingmachines.ai) 创建 API 密钥，并将其设置为环境变量 `TINKER_API_KEY`。
3. 安装 Tinker Python 客户端：`pip install tinker`。
4. 推荐在虚拟环境中安装 `tinker-cookbook`：`pip install -e .`。

### 基本用法

使用 Tinker 的基本原语进行训练：

```python
import tinker

service_client = tinker.ServiceClient()
training_client = service_client.create_lora_training_client(
    base_model="meta-llama/Llama-3.2-1B", rank=32
)
training_client.forward_backward(...)
training_client.optim_step(...)
training_client.save_state(...)
training_client.load_state(...)

sampling_client = training_client.save_weights_and_get_sampling_client(name="my_model")
sampling_client.sample(...)
```

### 示例 Recipes

项目提供了多种预构建的 recipes，位于 `tinker_cookbook/recipes/` 文件夹中：

- **聊天监督学习**：在对话数据集如 Tulu3 上进行监督微调。
- **数学推理**：通过奖励正确回答数学问题来提升推理能力。
- **偏好学习**：展示三阶段 RLHF 管道：监督微调、学习奖励模型、对抗奖励模型进行 RL。
- **工具使用**：训练 LLM 更好地使用检索工具回答问题。
- **提示蒸馏**：将长而复杂的指令内部化到 LLM 中。
- **多代理**：优化 LLM 与其他 LLM 或自身对弈。

每个 recipe 文件夹包含 README.md，详细说明实现细节、运行命令和预期性能。

### 实用工具

- `renderers`：将 tokens 转换为结构化聊天消息对象，反之亦然。
- `hyperparam_utils`：帮助计算适合 LoRA 的超参数。
- `evaluation`：提供评估 Tinker 模型的抽象，并支持与 InspectAI 集成以便在标准基准上评估。

## 贡献

项目欢迎社区贡献，尤其在私人 beta 结束后。反馈可发送至 [tinker@thinkingmachines.ai](mailto:tinker@thinkingmachines.ai)。

## 引用

如果在研究中使用，请引用：

```
Thinking Machines Lab, 2025. Tinker. https://thinkingmachines.ai/tinker/.
```

BibTeX：

```
@misc{tml2025tinker,
  author = {Thinking Machines Lab},
  title = {Tinker},
  year = {2025},
  url = {https://thinkingmachines.ai/tinker/},
}
```
