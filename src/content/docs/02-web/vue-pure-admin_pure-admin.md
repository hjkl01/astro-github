---
title: vue-pure-admin
---

# vue-pure-admin 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/pure-admin/vue-pure-admin)

## 主要特性
vue-pure-admin 是一个基于 Vue 3、Vite、TypeScript 和 Element Plus 的现代后台管理系统模板。它采用纯净的代码风格，强调简洁、高效和可维护性。主要特性包括：
- **Vue 3 生态支持**：使用 Composition API 和最新的 Vue 3 特性，确保代码模块化和响应式。
- **TypeScript 集成**：全程使用 TypeScript 提供类型安全，提高开发效率和代码可靠性。
- **Vite 构建工具**：快速的热重载和模块化构建，支持开发和生产环境的优化。
- **Element Plus UI 组件**：内置丰富的 UI 组件库，支持主题定制和国际化。
- **权限管理**：支持动态路由和角色-based 访问控制（RBAC），便于实现多用户权限系统。
- **多主题支持**：内置浅色/深色模式切换，以及自定义主题配置。
- **国际化（i18n）**：支持多语言切换，内置中文和英文，默认支持更多语言扩展。
- **响应式设计**：适配 PC 和移动端，支持 PWA（渐进式 Web 应用）。
- **插件化架构**：易于扩展，如集成 Pinia 状态管理、Vue Router 路由管理等。
- **代码质量**：遵循 ESLint 和 Prettier 规范，包含单元测试和 E2E 测试支持。

## 主要功能
该项目提供了一个完整的后台管理框架，核心功能模块包括：
- **用户认证**：登录/登出、JWT Token 管理、记住密码等。
- **仪表盘**：数据可视化展示，支持 ECharts 图表集成。
- **内容管理**：文章/文件上传、CRUD 操作（创建、读取、更新、删除）。
- **系统设置**：用户管理、角色分配、菜单配置、日志审计。
- **表单与表格**：动态表单生成、表格排序/分页/搜索、批量操作。
- **工作流**：任务分配、流程审批（可扩展）。
- **通知与消息**：实时消息推送、公告管理。
- **API 接口管理**：Mock 数据支持、Axios 封装的 HTTP 请求处理。
- **错误处理**：全局错误捕获、404/500 页面。
- **性能优化**：懒加载、代码分割、Tree Shaking。

## 用法
### 安装与启动
1. **克隆仓库**：
   ```
   git clone https://github.com/pure-admin/vue-pure-admin.git
   cd vue-pure-admin
   ```

2. **安装依赖**：
   ```
   npm install
   # 或使用 yarn/pnpm
   yarn install
   # pnpm install
   ```

3. **开发模式启动**：
   ```
   npm run dev
   # 访问 http://localhost:3000
   ```

4. **构建生产版本**：
   ```
   npm run build
   # 输出到 dist 目录
   ```

5. **预览构建版本**：
   ```
   npm run preview
   ```

### 自定义开发
- **路由配置**：修改 `src/router/index.ts` 添加新路由，支持动态导入。
- **状态管理**：使用 Pinia，在 `src/store` 目录创建模块。
- **组件扩展**：在 `src/components` 添加自定义组件，注册到 `src/App.vue`。
- **API 接口**：在 `src/api` 定义接口，封装请求方法。
- **主题定制**：编辑 `src/theme` 目录的 SCSS 文件，或通过 Element Plus 的主题工具生成。
- **环境配置**：通过 `.env` 文件设置开发/生产环境变量，如 API_BASE_URL。
- **部署**：支持 Docker 部署，参考仓库的 `Dockerfile`；或直接上传 `dist` 到服务器。

项目文档详见仓库的 `README.md` 和 `docs` 目录。建议先阅读官方文档以熟悉项目结构。