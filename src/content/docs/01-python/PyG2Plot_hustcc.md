---
title: PyG2Plot
---

# PyG2Plot 项目

**GitHub 项目地址:** [https://github.com/hustcc/PyG2Plot](https://github.com/hustcc/PyG2Plot)

## 主要特性
PyG2Plot 是一个基于 AntV G2 图形语法开发的 Python 库，用于创建交互式数据可视化图表。它将 Python 的简洁语法与 G2 的强大可视化能力相结合，支持多种图表类型，并提供 Web 渲染支持。主要特性包括：
- **交互式图表**：支持缩放、悬停提示、点击事件等交互功能。
- **跨平台渲染**：使用 VChart 作为底层渲染引擎，支持 Jupyter Notebook、Streamlit 等环境。
- **丰富图表类型**：覆盖柱状图、折线图、散点图、饼图、热力图等多种可视化形式。
- **Python 友好**：纯 Python 接口，无需 JavaScript 知识，即可快速生成图表。
- **自定义配置**：支持主题、颜色、动画等高级自定义选项。
- **轻量级**：依赖少，易于集成到数据分析工作流中。

## 主要功能
- **图表生成**：通过 Python 类和方法快速创建各种图表，支持数据绑定和样式调整。
- **数据处理集成**：无缝兼容 Pandas DataFrame，支持直接传入数据源进行可视化。
- **导出与分享**：可导出为 HTML 文件或静态图像，便于报告和分享。
- **动画与过渡**：内置动画效果，提升用户体验。
- **响应式设计**：图表自动适应容器大小，支持移动端显示。
- **扩展性**：可与 Plotly、Matplotlib 等其他库结合使用。

## 用法
### 安装
```bash
pip install pyg2plot
```

### 基本用法示例
1. **导入库**：
   ```python
   from pyg2plot import Plot
   ```

2. **创建简单折线图**：
   ```python
   data = [
       {"year": "1991", "value": 3},
       {"year": "1992", "value": 4},
       {"year": "1993", "value": 3.5},
       {"year": "1994", "value": 5}
   ]
   line_plot = Plot("Line", data)
   line_plot.render()
   ```

3. **在 Jupyter Notebook 中渲染**：
   ```python
   line_plot.render_notebook()  # 在 Notebook 中显示交互图表
   ```

4. **自定义配置**：
   ```python
   line_plot = Plot("Line", data, 
                    config={
                        "title": {"text": "年度数据趋势"},
                        "xField": "year",
                        "yField": "value",
                        "point": {"size": 5}
                    })
   line_plot.render()
   ```

5. **导出 HTML**：
   ```python
   line_plot.render("output.html")  # 保存为 HTML 文件
   ```

更多高级用法和图表示例，请参考项目文档和 GitHub 仓库中的示例代码。