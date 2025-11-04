
---
title: node-red
---

**文件路径**  
`src/content/docs/00/node-red_node-red.md`

**内容**  

```markdown
# Node-RED 项目概述

- **官方地址**: [https://github.com/node-red/node-red](https://github.com/node-red/node-red)

## 主要特性

- **可视化开发**：通过拖拽节点（Node）的方式在浏览器中构建流程，避免大量编写代码。
- **节点生态**：内置基础节点（如 HTTP、MQTT、TCP 等）并支持插件机制，可通过 `npm` 安装扩展节点。
- **低代码/无代码**：适合硬件、物联网、业务流程自动化等场景，无需深度编程知识。
- **多平台支持**：Node.js 运行，支持 Linux、Windows、macOS、Raspberry Pi 等多种硬件。
- **实时调试**：节点执行过程可实时监控、日志输出，支持“调试”节点查看消息流。
- **安全与权限**：内置 HTTPS、用户认证（基本身份验证、授权）、权限层级管理。
- **可扩展性**：通过 HTTP API、WebSocket 与外部系统集成；支持 JavaScript、函数节点、HTTP 导入/导出流程。

## 核心功能

| 功能 | 说明 |
|------|------|
| **流程编辑器** | 浏览器可视化编辑，支持撤销、重做、快捷键 |
| **节点注册** | 通过 `npm install node-red-node-*` 安装第三方节点 |
| **部署** | 一键部署到运行环境，支持 `NODE_RED_HOME` 与 `--settings` 进行配置 |
| **调试** | 内置 “Debug” 窗口，查看每个节点输出 |
| **流量跟踪** | 通过“Dashboard”节点创建 IoT 可视化面板 |
| **函数节点** | 运行自定义 JavaScript 代码处理消息 |
| **触发节点** | 触发 HTTP 请求、MQTT 收发、定时等事件 |
| **配置信息** | `settings.js` 进行主题、端口、 HTTPS、用户等配置 |

## 使用方法

1. **安装 Node.js（>=12）**  
   ```bash
   curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **全局安装 Node-RED**  
   ```bash
   npm install -g node-red
   ```

3. **启动**  
   ```bash
   node-red
   ```
   浏览器访问 `http://localhost:1880` 开始编辑流程。

4. **部署流程**  
   - 设计完成后点击顶部 “Deploy” 按钮，应用自动在后台运行。

5. **安装扩展节点**  
   ```bash
   cd ~/.node-red
   npm install node-red-node-mqtt
   ```
   或者在编辑器右上角 **Manage palette** → **Install** 搜索并安装。

6. **配置与安全**  
   - 打开 `~/.node-red/settings.js` 修改端口、HTTPS、用户验证等。

7. **运行与监控**  
   - `node-red` 后台运行，日志可通过 `--verbose` 查看。
   - 通过 `node-red-admin` 命令管理流、重置、导入/导出。

8. **部署到服务器**  
   - 使用 systemd、PM2 或 Docker 部署，可参考官方文档。

> **提示**：任何节点可通过右键 `copy node(type)`、`rename` 或 `delete` 操作。  
> **调试**：添加 Debug 节点，可实时看到消息内容，适合排查流程异常。

**文档来源**  
- 官方文档: https://nodered.org/docs  
- GitHub 项目: https://github.com/node-red/node-red
```

---