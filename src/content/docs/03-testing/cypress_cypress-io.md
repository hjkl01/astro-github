---
title: cypress
---

# Cypress 项目

**GitHub 项目地址:** [https://github.com/cypress-io/cypress](https://github.com/cypress-io/cypress)

## 主要特性
Cypress 是一个开源的端到端（E2E）测试框架，专为现代 Web 应用程序设计。它提供快速、可靠的测试执行，支持实时重载和调试。主要特性包括：
- **实时运行和调试**：测试在浏览器中实时执行，支持时间旅行调试，能暂停、回放和检查测试步骤。
- **自动等待**：内置智能等待机制，避免了手动添加等待时间，减少了测试不稳定因素。
- **网络拦截和模拟**：可以轻松拦截和修改网络请求，支持模拟 API 响应，提高测试隔离性。
- **跨浏览器支持**：兼容 Chrome、Firefox、Edge 等主流浏览器，并支持组件测试。
- **CI/CD 集成**：无缝集成到 Jenkins、GitHub Actions 等持续集成环境中，支持并行测试以加速执行。
- **TypeScript 和 JavaScript 支持**：原生支持现代 JavaScript 生态，无需额外配置。
- **视觉回归测试**：通过插件扩展，支持截图比较和视频录制，便于故障诊断。

## 主要功能
Cypress 的核心功能聚焦于 Web 应用的自动化测试：
- **端到端测试**：模拟真实用户交互，如点击、表单填写、导航等，验证整个应用流程。
- **组件测试**：隔离测试 UI 组件，而非完整页面，提高开发效率。
- **API 测试**：直接测试后端 API 接口，支持断言响应数据。
- **访问性测试**：集成 axe-core 工具，检查应用的 WCAG 合规性。
- **插件生态**：丰富的插件系统，如 cypress-real-events（真实事件模拟）和 cypress-xpath（XPath 支持）。

## 用法
### 安装
1. 确保 Node.js 版本 ≥ 14，并安装 npm 或 yarn。
2. 在项目根目录运行：
   ```
   npm install cypress --save-dev
   ```
   或
   ```
   yarn add cypress --dev
   ```

### 配置和运行
1. **初始化**：运行 `npx cypress open` 打开 Cypress 启动器，选择 E2E 测试或组件测试模板。
2. **编写测试**：在 `cypress/e2e/` 目录下创建 `.cy.js` 或 `.cy.ts` 文件。例如，一个简单测试：
   ```javascript
   describe('我的应用', () => {
     it('访问首页', () => {
       cy.visit('http://localhost:3000');
       cy.contains('欢迎').should('be.visible');
     });
   });
   ```
3. **运行测试**：
   - 交互模式：`npx cypress open`
   - 命令行模式：`npx cypress run`（ headless 模式）
   - 指定浏览器：`npx cypress run --browser chrome`
4. **自定义配置**：编辑 `cypress.config.js` 文件调整 baseUrl、viewport 等设置。
5. **集成到项目**：在 package.json 的 scripts 中添加 `"test:e2e": "cypress run"`，并在 CI 中调用。

更多详情请参考官方文档：https://docs.cypress.io/