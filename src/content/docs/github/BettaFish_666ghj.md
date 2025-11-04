
---
title: BettaFish
---

# BettaFish

**项目地址**: <https://github.com/666ghj/BettaFish>

---

## 概述  
BettaFish 是一个基于 Node.js 与 Vue.js 的轻量级前后端分离项目，旨在帮助养鱼爱好者方便地记录、管理与分析金鱼（Betta Fish）养殖过程中的各种信息。项目提供了数据可视化、日程安排、健康监测等核心功能，支持多用户登录、权限管理以及数据导出。

---

## 主要特性  

| 序号 | 功能描述 | 关键技术 |
|------|----------|----------|
| 1 | **用户管理** | JWT、bcrypt、Vuex |
| 2 | **鱼类信息录入** | 表单验证、RESTful API |
| 3 | **喂食与药物记录** | 日历视图、数据导入/导出 |
| 4 | **健康状态监测** | 图片上传、状态评估、历史追踪 |
| 5 | **数据可视化** | ECharts、Chart.js |
| 6 | **数据导出** | CSV、Excel |
| 7 | **权限控制** | RBAC、路由守卫 |
| 8 | **响应式 UI** | Element Plus、Vue 3 |

---

## 功能模块  

1. **用户模块**  
   - 注册、登录、忘记密码、资料编辑  
   - 角色划分：管理员、普通用户  

2. **鱼类管理**  
   - 添加/编辑/删除金鱼信息（品种、尺寸、颜色、出生日期等）  
   - 查看鱼类列表、详情页  

3. **喂食记录**  
   - 记录喂食时间、用量、饲料种类  
   - 通过日历与时间轴查看历史记录  

4. **药物与健康**  
   - 记录药物使用、剂量、疗程  
   - 上传健康检查图片并进行人工评估  
   - 生成健康报告  

5. **数据分析**  
   - 饲料消耗趋势图、体重增长曲线、疾病发病率统计  
   - 自定义报表并支持导出  

---

## 用法

### 1. 环境准备  
- Node.js >= 20.x  
- npm >= 10.x  

### 2. 克隆项目  
```bash
git clone https://github.com/666ghj/BettaFish.git
cd BettaFish
```

### 3. 安装依赖  
```bash
# 前端
cd frontend
npm install

# 后端
cd ../backend
npm install
```

### 4. 配置环境变量  
复制 `.env.example` 至 `.env` 并按需修改（数据库、JWT 秘钥等）。

```bash
# backend/.env
PORT=3000
DB_URI=mongodb://localhost:27017/bettafish
JWT_SECRET=your_jwt_secret
```

### 5. 运行

#### 启动后端  
```bash
cd backend
npm run dev
```

#### 启动前端  
```bash
cd ../frontend
npm run dev
```

> 默认访问地址：`http://localhost:5173`

### 6. 生产构建  

```bash
# 后端
cd backend
npm run build

# 前端
cd ../frontend
npm run build
```

将 `frontend/dist` 静态文件与后端结合，或使用 Nginx 做静态文件托管。

### 7. 单元测试  

```bash
# 后端
cd backend
npm test

# 前端
cd ../frontend
npm run test
```

---

## 参与贡献  

1. Fork 本仓库  
2. 创建特性分支 (`feature/xxx`)  
3. 提交代码并推送  
4. 发起 Pull Request 并描述变更细节  

请遵循代码规范，提交前执行 `npm run lint`。

---

> 如需进一步帮助，请查看项目根目录下的 `README.md` 或 `docs/` 目录。祝你使用愉快！