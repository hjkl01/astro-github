
---
title: tinker-cookbook
---

# Tinker Cookbook  
**GitHub 项目地址**: https://github.com/thinking-machines-lab/tinker-cookbook  

## 主要特性
- **全栈调研工具**：整合前后端代码、实验脚本与结果可视化，方便做实验复现与调研。  
- **模块化结构**：分为 `tinker-core`（核心逻辑）与 `tinker-experiments`（示例实验），可按需使用。  
- **可扩展插件**：通过插件机制快速接入新的算法、模型或实验场景，插件 API 简洁易用。  
- **自动化实验管理**：支持实验配置、批量提交、结果追踪，兼容多种计算资源（本地GPU、云端）。  
- **可视化结果**：内置 Tableau/Plotly 风格的图表，支持在线浏览与导出。  

## 功能概览
- **数据预处理**：提供多种常见的数据清洗、特征工程模板。  
- **模型训练**：支持常见深度学习框架（PyTorch、TensorFlow）训练脚本。  
- **实验版本控制**：实验配置、代码与模型一键提交到 GitHub/MLflow。  
- **结果比较**：集成 A/B 对比、混淆矩阵、ROC 曲线等评测工具。  
- **报告自动生成**：按预测任务自动生成 Markdown/HTML 报告，附完整实验日志。  

## 用法示例
```bash
# 1. 克隆仓库
git clone https://github.com/thinking-machines-lab/tinker-cookbook.git
cd tinker-cook2. 安装依赖
pip install -r requirements.txt

# 3. 运行示例实验
python tinker-experiments/run_demo.py --config config/demo.yaml

# 4. 查看结果
open docs/demo_report.html
```

> **提示**：所有实验配置均在 `config/` 目录下，按需修改后即可启动。  

---  

> 注：项目 README 已更新，详见官方仓库。