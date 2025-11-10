---
title: Sigma-Web-Dev-Course
---


# Sigma-Web-Dev-Course (CodeWithHarry)

> GitHub 地址: <https://github.com/CodeWithHarry/Sigma-Web-Dev-Course>

## 项目简介
Sigma-Web-Dev-Course 是 CodeWithHarry 教程系列中，用来帮助学习者快速掌握前端基础及实战项目的代码仓库。仓库内容涵盖多种常见网页布局、交互效果、响应式设计、CSS和 JavaScript 的应用。

## 主要特性 & 功能

|  #  | 功能 | 说明 |
|-----|------|------|
| 1 | **响应式布局** | 使用 Flexbox、Grid、媒体查询实现不同设备宽度下的自适应展示。 |
| 2 | **CSS 变量 & 预处理** | 用 CSS 变量统一管理颜色、间距、字体等，便于主题切换维护。 |
| 3 | **原生 JavaScript DOM 操作** | 包含表单验证、AJAX 请求、节点增删改查等实战案例。 |
| 4 | **动画与过渡** | 利用 CSS `@keyframes` 与 JavaScript 结合实现页面加载、按钮 hover 等动效。 |
| 5 | **组件化结构** | 采用模块化将页面拆分为 Header、Footer、Navbar、侧边栏等可复用组件。 |
| 6 | **多页面演示** | 包含多种项目演示：个人博客、电商模板、社交媒体页面等，方便学习者逐步理解。 |
| 7 | **SEO 与可访问性** | 使用语义化标签 (header, nav, main, footer)、aria 属性、alt 文本等提升可访问性与 SEO。 |
| 8 | **版本控制最佳实践** | 提供 `.gitignore`、`LICENSE`、`README`，示例如何在项目中使用 Git 工作流。 |

## 如何使用

1. **克隆仓库**  
   ```bash
   git clone https://github.com/CodeWithHarry/Sigma-Web-Dev-Course.git
   cd Sigma-Web-Dev-Course
   ```

2. **打开项目**  
   直接在浏览器中打开 `index.html` 或任何你想实验的 HTML 文件。  
   ```bash
   open index.html   # macOS
   start index.html  # Windows
   ```

3. **运行本地服务器（推荐）**  
   若项目使用 fetch / Ajax，需要运行 HTTP 服务器。  
   ```bash
   # 任选一种方式
   python -m http.server   # Python 3.x
   npx live-server .       # Node.js
   ```

4. **编辑与学习**  
   - 修改 `assets/css/style.css` 进行样式调整。  
   - 在 `assets/js/main.js` 添加/修改 JavaScript。  
   - 按需更换/添加图片与资源文件 `assets/images/`。

5. **发布**  
   ```bash
   git add .
   git commit -m "your message"
   git push origin main
   ```

## 贡献者须知

- 代码遵循 **Google JavaScript Style Guide**、**Airbnb CSS Style Guide**  
- 提交前请先确保文件通过 `ESLint` / `Stylelint` 检查  
- 所有新功能/修复需写相关测试（若适用）并更新 `README` 文档

> **备注：** 该仓库仅为教学演示，部分实例使用 `fake` 数据，若需正式部署，请自行替换后端接口与配置。

**End of file**

