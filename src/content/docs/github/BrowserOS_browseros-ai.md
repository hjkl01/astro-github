
---
title: BrowserOS
---

# BrowserOS – 浏览器内置操作系统

**项目地址:**  
[https://github.com/browseros-ai/BrowserOS](https://github.com/browseros-ai/BrowserOS)

---

## 1. 项目概述  
BrowserOS 是一个完全基于 Web 的操作系统模拟器，旨在让开发者和技术爱好者在浏览器中直接体验类桌面环境。它通过前端技术（React / Vite / TypeScript）构建，使用浏览器内置的存储（IndexedDB）实现文件系统持久化，并内置 AI 助手（基于 OpenAI GPT）提供即时编程与命令帮助。

---

## 2. 核心特性  

| 特性 | 说明 |
|------|------|
| **终端模拟** | 提供类 Bash 的命令行，支持常见文件操作、脚本执行与自定义命令。 |
| **文件系统** | 基于 IndexedDB 的虚拟文件系统，支持文件夹树、拖拽上传、文件预览等。 |
| **多窗口桌面** | 传统窗口化界面，可拖拽、缩放、最小化/最大化。 |
| **应用生态** | 预置文本编辑器、终端、浏览器等基础应用，可通过插件机制扩展。 |
| **AI 助手** | 通过 GPT 接口实现代码补全、命令建议、问题解答等功能。 |
| **主题与自定义** | 支持多种主题、壁纸、快捷键自定义。 |
| **离线运行** | 通过 Service Worker 缓存实现离线使用。 |
| **安全沙箱** | 所有操作均在浏览器沙箱内完成，避免对宿主系统的影响。 |

---

## 3. 主要功能  

- **启动与登录**：首次访问时自动创建本地用户，支持后续登录。  
- **文件管理**：创建、删除、重命名文件/文件夹，支持拖拽上传/下载。  
- **终端命令**：`ls`, `cd`, `cat`, `mkdir`, `rm`, `echo`, `help` 等，并可通过 `alias` 自定义快捷命令。  
- **应用启动**：点击桌面图标或在启动器中搜索即可打开对应应用。  
- **AI 交互**：在终端或聊天窗口中输入 `/ai` 或 `@ai` 调用 AI 助手，获取编程建议或命令解释。  
- **插件系统**：在 `src/plugins` 目录下添加插件，按需加载。  
- **跨设备同步**：利用 IndexedDB 与浏览器同步功能，可在不同设备上保持文件与设置一致。  

---

## 4. 用法  

### 4.1 本地开发  
```bash
# 克隆仓库
git clone https://github.com/browseros-ai/BrowserOS.git
cd BrowserOS

# 安装依赖
npm install

# 运行开发服务器
npm run dev
# 打开浏览器访问 http://localhost:5173 (默认端口)
```

### 4.2 打包与部署  
```bash
# 打包生产版本
npm run build
# 生成的静态文件位于 dist/，可部署至任何静态托管环境（GitHub Pages、Vercel、Netlify 等）
```

### 4.3 Docker 部署  
```bash
# 构建镜像
docker build -t browseros .

# 运行容器（端口 80 对应浏览器访问）
docker run -d -p 80:80 browseros
```

### 4.4 使用 AI 助手  
1. 在终端输入 `/ai` 或 `@ai` 触发 AI 对话框。  
2. 输入问题或代码片段，AI 将返回补全建议或解释。  
3. 通过 `/api-key` 命令设置 OpenAI API Key，或在 `.env` 中配置 `VITE_OPENAI_KEY`。

---

## 5. 进一步阅读  

- **文档**：`docs/` 目录下包含使用手册与插件开发指南。  
- **源码结构**  
  - `src/`：应用核心代码（React 组件、状态管理、插件）。  
  - `public/`：静态资源与 Service Worker。  
  - `vite.config.ts`：Vite 配置。  
- **贡献指南**：请遵循 `CONTRIBUTING.md`。  

---

**祝你在 BrowserOS 中玩得开心！**