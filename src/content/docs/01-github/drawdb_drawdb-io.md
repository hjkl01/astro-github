
---
title: drawdb
---


# DrawDB

**项目地址**: <https://github.com/drawdb-io/drawdb>

## 主要特性

- 直观可视化数据库模型编辑器  
- 支持 MySQL、PostgreSQL、SQL Server、SQLite 等常见数据库  
- 自由拖拽、缩放、对齐、连线功能  
- 表、视图、索引、触发器等实体均可编辑  
- 主外键关系自动标注、自动更新  
- 同步 SQL DDL：对图形的任何更改即刻生成对应 SQL  
- 导出 PDF / PNG / SVG / SQL / CSV  
- 主题切换、国际化（中文、英文等）  
- 模板与示例库，提升快速迭代效率  

## 功能说明

| 功能 | 操作方式 | 说明 |
|------|----------|------|
| 添加/删除表 | 双击画布右键 / 侧边栏拖拽 | 创建或移除表节点 |
| 编辑列 | 双击表 → 右键 → Edit | 名称、类型、默认值、是否为主键等 |
| 关系连线 | 拖拽表之间 | 自动生成外键关系线，显示角色 |
| 导入/导出 | File → Import / Export | 支持 SQL、JSON、SVG、SQL DDL |
| SQL 同步 | 右侧 SQL 预览 | 所有更改即时反映在 SQL 代码中 |
| 自动布局 | Auto Layout | 自动排列节点，避免重叠 |
| 主题切换 | Settings → Theme | Light / Dark / Midnight |
| 多语言 | Settings → Language | 中文、英文等 |

## 用法

### 1. 线上使用

直接访问部署好的站点（如 <https://drawdb.io/>）即可使用，注册后可保存项目到云端。

### 2. 本```bash
# 克隆仓库
git clone https://github.com/drawdb-io/drawdb.git
cd drawdb

# 安装依赖
npm install   # 或者 yarn

# 运行开发服务器
npm run dev   # 访问 http://localhost:3000

# 打包生产
npm run build
```

### 3. 部署

- **Vercel / Netlify**：直接 `vercel` 或 `npm run deploy` 即可  
- **Docker**：

```dockerfile
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY . .
RUN npm ci && npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

### 4. 使用流程示例

1. 在左侧面板 `Tables` 右键 → `New Table` → 输入表名。  
2. 双击表节点 → 右键 → `Edit`，添加/修改列、设置类型、默认值、是否主键。  
3. 拖拽表节点至画布，使用连线工具绘制外键关系。  
4. 右侧 `SQL` 预览板自动生成 DDL，复制粘贴到数据库客户端执行。  
5. `File → Export` → 选择 `PNG/SVG/PDF/SQL` 导出所需格式。

## 贡献

欢迎提交 Issues / Pull Requests，详见 `CONTRIBUTING.md`。

---

**项目地址**: <https://github.com/drawdb-io/drawdb>
```
