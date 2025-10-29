
---
title: javascript-algorithms
---

# JavaScript 算法与数据结构

**GitHub 项目地址:** https://github.com/trekhleb/javascript-algorithms

---

## 简介  
本仓库聚焦于通过 **JavaScript**（Node.js 与浏览器端）实现常见数据结构和算法，实现方式与实例化细节均会附带详尽说明。目标是帮助学习者在掌握算法本质的同时，感受 JavaScript 生态中的实际编码风格。

---

## 主要特性

| 领域 | 具体实现 | 说明 |
|------|----------|------|
| **数组** | `Array` + 某些原生方法的补全 | 介绍经典数组排序与查找、双指针、滑动窗口等 |
| **链表** | 单向链表、双向链表 | 包含插入、删除、反转、寻找中点等 |
| **栈/队列** | 采用数组或链表实现 | 支持深度优先遍历（DFS）、宽度优先遍历（BFS）等场景 |
| **堆** | 二叉堆 | 用作优先队列，演示堆排序、原地堆化 |
| **映射** | 对象、`Map` | 包含哈希查找、链式哈希等 |
| **树** | 二叉树、AVL 树、Trie | 搜索树、B 树、前缀树等 |
| **图** | 邻接表 / 邨接矩阵 | 迪杰斯特拉、Bellman–Ford、Floyd–Warshall、Tarjan 的强连通分量 |
| **排序** | 快速排序、归并排序、堆排序、计数排序、基数排序 | 逐步深入分析时间/空间复杂度 |
| **搜索** | 二分搜索、深度优先搜索、广度优先搜索 | 包含递归与迭代实现 |
| **动态规划** | 斐波那契数列、背包问题、硬币找零 | 递归+记忆化、表格法 |
| **贪心** | 活动安排、最小生成树 (Kruskal、Prim) | 适配 `Set`/`Map` 的实现细节 |
| **递归** | 汉诺塔、全排列、子集 | 说明递归的时间/空间占用 |
| **并发** | ES6 Promise、async/await | 在异步场景中演示算法实现 |

> 🔍 所有实现均遵循 **统一目录结构**：  
> `src` → `algorithms`/`data-structures` → `folder-of-algorithm` → `index.js`（代码） + `README.md`（说明） + `test.js`（测试）。

---

## 用法示例

1. **安装依赖**

```bash
# 克隆仓库
git clone https://github.com/trekhleb/javascript-algorithms.git
cd javascript-algorithms

# 安装 npm 包（Jest、Node 等）
npm install
```

2. **运行单元测试**

```bash
# 运行所有测试
npm test

# 运行指定文件的测试
npm test -- src/algorithms/sorting/quick-sort/test.js
```

> 💡 测试框架：**Jest**。测试文件以 `test.js` 结尾，并使用 `describe()`、`it()` 简洁写作。

3. **查看示例代码**

```bash
# 直接在浏览器中打开对应 README
# 例如：https://github.com/trekhleb/javascript-algorithms/blob/master/src/algorithms/graph/shortest-paths/least-cost-paths/README.md

# 或者在本地使用 `highlight.js` 进行代码高亮
```

4. **实验**  
  进入任意功能目录，例如 `src/algorithms/sorting/merge-sort`，查看 `/index.js`、`/description.md`、`/test.js`。可以直接在 Node.js 环境尝试：

```bash
node src/algorithms/sorting/merge-sort/index.js
```

---

## 如何贡献

1. Fork 本仓库。  
2. 建议/修复/补充的算法请在对应目录下直接提 PR。  
3. PR 必须通过所有 Jest 单元测试。  
4. 参考 `CONTRIBUTING.md`（若存在）或按上述方式操作。

---

> 本文件是 **维护者** 以及 **学习者** 的速查手册，务必保持**更新** 与 **精准**。祝学习愉快 🚀