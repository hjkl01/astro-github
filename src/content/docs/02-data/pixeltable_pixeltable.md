---
title: pixeltable
---

# Pixeltable

**项目地址**: <https://github.com/pixeltable/pixeltable>

## 简介

Pixeltable 是唯一一个开源 Python 库，提供用于构建多模态 AI 应用的声明式数据基础设施，实现数据的增量存储、转换、索引、检索和编排。

## 主要特性

Pixeltable 替换了构建 AI 应用时通常需要的复杂多系统架构（数据库、文件存储、向量数据库、API、编排），使用单个声明式表接口，该接口原生处理多模态数据，如图像、视频和文档。

- **统一的多模态接口**：`pxt.Image`、`pxt.Video`、`pxt.Audio`、`pxt.Document` 等 – 一致管理多样化数据。
- **声明式计算列**：定义处理步骤一次；在新的/更新的数据上自动运行。
- **内置向量搜索**：直接在表/视图上添加嵌入索引并执行相似性搜索。
- **增量视图维护**：使用迭代器创建虚拟表以高效处理，而不复制数据。
- **无缝 AI 集成**：内置函数用于 OpenAI、Anthropic、Hugging Face、CLIP、YOLOX 等。
- **自带代码**：通过 UDF、批处理和自定义聚合器扩展 Pixeltable。
- **代理工作流 / 工具调用**：注册 `@pxt.udf`、`@pxt.query` 函数或 **MCP 工具**作为工具。
- **数据持久性**：所有数据、元数据和计算结果自动存储和版本化。
- **时间旅行**：默认情况下，Pixeltable 保留每个表的完整变更历史，可以选择和查询任何先版本。
- **SQL-like Python 查询**：熟悉的语法结合强大的 AI 功能。

## 核心功能

- **多模态数据存储和数据转换（计算列）**：

  ```python
  import pixeltable as pxt

  # 创建表
  t = pxt.create_table(
      'films',
      {'name': pxt.String, 'revenue': pxt.Float, 'budget': pxt.Float},
      if_exists="replace"
  )

  t.insert([
      {'name': 'Inside Out', 'revenue': 800.5, 'budget': 200.0},
      {'name': 'Toy Story', 'revenue': 1073.4, 'budget': 200.0}
  ])

  # 添加利润计算列 - 自动运行！
  t.add_computed_column(profit=(t.revenue - t.budget), if_exists="replace")

  # 查询结果
  print(t.select(t.name, t.profit).collect())
  ```

- **使用 YOLOX 进行对象检测**：

  ```python
  import PIL
  import pixeltable as pxt
  from yolox.models import Yolox
  from yolox.data.datasets import COCO_CLASSES

  t = pxt.create_table('image', {'image': pxt.Image}, if_exists='replace')

  # 插入图像
  prefix = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg/1920px-Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg'
  t.insert([{'image': prefix}])

  @pxt.udf
  def detect(image: PIL.Image.Image) -> list[str]:
      model = Yolox.from_pretrained("yolox_s")
      result = model([image])
      coco_labels = [COCO_CLASSES[label] for label in result[0]["labels"]]
      return coco_labels

  t.add_computed_column(classification=detect(t.image))

  print(t.select().collect())
  ```

- **图像相似性搜索（CLIP 嵌入索引）**：

  ```python
  import pixeltable as pxt
  from pixeltable.functions.huggingface import clip

  # 创建图像表并添加示例图像
  images = pxt.create_table('my_images', {'img': pxt.Image}, if_exists='replace')
  images.insert([
      {'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg/1920px-Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg'},
      {'img': 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Retriever_in_water.jpg'}
  ])

  # 添加 CLIP 嵌入索引以进行相似性搜索
  images.add_embedding_index(
      'img',
      embedding=clip.using(model_id='openai/clip-vit-base-patch32')
  )

  # 文本-based 图像搜索
  query_text = "a dog playing fetch"
  sim_text = images.img.similarity(query_text)
  results_text = images.order_by(sim_text, asc=False).limit(3).select(
      image=images.img, similarity=sim_text
  ).collect()
  print("--- 文本查询结果 ---")
  print(results_text)
  ```

