
---
title: javascript-algorithms
---

# JavaScript Algorithms（Trekhleb）

> **项目地址**：<https://github.com/trekhleb/javascript-algorithms>

本项目是一个用 JavaScript 实现的数据结构与算法教程，适合作为学习和复习算法的参考书籍。

## 主要特性

- **完整的实现**：包含常见数据结构（数组、链表、栈、队列、树、图等）和经典算法（排序、搜索、遍历、动态规划等）。
- **模块化结构**：每个数据结构或算法都放在独立文件，易于阅读与维护。
- **均衡的深度**：示例代码简洁明了，既覆盖理论实现，又展示实际用途，适合初学者与进阶者。
- **文档化**：每个文件都有详细注释，解释算法思路、复杂度和使用场景。
- **实用工具**：包含随机数生成、矩阵运算等辅助工具，帮助学习者快速构建测试案例。

## 功能概览

| 文件夹 | 说明 |
|------|------|
| `data-structures/...` | 实现各类数据结构（数组、链表、栈、队列、树、图等）。 |
| `sorting/...` | 经典排序算法（冒泡、选择、插入、归并、快速等）。 |
| `searching/...` | 搜索算法（线性搜索、二分搜索、深度优先、广度优先）。 |
| `shuffling/...` | 洗牌与随机生成实现。 |
| `trees/...` | 二叉树、树遍历、BST、AVL、红黑树等。 |
| `graphs/...` | 图结构及相关算法（DFS、BFS、Dijkstra、Kruskal 等）。 |
| `trie/...` | 前缀树（Trie）及其应用。 |
| `dynamic-programming/...` | 经典 DP 题目实现。 |
| `math/...` | 数学相关算法（GCD、素数检测等）。 |
| `utils/...` | 通用工具函数（随机、交换、数组拷贝等）。 |

## 用法示例

```bash
# 克隆仓库
git clone https://github.com/trekhleb/javascript-algorithms.git

# 进入项目
cd javascript-algorithms

# 示例：使用快速排序
import quickSort from './sorting/quick-sort.js';

const array = [5, 2, 9, 1, 5, 6];
console.log(quickSort(array));  // [1, 2, 5, 5, 6, 9]
```

也可直接在浏览器中通过 `<script src="...">` 引用对应文件，后面会训练。

## 如何参与

- Fork 本仓库，提交 Pull Request。
- 关注 README 中的贡献指南，保持代码风格一致。
- 使用 `npm run test` 检查新增实现的正确性（如果项目包含测试）。

---

> 本文件为项目概览，供快速了解其结构与功能。如需深入学习，请参考各模块源代码及其注释。