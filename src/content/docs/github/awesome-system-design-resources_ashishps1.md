
---
title: awesome-system-design-resources
---


# Awesome System Design Resources

**GitHub 项目地址**  
<https://github.com/ashishps1/awesome-system-design-resources>

---

## 项目概述
该项目是一个持续维护的系统设计学习资源列表，涵盖书籍、文章、课程、工具、案例等多种类型，旨在帮助面向系统设计的工程师快速定位高质量参考资料。

---

## 主要特性

- **精准分类**  
  按照技术维度（分布式系统、数据库、缓存、消息队列等）和学习阶段（入门、进阶）进行分门别类，方便快速查找。

- **社区协作**  
  所有资源通过 `README.md` 和 `CONTRIBUTING.md` 开放贡献，任何人都可提交 PR、问题（Issue）进行更新、纠正或新增资源。

- **多语种支持**  
  提供英文与中文（以及部分其他语言）版本，满足不同语言背景的学习者。

- **可搜索与筛选**  
  通过 GitHub 的搜索功能可直接按关键词筛选所需资源；若使用手动下载的 `.md` 文件，可使用 IDE 内置搜索快速定位。

---

## 功能亮点

| 功能 | 说明 |
|------|------|
| **资源类型标注** | 对每个资源标注 `Book / Article / Course / Video / Tool / Tutorial` 等 |
| **分级标签** | `Beginner / Intermediate / Advanced`，帮助定位学习难度 |
| **贡献说明** | `CONTRIBUTING.md` 指导如何提建议、提交 PR |
| **执行脚本** | `scripts/` 目录下的脚本可生成自定义的 README、目录或统计表 |
| **持续集成** | CI 检查 PR 的 Format 与合规性，保证质量 |

---

## 用法示例

1. **浏览资料**  
   - 直接打开 `README.md`，使用折叠面板分类展开，查看对应资源详细信息。

2. **下载使用**  
   ```bash
   git clone https://github.com/ashishps1/awesome-system-design-resources.git
   cd awesome-system-design-resources
   less README.md   # 或使用 VS Code、Typora 等 Markdown 编辑器
   ```

3. **本地搜索**  
   ```bash
   grep -i "distributed" README.md   # 关键字检索
   ```

4. **本地生成目录**  
   ```bash
   python scripts/generate_toc.py   # 会在 README 中插入目录结构
   ```

5. **贡献新增资源**  
   - Fork 本仓库  
   - 在对应分类下新增 `<title> | <link> | <description>` 行  
   - 提交 PR 并填写模板，等待 maintainer 审核

---

## 社区与维护

- **issue**：用于记录已知问题、资源缺失或细节纠正。  
- **pull request**：所有 PR 必须根据 `CONTRIBUTING.md` 进行格式化，推荐使用统一的 Markdown 格式。  
- **讨论**：可在 GitHub Discussions 区域讨论学习经验、热门技术细节。

> 该项目属于聚合型资源库，主要职责是聚合与整理；真正的资源内容来自各自作者，遵循其原始许可协议。

---

**开始探索系统设计的知识海洋吧！**