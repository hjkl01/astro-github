---
title: computer-science
---

# OSSU 作业 – 计算机科学

项目地址: <https://github.com/ossu/computer-science>

## 项目概述
该仓库提供了一个 **开源计算机科学课程**。内容基于学术教材、在线教程以及社区贡献，帮助学习者从基础到进阶系统地掌握计算机科学核心知识。

## 主要特性
- **模块化学习路径**：课程分为课程本身、任务以及作业三大部分，形成完整的学习链。
- **多媒体内容**：包含视频、播客、课程笔记与互动章节，满足不同学习方式。
- **示例与实验**：每个单元都带有代码示例、练习题和实验，帮助巩固理论。
- **跨学科资源**：结合数学、统计、理论与实践，涵盖算法、系统、人工智能等领域。
- **持续更新**：社区活跃，定期更新课程内容、补充资源和修正问题。

## 功能点
| 功能 | 说明 |
|------|------|
| 学习路径规划 | 提供详细的章节顺序和学习时间建议 |
| 进度跟踪 | 通过 `modules.json` 记录学习进度 |
| 任务完成指引 | 随单元附带的 `README.md` 给出完成任务的详细步骤 |
| 代码评审 | 所有作业都保存为 Jupyter Notebook 或源码文件，可在 GitHub 上进行评审 |
| 社区讨论 | 每次更新后自动生成讨论区，便于提问与协作 |

## 用法

1. **克隆仓库**
   ```bash
   git clone https://github.com/ossu/computer-science.git
   cd computer-science
   ```

2. **安装依赖（如果需要）**
   ```bash
   # 示例：Jupyter notebook
   pip install -r requirements.txt
   ```

3. **按顺序阅读**  
   在 `modules/` 文件夹中，打开 `index.md` 开始学习。每个单元都有 `README.md` 指导如何完成相应练习。

4. **完成作业**  
   在对应单元目录下创建 `solutions/` 文件夹，提交代码或笔记。

5. **提交 PR**  
   完成练习后，使用 `git add . && git commit` 并推送到自己的 fork，然后提交 Pull Request，社区会对作业进行评审。

6. **跟进更新**  
   使用 `git pull upstream/main`（已在仓库中配置 upstream）保持最新内容。

> **小技巧**：可以在 `config.py` 中自定义学习进度或生成学习日程。

## 快速上手示例（Python 机器学习单元）

```bash
cd modules/001/algebra
git clone https://github.com/ossu/computer-science.git
pip install jupyter matplotlib pandas
jupyter notebook
```

在 Jupyter 中打开 `project.ipynb` 并按提示完成数据分析作业。

## 结语
该项目对想系统学习计算机科学并通过实践提升技能的人尤其友好。通过阅读文档、完成实验与提交作业，你可以获得一个完整、可评估的学习经历。

---  

> 如有疑问请在项目的 Issues 区讨论或参见 `docs/` 目录下的帮助文件。