- **查询与过滤**

  ```python
  result = df.filter(pt.col("age") > 30).select("name", "age")
  ```

- **聚合**

  ```python
  agg = df.group_by("country").agg(
          total_sales=pt.sum("sales"),
          avg_age=pt.mean("age")
      )
  ```

- **连接**

  ```python
  joined = df_left.join(df_right, how="inner", on="id")
  ```

- **窗口函数**

  ```python
  win = pt.window.partition_by("category").order_by("date")
  df = df.with_column("rank", win.rank())
  ```

- **SQL 语法**

  ```python
  sql_df = pt.sql("""
      SELECT name, SUM(sales) AS total
      FROM sales
      GROUP BY name
      HAVING total > 1000
  """)
  ```

- **延迟执行**

  ```python
  lazy = df.filter(...).select(...)
  # 仍未执行
  result = lazy.collect()           # 触发执行
  ```

- **分布式 Dask**
  ```python
  import dask
  engine = pt.DaskEngine(dask_client)
  df = pt.read_parquet(..., engine=engine)
  ```

## 使用示例

```python
# 安装
pip install pixeltable

# 基本设置
import pixeltable as pxt

# 表与多模态列类型（Image, Video, Audio, Document）
t = pxt.create_table('images', {'input_image': pxt.Image})

# 计算列：定义转换逻辑一次，在所有数据上运行
from pixeltable.functions import huggingface

# 使用自动模型管理进行对象检测
t.add_computed_column(
    detections=huggingface.detr_for_object_detection(
        t.input_image,
        model_id='facebook/detr-resnet-50'
    )
)

# 从检测结果中提取特定字段
t.add_computed_column(detections_text=t.detections.label_text)

# OpenAI Vision API 集成与内置速率限制和异步管理
from pixeltable.functions import openai

t.add_computed_column(
    vision=openai.vision(
        prompt="Describe what's in this image.",
        image=t.input_image,
        model='gpt-4o-mini'
    )
)

# 直接从外部 URL 插入数据
# 自动触发所有计算列的计算
t.insert(input_image='https://raw.github.com/pixeltable/pixeltable/release/docs/resources/images/000000000025.jpg')

# 查询 - 结构化和非结构化数据并排返回
results = t.select(
    t.input_image,
    t.detections_text,
    t.vision
).collect()
```

> **发生了什么？**
>
> - **数据摄取 & 存储：** 就地引用 [文件](https://docs.pixeltable.com/datastore/bringing-data)（图像、视频、音频、文档），处理结构化数据。
> - **转换 & 处理：** 应用 _任何_ Python 函数（[UDFs](https://docs.pixeltable.com/datastore/custom-functions)）或内置操作（[分块、帧提取](https://docs.pixeltable.com/datastore/iterators)）自动。
> - **AI 模型集成：** 作为数据管道的一部分运行推理（[嵌入](https://docs.pixeltable.com/datastore/vector-database)、[对象检测](https://docs.pixeltable.com/examples/vision/yolox)、[LLMs](https://docs.pixeltable.com/integrations/frameworks#cloud-llm-providers)）。
> - **索引 & 检索：** 创建和管理系统向量索引以进行快速 [语义搜索](https://docs.pixeltable.com/datastore/vector-database#phase-3%3A-query)，同时进行传统过滤。
> - **增量计算：** 仅在数据或代码更改时 [重新计算](https://docs.pixeltable.com/overview/quick-start) 必要的内容，节省时间和成本。
> - **版本控制 & 沿袭：** 自动跟踪数据和模式更改以实现可重现性。

---

以上内容可直接复制到 `src/content/docs/00/pixeltable_pixeltable.md`，即可完成所需说明。
