---
title: slash-admin
---

# Slash Admin 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/d3george/slash-admin/blob/main/README.zh-CN.md)

## 主要特性
Slash Admin 是一个基于 Vue 3、Vite 和 TypeScript 的现代后台管理系统模板，具有以下核心特性：
- **响应式设计**：支持 PC 和移动端自适应布局，确保在不同设备上的良好体验。
- **模块化架构**：采用 Vue 3 Composition API 和 TypeScript，提供类型安全的开发环境，便于扩展和维护。
- **国际化支持**：内置 i18n 多语言功能，支持中文、英文等多种语言切换。
- **主题定制**：支持暗黑模式和自定义主题颜色，增强用户界面个性化。
- **权限管理**：集成角色-based 访问控制 (RBAC)，支持动态路由和菜单权限配置。
- **高效构建**：使用 Vite 作为构建工具，提供快速的热重载和开发体验。
- **UI 组件库**：基于 Element Plus 和 Iconify，提供丰富的 UI 组件和图标库。

## 主要功能
Slash Admin 提供了全面的后台管理功能，包括但不限于：
- **用户与权限**：用户登录、注册、角色分配、权限设置，支持 JWT 令牌认证。
- **仪表盘**：实时数据展示、图表统计（集成 ECharts），用于监控系统关键指标。
- **内容管理**：文章、产品等 CRUD 操作，支持富文本编辑器（如 WangEditor）。
- **系统设置**：配置管理、日志记录、缓存清理等系统级功能。
- **表单与表格**：高级表单验证、动态表格、批量操作，支持分页、搜索和排序。
- **API 接口**：内置 Mock 数据模拟和 Axios 封装，便于前后端联调。
- **错误处理**：全局异常捕获、404 页面和错误提示，提升应用稳定性。

## 用法
### 安装与启动
1. **克隆项目**：
   ```
   git clone https://github.com/d3george/slash-admin.git
   cd slash-admin
   ```

2. **安装依赖**：
   ```
   npm install
   # 或使用 yarn
   yarn install
   ```

3. **启动开发服务器**：
   ```
   npm run dev
   # 或 yarn dev
   ```
   访问 `http://localhost:5173` 查看应用。

### 构建与部署
- **生产构建**：
  ```
  npm run build
  # 输出目录：dist/
  ```
- **部署**：将 `dist` 目录内容上传至静态服务器（如 Nginx），或集成到 Node.js/Express 等环境中。

### 自定义开发
- **路由配置**：编辑 `src/router/index.ts` 添加新路由。
- **组件扩展**：在 `src/components` 目录创建自定义组件，使用 Vue 3 单文件组件格式。
- **API 集成**：修改 `src/api` 目录下的接口文件，替换 Mock 数据为真实后端 API。
- **主题配置**：在 `src/settings` 中调整主题变量，支持 SCSS 变量覆盖。

更多细节请参考项目 README 文件。项目开源，欢迎贡献代码和 issue。