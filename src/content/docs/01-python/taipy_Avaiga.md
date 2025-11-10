---
title: taipy
---

# Taipy 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/Avaiga/taipy)

## 主要特性
Taipy 是一个开源的 Python 库，专为构建和部署数据驱动的 Web 应用程序而设计。它将数据科学、机器学习和业务逻辑无缝集成到交互式 Web 界面中。主要特性包括：
- **声明式 UI 开发**：使用 Python 代码定义用户界面，无需前端技能，支持动态更新和响应式设计。
- **端到端管道管理**：内置数据管道功能，支持数据处理、模型训练和可视化的一体化工作流。
- **可视化支持**：集成 Chart.js 和其他库，提供丰富的图表和仪表盘组件，便于数据探索和展示。
- **多页面应用**：支持单页或多页 Web 应用构建，易于扩展复杂项目。
- **跨平台兼容**：基于 Web 技术，可在浏览器中运行，支持桌面和移动端访问。
- **开源与社区驱动**：Apache 2.0 许可，活跃社区，提供丰富的文档和示例。

## 主要功能
Taipy 的核心功能聚焦于简化 AI 和数据应用开发：
- **页面和组件管理**：通过 `tpy.Page` 和各种 GUI 组件（如按钮、输入框、图表）构建交互界面。
- **数据管道（Pipeline）**：定义任务、数据节点和场景，实现自动化数据流和版本控制。
- **状态管理**：使用 `State` 类处理前后端状态同步，支持实时更新。
- **可视化与图表**：内置支持线图、柱状图、热力图等，结合 Pandas 和 NumPy 等库处理数据。
- **部署与运行**：一键启动 Web 服务器，支持生产环境部署。
- **扩展性**：可集成 TensorFlow、Scikit-learn 等 ML 框架，适用于数据科学和业务分析场景。

## 用法
### 安装
使用 pip 安装：
```
pip install taipy
```

### 基本用法示例
1. **创建简单页面**：
   ```python
   from taipy import Gui

   def submit_action(state):
       state.value = state.input_value.upper()

   pages = {
       "/": "<h1>欢迎使用 Taipy</h1><|{input_value}|input|><|submit|button|on_action=submit_action|><|value|text|>"
   }

   if __name__ == "__main__":
       Gui(pages=pages).run(use_reloader=True)
   ```
   这将启动一个 Web 应用，用户输入文本后点击按钮转换为大写显示。

2. **数据管道示例**：
   ```python
   from taipy import Config, Scope
   from taipy.core import Pipeline

   # 配置数据节点和任务
   config_data = Config.load_data_node_config("data", Scope.SCENARIO)
   config_task = Config.task_config("task", function=process_data, input=config_data)
   config_pipeline = Config.pipeline_config("pipeline", [config_task])

   # 运行管道
   scenario = Pipeline("my_scenario", config_pipeline)
   scenario.run()
   ```

3. **运行应用**：
   - 执行 Python 脚本后，访问 `http://localhost:5000` 查看应用。
   - 对于复杂项目，参考官方文档配置多场景和高级组件。

更多细节请参考项目文档和示例仓库。