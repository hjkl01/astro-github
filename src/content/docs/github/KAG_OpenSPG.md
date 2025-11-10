---
title: KAG
---


# KAG（OpenSPG 项目）

项目地址: https://github.com/OpenSPG/KAG  

## 主要特性  
- **知识图谱构建**：结合规则与机器学习，自动抽取实体、关系与属性。  
- **可视化分析**：提供交互式图形界面，支持节点搜索、属性过滤与路径分析。  
- **多语言支持**：内置中英文实体识别与多语言翻译组件。  
- **插件化架构**：模块化设计，易于扩展自定义抽取器、匹配器和存储后端。  
- **生态兼容**：可直接导入 OpenSPG 数据集，方便实验复现。  

## 主要功能  
- **文本抽取**：利用 NLP pipeline 将文本中的和关系转换成三元组。  
- **知识融合**：将新抽取的三元组与已有知识库进行去重和版本控制。  
- **问答生成**：基于知识图谱自动生成问答对，支持自然语言对话场景。  
- **数据可视化**：图形化展示网络结构，支持自定义查询。  

## 快速使用  
```bash
# 克隆仓库
git clone https://github.com/OpenSPG/KAG.git
cd KAG

# 创建虚拟环境并安装
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 运行抽取示例
python -m kag.run -c configs/example.yaml
```
- 配置文件 `configs/example.yaml` 说明了数据来源、抽取规则与存储方式。  
- 结果存储在 `output/` 目录下，可直接导入 Neo4j 或其他图数据库。  

## 文档与支持  
- 官方文档：`docs/README.md`  
- 讨论与问题提交：GitHub Issues  

> 如需更多自定义或社区插件，请查看 `plugins/` 目录和 README。  
