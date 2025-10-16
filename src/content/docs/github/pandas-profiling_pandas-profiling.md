
---
title: pandas-profiling
---

# pandas-profiling 项目

## 项目地址
[GitHub 项目地址](https://github.com/pandas-profiling/pandas-profiling)

## 主要特性
pandas-profiling 是一个 Python 库，用于生成数据分析报告。它基于 pandas DataFrame，自动分析数据集的统计信息、相关性和模式，提供可视化图表和摘要报告。主要特性包括：
- **自动化分析**：快速生成全面的数据集概述，包括缺失值、唯一值分布和数据类型检测。
- **可视化支持**：内置图表，如直方图、散点图和相关性热图，帮助可视化数据分布和关系。
- **报告生成**：输出 HTML 格式的交互式报告，便于分享和探索。
- **高效处理**：支持大规模数据集，通过并行计算和内存优化，提高性能。
- **扩展性**：可自定义分析选项，集成到 Jupyter Notebook 或其他工作流中。

## 主要功能
- **数据集摘要**：计算变量类型、缺失值比例、唯一值计数和基本统计（如均值、标准差）。
- **相关性分析**：检测数值变量间的相关性，并可视化潜在关联。
- **异常检测**：识别高基数变量、零方差列和不平衡类别。
- **交互式报告**：生成可排序、可过滤的 HTML 报告，支持警告和建议（如数据清洗提示）。
- **多语言支持**：报告可生成多种语言版本，包括中文。

## 用法
1. **安装**：
   使用 pip 安装：
   ```
   pip install pandas-profiling
   ```

2. **基本用法**：
   在 Python 环境中导入并生成报告：
   ```python
   import pandas as pd
   from pandas_profiling import ProfileReport

   # 加载数据
   df = pd.read_csv('your_dataset.csv')

   # 生成报告
   profile = ProfileReport(df, title="数据集报告", explorative=True)
   profile.to_file("report.html")
   ```
   这将生成一个名为 `report.html` 的文件，可在浏览器中打开查看。

3. **高级选项**：
   - 自定义报告：`ProfileReport(df, minimal=True)` 用于简化版本，或指定 `pool_size` 调整并行处理。
   - Jupyter 集成：在 Notebook 中直接运行 `profile` 以内嵌显示报告。
   - 示例：对于小型数据集，报告生成通常只需几秒；对于大型数据，可添加 `sample` 参数采样分析。

更多细节请参考项目文档。