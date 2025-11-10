---
title: 3x-ui
---


# 3x‑UI by MHSanaei

**项目地址**: <https://github.com/MHSanaei/3x-ui>

## 项目简介  
3x‑UI 是一个轻量级、开源的 Web UI 框架，旨在为开发者提供快速搭建现代化前端应用的工具。它基于现代浏览器技术（HTML5、CSS3、JavaScript ES6+）实现，兼容主流浏览器，具有可扩展、易维护的特点。

## 主要特性  
- **模块化组件**：提供丰富的 UI 组件（按钮、表单、对话框、导航等），支持按需引入。  
- **响应式布局**：内置网格系统，支持自适应布局，兼容移动端设备。  
- **主题定制**：支持主题切换与自定义，使用 CSS 变量轻松更改配色与字体。  
- **国际化（i18n）**：内置多语言支持，方便多语种项目开发。  
- **无障碍友好**：遵循 WCAG 规范，组件具备键盘导航与 ARIA 属性。  
- **开发工具**：提供 CLI 工具（`3x-cli`）用于项目脚手架、构建与打包。  
- **插件机制**：支持自定义插件，扩展功能与主题。  

## 核心功能  
| 功能 | 描述 |
|------|------|
| 组件库 | 按需引入，支持自定义组件开发 |
| 主题系统 | CSS 变量 + SASS 变量，支持多主题 |
| 响应式网格 | 12 列网格系统，支持断点配置 |
| 国际化 | JSON 语言文件，自动切换 |
| 开发工具 | CLI、热重载、ESLint、Prettier 自动化配置 |
| 打包优化 | Tree-shaking、代码拆分、压缩 |
| 访问控制 | 基于角色的权限管理（可选） |

## 用法示例  

```bash
# 安装 CLI
npm i -g 3x-cli

# 创建新项目
3x-cli create my-app

# 进入项目目录
cd my-app

# 开发环境启动
npm run dev

# 生产构建
npm run build
```

> **快速引入组件**  
> ```js
> import { Button, Modal } from '3x-ui';
> // 或者按需导入
> import Button from '3x-ui/lib/Button';
> ```

## 贡献与维护  
- **提交 Issue**：报告 bugs 或提出功能建议。  
- **Pull Request**：欢迎提交代码，遵循项目代码规范。  
- **文档**：所有文档均保存在 `docs/` 目录，使用 Markdown 编写。  

> 该项目采用 MIT 许可证，欢迎自由使用与修改。  

---  

> **联系**  
> GitHub 仓库: <https://github.com/MHSanaei/3x-ui>
