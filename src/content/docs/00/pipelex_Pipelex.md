
---
title: pipelex
---

下面是 **Pipelex** 项目的中文说明。  
请以 Markdown 格式保存为文件，路径为：

```
src/content/docs/00/pipelex_Pipelex.md
```

```markdown
# Pipelex（Pipelex）

**项目地址**  
<https://github.com/Pipelex/pipelex>

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **可配置化 Pipeline** | 支持基于 Python 函数和自定义 DSL 轻松定义任务与依赖关系。 |
| **内置并发执行** | 支持多进程 / 多线程执行，自动调度任务并最大化 CPU 与 IO 资源利用。 |
| **容错与重试** | 可为每个任务设置超时、重试策略与失败回调，保障整个流水线稳健运行。 |
| **统一日志管理** | 内置日志收集与格式化，支持按任务、阶段、级别过滤输出。 |
| **轻量级调试** | 可在开发阶段开启调试模式，实时查看每个节点的输入输出；支持断点与回溯。 |
| **可视化监控** | 集成 `FastAPI` 与 `WebSocket`，可实现在线监控任务状态与性能指标。 |
| **插件扩展** | 通过插件机制支持第三方数据源、存储与计算框架（如 Spark、S3、Redis 等）。 |

---

## 核心功能

1. **任务定义 (`Task`)**  
   ```python
   from pipelex import Task

   @Task(name="example")
   def my_task(a: int, b: int) -> int:
       return a + b
   ```

2. **阶段与流水线 (`Stage`, `Pipeline`)**  
   ```python
   from pipelex import Stage, Pipeline

   stage1 = Stage(name="stage1", tasks=[my_task])
   pipeline = Pipeline(name="my_pipeline", stages=[stage1])
   ```

3. **依赖关系 & DAG**  
   - 通过 `depends_on` 指定依赖；  
   - 自动生成 DAG，避免循环依赖。

4. **并发执行**  
   - 默认使用 `concurrent.futures.ProcessPoolExecutor`；  
   - 通过 `max_workers` 调整并发度。

5. **错误处理**  
   ```python
   @Task(name="task_with_retry", retries=3, timeout=60)
   def risky_task():
       # 产生可能抛错的代码
   ```

6. **监控与报告**  
   - 运行时实时 Web 队列展示：`http://localhost:8000/dashboard`；  
   - 生成简单报告 JSON。

---

## 用法示例

```bash
# 安装
pip install git+https://github.com/Pipelex/pipelex.git

# 编写 pipeline
from pipelex import Task, Stage, Pipeline

@Task(name="add")
def add(a: int, b: int) -> int:
    return a + b

@Task(name="multiply")
def multiply(x: int, y: int) -> int:
    return x * y

stage_sum = Stage(name="sum", tasks=[add])
stage_prod = Stage(name="product", tasks=[multiply])

pipeline = Pipeline(name="demo_pipeline",
                    stages=[stage_sum, stage_prod])

# 运行
pipeline.run({"add": {"a": 2, "b": 3},
              "multiply": {"x": 4, "y": 5}})
```

运行后会在控制台打印任务执行日志，并在浏览器 `http://localhost:8000/dashboard` 查看实时状态。

---

> **注意**  
> 1. 详细配置请参考 repo 中 `docs/` 与 `examples/`。  
> 2. 所有代码均基于 Python 3.9+，兼容 `asyncio` 版本。

---

**作者**：Pipelex 团队  
**语言**：Python  
**许可证**：MIT
