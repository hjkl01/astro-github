
---
title: public-apis
---


# Public APIs

**项目地址**：<https://github.com/public-apis/public-apis>

## 项目概述
Public APIs 是一个公开的、可搜索的免费 API 列表，旨在帮助开发者快速找到适合自己项目的接口。它由社区维护，涵盖了从天气、金融、娱乐到教育等多种领域。

## 主要特性
- **多样化分类**  
  - 业务类型（Authentication、CORS、HTTPS、OpenAPI 等）  
  - 主题分类（Animals、Anime、Books、Business、Crime、Education、Entertainment、Events 等）
- **开放且免费**  
  所有列出的 API 均提供免费访问（或至少有免费额度），并公开 API 文档或示例。
- **易于检索**  
  - 通过 GitHub 搜索、标签或直接浏览 Markdown 文件  
  - 提供 `search.json`（可下载）或在 GitHub 上直接搜索关键词
- **社区驱动**  
  - 通过 Issues 或 Pull Requests 提交新 API、更新信息或纠正错误。  
  - 采用 `README.md` 维护统一格式，便于快速查看。
- **持续更新**  
  - 每日或每周有新的 API 被加入，老的 API 会被标记或移除。

## 核心功能
| 功能 | 说明 |
|------|------|
| **目录结构** | `api/` 目录下按主题存放 Markdown 文件，每个文件包含 API 名称、描述、Auth、HTTPS、CORS、Link、Category、Response |
| **搜索** | 直接在 GitHub 上搜索关键词或使用 `search.json` 做更高级的查询 |
| **贡献指南** | `CONTRIBUTING.md` 说明如何提交 PR，格式规范和审核流程 |

## 用法示例

```bash
# 1. 克隆仓库
git clone https://github.com/public-apis/public-apis.git

# 2. 进入目录
cd public-apis/api/Weather

# 3. 查看某个 API 的详细信息
cat OpenWeatherMap.md
```

### 在代码中使用示例（JavaScript + fetch）

```js
// 示例：获取 OpenWeatherMap 当前天气
const apiKey = 'YOUR_API_KEY';
const city = 'London';
const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

fetch(url)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### 在 Python 中使用示例

```python
import requests

api_key = 'YOUR_API_KEY'
city = 'London'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()
print(data)
```

## 如何贡献

1. Fork 本仓库并创建新分支。  
2. 在相应主题文件夹下添加新的 Markdown 文档，遵循现有格式。  
3. 提交 Pull Request，说明 API 的用途与使用方式。  
4. 等待社区审核，合并后即可上线。

> **提示**：若 API 需要身份验证，请在 `Auth` 字段注明（如 `apiKey`、`OAuth`、`No` 等），并在 `Link` 字段提供官方文档链接。

## 结语
Public APIs 是一个极具价值的资源，适合想要快速集成第三方接口、进行原型开发或学习 API 调用的开发者。通过社区协作，它始终保持着最新、最全面的免费接口集合。

> 项目地址：<https://github.com/public-apis/public-apis>
```
