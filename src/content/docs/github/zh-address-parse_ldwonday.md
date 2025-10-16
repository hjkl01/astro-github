
---
title: zh-address-parse
---

# zh-address-parse 项目

## 项目地址
[GitHub 项目地址](https://github.com/ldwonday/zh-address-parse)

## 主要特性
- **高效地址解析**：专为中文地址设计，支持从完整地址字符串中提取省市区县、街道、门牌号等详细组件。
- **准确性高**：基于中国行政区划数据，提供精确的地址分词和标准化处理，支持模糊匹配。
- **轻量级实现**：纯 JavaScript 实现，无需外部依赖，适用于浏览器和 Node.js 环境。
- **自定义扩展**：允许用户自定义地址规则和数据源，便于适应特定场景。
- **性能优化**：解析速度快，适合大规模地址数据处理。

## 主要功能
- **地址分词**：将输入的中文地址字符串拆分为结构化组件，如省份、市、县、区、乡镇、村、街道、门牌号等。
- **标准化输出**：返回 JSON 格式的解析结果，便于后续数据存储或查询。
- **地址验证**：检查地址的合法性和完整性，支持缺失组件的智能补全。
- **批量处理**：支持一次性解析多个地址，提高效率。
- **行政区查询**：提供基于行政代码的查询功能，用于地址关联和验证。

## 用法
### 安装
```bash
npm install zh-address-parse
```

### 基本用法（Node.js 示例）
```javascript
const AddressParser = require('zh-address-parse');

// 初始化解析器（可选，加载默认数据）
const parser = new AddressParser();

// 解析地址
const address = "北京市朝阳区望京街道北京市朝阳区望京西路甲1号楼";
const result = parser.parse(address);

console.log(result);
// 输出示例：
// {
//   province: "北京市",
//   city: "北京市",
//   district: "朝阳区",
//   street: "望京街道",
//   road: "望京西路",
//   number: "甲1号楼"
// }
```

### 浏览器环境用法
```html
<script src="path/to/zh-address-parse.min.js"></script>
<script>
  const parser = new AddressParser();
  const result = parser.parse("上海市浦东新区张江高科技园区");
  console.log(result);
</script>
```

### 高级用法
- **自定义数据源**：通过 `parser.loadData(customData)` 加载自定义行政区划数据。
- **选项配置**：`parser.parse(address, options)` 支持传入选项，如 `{ strict: true }` 用于严格模式验证。
- **批量解析**：`parser.batchParse(addressesArray)` 处理地址数组，返回结果列表。

更多细节请参考项目 README 文档。