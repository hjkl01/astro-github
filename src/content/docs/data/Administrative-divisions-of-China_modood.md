
---
title: Administrative-divisions-of-China
---

# 中国行政区划数据项目

## 项目地址
[GitHub 项目地址](https://github.com/modood/Administrative-divisions-of-China)

## 主要特性
- **完整行政区划数据**：提供中国大陆所有省市县区、乡镇街道的行政区划信息，数据基于官方来源，覆盖最新行政划分。
- **多种格式支持**：数据以 JSON、JS 等格式提供，便于前端和后端集成。
- **轻量级和易用**：纯数据文件，无需额外依赖，适合快速导入使用。
- **开源免费**：MIT 许可，允许自由使用和修改。

## 功能
- **数据查询**：支持通过代码、区域码或名称快速查询行政区划信息，如获取某个省份的所有城市。
- **级联选择**：常用于表单中的省市区三级联动功能，例如在 Web 应用中实现地址选择器。
- **数据导出与导入**：可直接导入项目中使用，或导出为其他格式进行二次开发。
- **历史版本支持**：包含多个年份的行政区划数据，便于历史对比或特定需求。

## 用法
1. **克隆或下载项目**：从 GitHub 下载仓库，获取 `dist` 目录下的数据文件（如 `province.json`、`city.json` 等）。
2. **导入数据**：在 JavaScript 项目中，直接引入文件，例如：
   ```javascript
   import provinceData from './dist/province.json';
   console.log(provinceData); // 输出省份列表
   ```
3. **实现级联查询**：使用区域码（code）过滤子级数据，例如查询北京市的所有区县：
   ```javascript
   const beijingCode = '110000';
   const districts = cityData.filter(item => item.parent_code === beijingCode);
   ```
4. **集成到框架**：适用于 Vue、React 等框架的地址选择组件，或 Node.js 后端 API。
5. **更新数据**：定期检查仓库更新，以获取最新的行政区划变动。