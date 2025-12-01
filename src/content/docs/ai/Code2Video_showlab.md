---
title: Code2Video
---

## 项目简介

Code2Video 是一个基于代码的代理框架，用于从知识点生成高质量的教育视频。它利用可执行的 Manim 代码（而非像素级文本到视频模型）确保视频的清晰度、一致性和可重现性，适用于教学内容创作。

## 关键特性

- **代码为中心范式**：使用可执行代码统一处理视频的时间序列和空间组织。
- **模块化三代理设计**：Planner（故事板扩展）、Coder（可调试代码合成）和 Critic（锚点布局优化）协同工作，实现结构化生成。
- **MMMC 基准**：首个代码驱动视频生成基准，涵盖 117 个学习主题，灵感来自 3Blue1Brown，涉及多个领域。
- **多维度评估**：从知识转移（TeachQuiz）、美学与结构质量（AES）以及效率（令牌使用、执行时间）进行系统评估。

## 使用方法

1. **环境要求**：进入 `src/` 目录，运行 `pip install -r requirements.txt`。参考 Manim Community v0.19.0 官方安装指南。
2. **配置 API 密钥**：在 `api_config.json` 中填写 LLM API（推荐 Claude-4-Opus 用于 Planner 和 Coder）、VLM API（推荐 Gemini-2.5-Pro 用于 Critic）和视觉资产 API（IconFinder 用于图标）。
3. **运行代理**：
   - 单知识点模式：运行 `sh run_agent_single.sh --knowledge_point "知识点"`（例如 "Linear transformations and matrices"）。
   - 完整基准模式：运行 `sh run_agent.sh`，处理 `long_video_topics_list.json` 中的主题，支持并行运行。
4. **项目结构**：输出保存在 `CASES/` 下，按 `FOLDER_PREFIX` 组织；资产缓存于 `assets/`。

## 重要注意事项

- 需要有效的 API 密钥，否则无法运行；视觉资产 API 可选，但有助于丰富视频。
- 生成视频依赖 Manim，确保环境正确安装。
- 评估脚本位于 `eval_TQ.py` 和 `eval_AES.py`；更多数据见 HuggingFace MMMC 数据集。
- 项目基于开源贡献，如 Manim Community 和 3Blue1Brown 视频；引用时请使用提供的 BibTeX。
- 最近更新：优化了安装时间，更新了数据集和图标资源。
