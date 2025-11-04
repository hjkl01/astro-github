
---
title: openevolve
---


# Openevolve by codelion

**项目地址**: https://github.com/codelion/openevolve

## 项目简介
Openevolve 是一个基于 Python 的开源进化计算框架，旨在为科研、工程和教学提供一个易用、可扩展且高性能的进化算法实现。它支持单目标与多目标优化，提供了多种经典算法（如遗传算法、差分进化、NSGA‑II、MOEA/D 等）以及自定义算子和约束处理机制。

## 主要特性
- **多种算法实现**：遗传算法（GA）、差分进化（DE）、粒子群优化（PSO）、NSGA‑II、MOEA/D、SPEA2 等。
- **灵活的算子框架**：可轻松自定义交叉、变异、选择、聚合等算子。
- **多目标优化支持**：内置 Pareto 前沿生成、拥挤度距离、分层选择等机制。
- **约束处理**：多种约束处理策略（罚函数、修复算子、可行性优先等）。
- **并行评估**：支持多进程、分布式评估，提升大规模问题求解效率。
- **可视化与日志**：集成 Matplotlib、Bokeh 等，可实时绘制适应度曲线、Pareto 前沿；支持 TensorBoard、CSV 日志。
- **易用的 API**：基于 `Problem`、`Individual`、`Population` 等核心类，几行代码即可搭建完整求解流程。
- **可扩展性**：插件式架构，支持自定义算子、评估函数、进化策略。

## 主要功能
| 功能 | 描述 |
|------|------|
| **问题定义** | 通过继承 `Problem` 类实现目标函数、约束、变量界限、种群初始化等。 |
| **算子管理** | `GeneticOperators`、`MutationOperators`、`CrossoverOperators` 等预置算子，支持自定义实现。 |
| **进化控制** | `EvolutionController` 负责迭代、终止判定、种群更新、日志记录。 |
| **多目标方法** | `NSGA2`, `MOEAD`, `SPEA2` 等多目标算法实现。 |
| **并行评估** | `ParallelEvaluator` 支持 `multiprocessing`、`dask` 等后端。 |
| **可视化** | `Visualizer` 提供实时绘图、Pareto 前沿展示、进化曲线。 |
| **结果导出** | 支持 CSV、JSON、pickle、Matplotlib 图片等多种导出方式。 |

## 用法

### 安装
```bash
pip install openevolve
```

### 快速示例（单目标）
```python
from openevolve import Problem, GA, EvolutionController, logger

# 1. 定义问题
class SphereProblem(Problem):
    def __init__(self):
        super().__init__(dim=30, bounds=(-5.12, 5.12))

    def evaluate(self, individual):
        # Sphere function
        return [sum(x**2 for x in individual.x)]

# 2. 选择算子
ga = GA(
    population_size=100,
    crossover_rate=0.9,
    mutation_rate=0.1,
    tournament_size=2,
)

# 3. 进化控制
controller = EvolutionController(
    problem=SphereProblem(),
    algorithm=ga,
    max_generations=200,
    log_interval=10,
)

# 4. 开始进化
best = controller.run()

print("Best solution:", best.x)
print("Best fitness:", best.fitness)
```

### 多目标示例（NSGA‑II）
```python
from openevolve import Problem, NSGA2, EvolutionController, logger

class ZDT1Problem(Problem):
    def __init__(self):
        super().__init__(dim=30, bounds=(0, 1))

    def evaluate(self, individual):
        x = individual.x
        f1 = x[0]
        g = 1 + 9 * sum(x[1:]) / (self.dim - 1)
        f2 = g * (1 - (f1 / g)**0.5)
        return [f1, f2]

nsga2 = NSGA2(
    population_size=100,
    crossover_rate=0.9,
    mutation_rate=0.1,
    generations=250,
)

controller = EvolutionController(
    problem=ZDT1Problem(),
    algorithm=nsga2,
    max_generations=250,
)

pareto_front = controller.run()
# 可视化 Pareto 前沿
controller.visualize_pareto()
```

## 贡献方式
1. Fork 本仓库  
2. 在自己的分支中实现/改进功能  
3. 提交 Pull Request 并说明变更内容  
4. 代码需通过单元测试并符合 PEP8

## 许可证
本项目采用 MIT 许可证，详情请参阅 `LICENSE` 文件。

---

> **提示**：完整的 API 文档请查看仓库中的 `docs/` 目录或在线文档。
