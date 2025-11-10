---
title: china
---

# 中国行政区划数据项目

## 项目地址
[https://github.com/adyliu/china_area](https://github.com/adyliu/china_area)

## 主要特性
- **全面覆盖中国行政区划**：提供从省级到乡镇级的中国行政区划数据，基于官方标准，支持最新行政区划更新。
- **数据格式多样**：以JSON、CSV等格式提供数据，便于集成到各种应用中。
- **开源免费**：MIT许可证，允许自由使用、修改和分发。
- **轻量级设计**：数据结构清晰，易于查询和解析，支持前端和后端开发。

## 主要功能
- **行政区划查询**：通过代码或名称快速检索省市区县乡镇信息。
- **层级结构支持**：提供树状层级数据，便于构建级联选择器（如省市区选择）。
- **数据导出与导入**：支持数据导出为多种格式，适用于数据库导入或API集成。
- **自定义扩展**：允许开发者根据需要添加或修改区划数据。

## 用法
1. **克隆仓库**：  
   ```
   git clone https://github.com/adyliu/china_area.git
   ```

2. **安装依赖**（如果需要Node.js环境）：  
   ```
   npm install
   ```

3. **使用数据**：  
   - 直接在项目中找到`data`目录下的JSON文件（如`china_area.json`），导入到你的应用中。  
   - 示例（JavaScript）：  
     ```javascript
     const chinaArea = require('./data/china_area.json');
     // 查询北京市下属区县
     const beijing = chinaArea.find(item => item.name === '北京市');
     console.log(beijing.children); // 输出北京市下属区县
     ```

4. **集成到项目**：  
   - 前端：用于Vue、React等框架的省市区选择组件。  
   - 后端：导入到MySQL、MongoDB等数据库，用于API服务。  
   - 更新数据：定期拉取仓库最新版本以获取行政区划变更。