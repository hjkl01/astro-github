---
title: Agent-S
---

# Agent S 项目

## 项目地址

https://github.com/simular-ai/Agent-S

## 主要特性

Agent S 是一个开源框架，旨在通过 Agent-Computer Interface 实现与计算机的自主交互。我们的使命是构建能够从过去经验中学习并自主执行复杂任务的智能 GUI Agent。

- **高度模块化**：把 Agent-S 的各种能力拆解成可复用的组件（感知、推理、规划、行动、记忆等），便于快速组合不同功能。
- **多任务与多模态支持**：一次开发即可服务文本、语音、图片等多种输入输出，兼容主流 LLM（OpenAI、Claude、Anthropic 等）。
- **强化学习与搜索**：集成深度 RL、蒙特卡洛树搜索（MCTS）、规划算法，提升 Agent 的决策质量。
- **协作与多 Agent 系统**：支持跨 Agent 共享记忆、对话与任务分配，适合构建团队协作场景。
- **可扩展的插件生态**：通过轻量级插件机制，可插拔自定义数据源、外部接口与工具，让 Agent 直接与数据库、API、软件工具结合。

## 当前结果

在 OSWorld 上，Agent S3 单独使用时达到 62.6%（100 步设置），已超过之前的 SOTA 61.4%（Claude Sonnet 4.5）。通过添加 Behavior Best-of-N，性能进一步提升至 69.9%，使计算机使用 Agent 接近人类水平的准确性（72%）。

Agent S3 还展示了强大的零样本泛化。在 WindowsAgentArena 上，准确率从仅使用 Agent S3 的 50.2% 上升到使用 3 个 rollout 的 56.6%。在 AndroidWorld 上，从 68.1% 上升到 71.6%。

## 主要功能

| 功能           | 说明                                              | 典型使用场景               |
| -------------- | ------------------------------------------------- | -------------------------- |
| **对话代理**   | 通过自然语言交互完成问答、辅助写作、知识检索等    | 客服机器人、写作助手       |
| **计划与执行** | 输入目标 → 生成内容计划 → 自动执行                | 任务管理工具、工作流自动化 |
| **感知整合**   | 支持文本、图片、音频、传感器数据输入              | 视觉问答、语音助手         |
| **知识蒸馏**   | 把大模型压缩为较小模型，以降低推理成本            | 移动端部署、云边协同       |
| **评估与监控** | 提供 MSE、BLEU、ROUGE 等指标，实时监控 Agent 表现 | 开发调试、模型迭代         |

## 用法

### 安装

```bash
pip install gui-agents
```

如果您想在更改时测试 Agent S3，请克隆仓库并使用以下方式安装：

```bash
pip install -e .
```

不要忘记 `brew install tesseract`！Pytesseract 需要此额外安装才能工作。

### API 配置

#### 选项 1：环境变量

添加到您的 `.bashrc`（Linux）或 `.zshrc`（MacOS）：

```bash
export OPENAI_API_KEY=<YOUR_API_KEY>
export ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>
export HF_TOKEN=<YOUR_HF_TOKEN>
```

#### 选项 2：Python 脚本

```python
import os
os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"
```

### 支持的模型

我们支持 Azure OpenAI、Anthropic、Gemini、Open Router 和 vLLM 推理。请参阅 [models.md](models.md) 获取详细信息。

### 接地模型（必需）

