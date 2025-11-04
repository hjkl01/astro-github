
---
title: storybook
---


# Storybook（storybookjs）

**GitHub 地址**: [https://github.com/storybookjs/storybook](https://github.com/storybookjs/storybook)

## 项目概述
Storybook 是一个开源工具，用于构建 UI 组件库，支持多种前端框架（React、Vue、Angular、Svelte 等）。它提供了一个隔离的环境，让开发者可以独立开发、测试和展示 UI 组件。

## 主要特性

| 特性 | 说明 |
|------|------|
| **组件隔离** | 在 Storybook 中，每个组件都有自己的“Story”，可在无业务逻辑干扰的环境下单独展示。 |
| **交互式 UI** | 通过 Knobs、Controls 等插件，实时调节组件属性，观察效果。 |
| **自动化测试** | 与 Jest、Cypress、Playwright 等工具集成，支持视觉回归测试（Chromatic）。 |
| **文档生成** | 自动生成组件文档，支持 MDX 语法，方便团队共享。 |
| **插件生态** | 丰富的官方和社区插件，满足需求：Actions、Viewport、Accessibility、Dark Mode 等。 |
| **可视化调试** | 使用 Addons（如 Storyshots）可快速捕获 UI 变更。 |

## 核心功能

1. **启动与配置**  
   ```bash
   npx sb init   # 自动生成 .storybook 目录与配置文件
   npm run storybook
   ```

2. **编写 Story**  
   ```js
   // Button.stories.jsx
   import { Button } from './Button';

   export default {
     title: 'Example/Button',
     component: Button,
     argTypes: { backgroundColor: 'color' },
   };

   const Template = (args) => <Button {...args} />;

   export const Primary = Template.bind({});
   Primary.args = {
     label: 'Click me',
     primary: true,
   };
   ```

3. **使用 Addons**  
   - `@storybook/addon-controls`：动态控制 props。  
   - `@storybook/addon-actions`：监控事件。  
   - `@storybook/addon-a11y`：无障碍检测。  
   - `@storybook/addon-viewport`：模拟不同设备。  

4. **与 CI/CD 集成**  
   - 在 CI 环境中执行 `npm run storybook:build` 生成静态文件。  
   - 使用 Chromatic 进行视觉回归测试。  

5. **导出和发布**  
   - `npm run build-storybook` 生成可托管的静态站点。  
   - 通过 Netlify、Vercel 等平台快速部署。  

## 快速上手

1. **安装**  
   ```bash
   npx sb init
   ```

2. **运行**  
   ```bash
   npm run storybook
   ```

3. **开发**  
   - 在 `src` 目录下创建组件与对应 `.stories.js` 文件。  
   - 通过 `Controls` 交互式修改 props。  

4. **构建**  
   ```bash
   npm run build-storybook
   ```

5. **部署**  
   - 将 `storybook-static` 目录推送至 GitHub Pages 或其他托管平台。  

## 结语
Storybook 通过组件隔离与丰富的插件生态，为前端团队提供了高效、可复用的 UI 开发与文档化工作流。无论是单个组件还是完整的设计系统，Storybook 都能帮助你快速迭代与交付。