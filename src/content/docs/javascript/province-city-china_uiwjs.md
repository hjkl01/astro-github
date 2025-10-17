
---
title: province-city-china
---

# GitHub项目：province-city-china

## 项目地址
[https://github.com/uiwjs/province-city-china](https://github.com/uiwjs/province-city-china)

## 主要特性
- **全面的中国省市区数据**：提供中国大陆所有省份、直辖市、自治区、行政区、县级市和乡镇级数据，支持多级联动。
- **JSON格式数据**：数据以JSON结构组织，便于前端框架集成，如React、Vue等。
- **轻量级和易集成**：无外部依赖，支持自定义过滤和搜索功能。
- **更新及时**：基于最新行政区划数据，定期维护以确保准确性。
- **多语言支持**：数据包含中文名称，便于国际化应用。

## 主要功能
- **省市区选择器**：实现三级（省-市-区）或四级（省-市-区-乡镇）联动选择。
- **数据查询和过滤**：支持根据代码或名称快速搜索特定区域。
- **自定义扩展**：允许用户修改或扩展数据结构，用于个性化需求。
- **API接口**：提供简单的方法来获取指定层级的行政区数据。

## 用法
1. **安装**：通过npm安装包：
   ```
   npm install province-city-china
   ```
   或直接从GitHub克隆仓库。

2. **导入数据**：在JavaScript项目中导入：
   ```javascript
   import { provinceList, cityList, areaList } from 'province-city-china';
   // 或直接使用JSON文件：import data from 'province-city-china/data.json';
   ```

3. **基本使用示例**（React组件）：
   ```jsx
   import React, { useState } from 'react';
   import { provinceAndCityData } from 'province-city-china';

   function AddressSelector() {
     const [province, setProvince] = useState('');
     const [city, setCity] = useState('');

     return (
       <div>
         <select onChange={(e) => setProvince(e.target.value)}>
           <option>选择省份</option>
           {provinceAndCityData.map(item => (
             <option key={item.value} value={item.value}>{item.label}</option>
           ))}
         </select>
         {/* 类似地渲染城市选项 */}
       </div>
     );
   }
   ```

4. **数据结构示例**：
   - 省份数据：`[{ value: '110000', label: '北京市' }]`
   - 城市数据：根据省份代码过滤获取子级。

更多细节请参考项目README文档，支持自定义配置以适应不同场景。