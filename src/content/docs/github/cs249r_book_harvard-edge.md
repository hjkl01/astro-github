
---
title: cs249r_book
---


# Harvard Edge CS 249R 课程材料

> 项目地址：[https://github.com/harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book)

## 主要特性

| 特色 | 说明 |
|------|------|
| **完整课程内容** | 课程大纲、讲义、作业、实验、参考资料一并包含，方便快速查阅。 |
| **Jupyter Notebook 实战** | 每章节均配有可运行的 Notebook，涵盖数据处理、可视化、机器学习等实战代码。 |
| **Docker 环境** | 提供 `Dockerfile` 与 `docker-compose.yml`，一键构建全部依赖（Python、R、所需库）并保证版本一致。 |
| **完整数据集** | 所有实验与作业使用的数据被打包，减轻下载负担。 |
| **脚本化的实验流程** | 通过 `scripts/` 中的入口脚本可批量执行实验或刷新结果。 |
| **社区友好** | 包含 README、贡献指南、Issue 模板，易于社区协作。 |

## 功能概览

1. **课程结构**  
   - `lectures/`：讲义与录播链接。  
   - `assignments/`：作业说明及 starter code。  
   - `exercises/`：实验代码与数据。  

2. **Notebook 核心模块**  
   - **数据清洗**：`clean_data.ipynb` 包含 Pandas、NumPy 的最佳实践。  
   - **可视化**：`visualize.ipynb` 展示 Seaborn、Plotly 等工具。  
   - **机器学习**：`ml_experiments.ipynb` 涵盖分类、回归、聚类等模型。  
   - **深度学习**：`deep_learning.ipynb` 用 TensorFlow/Keras 实现模型。  

3. **自动化脚本**  
   ```bash
   # 在 root 目录下执行
   python scripts/run_all.py   # 运行所有 notebook
   python scripts/refresh_data.py   # 更新数据集
   ```

4. **Docker 使用**  
   ```bash
   # 构建镜像
   docker build -t cs249r_image .

   # 运行容器
   docker run -it --rm -v $(pwd):/workspace cs249r_image bash
   ```

## 使用方法

1. **克隆仓库**

   ```bash
   git clone https://github.com/harvard-edge/cs249r_book.git
   cd cs249r_book
   ```

2. **准备环境**

   *若使用 Docker*  
   ```bash
   docker build -t cs249r_image .
   docker run -it --rm -v "$(pwd)":/workspace cs249r_image bash
   ```

   *若本地安装*  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **运行 Notebook**

   ```bash
   jupyter lab
   # 在浏览器中打开对应文件即可
   ```

4. **执行实验脚本**

   ```bash
   python scripts/run_all.py
   ```

5. **查看作业结果**

   - 参考 `results/` 目录，或在 notebooks 中直接观察输出。

> **注意**：每个 Notebook 依赖的库已在 `requirements.txt` 或 `environment.yml` 中列出，确保一次性安装后即可正常运行。

## 贡献与支持

- 在 Issues 中报告错误或功能。  
- PR 必须遵循 `CONTRIBUTING.md` 指南。  
- 详细的贡献流程、测试脚本、代码规范请参阅 repo 主页。

---

> 以上即为 CS 249R 课程材料的主要特性、功能与使用方法概览。祝学习愉快！
