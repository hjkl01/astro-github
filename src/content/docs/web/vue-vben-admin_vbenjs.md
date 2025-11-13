---
title: vue-vben-admin
---

# Vue Vben Admin 项目

## 项目地址
[GitHub 项目地址](https://github.com/vbenjs/vue-vben-admin)

## 主要特性
Vue Vben Admin 是一个基于 Vue 3、Vite 和 TypeScript 的现代后台管理系统模板，具有以下核心特性：
- **现代技术栈**：采用 Vue 3 Composition API、Vite 构建工具、TypeScript 类型支持，确保代码高效、可维护性和类型安全。
- **响应式设计**：支持多端适配，包括 PC、平板和移动端，使用 Element Plus UI 组件库，实现响应式布局。
- **国际化支持**：内置多语言切换功能，支持中文、英文等多种语言，易于扩展。
- **权限管理**：集成动态路由和角色-based 访问控制（RBAC），支持菜单权限、按钮权限等细粒度控制。
- **主题定制**：提供暗黑模式、主题颜色切换等个性化配置，支持用户自定义界面风格。
- **高性能**：Vite 的热重载和按需加载优化开发体验，生产环境支持代码拆分和 Tree Shaking。
- **插件生态**：集成 ECharts 图表、@vueuse 工具集、Pinia 状态管理等流行库，便于扩展。

## 主要功能
- **仪表盘与数据可视化**：内置仪表盘页面，支持实时数据展示、图表分析（如折线图、柱状图）。
- **用户与权限管理**：包括用户列表、角色分配、菜单配置等模块，实现完整的后台权限体系。
- **内容管理系统**：支持文章、分类、标签等 CRUD 操作，适用于博客或 CMS 场景。
- **表单与表格**：提供丰富的表单验证、表格排序、分页、导出功能，使用 VForm 和 VTable 组件简化开发。
- **工作台工具**：集成文件上传、富文本编辑器（基于 VueQuillEditor）、拖拽排序等实用功能。
- **系统设置**：支持配置管理、日志查看、系统监控等后台维护功能。
- **多页面布局**：支持侧边栏、顶部导航、标签页、多标签路由等布局模式。

## 用法
1. **环境准备**：
   - 安装 Node.js（推荐 v16+）和 Yarn 或 pnpm 包管理器。
   - 克隆仓库：`git clone https://github.com/vbenjs/vue-vben-admin.git`。
   - 进入项目目录：`cd vue-vben-admin`。

2. **安装依赖**：
   - 使用 Yarn：`yarn install`。
   - 或使用 pnpm：`pnpm install`。

3. **开发启动**：
   - 运行开发服务器：`yarn dev` 或 `pnpm dev`。
   - 访问 `http://localhost:3100`（默认端口）查看效果。

4. **构建生产环境**：
   - 运行构建命令：`yarn build` 或 `pnpm build`。
   - 输出文件位于 `dist` 目录，可部署到服务器。

5. **自定义配置**：
   - 修改 `src/settings/projectSetting.ts` 配置主题、路由等。
   - 在 `src/router` 目录添加自定义路由和页面。
   - 使用 `mock` 目录模拟 API 数据，或连接真实后端（如 Node.js 或 Spring Boot）。

项目文档详见仓库的 `README.md` 和 `docs` 目录，适合快速搭建企业级后台应用。