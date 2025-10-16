
---
title: lightence-ant-design-react-template
---

# Lightence Ant Design React 模板

## 项目地址
[GitHub 项目地址](https://github.com/altence/lightence-ant-design-react-template)

## 主要特性
Lightence Ant Design React 模板是一个基于 React 和 Ant Design 的现代前端开发模板，具有以下核心特性：
- **响应式设计**：采用 Ant Design 的组件库，支持移动端和桌面端的自适应布局，确保在各种设备上提供一致的用户体验。
- **现代化技术栈**：使用 React 18+、TypeScript、Vite 构建工具，以及 Tailwind CSS 进行样式管理，支持热重载和快速开发。
- **组件丰富**：内置 Ant Design 的 UI 组件，包括表单、表格、图表、导航等，支持自定义主题和国际化（i18n）。
- **状态管理**：集成 Zustand 或 Redux Toolkit 等轻量级状态管理解决方案，便于处理复杂应用状态。
- **路由支持**：基于 React Router v6，实现单页应用（SPA）的路由管理，支持嵌套路由和权限控制。
- **性能优化**：预配置代码拆分、懒加载和 Tree Shaking，提升应用加载速度和运行效率。
- **开发友好**：包含 ESLint、Prettier 代码规范，以及 Husky Git 钩子，确保代码质量；支持 PWA（渐进式 Web 应用）功能。

## 主要功能
该模板适用于快速构建企业级 Web 应用，提供以下关键功能：
- **仪表盘和页面模板**：预置登录、注册、仪表盘、用户管理、数据可视化等常见页面模板，便于快速原型开发。
- **表单与数据处理**：支持复杂表单验证、数据表格排序/分页/搜索，以及 API 集成（Axios 或 Fetch）。
- **认证与授权**：内置 JWT 令牌认证系统，支持角色-based 访问控制（RBAC）。
- **主题切换**：支持浅色/深色模式切换，以及自定义 Ant Design 主题配置。
- **集成工具**：易于集成第三方库，如 Chart.js 用于图表、React Query 用于数据获取和缓存。
- **部署友好**：支持一键构建和部署到 Vercel、Netlify 等平台。

## 用法
1. **克隆项目**：  
   ```
   git clone https://github.com/altence/lightence-ant-design-react-template.git
   cd lightence-ant-design-react-template
   ```

2. **安装依赖**：  
   使用 npm 或 yarn 安装：  
   ```
   npm install
   # 或
   yarn install
   ```

3. **启动开发服务器**：  
   ```
   npm run dev
   # 或
   yarn dev
   ```  
   项目将在 http://localhost:5173 上运行（端口可能因配置而异）。

4. **构建生产版本**：  
   ```
   npm run build
   # 或
   yarn build
   ```  
   构建输出在 `dist` 目录下，可直接部署。

5. **自定义开发**：  
   - 修改 `src/App.tsx` 作为入口文件。  
   - 在 `src/components` 中添加或修改 Ant Design 组件。  
   - 配置路由在 `src/router` 目录。  
   - 环境变量通过 `.env` 文件管理。  
   参考项目 README 以获取更多高级配置，如添加新页面或集成后端 API。