为了获得最佳性能，我们推荐 [UI-TARS-1.5-7B](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B) 在 Hugging Face Inference Endpoints 或其他提供商上托管。请参阅 [Hugging Face Inference Endpoints](https://huggingface.co/learn/cookbook/en/enterprise_dedicated_endpoints) 获取设置说明。

### CLI

注意，这正在运行 Agent S3，我们改进的 Agent，没有 bBoN。

使用必需的参数运行 Agent S3：

```bash
agent_s \
    --provider openai \
    --model gpt-5-2025-08-07 \
    --ground_provider huggingface \
    --ground_url http://localhost:8080 \
    --ground_model ui-tars-1.5-7b \
    --grounding_width 1920 \
    --grounding_height 1080
```

#### 本地编码环境（可选）

对于需要代码执行的任务（例如，数据处理、文件操作、系统自动化），您可以启用本地编码环境：

```bash
agent_s \
    --provider openai \
    --model gpt-5-2025-08-07 \
    --ground_provider huggingface \
    --ground_url http://localhost:8080 \
    --ground_model ui-tars-1.5-7b \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --enable_local_env
```

⚠️ **警告**：本地编码环境会在您的机器上本地执行任意 Python 和 Bash 代码。只有在受信任的环境中使用此功能，并使用受信任的输入。

#### 必需参数

- **`--provider`**：主生成模型提供商（例如，openai、anthropic 等）- 默认："openai"
- **`--model`**：主生成模型名称（例如，gpt-5-2025-08-07）- 默认："gpt-5-2025-08-07"
- **`--ground_provider`**：接地模型的提供商 - **必需**
- **`--ground_url`**：接地模型的 URL - **必需**
- **`--ground_model`**：接地模型的模型名称 - **必需**
- **`--grounding_width`**：从接地模型输出的坐标分辨率的宽度 - **必需**
- **`--grounding_height`**：从接地模型输出的坐标分辨率的高度 - **必需**

#### 可选参数

- **`--model_temperature`**：所有模型调用固定的温度（对于 o3 等模型必要设置为 1.0，但对于其他模型可以留空）

#### 接地模型维度

接地宽度和高度应匹配您的接地模型的输出坐标分辨率：

- **UI-TARS-1.5-7B**：使用 `--grounding_width 1920 --grounding_height 1080`
- **UI-TARS-72B**：使用 `--grounding_width 1000 --grounding_height 1000`

#### 可选参数

- **`--model_url`**：主生成模型的自定义 API URL - 默认：""
- **`--model_api_key`**：主生成模型的 API 密钥 - 默认：""
- **`--ground_api_key`**：接地模型端点的 API 密钥 - 默认：""
- **`--max_trajectory_length`**：轨迹中保留的图像转数最大数量 - 默认：8
- **`--enable_reflection`**：启用反射 Agent 以协助工作者 Agent - 默认：True
- **`--enable_local_env`**：启用本地编码环境以进行代码执行（警告：本地执行任意代码）- 默认：False

#### 本地编码环境详情

本地编码环境使 Agent S3 能够直接在您的机器上执行 Python 和 Bash 代码。这对于以下任务特别有用：

- **数据处理**：操作电子表格、CSV 文件或数据库
- **文件操作**：批量文件处理、内容提取或文件组织
- **系统自动化**：配置更改、系统设置或自动化脚本
- **代码开发**：编写、编辑或执行代码文件
- **文本处理**：文档操作、内容编辑或格式化

启用后，Agent 可以使用 `call_code_agent` 操作来执行代码块，以编程方式完成无法通过 GUI 交互完成的任务。

**要求：**

- **Python**：用于运行 Agent S3 的相同 Python 解释器（自动检测）
- **Bash**：在 `/bin/bash` 上可用（macOS 和 Linux 上的标准）
- **系统权限**：Agent 以运行它的用户的相同权限运行

**安全注意事项：**

- 本地环境以运行 Agent 的用户的相同权限执行任意代码
- 仅在受信任的环境中启用此功能
- 对于不受信任的任务，请考虑在沙盒环境中运行
- Bash 脚本以 30 秒超时执行，以防止挂起的进程

### `gui_agents` SDK

首先，我们导入必要的模块。`AgentS3` 是 Agent S3 的主要 Agent 类。`OSWorldACI` 是我们的接地 Agent，它将 Agent 操作转换为可执行的 Python 代码。

```python
import pyautogui
import io
from gui_agents.s3.agents.agent_s import AgentS3
from gui_agents.s3.agents.grounding import OSWorldACI
from gui_agents.s3.utils.local_env import LocalEnv  # 可选：用于本地编码环境

# 加载您的 API 密钥。
from dotenv import load_dotenv
load_dotenv()

current_platform = "linux"  # "darwin", "windows"
```

接下来，我们定义引擎参数。`engine_params` 用于主 Agent，`engine_params_for_grounding` 用于接地。对于 `engine_params_for_grounding`，我们支持自定义端点，如 HuggingFace TGI、vLLM 和 Open Router。

```python
engine_params = {
  "engine_type": provider,
  "model": model,
  "base_url": model_url,           # 可选
  "api_key": model_api_key,        # 可选
  "temperature": model_temperature # 可选
}

# 从自定义端点加载接地引擎
ground_provider = "<your_ground_provider>"
ground_url = "<your_ground_url>"
ground_model = "<your_ground_model>"
ground_api_key = "<your_ground_api_key>"

# 根据您的模型的输出坐标分辨率设置接地维度
# UI-TARS-1.5-7B：grounding_width=1920, grounding_height=1080
# UI-TARS-72B：grounding_width=1000, grounding_height=1000
grounding_width = 1920  # 从接地模型输出的坐标分辨率的宽度
grounding_height = 1080  # 从接地模型输出的坐标分辨率的高度

engine_params_for_grounding = {
  "engine_type": ground_provider,
  "model": ground_model,
  "base_url": ground_url,
  "api_key": ground_api_key,  # 可选
  "grounding_width": grounding_width,
  "grounding_height": grounding_height,
}
```

然后，我们定义接地 Agent 和 Agent S3。

```python
# 可选：启用本地编码环境
enable_local_env = False  # 设置为 True 以启用本地代码执行
local_env = LocalEnv() if enable_local_env else None

grounding_agent = OSWorldACI(
    env=local_env,  # 为代码执行能力传递 local_env
    platform=current_platform,
    engine_params_for_generation=engine_params,
    engine_params_for_grounding=engine_params_for_grounding,
    width=1920,  # 可选：屏幕宽度
    height=1080  # 可选：屏幕高度
)

agent = AgentS3(
    engine_params,
    grounding_agent,
    platform=current_platform,
    max_trajectory_length=8,  # 可选：保留的最大图像转数
    enable_reflection=True     # 可选：启用反射 Agent
)
```

最后，让我们查询 Agent！

```python
# 获取截图。
screenshot = pyautogui.screenshot()
buffered = io.BytesIO()
screenshot.save(buffered, format="PNG")
screenshot_bytes = buffered.getvalue()

obs = {
  "screenshot": screenshot_bytes,
}

instruction = "Close VS Code"
info, action = agent.predict(instruction=instruction, observation=obs)

exec(action[0])
```

请参阅 `gui_agents/s3/cli_app.py` 以获取推理循环的更多详细信息。

### OSWorld

要将 Agent S3 部署到 OSWorld，请遵循 [OSWorld 部署说明](osworld_setup/s3/OSWorld.md)。

项目适合 AI 爱好者和开发者使用，文档详见仓库的 README.md。
