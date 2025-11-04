
---
title: reactjs-interview-questions
---


# ReactJS Interview Questions (sudheerj)

**GitHub** : <https://github.com/sudheerj/reactjs-interview-questions>

---

## 项目概述

- 一个专门收录**React**相关面试题及答案的公开仓库  
- 题目按主题（组件、生命周期、Hooks、性能优化等）进行分类  
- 每道题目配有代码示例、思路分析与常见陷阱  
- 目标读者：想要准备 React 面试的前端工程师

---

## 主要特性

| 功能 | 说明 |
|------|------|
| **题库** | 超过 100 道精选 React 题目，包含基础、进阶、实战等不同层级 |
| **代码示例** | 每道题都有完整的可运行 TypeScript/JavaScript 示例，便于快速测试 |
| **类型安全** | 代码示例使用 TypeScript，强化类型意识 |
| **讨论区** | 通过 GitHub Issues 可讨论题目实现及最佳实践 |
| **持续更新** | 开发者主动维护，及时加入新技术或解决方案 |
| **可搜索** | 使用 GitHub 搜索标签或文件名可快速定位感兴趣的题目 |

---

## 如何使用

1. **浏览题目**  
   - 直接在仓库中打开 `questions/` 目录，按主题文件夹查看  
   - 每个文件都是一道完整题目，包含 `问题描述`、`代码实现` 与 `解析`

2. **本地运行代码**  
   ```bash
   # 克隆仓库
   git clone https://github.com/sudheerj/reactjs-interview-questions.git
   cd reactjs-interview-questions

   # 进入某个题目的文件夹，安装依赖
   cd questions/__\*\*\*\*\*\*\*/   # 例如 `questions/lifecycle-methods`
   npm install

   # 启动查看示例
   npm start
   ```

3. **参与讨论**  
   - 在 GitHub Issues 里提问或给出更优实现  
   - 通过 Pull Request 提高题目质量

4. **导出答案**  
   - 使用 `markdown` 直接复制题目及答案到笔记或面试复习工具

---

## 文件结构示例

```
├─ .github/
│  └─ workflows/          # 自动化 CI/CD
├─ questions/
│  ├─ basics/
│  │  ├─ controlled-components.md
│  │  └─ unmounted-components.md
│  ├─ lifecycle-methods/
│  │  ├─ getDerivedStateFromProps.md
│  │  └─ componentDidUpdate.md
│  ├─ hooks/
│  │  ├─ useState.md
│  │  └─ useReducer.md
│  └─ performance/
│     ├─ memoization.md
│     └─ lazy-loading.md
└─ README.md
```

---

## 结语

此项目是学习与复习 React 的好帮手。无论是自学者还是准备面试的开发者，都能快速定位关键概念，体验实际编码，提升面试准备效果。祝学习愉快！

``` 

保存为 `src/content/docs/00/reactjs-interview-questions_sudheerj.md`。