---
title: Mihomo
---

# mihomo

A simple Python Pydantic model for Honkai: Star Rail parsed data from the Mihomo API.

## 功能

- 提供Pydantic模型，用于解析Honkai: Star Rail游戏的数据。
- 支持类型提示和自动补全。
- 从Mihomo API获取解析后的数据，包括玩家信息、角色数据等。
- 支持两种数据格式：V1 和 V2。
- 提供工具函数，如移除重复角色、合并角色数据。
- 支持数据持久化（pickle 和 JSON 格式）。

## 用法

### 安装

```bash
pip install -U git+https://github.com/KT-Yeh/mihomo.git
```

### 基本用法

创建客户端并获取用户数据：

```python
import asyncio
from mihomo import Language, MihomoAPI
from mihomo.models import StarrailInfoParsed

client = MihomoAPI(language=Language.EN)

async def main():
    data: StarrailInfoParsed = await client.fetch_user(800333171)
    print(f"Name: {data.player.name}")
    print(f"Level: {data.player.level}")

asyncio.run(main())
```

### 数据格式

- **V1**: 使用 `client.fetch_user_v1(UID)` 获取 `StarrailInfoParsedV1` 数据。
- **V2**: 使用 `client.fetch_user(UID)` 获取 `StarrailInfoParsed` 数据，支持替换图标名称为URL。

### 工具函数

- **移除重复角色**:

  ```python
  from mihomo import tools
  data = await client.fetch_user(800333171)
  data = tools.remove_duplicate_character(data)
  ```

- **合并角色数据**:
  ```python
  old_data = await client.fetch_user(800333171)
  new_data = await client.fetch_user(800333171)
  data = tools.merge_character_data(new_data, old_data)
  ```

### 数据持久化

```python
import pickle
import zlib
from mihomo import MihomoAPI, Language, StarrailInfoParsed

client = MihomoAPI(language=Language.EN)
data = await client.fetch_user(800333171)

# 保存为 pickle
pickle_data = zlib.compress(pickle.dumps(data))

# 保存为 JSON
json_data = data.json(by_alias=True, ensure_ascii=False)

# 加载
data_from_pickle = pickle.loads(zlib.decompress(pickle_data))
data_from_json = StarrailInfoParsed.parse_raw(json_data)
```
