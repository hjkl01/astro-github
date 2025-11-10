---
title: create-react-app
---


# Create React App

项目地址: https://github.com/facebook/create-react-app

## 主要特性

- **零配置**：一次性脚手架即可启动开发，无需手动配置 Babel、Webpack 等构建工具。
- **现代化的构建流程**：内置支持 ES2015+、JSX、CSS Modules、Sass、PostCSS、图像/字体等。
- **快速热更新**：开发服务器支持 HMR（Hot Module Replacement），代码修改即时在浏览器中反映。
- **优化生产**：构建时自动压缩、树摇、代码拆分、缓存优化，生成的 `build/` 目录可直接部署。
- **ESLint、Prettier**：默认集成 lint 与格式化工具，保持代码质量。
- **可扩展**：通过 `react-scripts` 依赖可升级或自定义配置；使用 `eject` 将所有配置暴露给用户。

## 功能

- **脚手架**：`npx create-react-app my-app` 自动创建项目结构。
- **开发服务器**：`npm start` 启动本地开发环境，支持热更新。
- **构建**：`npm run build` 生成生产环境可部署文件。
- **测试**：`npm test` 运行 Jest 单元测试，支持覆盖率报告。
- **Lint**：`npm run lint` 运行 ESLint 检查代码。
- **类型检查**：内置 TypeScript 支持，使用 `--template typescript` 创建 TS 项目。
- **环境变量**：通过 `.env` 文件管理环境变量，前缀 `REACT_APP_` 的变量会注入到代码中。
- **服务工作者**：可选的 PWA 支持，使用 `npm run build` 后自动生成 Service Worker。

## 用法

1. **创建项目**  
   ```bash
   npx create-react-app my-app
   # 或者使用 TypeScript 模板
   npx create-react-app my-app --template typescript
   ```

2. **进入项目目录**  
   ```bash
   cd my-app
   ```

3. **启动开发服务器**  
   ```bash
   npm start
   # 浏览器自动打开 http://localhost:3000
   ```

4. **运行单元测试**  
   ```bash
   npm test
   ```

5. **生成生产构建**  
   ```bash
   npm run build
   # 输出在 build/ 目录
   ```

6. **自定义配置**  
   - **暂时自定义**：通过 `react-scripts` 的 `start`, `build`, `test` 等脚本参数实现，如 `npm run build -- --max_old_space_size=4096`。  
   - **彻底自定义**：执行 `npm run eject`，将所有内部配置暴露为可编辑的文件（不可逆）。

7. **添加环境变量**  
   - 在项目根目录创建 `.env`：  
     ```dotenv
     REACT_APP_API_URL=https://api.example.com
     ```
   - 在代码中使用：`process.env.REACT_APP_API_URL`

8. **添加第三方依赖**  
   ```bash
   npm install axios
   ```

9. **部署**  
   - 生成 `build/` 后直接部署到静态托管服务（Netlify、Vercel、GitHub Pages 等）。  
   - 对于单页面应用，服务器需将所有路由请求返回 `index.html`。

> **提示**  
> - `react-scripts` 版本会随项目更新而升级，保持 `npm install` 能获得最新构建工具。  
> - 若项目规模较大或需要高级自定义，建议先尝试 `eject` 或使用更灵活的工具（如 Vite、Next.js）。  

---   
> 以上即为 Create React App 的主要特性、功能与典型用法。祝你开发顺利！
