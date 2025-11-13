---
title: ML-From-Scratch
---

# ML-From-Scratch

## 功能

Machine Learning From Scratch 是由 eriklindernoren 创建的开源项目，提供用 Python 从头实现的基本机器学习模型和算法。项目使用 NumPy 库，专注于算法的透明性和可访问性，而不是计算效率。

该项目涵盖了从线性回归到深度学习的广泛主题，包括：

- **监督学习**：线性回归、逻辑回归、决策树、随机森林、支持向量机、朴素贝叶斯、多层感知机等。
- **无监督学习**：K-Means、DBSCAN、高斯混合模型、主成分分析、生成对抗网络、遗传算法等。
- **强化学习**：深度 Q 网络。
- **深度学习**：神经网络、卷积神经网络、循环神经网络等。

项目提供了清晰的代码实现，帮助学习者理解机器学习算法的内部机制。

## 用法

1. **克隆仓库**：

   ```bash
   git clone https://github.com/eriklindernoren/ML-From-Scratch
   cd ML-From-Scratch
   ```

2. **安装依赖**：

   ```bash
   python setup.py install
   ```

3. **运行示例**：
   项目包含多个示例脚本，可以直接运行以查看算法效果。例如：
   - 多项式回归：`python mlfromscratch/examples/polynomial_regression.py`
   - 卷积神经网络分类：`python mlfromscratch/examples/convolutional_neural_network.py`
   - DBSCAN 聚类：`python mlfromscratch/examples/dbscan.py`
   - 生成对抗网络生成手写数字：`python mlfromscratch/unsupervised_learning/generative_adversarial_network.py`
   - 深度 Q 网络强化学习：`python mlfromscratch/examples/deep_q_network.py`

每个示例都会输出训练过程和结果，帮助用户理解算法的工作原理。
