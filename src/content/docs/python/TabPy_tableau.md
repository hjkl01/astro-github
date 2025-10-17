
---
title: TabPy
---

# TabPy 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/tableau/TabPy)

## 主要特性
TabPy 是 Tableau 开发的一个开源工具，用于将 Python 脚本与 Tableau 集成。它允许用户在 Tableau 中执行自定义 Python 代码，从而扩展数据分析和可视化的能力。主要特性包括：
- **Python 脚本执行**：支持在 Tableau 中调用 Python 函数，实现复杂的数据处理和机器学习任务。
- **服务器架构**：基于客户端-服务器模型，TabPy 服务器处理 Python 代码的执行，确保安全性和性能。
- **多语言支持**：核心使用 Python，但可扩展到其他脚本语言。
- **安全性**：提供沙箱环境，限制外部访问，防止潜在的安全风险。
- **开源与社区驱动**：基于 MIT 许可，鼓励社区贡献和扩展。

## 主要功能
- **数据转换与分析**：在 Tableau 的计算字段中使用 Python 进行数据清洗、统计分析或机器学习预测。
- **外部库集成**：支持 NumPy、Pandas、Scikit-learn 等流行 Python 库，允许高级分析如回归、聚类等。
- **实时执行**：TabPy 服务器可处理 Tableau 仪表板中的动态查询，提供实时结果。
- **部署灵活性**：支持本地部署或云端运行，适用于个人开发者和企业环境。
- **错误处理**：内置日志和调试工具，帮助用户诊断 Python 代码问题。

## 用法
1. **安装**：
   - 确保安装 Python 3.6+ 和 Tableau Desktop/Server。
   - 通过 pip 安装 TabPy：`pip install tabpy`。
   - 启动服务器：`tabpy`（默认端口 9004）。

2. **部署脚本**：
   - 在 TabPy 服务器上部署 Python 函数，例如使用 `tabpy.deploy()` 命令上传脚本。
   - 示例脚本：定义一个函数如 `def multiply(x, y): return x * y`，然后部署为端点。

3. **在 Tableau 中使用**：
   - 在 Tableau 的计算字段中输入：`SCRIPT_REAL("return tabpy.query('multiply', _arg1, _arg2)", AVG([Sales]))`。
   - 参数 `_arg1`、`_arg2` 等对应 Tableau 字段。
   - 连接到 TabPy 服务器（默认 localhost:9004），执行查询。

4. **高级用法**：
   - 对于机器学习：部署 scikit-learn 模型，Tableau 可调用预测函数。
   - 监控：使用 TabPy 的 Web 接口（http://localhost:9004）查看状态和日志。
   - 停止服务器：运行 `tabpy stop`。

更多细节请参考项目文档和示例。