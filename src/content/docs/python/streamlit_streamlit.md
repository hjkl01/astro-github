
---
title: streamlit
---

# Streamlit 项目

**GitHub 项目地址:** [https://github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)

## 主要特性
Streamlit 是一个开源的 Python 库，用于快速构建和部署数据应用。它将数据科学和机器学习工作流转化为交互式 Web 应用，无需前端开发经验。主要特性包括：
- **简单易用**：使用纯 Python 脚本编写应用，Streamlit 会自动处理 UI 生成和状态管理。
- **交互式组件**：内置滑块、按钮、下拉菜单等小部件，支持实时用户输入和数据可视化。
- **数据集成**：无缝支持 Pandas、NumPy、Matplotlib、Altair 等流行数据科学库。
- **部署友好**：一键部署到 Streamlit Cloud、Heroku 或其他平台，支持缓存机制以优化性能。
- **模块化设计**：支持自定义组件、侧边栏、多页面应用和主题自定义。
- **社区驱动**：活跃的开源社区，提供丰富的插件和示例。

## 主要功能
Streamlit 的核心功能聚焦于数据应用的快速原型开发：
- **数据可视化**：轻松创建图表、地图和仪表板，支持 Plotly、Vega-Lite 等高级可视化工具。
- **机器学习集成**：内置支持 Hugging Face、TensorFlow 和 PyTorch 等框架，用于构建 ML 演示和预测应用。
- **文件上传与处理**：允许用户上传 CSV、图像等文件，并实时处理和显示结果。
- **缓存与优化**：使用 `@st.cache_data` 和 `@st.cache_resource` 装饰器，避免重复计算，提高应用效率。
- **会话状态管理**：通过 `st.session_state` 维护应用状态，支持复杂交互逻辑。
- **多媒体支持**：嵌入视频、音频和 Markdown 内容，增强应用表达力。

## 用法
### 安装
使用 pip 安装：
```
pip install streamlit
```

### 基本用法
1. **创建应用**：编写一个 Python 文件（如 `app.py`），使用 Streamlit 命令导入并调用函数。
   示例代码：
   ```python
   import streamlit as st
   import pandas as pd
   import numpy as np

   st.title("我的第一个 Streamlit 应用")

   # 添加交互元素
   x = st.slider("选择一个值", 0, 100, 50)
   data = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])

   # 显示数据
   st.line_chart(data)
   st.write(f"滑块值: {x}")
   ```

2. **运行应用**：在终端执行：
   ```
   streamlit run app.py
   ```
   这会启动本地服务器，默认在 `http://localhost:8501` 访问应用。

3. **高级用法**：
   - **多页面应用**：在项目根目录创建 `pages/` 文件夹，添加 Python 文件作为子页面。
   - **自定义组件**：使用 `st.components.v1.html` 或社区组件库扩展 UI。
   - **部署**：连接 GitHub 仓库到 Streamlit Cloud，自动构建和托管应用。
   - **配置**：通过 `.streamlit/config.toml` 文件自定义主题、端口等设置。

更多细节请参考官方文档：https://docs.streamlit.io/