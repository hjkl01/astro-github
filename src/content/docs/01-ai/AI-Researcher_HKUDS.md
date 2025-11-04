
---
title: AI-Researcher
---

# AI-Researcher (HKUDS)

<https://github.com/HKUDS/AI-Researcher>

---

## 项目概述  
AI-Researcher 是一个基于 GPT‑4 与 LangChain 的开源研究助手，旨在帮助科研人员快速获取文献信息、生成实验方案、撰写论文摘要等。通过命令行或 Web UI 交互，用户可以在短时间内完成从文献检索到实验代码的完整流程。

---

## 主要特性  
| 功能 | 说明 |
|------|------|
| **文献检索 & 摘要** | 输入 arXiv ID 或 PDF，系统自动提取关键信息并生成多段式摘要。 |
| **系统综述** | 根据关键词或主题自动搜集相关论文，并生成结构化综述。 |
| **实验设计** | 依据论文数据与目标，建议实验流程、超参数、评价指标。 |
| **代码生成** | 自动生成 PyTorch / TensorFlow / Jupyter Notebook 代码片段，支持自定义任务。 |
| **问答交互** | 通过自然语言提问，系统可在已检索文献中搜索答案或生成解释。 |
| **多模态支持** | 支持 PDF、Markdown、Word 等多种文件格式的内容解析。 |
| **可扩展插件** | 通过插件化接口，可以接入自定义 LLM、检索器或数据源。 |

---

## 功能细节  

- **文献检索**  
  - `search_arxiv(query)`：返回与查询关键词匹配的 arXiv 论文列表。  
  - `download_pdf(arxiv_id)`：下载对应论文 PDF。  

- **摘要生成**  
  - `summarize(pdf_path, level="short")`：生成短/中/长摘要，支持多段落输出。  

- **实验方案**  
  - `design_experiment(paper_id, task)`：根据论文目标生成实验流程图、代码框架与评估办法。  

- **代码生成**  
  - `generate_code(task_description, language="python")`：输出可直接运行的实验脚本。  

- **问答**  
  - `ask(question, context)`：在已加载的文献内容中检索答案，若无则生成推测。  

---

## 使用方法  

1. **克隆仓库**  
   ```bash
   git clone https://github.com/HKUDS/AI-Researcher.git
   cd AI-Researcher
   ```

2. **创建环境并安装依赖**  
   ```bash
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **配置 API Key**  
   在项目根目录创建 `.env` 文件，填入 OpenAI API Key：  
   ```dotenv
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

4. **运行 Web UI（推荐）**  
   ```bash
   streamlit run src/app.py
   ```
   打开浏览器访问 `http://localhost:8501`，即可使用交互式界面。

5. **命令行使用**  
   ```bash
   python src/main.py --help
   ```
   示例：  
   ```bash
   python src/main.py search --query "transformer self-attention"
   python src/main.py summarize --pdf path/to/paper.pdf --level short
   python src/main.py experiment --paper-id 2305.12345 --task "classification"
   ```

---

## 快速上手

```python
from ai_researcher import Researcher

researcher = Researcher(api_key="YOUR_OPENAI_KEY")

# 1. 搜索论文
papers = researcher.search_arxiv("graph neural network")
print(papers[0].title)

# 2. 下载并摘要
pdf_path = researcher.download_pdf(papers[0].arxiv_id)
summary = researcher.summarize(pdf_path, level="short")
print(summary)

# 3. 生成实验方案
exp_plan = researcher.design_experiment(papers[0].arxiv_id, task="node classification")
print(exp_plan)

# 4. 生成代码
code = researcher.generate_code("train a GNN on Cora dataset")
with open("train_gnn.py", "w") as f:
    f.write(code)
```

---

## 依赖

- Python 3.10+
- OpenAI Python SDK
- LangChain
- Streamlit
- PyMuPDF (PDF 解析)
- pandas, numpy, matplotlib, seaborn

---

## 贡献

欢迎提交 Issue 与 PR。请先阅读 `CONTRIBUTING.md` 与代码规范。

---

## 项目地址  
<https://github.com/HKUDS/AI-Researcher>