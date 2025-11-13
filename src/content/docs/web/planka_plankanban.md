---
title: planka
---


# 00. planka_plankanban

> 项目地址: <https://github.com/plankanban/planka>

## 项目概述
P**lanka** 是一款基于 Web 的开源看板工具，提供类似 Trello、Asana 的项目管理功能。项目采用前后端分离架构，后端基于 Node.js + Express，前端使用 React + Redux。支持多团队、多项目、任务分配、附件上传、评论、标签、子任务、定时推送等完整的协作功能。

## 主要特性
- **多看板 & 多项目**：支持在同一系统中创建共享或私有看板、项目。
- **任务（卡片）管理**：拖拽排序、标签、成员分配、优先级、附件、评论、子任务。
- **列表与列**：可自定义列（列名称、过滤器），列与任务拖拽自由。
- **用户与团队**：团队角色（Owner/Developer/Viewer）、成员邀请、邀请链接。
- **权限**：项目级、看板级、列级、卡级细粒度权限。
- **通知**：邮件+站内通知，支持对关键事件（成员变更、待办提醒）进行推送。
- **搜索 & 过滤**：按关键字、标签、成员、状态搜索卡片。
- **RESTful API**：所有功能均提供完整 API，方便第三方集成。
- **多语言**：支持多语言（默认中文/英文，可扩展）。
- **插件/集成**：可编写插件接口，集成 CI/CD、Slack、GitHub等工具。

## 目录结构（简要）
```
├── backend/          # Node.js 后端
│   ├── src/          # 源码
│   ├── config/       # 环境配置
│   └── scripts/      # 初始化/迁移脚本
├── frontend/         # React 前端
│   ├── public/
│   └── src/
├── docs/             # 文档与示例
└── docker/           # Docker Compose 配置
```

## 环境与依赖
- **Node.js** v20+
- **PostgreSQL** 服务器（默认）
- **Redis**（可选，支持缓存/队列）
- **Docker**（推荐一键部署）

## 安装与运行

### 1. 本地开发
```bash
# 克隆仓库
git clone https://github.com/plankanban/planka.git
cd planka

# 安装后端依赖
cd backend
npm install

# 安装前端依赖
cd ../frontend
npm install
```

### 2. 配置环境
复制 `.env.example` 至 `backend/.env`，按需修改：
```ini
DB_URL=postgres://user:pass@localhost:5432/planka
REDIS_URL=redis://localhost:6379
```

### 3. 启动后端
```bash
cd backend
npm run dev
```

### 4. 启动前端
```bash
cd frontend
npm start
```

应用默认运行在 http://localhost:3000。

### 5. 一键 Docker 部署（推荐）
```bash
docker compose up -d
```
默认后端监听 8000，前端 3000，使用 `docker compose` 管理数据库与缓存。

## 使用示例

1. **创建看板**  
   - 登录 → 新建 → 选择 "看板" 或 "项目" → 配置名称、成员、权限。

2. **添加列**  
   - 在看板中点击 "新增列表" → 输入列名 → 设置过滤规则（可为空）。

3. **创建任务**  
   - 在列中新建卡片 → 填写标题 → 可添加描述、标签、附件、子任务、指派成员。

4. **拖拽排序**  
   - 直接拖拽卡片可在同一列或跨列移动，列顺序同理。

5. **搜索与过滤**  
   - 使用右上角搜索框，or 进入 Column 上方的 “过滤器” 选择标签/成员/状态。

6. **API 示例**  
   ```bash
   # 获取所有看板
   curl -H "Authorization: Bearer <token>" https://localhost:8000/api/boards
   ```

## 贡献
- Fork → 新建分支 → 提交 PR  
- 代码采用 ESLint + Prettier，提交前请运行 `npm run lint && npm run test`。

## 许可证
Apache‑2.0 © Planka

``` 
