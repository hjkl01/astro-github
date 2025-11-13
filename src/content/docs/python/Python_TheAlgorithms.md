---
title: Python
---


# TheAlgorithms/Python

项目地址: https://github.com/TheAlgorithms/Python

## 主要特性
- **丰富的算法实现**：涵盖了数百种经典算法与数据结构，涵盖排序、查找、图论、动态规划、字符串处理、数论等领域。
- **Python 纯实现**：所有代码均使用标准 Python（Python 3+）编写，易于阅读和学习。
- **模块化组织**：算法按功能模块划分（如`sort`, `search`, `graph`, `dp`, `geometry`, `etc`），方便定位和复用。
- **注释与文档**：每个实现文件包含详细注释和使用说明，帮助初学者快速理解原理。
- **可扩展性**：社区友好的贡献流程，支持添加新算法、优化既有实现、写入文档等。

## 主要功能
| 类别 | 典型算法 | 说明 |
|------|----------|------|
| **排序** | quick_sort, merge_sort, heap_sort, bubble_sort, insertion_sort, radix_sort | 多种排序算法实现，演示时间复杂度与使用场景。 |
| **搜索** | binary_search, depth_first_search, breadth_first_search | 线性与树/图搜索方法。 |
| **图论** | dijkstra, floyd_warshall, kruskal, prim, bfs, dfs, topological_sort | 常见图算法与路径计算。 |
| **动态规划** | fibonacci, knapsack, longest_common_subsequence, edit_distance | 经典 DP 问题实现。 |
| **字符串** | edit_distance, longest_palindrome, knuth_morris_pratt | 字符串匹配与处理。 |
| **数论** | euclid_gcd, prime_sieve, modular_exponentiation | 质数检测、最大公约数、快速幂等。 |
| **几何** | convex_hull, point_in_polygon | 基础几何算法。 |
| **数据结构** | binary_tree, trie, linked_list, stack, queue | 典型数据结构实现。 |
| **其他** | merge_intervals, huffman_encoding, bipartite_matching, dfs_tree | 其它常用算法。 |

## 用法

1. **克隆仓库**

   ```bash
   git clone https://github.com/TheAlgorithms/Python.git
   cd Python
   ```

2. **运行示例**

   在任意算法文件所在目录，直接执行 Python 解释器即可看到示例输出。

   ```bash
   python sorts/quick_sort.py
   ```

3. **使用函数**

   在 Python 项目中直接导入对应模块使用算法：

   ```python
   from algorithms.sort.quick_sort import quick_sort

   arr = [5, 2, 9, 1, 5, 6]
   sorted_arr = quick_sort(arr)
   print(sorted_arr)  # [1, 2, 5, 5, 6, 9]
   ```

4. **贡献**

   - Fork/Clone → 新建分支 → 实现/修改 → 提交 PR
   - 查看 `CONTRIBUTING.md` 获取详细流程

5. **运行测试**

   ```bash
   python -m unittest discover -s tests
   ```

> 该项目由全球贡献者维护，欢迎你加入贡献。

