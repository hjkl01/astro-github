---
title: FinanceDatabase
---

# FinanceDatabase

## 项目简介

FinanceDatabase 是一个免费的金融数据库项目，由 JerBouma 创建。该数据库包含超过 300,000 个符号，涵盖股票（Equities）、ETF、基金（Funds）、指数（Indices）、货币（Currencies）、加密货币（Cryptocurrencies）和货币市场（Money Markets）。该项目的目标是为投资者和开发者提供全面的金融产品分类和信息，帮助用户更好地理解和分析金融市场。

项目地址：[https://github.com/JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase)

## 主要功能

- **全面的金融产品覆盖**：数据库包含多种资产类别，提供每个产品的基本信息，如名称、货币、行业、交易所、国家等。
- **分类和筛选**：支持按国家、行业、交易所等维度筛选产品，便于用户快速找到感兴趣的金融产品。
- **搜索功能**：提供灵活的搜索接口，支持在摘要、行业等字段中进行关键词搜索。
- **与 Finance Toolkit 集成**：可直接与 Finance Toolkit 结合，进行更深入的财务分析，如获取历史数据、计算财务比率等。
- **社区驱动**：鼓励社区贡献，保持数据库的更新和准确性。
- **免费且开源**：所有数据来自公开来源，完全免费使用。

### 数据库统计

| 产品类别         | 数量    | 主要属性示例                                       |
| ---------------- | ------- | -------------------------------------------------- |
| Equities         | 158,429 | 12 个行业，63 个子行业，111 个国家，83 个交易所    |
| ETFs             | 36,786  | 295 个类别，22 个子类别，111 个国家，53 个交易所   |
| Funds            | 57,881  | 1,541 个类别，52 个子类别，111 个国家，34 个交易所 |
| Indices          | 91,183  | 64 个交易所                                        |
| Currencies       | 2,556   | 175 种货币                                         |
| Cryptocurrencies | 3,367   | 352 种加密货币                                     |
| Money Markets    | 1,367   | 3 个交易所                                         |

## 安装和使用

### 安装

使用 pip 安装：

```bash
pip install financedatabase -U
```

### 基本用法

1. **导入包**：

```python
import financedatabase as fd
```

2. **初始化资产类别**（以股票为例）：

```python
equities = fd.Equities()
```

3. **查看所有选项**（无需加载数据）：

```python
fd.show_options("equities")
```

这将返回所有可用选项，如货币、行业等。

4. **筛选数据**：

```python
# 筛选荷兰的保险行业股票
equities.select(country='Netherlands', industry='Insurance')
```

示例输出：

| symbol | name       | currency | sector     | industry_group | industry  | exchange | market             | country     |
| ------ | ---------- | -------- | ---------- | -------------- | --------- | -------- | ------------------ | ----------- |
| AGN.AS | Aegon N.V. | EUR      | Financials | Insurance      | Insurance | AMS      | Euronext Amsterdam | Netherlands |

5. **高级筛选**：

```python
# 筛选多个国家，使用列表
equities.select(country=['Netherlands', 'United States'], industry='Insurance')
```

6. **搜索功能**：

```python
# 在摘要中搜索关键词
equities.search(summary=["Robotics", "Education"], industry_group="Equipment")
```

7. **与 Finance Toolkit 集成**（需要 API Key）：

```python
# 获取 API Key 从 FinancialModelingPrep
API_KEY = "YOUR_API_KEY"

# 选择公司
dutch_insurance = equities.select(country='Netherlands', industry='Insurance', market='Euronext Amsterdam')

# 转换为 Toolkit
toolkit = dutch_insurance.to_toolkit(api_key=API_KEY)

# 获取历史数据
toolkit.get_historical_data()

# 计算财务比率
toolkit.ratios.collect_all_ratios()
```

### 其他资产类别

- **ETF**：`etfs = fd.ETFs()`
- **基金**：`funds = fd.Funds()`
- **指数**：`indices = fd.Indices()`
- **加密货币**：`cryptos = fd.Cryptos()`

每个类别都有类似的 `select`、`search` 和 `show_options` 方法。

## 贡献

该项目依赖社区贡献来保持数据库的准确性和更新。如果您发现错误或缺失信息，请参考 [贡献指南](https://github.com/JerBouma/FinanceDatabase/blob/main/CONTRIBUTING.md)。

## 许可证

MIT License

## 联系方式

- 网站：[https://jeroenbouma.com/projects/financedatabase](https://jeroenbouma.com/projects/financedatabase)
- LinkedIn：[https://www.linkedin.com/in/boumajeroen/](https://www.linkedin.com/in/boumajeroen/)
- 邮箱：[jer.bouma@gmail.com](mailto:jer.bouma@gmail.com)
