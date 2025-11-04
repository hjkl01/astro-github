
---
title: social-analyzer
---


# Social Analyzer

项目地址: https://github.com/qeeqbox/social-analyzer

## 主要特性

- **多平台数据采集**  
  支持 Twitter、Instagram、Facebook 等主流社交网络的公开数据抓取（需配合各平台 API 访问令牌）。  
- **情感与主题分析**  
  内置 NLP 模型，可对采集内容进行情感倾向、关键词提取、话题聚类等分析。  
- **趋势与热点监测**  
  根据时间序列自动识别热门话题、关键事件，生成趋势图表。  
- **社交网络结构分析**  
  通过用户互动关系构建网络图，计算节点度、中心度等网络指标。  
- **可视化与报表**  
  生成交互式图表（基于 Plotly / Dash）以及 PDF/HTML 报告，方便展示与分享。  
- **命令行与 API 接口**  
  提供 CLI 工具和 RESTful API，支持自动化脚本调用与集成。  

## 功能概览

| 功能 | 说明 |
|------|------|
| 数据抓取 | `social-analyzer collect` <br> 读取 `config.yaml`，按平台抓取最近 7 天数据 |
| 分析处理 | `social-analyzer analyze` <br> 对已抓取的数据进行情感、主题、热点、网络分析 |
| 可视化 | `social-analyzer visualize` <br> 生成并打开交互式仪表盘 |
| 报告生成 | `social-analyzer report` <br> 输出 PDF/HTML 报告到 `output/` 目录 |
| API 服务器 | `social-analyzer serve` <br> 启动本地 API 服务器，默认端口 8000 |

## 使用方法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/qeeqbox/social-analyzer.git
   cd social-analyzer
   ```

2. **安装依赖**  
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **配置**  
   编辑 `config.yaml`，填写 API 访问令牌、抓取时间范围、输出路径等信息。

4. **执行流程**  
   ```bash
   # ① 数据抓取
   python -m social_analyzer.collect

   # ② 数据分析
   python -m social_analyzer.analyze

   # ③ 可视化
   python -m social_analyzer.visualize

   # ④ 报告生成
   python -m social_analyzer.report
   ```

5. **启动 API 服务器**（可选）  
   ```bash
   python -m social_analyzer.serve
   ```

6. **使用 REST API**  
   - `GET /api/summary`：获取最新分析摘要  
   - `GET /api/graph`：获取社交网络图数据  
   - `POST /api/refresh`：触发一次完整抓取 & 分析流程  

## 快速示例

```python
# 直接在 Python 中调用
from social_analyzer import Analyzer

analyzer = Analyzer(config_file='config.yaml')
analyzer.collect()   # 抓取数据
analyzer.analyze()   # 分析
report = analyzer.report()   # 生成报告对象
report.save('output/final_report.pdf')
```

> **提示**：对大规模数据集建议使用云端数据库或分布式存储，以避免内存瓶颈。

--- 

> 以上内容仅为简要概览，更多深入使用细节请参考官方文档与代码注释。